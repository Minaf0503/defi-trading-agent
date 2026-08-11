#!/usr/bin/env python
"""
Phase 5/6 prep: size-bucketed execution-quality table, mirroring Solidus
Labs' "The Ex Files" report's own methodology -- report cost conditional on
trade size via explicit buckets, not one pooled average, since their central
empirical finding is that pooling masks a super-linear size effect.

This project's real fork-sim data only has two real notional sizes ($10k,
$100k) across the combined Week 8 pilot (10 rows, ETH only, $10k) and Week
18's Mode 2 case studies (24 rows, ETH/UNI/AAVE, $10k and $100k) -- two real
buckets, not Solidus Labs' finer-grained ones. Disclosed plainly as a real,
coarse bucketing given the data this project actually has, not invented
buckets to match theirs.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd


def main():
    mode2 = pd.read_csv("experiments/results/fork_sim_mode2_case_studies.csv")
    mode2["source"] = "week18_mode2"

    pilot = pd.read_csv("experiments/results/fork_sim_pilot_eth_spot.csv")
    pilot["ticker"] = "ETH"
    pilot["notional_usd"] = 10_000  # by construction, per Week 8's design (BUILD_PLAN.md)
    pilot["source"] = "week8_pilot"

    combined = pd.concat([
        mode2[["ticker", "notional_usd", "diff_pct", "gas_used", "source"]],
        pilot[["ticker", "notional_usd", "diff_pct", "gas_used", "source"]],
    ], ignore_index=True)

    combined["diff_pct"] = combined["diff_pct"].astype(float)  # CSV already stores percentage points (e.g. 1.57 == 1.57%), verified against draft.md Section 6.3's published figures

    print(f"Combined: {len(combined)} rows ({len(mode2)} Mode 2 + {len(pilot)} Week 8 pilot)")
    print(f"  by notional: {combined['notional_usd'].value_counts().to_dict()}")

    bucket_summary = combined.groupby("notional_usd").agg(
        n=("diff_pct", "count"),
        mean_diff_pct=("diff_pct", "mean"),
        median_diff_pct=("diff_pct", "median"),
        max_diff_pct=("diff_pct", "max"),
        mean_gas=("gas_used", "mean"),
    ).reset_index()

    by_ticker_bucket = combined.groupby(["notional_usd", "ticker"]).agg(
        n=("diff_pct", "count"),
        mean_diff_pct=("diff_pct", "mean"),
        max_diff_pct=("diff_pct", "max"),
    ).reset_index()

    print("\n=== Size-bucketed (pooled across tickers) ===")
    print(bucket_summary.to_string(index=False))
    print("\n=== Size-bucketed by ticker ===")
    print(by_ticker_bucket.to_string(index=False))

    out_path = Path("experiments/results/execution_quality_by_size_bucket.csv")
    by_ticker_bucket.to_csv(out_path, index=False)
    bucket_summary.to_csv("experiments/results/execution_quality_by_size_bucket_pooled.csv", index=False)
    print(f"\nSaved: {out_path}")
    print("Saved: experiments/results/execution_quality_by_size_bucket_pooled.csv")


if __name__ == "__main__":
    main()
