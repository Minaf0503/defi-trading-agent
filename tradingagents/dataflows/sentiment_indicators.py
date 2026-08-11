"""
Deterministic sentiment indicator computation for DeFi Trading Agents.

Analogous to technical_indicators.py: ALL scoring is computed in Python
before the LLM ever sees the data. The LLM must interpret pre-computed
fields only — it must NOT re-score articles from raw text.

Key design principles:
  - recency decay: articles from <12h ago weight 1.0, >72h weight 0.50
  - source credibility weights per outlet
  - keyword-based bullish/bearish scoring with crypto-specific term lists
  - automatic event categorisation (exploit, regulatory, upgrade, etc.)
  - sentiment momentum: compare recent-half vs early-half of the window
  - output is a flat, JSON-serialisable dict matching the technical snapshot contract
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

# ─── Keyword dictionaries ──────────────────────────────────────────────────────

# Weight 2 = high-impact signal; weight 1 = supporting signal
BULLISH_TERMS: Dict[str, int] = {
    # High-impact
    "partnership": 2, "integration": 2, "adoption": 2, "listing": 2,
    "institutional": 2, "approval": 2, "milestone": 2, "launch": 2,
    "upgrade": 2, "mainnet": 2, "breakthrough": 2, "record high": 2,
    "bull run": 2, "bullrun": 2, "accumulate": 2, "airdrop": 2,
    "etf approved": 2, "etf": 2, "fund": 2, "acquisition": 2,
    "grant": 2, "raise": 2, "investment": 2,
    # Mid-impact
    "growth": 1, "increase": 1, "surge": 1, "gain": 1, "positive": 1,
    "optimistic": 1, "strong": 1, "support": 1, "bullish": 1,
    "buy": 1, "long": 1, "upside": 1, "recovery": 1, "rebound": 1,
    "higher": 1, "progress": 1, "innovation": 1, "expansion": 1,
    "momentum": 1, "rally": 1, "all-time high": 1, "ath": 1,
}

BEARISH_TERMS: Dict[str, int] = {
    # High-impact
    "hack": 2, "exploit": 2, "drain": 2, "breach": 2, "vulnerability": 2,
    "attack": 2, "stolen": 2, "rug": 2, "scam": 2, "fraud": 2,
    "sec": 2, "lawsuit": 2, "ban": 2, "enforcement": 2, "penalty": 2,
    "fine": 2, "indictment": 2, "arrest": 2,
    "crash": 2, "liquidation": 2, "delist": 2, "suspension": 2,
    "bearish": 2, "dump": 2, "sell-off": 2, "selloff": 2,
    "collapse": 2, "bankrupt": 2, "insolvency": 2,
    # Mid-impact
    "decline": 1, "drop": 1, "fall": 1, "lower": 1, "concern": 1,
    "warning": 1, "risk": 1, "negative": 1, "weak": 1,
    "sell": 1, "short": 1, "downside": 1, "loss": 1, "fud": 1,
    "regulatory": 1, "investigation": 1, "probe": 1, "scrutiny": 1,
}

# Event categories — ordered from highest to lowest trading relevance
EVENT_KEYWORDS: Dict[str, List[str]] = {
    "exploit_hack":      ["hack", "exploit", "drain", "breach", "vulnerability",
                          "attack", "stolen", "reentrancy", "flash loan", "drained",
                          "theft", "compromise"],
    "regulatory":        ["sec", "cftc", "doj", "fbi", "regulatory", "compliance",
                          "lawsuit", "ban", "enforcement", "subpoena", "penalty",
                          "fine", "indictment", "crackdown", "probe"],
    "protocol_upgrade":  ["upgrade", "v2", "v3", "v4", "v5", "mainnet", "testnet",
                          "deployment", "launch", "release", "feature", "patch",
                          "update", "migration", "fork"],
    "adoption":          ["adoption", "institutional", "listing", "exchange",
                          "mainstream", "enterprise", "etf", "fund", "custody",
                          "integration", "partnership"],
    "governance":        ["governance", "proposal", "vote", "dao", "snapshot",
                          "on-chain vote", "community vote", "quorum"],
    "macro_crypto":      ["bitcoin", "ethereum", "crypto market", "fed",
                          "interest rate", "inflation", "recession",
                          "altcoin season", "bull market", "bear market",
                          "risk-off", "risk-on"],
    "price_speculation": ["price analysis", "price target", "prediction",
                          "forecast", "technical analysis", "chart pattern",
                          "resistance level", "support level", "breakout"],
}

# Category trading relevance weight (used in event signal scoring)
EVENT_RELEVANCE: Dict[str, float] = {
    "exploit_hack":      2.0,
    "regulatory":        1.8,
    "protocol_upgrade":  1.5,
    "adoption":          1.4,
    "governance":        1.2,
    "macro_crypto":      0.8,
    "price_speculation": 0.3,  # low — opinion, not news
}

SOURCE_CREDIBILITY: Dict[str, float] = {
    "theblock":       0.90,
    "the block":      0.90,
    "cointelegraph":  0.85,
    "decrypt":        0.85,
    "coindesk":       0.85,
    "blockworks":     0.80,
    "default":        0.65,
}


# ─── Helper functions ──────────────────────────────────────────────────────────

def _recency_weight(published_str: str, as_of_dt: datetime) -> float:
    """Exponential decay based on article age relative to as_of_dt."""
    if not published_str:
        return 0.50
    try:
        # Try ISO first, then common RSS date formats
        pub_dt: Optional[datetime] = None
        for fmt in (
            "%Y-%m-%dT%H:%M:%S%z",
            "%Y-%m-%dT%H:%M:%SZ",
            "%a, %d %b %Y %H:%M:%S %z",
            "%a, %d %b %Y %H:%M:%S GMT",
        ):
            try:
                pub_dt = datetime.strptime(published_str.strip(), fmt)
                break
            except ValueError:
                continue
        if pub_dt is None:
            pub_dt = datetime.fromisoformat(published_str.replace("Z", "+00:00"))

        if pub_dt.tzinfo is None:
            pub_dt = pub_dt.replace(tzinfo=timezone.utc)

        age_h = (as_of_dt - pub_dt).total_seconds() / 3600
        if age_h < 0:
            age_h = 0  # future-dated article — treat as fresh
        if age_h < 12:   return 1.00
        if age_h < 24:   return 0.85
        if age_h < 48:   return 0.70
        if age_h < 96:   return 0.55
        if age_h < 168:  return 0.40   # up to 7 days
        return 0.20
    except Exception:
        return 0.50


def _source_weight(source: str) -> float:
    src = (source or "").lower()
    for k, v in SOURCE_CREDIBILITY.items():
        if k in src:
            return v
    return SOURCE_CREDIBILITY["default"]


def _score_text(text: str) -> tuple[float, int, int]:
    """
    Keyword-based sentiment score for a single piece of text.
    Returns (raw_score, bullish_hits, bearish_hits).
    raw_score > 0 = net bullish, < 0 = net bearish.
    """
    t = text.lower()
    bull = sum(w for term, w in BULLISH_TERMS.items() if term in t)
    bear = sum(w for term, w in BEARISH_TERMS.items() if term in t)
    return float(bull - bear), bull, bear


def _detect_events(text: str) -> List[str]:
    t = text.lower()
    return [cat for cat, kws in EVENT_KEYWORDS.items() if any(kw in t for kw in kws)]


def _normalize(raw: float, scale: float = 8.0) -> float:
    """Clamp to [-1, +1]."""
    return max(-1.0, min(1.0, raw / scale))


# ─── Main entry point ──────────────────────────────────────────────────────────

def compute_sentiment_snapshot(
    articles: List[Dict[str, Any]],
    token_symbol: str,
    as_of_date: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Deterministically compute a structured sentiment snapshot from article list.

    Each article dict should have:
      title, summary, published, source, link  (all optional but improve quality)

    Returns a flat, JSON-serialisable dict. Contract mirrors technical_indicators
    compute_technical_snapshot output so downstream consumers have a consistent shape.

    Bias thresholds (sentiment_score is −1 to +1):
      STRONG_BULL  >= +0.35
      BULL         >= +0.10
      NEUTRAL      (-0.10, +0.10)
      BEAR         <= −0.10
      STRONG_BEAR  <= −0.35

    Conviction = min(|sentiment_score| / 0.50, 1.0)
    """
    as_of_dt = (
        datetime.fromisoformat(str(as_of_date)).replace(tzinfo=timezone.utc)
        if as_of_date
        else datetime.now(timezone.utc)
    )

    if not articles:
        return {
            "token":                   token_symbol,
            "as_of":                   as_of_dt.isoformat(),
            "article_count":           0,
            "sentiment_score":         0.0,
            "sentiment_bias":          "NEUTRAL",
            "conviction":              0.0,
            "sentiment_momentum":      "stable",
            "event_breakdown":         {},
            "high_impact_events":      [],
            "bullish_article_count":   0,
            "bearish_article_count":   0,
            "neutral_article_count":   0,
            "top_articles":            [],
            "bullish_themes":          [],
            "bearish_themes":          [],
            "data_quality_note":       "No articles found — sentiment_score unreliable.",
        }

    # ── Per-article scoring ────────────────────────────────────────────────────
    scored: List[Dict[str, Any]] = []
    for art in articles:
        text = f"{art.get('title', '')} {art.get('summary', '')}"
        raw_score, bull_hits, bear_hits = _score_text(text)
        events    = _detect_events(text)
        rec_w     = _recency_weight(art.get("published", ""), as_of_dt)
        src_w     = _source_weight(art.get("source", ""))
        weight    = rec_w * src_w

        # Boost weight for high-relevance event categories
        if events:
            event_boost = max(EVENT_RELEVANCE.get(e, 1.0) for e in events)
            weight *= min(event_boost, 2.0)  # cap at 2× boost

        scored.append({
            "title":          art.get("title", "")[:120],
            "source":         art.get("source", ""),
            "published":      art.get("published", ""),
            "link":           art.get("link", ""),
            "raw_score":      raw_score,
            "bull_hits":      bull_hits,
            "bear_hits":      bear_hits,
            "recency_weight": round(rec_w, 3),
            "source_weight":  round(src_w, 3),
            "final_weight":   round(weight, 3),
            "weighted_score": round(raw_score * weight, 3),
            "events":         events,
            "norm_score":     round(_normalize(raw_score), 3),
        })

    # ── Weighted aggregate ────────────────────────────────────────────────────
    total_weight = sum(a["final_weight"] for a in scored)
    agg_score    = (
        sum(a["weighted_score"] for a in scored) / total_weight
        if total_weight > 0
        else 0.0
    )
    norm_agg = _normalize(agg_score)

    if   norm_agg >= 0.35:  bias = "STRONG_BULL"
    elif norm_agg >= 0.10:  bias = "BULL"
    elif norm_agg <= -0.35: bias = "STRONG_BEAR"
    elif norm_agg <= -0.10: bias = "BEAR"
    else:                   bias = "NEUTRAL"

    conviction = round(min(abs(norm_agg) / 0.50, 1.0), 3)

    # ── Event breakdown ───────────────────────────────────────────────────────
    event_counts: Dict[str, int] = {}
    for art in scored:
        for ev in art["events"]:
            event_counts[ev] = event_counts.get(ev, 0) + 1

    high_impact = [
        e for e in event_counts
        if EVENT_RELEVANCE.get(e, 0) >= 1.4
    ]

    # ── Sentiment momentum ────────────────────────────────────────────────────
    # Sort by published date; compare recent half vs early half
    time_sorted = sorted(
        [a for a in scored if a["published"]],
        key=lambda x: x["published"],
    )
    mid = max(1, len(time_sorted) // 2)
    early  = time_sorted[:mid]
    recent = time_sorted[mid:]

    def _avg_score(subset: List[Dict]) -> float:
        return sum(a["raw_score"] for a in subset) / len(subset) if subset else 0.0

    early_avg  = _avg_score(early)
    recent_avg = _avg_score(recent)
    delta = recent_avg - early_avg
    if   delta >  0.5:  momentum = "improving"
    elif delta < -0.5:  momentum = "deteriorating"
    else:               momentum = "stable"

    # ── Article buckets ───────────────────────────────────────────────────────
    bull_arts    = [a for a in scored if a["raw_score"] > 0]
    bear_arts    = [a for a in scored if a["raw_score"] < 0]
    neutral_arts = [a for a in scored if a["raw_score"] == 0]

    top5 = sorted(scored, key=lambda x: abs(x["weighted_score"]), reverse=True)[:5]
    bull_top3 = sorted(bull_arts, key=lambda x: x["weighted_score"], reverse=True)[:3]
    bear_top3 = sorted(bear_arts, key=lambda x: x["weighted_score"])[:3]

    return {
        "token":                   token_symbol,
        "as_of":                   as_of_dt.isoformat(),
        "article_count":           len(articles),
        # ── Core signal ──
        "sentiment_score":         round(norm_agg, 3),  # −1.0 to +1.0
        "sentiment_bias":          bias,                # STRONG_BULL … STRONG_BEAR
        "conviction":              conviction,          # 0.0 → 1.0
        "sentiment_momentum":      momentum,            # improving / stable / deteriorating
        # ── Event breakdown ──
        "event_breakdown":         event_counts,
        "high_impact_events":      high_impact,
        # ── Article counts ──
        "bullish_article_count":   len(bull_arts),
        "bearish_article_count":   len(bear_arts),
        "neutral_article_count":   len(neutral_arts),
        # ── Top articles (for LLM qualitative read) ──
        "top_articles":            top5,
        "bullish_themes":          [a["title"] for a in bull_top3],
        "bearish_themes":          [a["title"] for a in bear_top3],
    }
