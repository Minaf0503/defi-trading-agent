#!/usr/bin/env python
"""
Phase 2 Week 7 pilot: replay a real WETH->USDC swap against a forked
historical block, and compare the actual fork-sim execution result against
venues.py's same-tick approximation (Week 5) computed at the same block.

Usage:
    python scripts/validate_fork_sim.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tradingagents.dataflows.onchain.fork_sim import AnvilFork, simulate_spot_trade
from tradingagents.dataflows.onchain.rpc import get_web3
from tradingagents.dataflows.onchain.venues import SpotDEXVenue


def main():
    w3_archive = get_web3()
    latest = w3_archive.eth.block_number
    fork_block = latest - 100
    amount_in_eth = 5

    venue = SpotDEXVenue("WETH/USDC")
    fee_tier = venue.pool_config["fee_tier_bps"] * 100  # bps -> Uniswap's hundredths-of-a-bip units

    print(f"Reference state and estimate at block {fork_block} (before forking)...")
    reference_state = venue.get_state(block=fork_block)
    estimate = venue.simulate_trade({"sell_token": "WETH", "amount_in": amount_in_eth}, block=fork_block)
    print("Reference pool state:", reference_state)
    print("Week 5 same-tick approximation:", estimate)

    print(f"\nForking at block {fork_block}...")
    with AnvilFork(fork_block=fork_block) as w3_fork:
        print(f"Fork ready at block {w3_fork.eth.block_number}")
        result = simulate_spot_trade(w3_fork, sell_token="WETH", amount_in=amount_in_eth, fee_tier=fee_tier)
        print("Real fork-sim execution result:", result)

    print("\n-- Comparison: Week 5 estimate vs. Week 7 real fork-sim --")
    print(f"Estimated amount out: {estimate['amount_out_estimate']:.4f} USDC")
    print(f"Actual amount out:    {result['amount_out']:.4f} USDC")
    diff_pct = abs(result["amount_out"] - estimate["amount_out_estimate"]) / estimate["amount_out_estimate"] * 100
    print(f"Difference: {diff_pct:.4f}%")
    print(f"Real gas used (not modeled by the Week 5 estimate at all): {result['gas_used']}")
    print(f"Transaction status: {'success' if result['tx_status'] == 1 else 'REVERTED'}")


if __name__ == "__main__":
    main()
