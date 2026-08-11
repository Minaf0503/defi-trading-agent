#!/usr/bin/env python
"""
Phase 5 Week 21: execution-delay price cost.

Alpha Illusion's friction list includes "execution delay" -- the cost of
price moving against you while a (possibly slow) decision process runs.
This project measures the LATENCY of that delay (wall-clock per decision,
Week 18/19) but never the PRICE COST of it.

The Week 18 historical panel can't measure this directly: each decision and
its hypothetical execution are simulated at the SAME resolved historical
block, with zero real elapsed time in the 2022-2025 timeline -- there's no
"price 150 seconds later in 2022" inherent to that data.

Instead, this uses Ethereum's own block cadence as a real clock: each
decision's REAL measured wall-clock latency (multi-agent ~150-200s,
single-agent ~5s, from the Week 18 panel) is converted to a block count
using the LOCAL block time at that era (verified empirically per block --
12.00s post-merge, ~13.4s in mid-2022 pre-merge PoW, not assumed uniform).
Querying the same Uniswap v3 pool's real on-chain price at the decision
block and again that many blocks later gives a real, on-chain price-movement
measurement over a wall-clock-equivalent window, without needing intraday
OHLCV data this project doesn't have (Yahoo Finance is daily-only).

Reuses the same 12 ETH/UNI/AAVE directional decisions Mode 2 (Week 18)
already replayed, for coherence with that result. Zero LLM cost -- pure RPC
reads against existing infrastructure.

Usage:
    python scripts/run_execution_delay_cost.py
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd
from dotenv import load_dotenv

load_dotenv()

from tradingagents.dataflows.onchain.block_resolver import resolve_block_for_date
from tradingagents.dataflows.onchain.rpc import get_web3
from tradingagents.dataflows.onchain.venues import SpotDEXVenue

POOL_BY_TOKEN = {"ETH": "WETH/USDC", "UNI": "UNI/WETH", "AAVE": "AAVE/WETH"}
PRICE_KEY_BY_TOKEN = {"ETH": "USDC_per_WETH", "UNI": "WETH_per_UNI", "AAVE": "WETH_per_AAVE"}
NOTIONAL_SIZES_USD = [10_000, 100_000]


def local_block_time(w3, block, lookahead=50):
    t0 = w3.eth.get_block(block)["timestamp"]
    t1 = w3.eth.get_block(block + lookahead)["timestamp"]
    return (t1 - t0) / lookahead


def main():
    summary = json.load(open("eval_results/week18_panel/_summary.json"))
    w3 = get_web3()
    rows = []

    for d in summary:
        ticker = d["ticker"]
        if ticker not in POOL_BY_TOKEN:
            continue
        decision = d["multi_agent"]["decision"]
        if decision not in ("BUY", "SELL"):
            continue

        trade_date = d["trade_date"]
        block = resolve_block_for_date(trade_date)
        block_time = local_block_time(w3, block)
        venue = SpotDEXVenue(POOL_BY_TOKEN[ticker])
        price_key = PRICE_KEY_BY_TOKEN[ticker]
        price_before = venue.get_state(block=block)["price"][price_key]

        for arm, wall_clock_s in [
            ("multi_agent", d["multi_agent"]["wall_clock_s"]),
            ("single_agent", d["single_agent"]["wall_clock_s"]),
        ]:
            n_blocks = max(1, round(wall_clock_s / block_time))
            price_after = venue.get_state(block=block + n_blocks)["price"][price_key]
            pct_change = (price_after - price_before) / price_before

            # ETH: price_key is USD per WETH directly -- BUY=bad if price rises.
            # UNI/AAVE: price_key is WETH per TOKEN -- BUY=bad if price rises too
            # (costs more WETH per token), same sign convention as ETH.
            adverse_pct = pct_change if decision == "BUY" else -pct_change

            print(f"[{ticker} {trade_date} {decision}] {arm}: wall_clock={wall_clock_s:.1f}s -> "
                  f"{n_blocks} blocks (local block time {block_time:.2f}s), "
                  f"price {price_before:.6g} -> {price_after:.6g} ({pct_change*100:+.4f}%), "
                  f"adverse_pct={adverse_pct*100:+.4f}%")

            for notional in NOTIONAL_SIZES_USD:
                rows.append({
                    "ticker": ticker, "trade_date": trade_date, "decision": decision,
                    "arm": arm, "wall_clock_s": wall_clock_s, "n_blocks": n_blocks,
                    "block_time_s": round(block_time, 2), "price_before": price_before,
                    "price_after": price_after, "pct_change": pct_change,
                    "adverse_pct": adverse_pct, "notional_usd": notional,
                    "delay_cost_usd": adverse_pct * notional,
                })

    df = pd.DataFrame(rows)
    out_path = Path("experiments/results/execution_delay_cost.csv")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)

    pd.set_option("display.float_format", lambda x: f"{x:.4f}")
    print(f"\n=== Mean adverse delay cost (USD) by arm, by notional ===")
    print(df.groupby(["arm", "notional_usd"])["delay_cost_usd"].agg(["mean", "std", "min", "max", "count"]))
    print(f"\n=== Mean n_blocks of delay by arm ===")
    print(df.groupby("arm")["n_blocks"].agg(["mean", "min", "max"]))
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()
