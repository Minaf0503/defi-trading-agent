#!/usr/bin/env python
"""
Phase 5 Week 19: P6 (multi-agent disaggregation) ablation -- a real, live,
paired comparison of the full multi-agent debate pipeline against a single
LLM call given the same underlying analyst reports.

This is a LIVE decision (current data, no historical-as-of-date parameter --
same caveat as scripts/run_e2e_pipeline.py), and a SINGLE paired comparison,
not a backtest panel. What this script measures and what it does not:

  Measured here (per Alpha Illusion's P6 minimum reporting):
    - decision agreement (does the single agent reach the same BUY/HOLD/SELL
      call as the full debate pipeline, on identical underlying data)
    - confidence delta (raw self-reported confidence, both arms)
    - debate-round cost (LLM call count, both arms, via LLMCallTracker)
    - coordination latency (wall-clock time, both arms; the gap between
      wall-clock and the tracker's summed per-call latency is the
      multi-agent system's own coordination/tool-execution overhead, not
      LLM thinking time)
    - role similarity / a disagreement proxy (lexical word-overlap between
      bull/bear and risky/safe/neutral debate histories -- see
      tradingagents/ablation/role_similarity.py's caveat: this is a coarse
      proxy, not semantic stance classification)

  NOT measured here -- "multi-agent net-return delta" needs realized
  outcomes across MANY decision points over time, which a single paired
  live decision cannot provide. That requires running both arms across
  Phase 1's token panel or Week 8's fork-sim pilot's historical decision
  points and comparing realized returns -- a follow-up scale-out, not part
  of this script. Treat this script as having BUILT the comparable
  single-agent baseline + the instrumentation; running it at the scale
  needed for a real net-return-delta claim is separate future work.

Usage:
    python scripts/run_p6_ablation.py --ticker ETH
"""

import argparse
import json
import sys
from datetime import date, datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from dotenv import load_dotenv

