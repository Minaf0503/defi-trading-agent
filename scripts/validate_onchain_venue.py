#!/usr/bin/env python
"""
Validate the Phase 2 Week 5 on-chain venue layer: Chainlink price feed reads
and the Uniswap v3 SpotDEXVenue connector, at both the latest block and a
historical block (the latter is what fork-simulated execution and any
backtest-time on-chain feature will rely on).

Usage:
    python scripts/validate_onchain_venue.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tradingagents.dataflows.onchain import ChainlinkPriceFeed, PerpVenue, SpotDEXVenue, VaultVenue
from tradingagents.dataflows.onchain.rpc import get_web3


def main():
    w3 = get_web3()
    latest_block = w3.eth.block_number
    # Free public RPCs only serve recent state (confirmed: ~100 blocks back works,
    # ~1000 blocks back returns 403). True archive access (for Phase 2 Week 7
    # fork-sim at arbitrary historical blocks) will need a dedicated provider --
    # see PROGRESS_LOG.md 2026-06-21.
    historical_block = latest_block - 50

    print(f"Connected. Latest block: {latest_block}")

    feed = ChainlinkPriceFeed("ETH/USD")
    print("\n-- Chainlink ETH/USD --")
    print("latest:    ", feed.get_price())
    print("historical:", feed.get_price(block=historical_block))

    venue = SpotDEXVenue("WETH/USDC")
    print("\n-- Uniswap v3 WETH/USDC pool state --")
    state_latest = venue.get_state()
    state_hist = venue.get_state(block=historical_block)
    print("latest:    ", state_latest)
    print("historical:", state_hist)

    print("\n-- Simulated trade: sell 10,000 USDC for WETH (latest state) --")
    trade = venue.simulate_trade({"sell_token": "USDC", "amount_in": 10_000})
    print(trade)

    print("\n-- Simulated trade: sell 5 WETH for USDC (latest state) --")
    trade2 = venue.simulate_trade({"sell_token": "WETH", "amount_in": 5})
    print(trade2)

    print("\n-- Cost model --")
    print(venue.cost_model())

    # Sanity check: Uniswap pool price should be within a few % of the Chainlink oracle price.
    pool_price_usdc_per_weth = state_latest["price"]["USDC_per_WETH"]
    oracle_price = feed.get_price()["price"]
    deviation_pct = abs(pool_price_usdc_per_weth - oracle_price) / oracle_price * 100
    print(f"\nPool price vs oracle price deviation: {deviation_pct:.3f}%")
    if deviation_pct > 5:
        print("WARNING: pool price deviates from oracle by more than 5% -- check addresses/decimals.")
    else:
        print("OK: pool price consistent with oracle price.")

    # UNI/WETH and AAVE/WETH: added to verify the "liquidity-coverage first"
    # token-selection criterion (BUILD_PLAN.md) -- both tokens previously had
    # ERC20 supply data but no registered liquidity venue. No Chainlink
    # UNI/USD or AAVE/USD oracle cross-check yet (Feed Registry lookup hit an
    # eth_utils address-validation quirk on the USD quote sentinel address;
    # not pursued further -- documented as an open item, not silently
    # skipped) -- liquidity()/token0()/token1()/fee() were independently
    # verified directly against the Uniswap v3 Factory instead.
    for pool_key, sell_symbol in [("UNI/WETH", "UNI"), ("AAVE/WETH", "AAVE")]:
        venue = SpotDEXVenue(pool_key)
        print(f"\n-- Uniswap v3 {pool_key} pool state --")
        state = venue.get_state()
        print(state)
        trade = venue.simulate_trade({"sell_token": sell_symbol, "amount_in": 1000}, state=state)
        print(f"Simulated trade: sell 1000 {sell_symbol} -- price impact {trade['price_impact_bps_estimate']:.2f} bps")

    print("\n-- GMX v2 PerpVenue: ETH/USD market state --")
    perp = PerpVenue("ETH")
    perp_state = perp.get_state()
    print(perp_state)

    print("\n-- Simulated GMX trade: $50,000 long ETH --")
    print(perp.simulate_trade({"side": "long", "size_usd": 50_000}))

    print("\n-- GMX cost model --")
    print(perp.cost_model())

    # Sanity check: GMX's ETH index price should also track the Chainlink oracle.
    gmx_deviation_pct = abs(perp_state["index_price_usd"] - oracle_price) / oracle_price * 100
    print(f"\nGMX index price vs Chainlink oracle deviation: {gmx_deviation_pct:.3f}%")
    if gmx_deviation_pct > 5:
        print("WARNING: GMX index price deviates from oracle by more than 5% -- check token/decimals.")
    else:
        print("OK: GMX index price consistent with oracle price.")

    print("\n-- Morpho VaultVenue: Steakhouse USDC --")
    vault = VaultVenue("STEAKHOUSE_USDC")
    vault_state = vault.get_state()
    print(vault_state)

    print("\n-- Simulated deposit: 10,000 USDC --")
    deposit = vault.simulate_trade({"action": "deposit", "amount": 10_000})
    print(deposit)

    # Cross-check: previewDeposit's implied price should match get_state()'s
    # independently-computed share_price_underlying.
    implied_price = deposit["amount_in"] / (deposit["shares_out_estimate"] / 1e18)
    deviation_pct = abs(implied_price - vault_state["share_price_underlying"]) / vault_state["share_price_underlying"] * 100
    print(f"\nDeposit-implied share price vs get_state() share price deviation: {deviation_pct:.4f}%")
    if deviation_pct > 1:
        print("WARNING: deposit preview price deviates from get_state() price by more than 1% -- check decimals.")
    else:
        print("OK: deposit preview consistent with get_state().")

    print("\n-- VaultVenue cost model --")
    print(vault.cost_model())


if __name__ == "__main__":
    main()
