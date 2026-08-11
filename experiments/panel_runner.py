"""
Point-in-time panel runner for the FC27 DeFi Workshop experiment design.

Each panel point = one (token, date) pair → one agent decision (BUY/HOLD/SELL).
Ground truth = 7-day forward return sourced from Yahoo Finance cache.
Hit rate = directional accuracy, stratified by contamination bucket.

Usage:
    from experiments.panel_runner import PanelRunner
    runner = PanelRunner()
    results = runner.run_panel(tokens=["ETH", "AAVE"], dates=["2025-03-15"])
    runner.print_summary(results)
"""

from __future__ import annotations

import json
import os
import sys
import traceback
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import math

import pandas as pd

sys.path.insert(0, str(Path(__file__).parent.parent))

from experiments.config import (
    PANEL_TOKENS,
    PANEL_DATES,
    CONTAMINATION_BUCKETS,
    GROUND_TRUTH_CONFIG,
    get_panel_tokens_for_date,
    get_panel_points,
    AGENT_ARCHITECTURES,
)


def _extract_decision(decision_str: str) -> str:
    """Parse BUY / HOLD / SELL from the agent's final decision string."""
    if not decision_str:
        return "HOLD"
    upper = decision_str.upper()
    if "BUY" in upper:
        return "BUY"
    if "SELL" in upper:
        return "SELL"
    return "HOLD"


def _get_7d_forward_return(yahoo_ticker: str, panel_date: str) -> Optional[float]:
    """
    Compute 7-day forward return from Yahoo Finance cache.
    Returns None if price data is unavailable.
    """
    try:
        import yfinance as yf
        panel_dt  = datetime.strptime(panel_date, "%Y-%m-%d")
        start_str = (panel_dt - timedelta(days=2)).strftime("%Y-%m-%d")
        end_str   = (panel_dt + timedelta(days=10)).strftime("%Y-%m-%d")
        df = yf.download(yahoo_ticker, start=start_str, end=end_str,
                         auto_adjust=True, progress=False)
        if df.empty:
            return None
        # Closest close on or after panel_date
        df.index = pd.to_datetime(df.index)
        entry_rows = df[df.index >= panel_dt]
        exit_rows  = df[df.index >= panel_dt + timedelta(days=GROUND_TRUTH_CONFIG["forward_days"])]
        if entry_rows.empty or exit_rows.empty:
            return None
        # Handle MultiIndex columns (yfinance sometimes returns them)
        close = df["Close"]
        if isinstance(close, pd.DataFrame):
            close = close.iloc[:, 0]
        entry_price = float(close[entry_rows.index[0]])
        exit_price  = float(close[exit_rows.index[0]])
        return (exit_price - entry_price) / entry_price
    except Exception:
        return None


def _score_decision(decision: str, fwd_return: Optional[float]) -> Optional[bool]:
    """
    True  = correct directional call
    False = incorrect directional call
    None  = HOLD (evaluated on reasoning quality, excluded from hit rate)
    """
    if fwd_return is None:
        return None
    buy_thresh  = GROUND_TRUTH_CONFIG["buy_threshold"]
    sell_thresh = GROUND_TRUTH_CONFIG["sell_threshold"]
    if decision == "BUY":
        return fwd_return > buy_thresh
    if decision == "SELL":
        return fwd_return < sell_thresh
    return None  # HOLD