load_dotenv()


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ticker", default="ETH")
    parser.add_argument("--llm-provider", default="openai")
    parser.add_argument("--deep-think-llm", default="o4-mini")
    parser.add_argument("--quick-think-llm", default="gpt-4o-mini")
    parser.add_argument(
        "--no-memory",
        action="store_true",
        help="Run the single-agent baseline without trader-memory lookup (default: WITH memory, "
        "matching the production Trader node, so the comparison isolates debate structure only).",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    from tradingagents.default_config import DEFAULT_CONFIG
    from tradingagents.graph.trading_graph import TradingAgentsGraph
    from tradingagents.ablation import compute_role_similarity

    config = {
        **DEFAULT_CONFIG,
        "llm_provider": args.llm_provider,
        "deep_think_llm": args.deep_think_llm,
        "quick_think_llm": args.quick_think_llm,
        "max_debate_rounds": 1,
        "max_risk_discuss_rounds": 1,
    }

    trade_date = date.today().isoformat()

    print(f"=== Arm A: full multi-agent debate pipeline for {args.ticker} on {trade_date} ===")
    graph = TradingAgentsGraph(debug=False, config=config)
    graph.reset_llm_call_stats()
    multi_agent_wall_start = datetime.now(timezone.utc)
    final_state, multi_agent_signal = graph.propagate(args.ticker, trade_date)
    multi_agent_wall_s = (datetime.now(timezone.utc) - multi_agent_wall_start).total_seconds()
    multi_agent_stats = graph.get_llm_call_stats()

    print(f"Decision: {multi_agent_signal}, raw_confidence: {final_state.get('raw_confidence')}")
    print(f"Wall-clock: {multi_agent_wall_s:.2f}s, LLM call stats: {multi_agent_stats}")

    print(f"\n=== Arm B: single-agent baseline, same analyst reports, no debate ===")
    baseline = graph.build_single_agent_baseline(use_memory=not args.no_memory)
    graph.reset_llm_call_stats()
    single_agent_wall_start = datetime.now(timezone.utc)
    single_agent_result = baseline.decide(
        ticker=args.ticker,
        trade_date=trade_date,
        technical_report=final_state.get("technical_report", ""),
        onchain_report=final_state.get("onchain_report", ""),
        tokenomics_report=final_state.get("tokenomics_report", ""),
        sentiment_news_report=final_state.get("sentiment_news_report", ""),
    )
    # Same decision-extraction step the full pipeline's propagate() applies
    # internally (process_signal), so both arms pay symmetric extraction
    # overhead rather than letting one arm "skip" a real cost the other pays.
    single_agent_signal = graph.process_signal(single_agent_result["full_response"])
    single_agent_wall_s = (datetime.now(timezone.utc) - single_agent_wall_start).total_seconds()
    single_agent_stats = graph.get_llm_call_stats()

    print(f"Decision: {single_agent_signal}, raw_confidence: {single_agent_result['raw_confidence']}")
    print(f"Wall-clock: {single_agent_wall_s:.2f}s, LLM call stats: {single_agent_stats}")

    print(f"\n=== Role similarity (bull/bear, risky/safe/neutral debate histories) ===")
    role_similarity = compute_role_similarity(
        final_state.get("investment_debate_state", {}),
        final_state.get("risk_debate_state", {}),
    )
    print(json.dumps(role_similarity, indent=2))

    invest_debate = final_state.get("investment_debate_state", {})
    risk_debate = final_state.get("risk_debate_state", {})
    print(f"\n=== Multi-agent debate transcript (full text saved to the artifact; excerpts below) ===")
    print(f"\n--- Bull Researcher ---\n{(invest_debate.get('bull_history') or '(empty)')[:1500]}")
    print(f"\n--- Bear Researcher ---\n{(invest_debate.get('bear_history') or '(empty)')[:1500]}")
    print(f"\n--- Research Manager's investment plan ---\n{(final_state.get('investment_plan') or '(empty)')[:1500]}")
    print(f"\n--- Trader's plan (pre-risk-debate) ---\n{(final_state.get('trader_investment_plan') or '(empty)')[:1500]}")
    print(f"\n--- Risky Analyst ---\n{(risk_debate.get('risky_history') or '(empty)')[:1500]}")
    print(f"\n--- Safe Analyst ---\n{(risk_debate.get('safe_history') or '(empty)')[:1500]}")
    print(f"\n--- Neutral Analyst ---\n{(risk_debate.get('neutral_history') or '(empty)')[:1500]}")
    print(f"\n--- Risk Judge's final_trade_decision ---\n{(final_state.get('final_trade_decision') or '(empty)')[:1500]}")

    print(f"\n=== Comparison ===")
    decisions_agree = multi_agent_signal.strip().upper() == single_agent_signal.strip().upper()
    raw_conf_a = final_state.get("raw_confidence")
    raw_conf_b = single_agent_result["raw_confidence"]
    confidence_delta = (raw_conf_a - raw_conf_b) if (raw_conf_a is not None and raw_conf_b is not None) else None

    comparison = {
        "decisions_agree": decisions_agree,
        "multi_agent_decision": multi_agent_signal,
        "single_agent_decision": single_agent_signal,
        "confidence_delta_multi_minus_single": confidence_delta,
        "call_count_delta_multi_minus_single": multi_agent_stats["call_count"] - single_agent_stats["call_count"],
        "wall_clock_delta_s_multi_minus_single": round(multi_agent_wall_s - single_agent_wall_s, 2),
        "multi_agent_coordination_overhead_s": round(multi_agent_wall_s - multi_agent_stats["total_latency_s"], 2),
        "single_agent_coordination_overhead_s": round(single_agent_wall_s - single_agent_stats["total_latency_s"], 2),
    }
    print(json.dumps(comparison, indent=2))

    print(
        "\nNote: this is a single paired live decision, not a net-return-delta claim -- "
        "that requires running both arms across many historical decision points with known "
        "outcomes (see this script's module docstring)."
    )

    out_dir = Path("eval_results") / args.ticker
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"p6_ablation_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json"
    artifact = {
        "ticker": args.ticker,
        "trade_date": trade_date,
        "config": config,
        "multi_agent": {
            "decision": multi_agent_signal,
            "raw_confidence": raw_conf_a,
            "wall_clock_s": round(multi_agent_wall_s, 2),
            "llm_call_stats": multi_agent_stats,
            "final_trade_decision": final_state.get("final_trade_decision"),
            "investment_debate_state": final_state.get("investment_debate_state"),
            "risk_debate_state": final_state.get("risk_debate_state"),
            "investment_plan": final_state.get("investment_plan"),
            "trader_investment_plan": final_state.get("trader_investment_plan"),
        },
        "single_agent": {
            "decision": single_agent_signal,
            "raw_confidence": raw_conf_b,
            "wall_clock_s": round(single_agent_wall_s, 2),
            "llm_call_stats": single_agent_stats,
            "full_response": single_agent_result["full_response"],
            "used_memory": not args.no_memory,
        },
        "role_similarity": role_similarity,
        "comparison": comparison,
        "reports": {
            "technical_report": final_state.get("technical_report"),
            "onchain_report": final_state.get("onchain_report"),
            "tokenomics_report": final_state.get("tokenomics_report"),
            "sentiment_news_report": final_state.get("sentiment_news_report"),
        },
    }
    with open(out_path, "w") as f:
        json.dump(artifact, f, indent=2, default=str)
    print(f"\nSaved full artifact to {out_path}")


if __name__ == "__main__":
    main()
