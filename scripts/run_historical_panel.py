#!/usr/bin/env python
"""
Phase 5 Week 18: Mode 1 historical agent backtest panel.

Runs the full multi-agent pipeline (Arm A) AND the P6 single-agent
ablation baseline (Arm B, same analyst reports, no debate -- see
tradingagents/ablation/) at a curated set of real historical decision
points, across the 7-token panel, spanning both default models'
self-reported knowledge cutoffs (gpt-4o-mini: Oct 2023, o4-mini: June 2024
-- see writing/papers/PROGRESS_LOG.md 2026-06-22).

Scope decisions made before building this (see BUILD_PLAN.md Week 18):
  - 3-analyst configuration (technical, onchain, tokenomics) for historical
    decisions -- the Sentiment/News analyst's RSS tools cannot retrieve
    historical news (no archive), so it is dropped rather than kept with a
    permanently-empty "unavailable" message. This differs from the 4-analyst
    live runs in Weeks 17/19.
  - Technical analyst: real cached Yahoo Finance OHLCV (no look-ahead).
  - On-chain analyst: real on-chain liquidity/supply at the resolved
    historical block (ETH/UNI/AAVE liquidity; BTC/ETH/UNI/AAVE supply).
    Holder/transaction data (Dune) has no date filter and stays current-only
    with an explicit caveat (see agent_utils.py).
  - Tokenomics: market cap via real historical price x real on-chain supply
    (UNI/AAVE) or a static circulating-supply estimate (BTC/ETH/SOL) --
    see CryptoDataProvider.get_historical_crypto_snapshot's docstring.
  - SOL/ZEC/XMR: on-chain liquidity/supply tools correctly return "not
    configured" regardless of date (non-EVM, by design -- see
    BUILD_PLAN.md's token-selection-criteria entry), same as live mode.

Decision points (28 = 4 dates x 7 tokens) are fixed in advance, not
selected after seeing results, to avoid P2's ex-post-cleaned-sample
failure mode: one date well before either model's cutoff, one between the
two cutoffs, one shortly after the later cutoff, one near the end of the
cached window (leaving room for forward-return evaluation).

Real LLM cost: comparable to ~28x a single live e2e run for Arm A (the full
debate pipeline), plus a much smaller increment for Arm B (the single-agent
baseline runs in ~5-10s with 2 LLM calls vs Arm A's ~150-200s/7-9 calls --
see Week 19's real run data in PROGRESS_LOG.md).

Usage:
    python scripts/run_historical_panel.py                  # full panel
    python scripts/run_historical_panel.py --limit 1         # one point, for validation
"""

import argparse
import json
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from dotenv import load_dotenv

load_dotenv()

DECISION_DATES = ["2022-06-01", "2023-12-01", "2024-08-01", "2025-05-01"]
TOKENS = ["BTC", "ETH", "SOL", "UNI", "AAVE", "ZEC", "XMR"]
FORWARD_HORIZONS_DAYS = [7, 30]
SELECTED_ANALYSTS = ["technical", "onchain", "tokenomics"]


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--llm-provider", default="openai")
    parser.add_argument("--deep-think-llm", default="o4-mini")
    parser.add_argument("--quick-think-llm", default="gpt-4o-mini")
    parser.add_argument("--limit", type=int, default=None, help="Only run the first N decision points (for validation).")
    parser.add_argument("--out-dir", default="eval_results/week18_panel")
    return parser.parse_args()


def compute_forward_returns(symbol: str, decision_date: str):
    from tradingagents.dataflows.historical_data import HistoricalDataCache
    from tradingagents.dataflows.crypto_utils import HISTORICAL_YAHOO_TICKERS

    yahoo_ticker = HISTORICAL_YAHOO_TICKERS[symbol]
    decision = date.fromisoformat(decision_date)
    cache = HistoricalDataCache()
    start = datetime.combine(decision - timedelta(days=5), datetime.min.time())
    end = datetime.combine(decision + timedelta(days=max(FORWARD_HORIZONS_DAYS) + 5), datetime.min.time())
    df = cache.get(symbol, yahoo_ticker, start, end, source="yahoo")
    if df.empty:
        return {"error": "no OHLCV available"}

    df = df.set_index(df["timestamp"].dt.date)
    available_dates = sorted(df.index)

    def price_on_or_before(d):
        candidates = [x for x in available_dates if x <= d]
        return float(df.loc[max(candidates), "close"]) if candidates else None

    def price_on_or_after(d):
        candidates = [x for x in available_dates if x >= d]
        return float(df.loc[min(candidates), "close"]) if candidates else None

    decision_price = price_on_or_before(decision)
    result = {"decision_price": decision_price}
    for horizon in FORWARD_HORIZONS_DAYS:
        future_price = price_on_or_after(decision + timedelta(days=horizon))
        if decision_price and future_price:
            result[f"return_{horizon}d_pct"] = (future_price - decision_price) / decision_price * 100
        else:
            result[f"return_{horizon}d_pct"] = None
    return result


