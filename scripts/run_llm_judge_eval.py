#!/usr/bin/env python
"""
Phase 5 Week 19: LLM-as-judge evaluation, the second half of Week 19
(alongside the P6 single-agent ablation, already built and run at scale
in Week 18). Evaluates REASONING QUALITY -- not just decision agreement or
realized return -- by having gpt-4o blindly compare each decision point's
multi-agent final reasoning against the single-agent baseline's, given the
same underlying analyst reports both arms saw.

Reuses the 28 real decision points from eval_results/week18_panel/. Judge
never sees realized outcomes; correlation with actual hit/miss is computed
separately afterward, not part of the judge's prompt. See
tradingagents/ablation/llm_judge.py's module docstring for the full design
rationale and disclosed bias-mitigation limitations.

Usage:
    python scripts/run_llm_judge_eval.py
    python scripts/run_llm_judge_eval.py --seed 42  # for reproducible A/B order
"""

import argparse
import json
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd
from dotenv import load_dotenv

load_dotenv()

from tradingagents.ablation.llm_judge import judge_decision_pair


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260623, help="Seed for A/B order randomization (reproducible).")
    parser.add_argument("--panel-dir", default="eval_results/week18_panel")
    return parser.parse_args()


def hit(decision, ret):
    if ret is None or decision == "HOLD":
        return None
    return (ret > 0) if decision == "BUY" else (ret < 0)


def main():
    args = parse_args()
    rng = random.Random(args.seed)

    summary = json.load(open(Path(args.panel_dir) / "_summary.json"))
    per_point_dir = Path("experiments/results/llm_judge_eval_points")
    per_point_dir.mkdir(parents=True, exist_ok=True)

    for i, d in enumerate(summary):
        ticker, trade_date = d["ticker"], d["trade_date"]
        point_path = per_point_dir / f"{ticker}_{trade_date}.json"
        if point_path.exists():
            print(f"[{i+1}/{len(summary)}] {ticker} {trade_date} already judged, skipping (resumable run).")
            continue

        artifact = json.load(open(Path(args.panel_dir) / f"{ticker}_{trade_date}.json"))
        reports = artifact["reports"]
        multi_text = artifact["multi_agent"]["final_trade_decision"] or ""
        single_text = artifact["single_agent"]["full_response"] or ""

        print(f"[{i+1}/{len(summary)}] Judging {ticker} {trade_date}...")
        result = judge_decision_pair(
            reports.get("technical_report") or "(not available)",
            reports.get("onchain_report") or "(not available)",
            reports.get("tokenomics_report") or "(not available)",
            multi_text, single_text, rng,
        )

        ma_hit = hit(d["multi_agent"]["decision"], d["forward_returns"].get("return_30d_pct"))
        sa_hit = hit(d["single_agent"]["decision"], d["forward_returns"].get("return_30d_pct"))

        row = {
            "ticker": ticker, "trade_date": trade_date,
            "multi_agent_decision": d["multi_agent"]["decision"],
            "single_agent_decision": d["single_agent"]["decision"],
            "multi_agent_30d_hit": ma_hit, "single_agent_30d_hit": sa_hit,
            **result,
        }
        # Save immediately -- a later point's rate-limit error (or any
        # crash) must not lose already-completed, real-money judgments.
        with open(point_path, "w") as f:
            json.dump(row, f, indent=2, default=str)
        print(f"  judge preference: {result['overall_preference']} "
              f"(evidence: {result['evidence_grounding_multi_agent']} vs {result['evidence_grounding_single_agent']}, "
              f"coherence: {result['logical_coherence_multi_agent']} vs {result['logical_coherence_single_agent']}, "
              f"uncertainty: {result['uncertainty_engagement_multi_agent']} vs {result['uncertainty_engagement_single_agent']})")

    rows = [json.load(open(per_point_dir / f"{d['ticker']}_{d['trade_date']}.json")) for d in summary]
    df = pd.DataFrame(rows)
    out_path = Path("experiments/results/llm_judge_eval.csv")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)

    print(f"\n{'='*70}\nSummary\n{'='*70}")
    pref_counts = df["overall_preference"].value_counts()
    print(f"Overall preference counts: {pref_counts.to_dict()}")

    for axis in ["evidence_grounding", "logical_coherence", "uncertainty_engagement"]:
        ma_mean = df[f"{axis}_multi_agent"].mean()
        sa_mean = df[f"{axis}_single_agent"].mean()
        print(f"Mean {axis}: multi_agent={ma_mean:.2f}, single_agent={sa_mean:.2f}")

    print(f"\n=== Does judge preference correlate with realized correctness? ===")
    scoreable = df.dropna(subset=["multi_agent_30d_hit", "single_agent_30d_hit"])
    print(f"({len(scoreable)}/{len(df)} points have both arms' hit/miss computable -- HOLD decisions excluded)")
    agree_with_hit = 0
    for _, r in scoreable.iterrows():
        if r["overall_preference"] == "tie":
            continue
        preferred_was_right = r[f"{r['overall_preference']}_30d_hit"]
        if preferred_was_right is not None:
            agree_with_hit += int(bool(preferred_was_right))
    non_tie = scoreable[scoreable["overall_preference"] != "tie"]
    if len(non_tie) > 0:
        print(f"Of {len(non_tie)} non-tie, both-scoreable points: judge's PREFERRED arm was actually "
              f"realized-correct {agree_with_hit}/{len(non_tie)} times ({agree_with_hit/len(non_tie)*100:.1f}%)")

    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()
