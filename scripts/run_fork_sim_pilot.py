#!/usr/bin/env python
"""
Phase 2 Week 8 pilot: replay N real historical trading decisions (from the
already-validated MACD baseline on ETH, Phase 1) through the Mode 2
fork-simulated execution harness, and compare against the Week 5 same-tick
approximation at each decision's actual historical block.

Scope note: this pilot covers ETH SPOT only. A genuine historical PerpVenue
(GMX v2) fork-sim would require direct DataStore contract reads (GMX v2's
REST API, used in Week 6, only exposes current state) -- a substantially
larger build, deferred past this pilot. See PROGRESS_LOG.md 2026-06-21.

Usage:
    python scripts/run_fork_sim_pilot.py --n 10
"""

import argparse
import sys
from datetime import timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd

from experiments.baseline import get_baseline_strategy
from experiments.config import BASELINE_STRATEGIES, EXPERIMENT_PATHS, EXPERIMENT_TOKENS, TIME_PERIODS
from tradingagents.dataflows.historical_data import HistoricalDataCache
from tradingagents.dataflows.onchain.fork_sim import AnvilFork, simulate_spot_trade
from tradingagents.dataflows.onchain.rpc import block_at_timestamp, get_web3
from tradingagents.dataflows.onchain.venues import SpotDEXVenue


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=10, help="Number of decision points to sample")
    parser.add_argument("--notional-usd", type=float, default=10_000)
    return parser.parse_args()


def main():
    args = parse_args()

    period = TIME_PERIODS["backtesting"]
    cache = HistoricalDataCache()
    price_data = cache.get(
        "ETH",
        EXPERIMENT_TOKENS["ETH"]["yahoo_ticker"],
        pd.Timestamp(period["start"], tz="UTC").to_pydatetime(),
        pd.Timestamp(period["end"], tz="UTC").to_pydatetime(),
        source="yahoo",
    )

    strategy = get_baseline_strategy("macd", BASELINE_STRATEGIES["macd"]["params"])
    result = strategy.backtest(price_data, initial_capital=10000)
    trades = [t for t in result["trades"] if t["action"] in ("BUY", "SELL")]
    print(f"MACD strategy produced {len(trades)} real trade signals on ETH in the backtesting period.")

    step = max(1, len(trades) // args.n)
    sampled = trades[::step][: args.n]
    print(f"Sampling {len(sampled)} decision points for the fork-sim pilot.\n")

    w3_archive = get_web3()
    venue = SpotDEXVenue("WETH/USDC")
    fee_tier = venue.pool_config["fee_tier_bps"] * 100

    rows = []
    for i, trade in enumerate(sampled):
        trade_ts = int(pd.Timestamp(trade["timestamp"]).tz_localize(None).replace(tzinfo=timezone.utc).timestamp())
        block = block_at_timestamp(w3_archive, trade_ts)

        reference_state = venue.get_state(block=block)
        usdc_per_weth = reference_state["price"]["USDC_per_WETH"]

        if trade["action"] == "BUY":
            sell_token, amount_in = "USDC", args.notional_usd
        else:
            sell_token, amount_in = "WETH", args.notional_usd / usdc_per_weth

        estimate = venue.simulate_trade({"sell_token": sell_token, "amount_in": amount_in}, block=block)

        print(f"[{i+1}/{len(sampled)}] {trade['timestamp']} ({trade['action']}) -> block {block}, forking...")
        with AnvilFork(fork_block=block, port=8550 + i) as w3_fork:
            actual = simulate_spot_trade(w3_fork, sell_token=sell_token, amount_in=amount_in, fee_tier=fee_tier)

        diff_pct = abs(actual["amount_out"] - estimate["amount_out_estimate"]) / estimate["amount_out_estimate"] * 100

        rows.append(
            {
                "timestamp": trade["timestamp"],
                "action": trade["action"],
                "block": block,
                "sell_token": sell_token,
                "amount_in": amount_in,
                "estimate_amount_out": estimate["amount_out_estimate"],
                "actual_amount_out": actual["amount_out"],
                "diff_pct": diff_pct,
                "gas_used": actual["gas_used"],
            }
        )

    df = pd.DataFrame(rows)
    results_dir = Path(EXPERIMENT_PATHS["results_dir"])
    results_dir.mkdir(parents=True, exist_ok=True)
    out_path = results_dir / "fork_sim_pilot_eth_spot.csv"
    df.to_csv(out_path, index=False)

    pd.set_option("display.float_format", lambda x: f"{x:.4f}")
    print(f"\n{df.to_string(index=False)}")
    print(f"\nMean diff: {df['diff_pct'].mean():.4f}%  Max diff: {df['diff_pct'].max():.4f}%  Mean gas: {df['gas_used'].mean():.0f}")
    print(f"Saved to {out_path}")


if __name__ == "__main__":
    main()