def run_one_point(graph, ticker, trade_date, out_dir):
    from tradingagents.ablation import compute_role_similarity

    print(f"\n{'='*70}\n{ticker} @ {trade_date}\n{'='*70}")

    graph.reset_llm_call_stats()
    wall_start = datetime.now(timezone.utc)
    final_state, multi_agent_signal = graph.propagate(ticker, trade_date)
    multi_agent_wall_s = (datetime.now(timezone.utc) - wall_start).total_seconds()
    multi_agent_stats = graph.get_llm_call_stats()
    print(f"Arm A (multi-agent): {multi_agent_signal}, confidence={final_state.get('raw_confidence')}, "
          f"wall_clock={multi_agent_wall_s:.1f}s, calls={multi_agent_stats['call_count']}")

    baseline = graph.build_single_agent_baseline(use_memory=True)
    graph.reset_llm_call_stats()
    wall_start = datetime.now(timezone.utc)
    single_result = baseline.decide(
        ticker=ticker,
        trade_date=trade_date,
        technical_report=final_state.get("technical_report", ""),
        onchain_report=final_state.get("onchain_report", ""),
        tokenomics_report=final_state.get("tokenomics_report", ""),
        sentiment_news_report=final_state.get("sentiment_news_report", "") or "(not run in 3-analyst historical mode)",
    )
    single_agent_signal = graph.process_signal(single_result["full_response"])
    single_agent_wall_s = (datetime.now(timezone.utc) - wall_start).total_seconds()
    single_agent_stats = graph.get_llm_call_stats()
    print(f"Arm B (single-agent): {single_agent_signal}, confidence={single_result['raw_confidence']}, "
          f"wall_clock={single_agent_wall_s:.1f}s, calls={single_agent_stats['call_count']}")

    role_similarity = compute_role_similarity(
        final_state.get("investment_debate_state", {}),
        final_state.get("risk_debate_state", {}),
    )

    forward_returns = compute_forward_returns(ticker, trade_date)
    print(f"Forward returns: {forward_returns}")

    artifact = {
        "ticker": ticker,
        "trade_date": trade_date,
        "selected_analysts": SELECTED_ANALYSTS,
        "forward_returns": forward_returns,
        "multi_agent": {
            "decision": multi_agent_signal,
            "raw_confidence": final_state.get("raw_confidence"),
            "wall_clock_s": round(multi_agent_wall_s, 2),
            "llm_call_stats": multi_agent_stats,
            "final_trade_decision": final_state.get("final_trade_decision"),
            "investment_debate_state": final_state.get("investment_debate_state"),
            "risk_debate_state": final_state.get("risk_debate_state"),
            "investment_plan": final_state.get("investment_plan"),
        },
        "single_agent": {
            "decision": single_agent_signal,
            "raw_confidence": single_result["raw_confidence"],
            "wall_clock_s": round(single_agent_wall_s, 2),
            "llm_call_stats": single_agent_stats,
            "full_response": single_result["full_response"],
        },
        "role_similarity": role_similarity,
        "decisions_agree": multi_agent_signal.strip().upper() == single_agent_signal.strip().upper(),
        "reports": {
            "technical_report": final_state.get("technical_report"),
            "onchain_report": final_state.get("onchain_report"),
            "tokenomics_report": final_state.get("tokenomics_report"),
        },
    }

    out_path = Path(out_dir) / f"{ticker}_{trade_date}.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(artifact, f, indent=2, default=str)
    print(f"Saved {out_path}")
    return artifact


def main():
    args = parse_args()
    from tradingagents.default_config import DEFAULT_CONFIG
    from tradingagents.graph.trading_graph import TradingAgentsGraph

    config = {
        **DEFAULT_CONFIG,
        "llm_provider": args.llm_provider,
        "deep_think_llm": args.deep_think_llm,
        "quick_think_llm": args.quick_think_llm,
        "max_debate_rounds": 1,
        "max_risk_discuss_rounds": 1,
    }

    points = [(t, d) for t in TOKENS for d in DECISION_DATES]
    if args.limit:
        points = points[: args.limit]

    print(f"Running {len(points)} decision point(s): {points}")
    graph = TradingAgentsGraph(debug=False, config=config, selected_analysts=SELECTED_ANALYSTS)

    results = []
    for ticker, trade_date in points:
        try:
            results.append(run_one_point(graph, ticker, trade_date, args.out_dir))
        except Exception as e:
            print(f"ERROR on {ticker}@{trade_date}: {e}")
            results.append({"ticker": ticker, "trade_date": trade_date, "error": str(e)})

    summary_path = Path(args.out_dir) / "_summary.json"
    with open(summary_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nDone. {len(results)} points run. Summary: {summary_path}")


if __name__ == "__main__":
    main()