class PanelRunner:
    """Run the FC27 point-in-time panel and score decisions."""

    def __init__(self, results_dir: str = "./experiments/panel_results"):
        self.results_dir = Path(results_dir)
        self.results_dir.mkdir(parents=True, exist_ok=True)

    # ── Core execution ────────────────────────────────────────────────────────

    def run_panel_point(
        self,
        token: str,
        date: str,
        architecture: str = "role_based",
        run_ablation: bool = True,
    ) -> Dict[str, Any]:
        """
        Run a single (token, date) panel point.

        Runs Arm A (multi-agent debate) and, when run_ablation=True, Arm B
        (single-agent baseline using the same analyst reports — P6 requirement).
        Saves both decisions so McNemar's test can be computed offline.
        """
        from tradingagents.graph.trading_graph import TradingAgentsGraph
        from tradingagents.ablation import LLMCallTracker

        token_info = PANEL_TOKENS.get(token)
        if token_info is None:
            return {"error": f"Unknown token {token}", "token": token, "date": date}

        analysts = AGENT_ARCHITECTURES[architecture]["analysts"]

        print(f"  [{token} @ {date}] starting {architecture} agent...")

        result: Dict[str, Any] = {
            "token":        token,
            "date":         date,
            "architecture": architecture,
            "tier":         token_info["tier"],
            "liquidity":    token_info["liquidity_tier"],
            "regime":       self._get_regime(date),
            "cutoff":       self._get_cutoff(date),
            "ran_at":       datetime.utcnow().isoformat(),
        }

        try:
            tracker = LLMCallTracker()
            graph = TradingAgentsGraph(
                selected_analysts=analysts,
                debug=False,
            )
            # Wire the tracker into the graph so all LLM calls are counted
            graph.llm_call_tracker = tracker

            final_state, raw_decision = graph.propagate(token, date)

            decision = _extract_decision(raw_decision)
            result["raw_decision"]    = raw_decision
            result["decision"]        = decision
            result["technical_report"]  = final_state.get("technical_report", "")
            result["onchain_report"]    = final_state.get("onchain_report", "")
            result["tokenomics_report"] = final_state.get("tokenomics_report", "")
            result["sentiment_report"]  = final_state.get("sentiment_news_report", "")
            result["trader_decision"]   = final_state.get("final_trade_decision", "")
            result["llm_tracker_arm_a"] = tracker.summary()

            # Arm B: single-agent baseline using the SAME analyst reports (P6)
            if run_ablation:
                try:
                    baseline = graph.build_single_agent_baseline(use_memory=False)
                    ablation_out = baseline.decide(
                        ticker=token,
                        trade_date=date,
                        technical_report=result["technical_report"],
                        onchain_report=result["onchain_report"],
                        tokenomics_report=result["tokenomics_report"],
                        sentiment_news_report=result["sentiment_report"],
                    )
                    result["single_agent_decision"] = _extract_decision(
                        ablation_out.get("full_response", "")
                    )
                    result["single_agent_raw"]      = ablation_out.get("full_response", "")
                    result["single_agent_confidence"] = ablation_out.get("raw_confidence")
                    result["single_agent_latency_s"]  = ablation_out.get("latency_s")
                except Exception as abl_exc:
                    result["single_agent_decision"] = "HOLD"
                    result["single_agent_error"]    = str(abl_exc)
                    print(f"  [{token} @ {date}] ablation ERROR: {abl_exc}")

        except Exception as exc:
            result["error"]    = str(exc)
            result["decision"] = "HOLD"
            result["traceback"]= traceback.format_exc()
            print(f"  [{token} @ {date}] ERROR: {exc}")

        # Ground truth
        yahoo_ticker = token_info["yahoo_ticker"]
        fwd_return   = _get_7d_forward_return(yahoo_ticker, date)
        result["fwd_return_7d"] = fwd_return
        result["correct"]       = _score_decision(result["decision"], fwd_return)

        self._save_point(result)
        return result

    def run_panel(
        self,
        tokens: Optional[List[str]] = None,
        dates: Optional[List[str]] = None,
        architecture: str = "role_based",
        skip_existing: bool = True,
    ) -> List[Dict[str, Any]]:
        """
        Run all (token, date) combinations.

        tokens / dates: pass None to use the full panel config.
        skip_existing:  skip (token, date) pairs already saved to disk.
        """
        if tokens is None:
            tokens = list(PANEL_TOKENS.keys())
        if dates is None:
            dates = [d["date"] for d in PANEL_DATES]

        panel_points = [
            (tok, dt) for dt in dates for tok in tokens
            if tok in get_panel_tokens_for_date(dt)
        ]

        print(f"Panel: {len(panel_points)} points | arch={architecture}")
        print(f"Tokens: {tokens}")
        print(f"Dates:  {dates}\n")

        results: List[Dict[str, Any]] = []
        for i, (token, date) in enumerate(panel_points, 1):
            print(f"[{i}/{len(panel_points)}] {token} @ {date}")
            if skip_existing and self._point_exists(token, date, architecture):
                print(f"  skipped (already saved)")
                results.append(self._load_point(token, date, architecture))
                continue
            result = self.run_panel_point(token, date, architecture)
            results.append(result)
            dec = result.get("decision", "?")
            fwd = result.get("fwd_return_7d")
            cor = result.get("correct")
            fwd_str = f"{fwd:+.1%}" if fwd is not None else "n/a"
            cor_str = "✓" if cor is True else ("✗" if cor is False else "—")
            print(f"  → {dec} | 7d fwd={fwd_str} | {cor_str}")

        return results

    # ── Analysis ──────────────────────────────────────────────────────────────

    def compute_hit_rates(self, results: List[Dict]) -> Dict[str, Any]:
        """
        Compute hit rates stratified by contamination bucket and tier.
        Returns a dict suitable for printing or JSON serialisation.
        """
        def _bucket_stats(points: List[Dict]) -> Dict:
            directional = [p for p in points if p.get("decision") in ("BUY", "SELL")]
            correct     = [p for p in directional if p.get("correct") is True]
            hold_count  = sum(1 for p in points if p.get("decision") == "HOLD")
            scored      = [p for p in directional if p.get("correct") is not None]
            return {
                "n_points":        len(points),
                "n_directional":   len(scored),
                "n_correct":       len(correct),
                "n_hold":          hold_count,
                "hit_rate":        len(correct) / len(scored) if scored else None,
                "buy_count":       sum(1 for p in scored if p["decision"] == "BUY"),
                "sell_count":      sum(1 for p in scored if p["decision"] == "SELL"),
                "error_count":     sum(1 for p in points if "error" in p),
            }

        all_stats = _bucket_stats(results)

        buckets: Dict[str, Any] = {}
        for bucket_name, dates in CONTAMINATION_BUCKETS.items():
            bucket_pts = [r for r in results if r.get("date") in dates and r.get("tier") == 1]
            buckets[bucket_name] = _bucket_stats(bucket_pts)

        tier1 = [r for r in results if r.get("tier") == 1]
        tier2 = [r for r in results if r.get("tier") == 2]

        by_token: Dict[str, Dict] = {}
        for tok in set(r.get("token") for r in results):
            by_token[tok] = _bucket_stats([r for r in results if r.get("token") == tok])

        return {
            "overall":                  all_stats,
            "by_contamination_bucket":  buckets,
            "tier1":                    _bucket_stats(tier1),
            "tier2":                    _bucket_stats(tier2),
            "by_token":                 by_token,
        }

    def print_summary(self, results: List[Dict]) -> None:
        """Print a concise panel summary to stdout."""
        stats = self.compute_hit_rates(results)

        print("\n" + "="*70)
        print("FC27 PANEL RESULTS SUMMARY")
        print("="*70)

        ov = stats["overall"]
        print(f"\nOverall:  {ov['n_points']} points | "
              f"{ov['n_directional']} directional | "
              f"hit rate = {ov['hit_rate']:.1%}" if ov['hit_rate'] is not None
              else f"\nOverall:  {ov['n_points']} points | hit rate = n/a")

        print("\nContamination stratification (Tier 1 only):")
        for bucket, s in stats["by_contamination_bucket"].items():
            hr = f"{s['hit_rate']:.1%}" if s["hit_rate"] is not None else "n/a"
            print(f"  {bucket:12s}: n={s['n_directional']:3d} | hit rate={hr}")

        print("\nBy token:")
        for tok, s in sorted(stats["by_token"].items()):
            hr  = f"{s['hit_rate']:.1%}" if s["hit_rate"] is not None else "n/a"
            err = f" ({s['error_count']} errors)" if s["error_count"] else ""
            print(f"  {tok:6s}: {s['n_directional']:2d} directional | {hr}{err}")

        print("\nDecision breakdown:")
        print(f"  BUY={sum(1 for r in results if r.get('decision')=='BUY')} | "
              f"SELL={sum(1 for r in results if r.get('decision')=='SELL')} | "
              f"HOLD={sum(1 for r in results if r.get('decision')=='HOLD')}")

        print(f"\nResults saved to: {self.results_dir.resolve()}")
        print("="*70 + "\n")

    # ── Persistence ───────────────────────────────────────────────────────────

    def _point_path(self, token: str, date: str, architecture: str) -> Path:
        fname = f"{token}_{date}_{architecture}.json"
        return self.results_dir / fname

    def _point_exists(self, token: str, date: str, architecture: str) -> bool:
        path = self._point_path(token, date, architecture)
        if not path.exists():
            return False
        # Re-run if the saved result predates the two-arm design (no ablation field)
        try:
            with open(path) as f:
                r = json.load(f)
            return "single_agent_decision" in r
        except Exception:
            return False

    def _save_point(self, result: Dict) -> None:
        path = self._point_path(
            result["token"], result["date"], result.get("architecture", "role_based")
        )
        with open(path, "w") as f:
            json.dump(result, f, indent=2, default=str)

    def _load_point(self, token: str, date: str, architecture: str) -> Dict:
        path = self._point_path(token, date, architecture)
        with open(path) as f:
            return json.load(f)

    def load_all_results(self, architecture: str = "role_based") -> List[Dict]:
        """Load all saved panel results for a given architecture."""
        results = []
        for path in sorted(self.results_dir.glob(f"*_{architecture}.json")):
            with open(path) as f:
                results.append(json.load(f))
        return results

    # ── Statistical tests (RQ1 and RQ3) ──────────────────────────────────────

    @staticmethod
    def mcnemar_test(
        multi_decisions: List[str],
        single_decisions: List[str],
    ) -> Dict[str, Any]:
        """McNemar's test for RQ1: does debate change decisions systematically?

        Operates on paired (multi-agent, single-agent) decision lists. Counts
        discordant pairs (where the two arms disagree on directional vs. HOLD)
        and applies Yates-corrected chi-squared. At small n, this test has low
        power -- report alongside n_discordant so readers can judge.

        Returns chi2, p_value, n_discordant, n_concordant, n_total.
        """
        if len(multi_decisions) != len(single_decisions):
            raise ValueError("Decision lists must be the same length")

        # b = multi=directional but single=HOLD; c = single=directional but multi=HOLD
        b, c = 0, 0
        n_concordant = 0
        for m, s in zip(multi_decisions, single_decisions):
            m_dir = m in ("BUY", "SELL")
            s_dir = s in ("BUY", "SELL")
            if m_dir and not s_dir:
                b += 1
            elif s_dir and not m_dir:
                c += 1
            else:
                n_concordant += 1

        n_discordant = b + c
        n_total = len(multi_decisions)

        if n_discordant == 0:
            return {
                "chi2": 0.0,
                "p_value": 1.0,
                "n_discordant": 0,
                "n_concordant": n_concordant,
                "n_total": n_total,
                "note": "No discordant pairs — test undefined",
            }

        # Yates continuity correction: chi2 = (|b-c| - 1)^2 / (b+c)
        chi2 = (abs(b - c) - 1) ** 2 / n_discordant
        # chi2 distribution with 1 degree of freedom, survival function
        # Approximation: p-value = P(chi2(1) > observed)
        # Using incomplete gamma: p = 1 - regularized_gamma(0.5, chi2/2)
        # scipy.stats.chi2.sf is ideal; fall back to a pure-math approximation
        try:
            from scipy.stats import chi2 as chi2_dist
            p_value = float(chi2_dist.sf(chi2, df=1))
        except ImportError:
            # Accurate normal approximation for chi2(1): p ≈ erfc(sqrt(chi2/2) / sqrt(2))
            p_value = math.erfc(math.sqrt(chi2 / 2) / math.sqrt(2))

        return {
            "chi2": round(chi2, 4),
            "p_value": round(p_value, 4),
            "n_discordant": n_discordant,
            "n_concordant": n_concordant,
            "n_total": n_total,
            "b_multi_dir_single_hold": b,
            "c_single_dir_multi_hold": c,
        }

    @staticmethod
    def contamination_proportion_test(
        pre_results: List[Dict],
        post_results: List[Dict],
    ) -> Dict[str, Any]:
        """Two-sample proportion test for RQ3: does hit rate degrade post-cutoff?

        Filters each list to directional calls (BUY/SELL, not HOLD) with
        known outcomes. Tests H0: pre-cutoff hit rate == post-cutoff hit rate
        using a two-sample z-test for proportions. Reports estimated statistical
        power at the observed sample sizes -- the experiment design notes that
        n < 60 total gives only ~0.65 power at the expected effect size.
        """
        def _directional(results: List[Dict]) -> List[Dict]:
            return [r for r in results
                    if r.get("decision") in ("BUY", "SELL") and r.get("correct") is not None]

        pre_dir  = _directional(pre_results)
        post_dir = _directional(post_results)
        n1, n2   = len(pre_dir), len(post_dir)

        if n1 == 0 or n2 == 0:
            return {
                "pre_hit_rate":  sum(1 for r in pre_dir  if r["correct"]) / n1 if n1 else None,
                "post_hit_rate": sum(1 for r in post_dir if r["correct"]) / n2 if n2 else None,
                "z_stat": None, "p_value": None, "power_note": None,
                "note": f"Insufficient directional calls (pre={n1}, post={n2})",
            }

        p1 = sum(1 for r in pre_dir  if r["correct"]) / n1  # pre-cutoff hit rate
        p2 = sum(1 for r in post_dir if r["correct"]) / n2  # post-cutoff hit rate

        # Pooled proportion under H0
        p_pool = (p1 * n1 + p2 * n2) / (n1 + n2)
        se = math.sqrt(p_pool * (1 - p_pool) * (1/n1 + 1/n2))
        z_stat = (p1 - p2) / se if se > 0 else 0.0
        # One-tailed p-value (H_a: pre > post, i.e. contamination inflates pre)
        try:
            from scipy.stats import norm
            p_value = float(norm.sf(z_stat))
        except ImportError:
            p_value = 0.5 * math.erfc(z_stat / math.sqrt(2))

        # Power note: design doc threshold is 60 total directional calls for 0.80
        total = n1 + n2
        power_note = (
            f"n={total} total directional calls — below the ~60-point threshold "
            f"for 0.80 power at the expected effect size. Treat as suggestive."
            if total < 60 else
            f"n={total} total directional calls — adequate for the primary contamination test."
        )

        return {
            "pre_hit_rate":  round(p1, 4),
            "post_hit_rate": round(p2, 4),
            "pre_n":  n1,
            "post_n": n2,
            "z_stat":  round(z_stat, 4),
            "p_value": round(p_value, 4),
            "power_note": power_note,
        }

    def run_statistical_analysis(self, results: List[Dict]) -> Dict[str, Any]:
        """Run RQ1 (McNemar) and RQ3 (proportion test) after a panel completes.

        Expects results that include both 'decision' (multi-agent) and optionally
        'single_agent_decision' fields. If single-agent decisions are absent,
        McNemar's test is skipped with a note.
        """
        print("\n" + "="*70)
        print("STATISTICAL ANALYSIS")
        print("="*70)

        # RQ3: contamination proportion test (Tier 1 only)
        pre_pts  = [r for r in results if r.get("cutoff") == "pre_cutoff"  and r.get("tier") == 1]
        post_pts = [r for r in results if r.get("cutoff") == "post_cutoff" and r.get("tier") == 1]
        prop_result = self.contamination_proportion_test(pre_pts, post_pts)
        print("\nRQ3 — Contamination proportion test (Tier 1, pre vs. post cutoff):")
        if prop_result.get("z_stat") is not None:
            print(f"  Pre-cutoff hit rate:  {prop_result['pre_hit_rate']:.1%} (n={prop_result['pre_n']})")
            print(f"  Post-cutoff hit rate: {prop_result['post_hit_rate']:.1%} (n={prop_result['post_n']})")
            print(f"  z = {prop_result['z_stat']}, p = {prop_result['p_value']} (one-tailed, H_a: pre > post)")
            print(f"  {prop_result['power_note']}")
        else:
            print(f"  {prop_result.get('note', 'n/a')}")

        # RQ1: McNemar's test (only if single-agent decisions are present)
        paired = [r for r in results if "single_agent_decision" in r]
        mcnemar_result: Optional[Dict] = None
        print("\nRQ1 — McNemar's test (multi-agent vs. single-agent):")
        if not paired:
            print("  No single_agent_decision field found — run P6 ablation to populate.")
        else:
            multi_dec  = [r["decision"] for r in paired]
            single_dec = [r["single_agent_decision"] for r in paired]
            mcnemar_result = self.mcnemar_test(multi_dec, single_dec)
            print(f"  n_total={mcnemar_result['n_total']}, n_discordant={mcnemar_result['n_discordant']}")
            print(f"  chi2 = {mcnemar_result['chi2']}, p = {mcnemar_result['p_value']}")

        print("="*70 + "\n")

        return {
            "rq3_proportion_test": prop_result,
            "rq1_mcnemar": mcnemar_result,
        }

    # ── Helpers ───────────────────────────────────────────────────────────────

    def _get_regime(self, date: str) -> str:
        for d in PANEL_DATES:
            if d["date"] == date:
                return d["regime"]
        return "unknown"

    def _get_cutoff(self, date: str) -> str:
        for bucket, dates in CONTAMINATION_BUCKETS.items():
            if date in dates:
                return bucket
        return "unknown"
