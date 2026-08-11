#!/usr/bin/env python
"""
Phase 5 Mode 2: fork-simulated execution cost measurements.

Replays multi-agent BUY/SELL decisions from a completed panel run as real
transactions against a local Anvil fork at the historical block, measuring:
  - price_impact_pct: slippage vs. pre-swap slot0 spot price
  - gas_cost_eth / gas_cost_usd: real gas units × block base fee × ETH price
  - total_execution_cost_usd: price impact cost + gas cost

Each directional decision is simulated at FOUR notional sizes:
  $10k, $50k, $100k, $500k
to surface the super-linear cost scaling at shallow pools (CRV, PEPE, ONDO,
ENA, MKR) vs. deep pools (ETH, WBTC), which is the core RQ2 finding.

For SELL decisions: uses a buy-then-sell round trip in the same fork session
(acquire token at market, immediately sell that exact balance back). This
gives real gas/slippage data for the sell leg without needing to locate and
verify a real whale address at each historical block.

Usage:
    python scripts/run_fork_sim_mode2.py --results-dir experiments/panel_results
    python scripts/run_fork_sim_mode2.py --token ETH --token WBTC  # subset
"""

import argparse
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd
from dotenv import load_dotenv

load_dotenv()

from tradingagents.dataflows.crypto_utils import CryptoDataProvider
from tradingagents.dataflows.onchain.block_resolver import resolve_block_for_date
from tradingagents.dataflows.onchain.contracts import ERC20_TOKENS, UNISWAP_V3_POOLS
from tradingagents.dataflows.onchain.fork_sim import (
    AnvilFork,
    simulate_spot_trade,
    simulate_weth_pair_trade,
    spot_price_from_slot0,
)
from tradingagents.dataflows.onchain.venues import SpotDEXVenue

# Maps each token to its UNISWAP_V3_POOLS key. "eth_usdc" means the WETH/USDC
# pool where ETH is the primary asset priced in USDC (special case).
# All other tokens use "weth_pair" routing (WETH as the intermediate quote).
POOL_ROUTING = {
    "ETH":  ("WETH/USDC", "eth_usdc"),
    "WBTC": ("WBTC/WETH", "weth_pair"),
    "LINK": ("LINK/WETH", "weth_pair"),
    "AAVE": ("AAVE/WETH", "weth_pair"),
    "UNI":  ("UNI/WETH",  "weth_pair"),
    "MKR":  ("MKR/WETH",  "weth_pair"),
    "CRV":  ("CRV/WETH",  "weth_pair"),
    "PEPE": ("PEPE/WETH", "weth_pair"),
    "ONDO": ("ONDO/WETH", "weth_pair"),
    "ENA":  ("ENA/WETH",  "weth_pair"),
}

NOTIONAL_SIZES_USD = [10_000, 50_000, 100_000, 500_000]


def _compute_price_impact(
    amount_in: float,
    amount_out: float,
    slot0_data: dict,
    pool_cfg: dict,
    side: str,
) -> float | None:
    """Return price impact as % (positive = cost to trader)."""
    price_t1_per_t0 = slot0_data.get("price_t1_per_t0")
    if not price_t1_per_t0:
        return None

    t0 = pool_cfg["token0_symbol"]

    if side == "buy":
        # Paying WETH, receiving TOKEN.
        # Expected token out = weth_in × (TOKEN per WETH)
        token_per_weth = price_t1_per_t0 if t0 == "WETH" else 1.0 / price_t1_per_t0
        expected = amount_in * token_per_weth
        return (expected - amount_out) / expected * 100 if expected else None
    else:
        # Paying TOKEN, receiving WETH.
        # Expected weth out = token_in × (WETH per TOKEN)
        weth_per_token = 1.0 / price_t1_per_t0 if t0 == "WETH" else price_t1_per_t0
        expected = amount_in * weth_per_token
        return (expected - amount_out) / expected * 100 if expected else None


def load_decisions(results_dir: Path, tokens: list[str] | None = None) -> list[dict]:
    """Load BUY/SELL decisions from a completed panel run."""
    decisions = []
    for path in sorted(results_dir.glob("*_role_based.json")):
        try:
            with open(path) as f:
                r = json.load(f)
        except Exception:
            continue
        if r.get("decision") not in ("BUY", "SELL"):
            continue
        if tokens and r.get("token") not in tokens:
            continue
        if r.get("token") not in POOL_ROUTING:
            continue
        decisions.append(r)
    return decisions


def run_eth_case(
    decision: str, block: int, notional_usd: float, port: int, eth_price_usd: float
) -> tuple[dict, dict]:
    """Execute an ETH BUY or SELL via WETH/USDC pool."""
    venue = SpotDEXVenue("WETH/USDC")
    state = venue.get_state(block=block)
    weth_price = state["price"]["USDC_per_WETH"]

    if decision == "BUY":
        sell_token, amount_in = "USDC", notional_usd
    else:
        sell_token, amount_in = "WETH", notional_usd / weth_price

    estimate = venue.simulate_trade(
        {"sell_token": sell_token, "amount_in": amount_in}, state=state
    )
    fee_units = venue.pool_config["fee_tier_bps"] * 100

    with AnvilFork(fork_block=block, port=port) as w3:
        pool_cfg = UNISWAP_V3_POOLS["WETH/USDC"]
        pre_price = spot_price_from_slot0(
            w3,
            pool_cfg["address"],
            pool_cfg["token0_decimals"],
            pool_cfg["token1_decimals"],
        )
        actual = simulate_spot_trade(
            w3, sell_token=sell_token, amount_in=amount_in, fee_tier=fee_units
        )
        block_obj = w3.eth.get_block(block)
        base_fee_wei = block_obj.get("baseFeePerGas", 0)

    actual["pre_price"] = pre_price
    actual["base_fee_wei"] = base_fee_wei
    return estimate, actual


def run_weth_pair_case(
    ticker: str,
    decision: str,
    block: int,
    notional_usd: float,
    port: int,
    eth_price_usd: float,
) -> tuple[dict, dict]:
    """Execute a WETH-pair BUY or SELL for any non-ETH panel token."""
    pool_key = POOL_ROUTING[ticker][0]
    pool_cfg = UNISWAP_V3_POOLS[pool_key]
    venue = SpotDEXVenue(pool_key)
    state = venue.get_state(block=block)

    token_address = ERC20_TOKENS[ticker]["address"]
    token_decimals = ERC20_TOKENS[ticker]["decimals"]
    fee_units = pool_cfg["fee_tier_bps"] * 100
    weth_amount = notional_usd / eth_price_usd

    if decision == "BUY":
        estimate = venue.simulate_trade(
            {"sell_token": "WETH", "amount_in": weth_amount}, state=state
        )
        with AnvilFork(fork_block=block, port=port) as w3:
            pre_price = spot_price_from_slot0(
                w3,
                pool_cfg["address"],
                pool_cfg["token0_decimals"],
                pool_cfg["token1_decimals"],
            )
            actual = simulate_weth_pair_trade(
                w3, token_address, token_decimals,
                side="buy", amount_in=weth_amount, fee_tier=fee_units,
            )
            block_obj = w3.eth.get_block(block)
            base_fee_wei = block_obj.get("baseFeePerGas", 0)

    else:  # SELL: buy-then-sell round trip, see module docstring
        estimate = {"amount_out_estimate": None}
        with AnvilFork(fork_block=block, port=port) as w3:
            pre_price = spot_price_from_slot0(
                w3,
                pool_cfg["address"],
                pool_cfg["token0_decimals"],
                pool_cfg["token1_decimals"],
            )
            buy_leg = simulate_weth_pair_trade(
                w3, token_address, token_decimals,
                side="buy", amount_in=weth_amount, fee_tier=fee_units,
            )
            actual = simulate_weth_pair_trade(
                w3, token_address, token_decimals,
                side="sell", amount_in=None,
                amount_in_token_units=buy_leg["amount_out_raw"],
                fee_tier=fee_units,
            )
            actual["buy_leg_amount_out"] = buy_leg["amount_out"]
            block_obj = w3.eth.get_block(block)
            base_fee_wei = block_obj.get("baseFeePerGas", 0)

    actual["pre_price"] = pre_price
    actual["base_fee_wei"] = base_fee_wei
    return estimate, actual


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--results-dir", default="experiments/panel_results",
        help="Directory of completed panel run (*.json files)",
    )
    parser.add_argument(
        "--token", dest="tokens", action="append", default=None,
        help="Restrict to specific token(s) (may repeat; default: all)",
    )
    parser.add_argument(
        "--port-start", type=int, default=8560,
        help="Starting Anvil port; incremented per fork to avoid conflicts",
    )
    parser.add_argument(
        "--out", default="experiments/results/fork_sim_mode2_case_studies.csv",
    )
    args = parser.parse_args()

    results_dir = Path(args.results_dir)
    decisions = load_decisions(results_dir, args.tokens)
    total = len(decisions) * len(NOTIONAL_SIZES_USD)
    print(
        f"Replaying {len(decisions)} directional decisions "
        f"× {len(NOTIONAL_SIZES_USD)} notional sizes = {total} fork-sim case studies.\n"
    )
    if not decisions:
        print("No directional decisions found — run the panel first.")
        sys.exit(1)

    crypto = CryptoDataProvider()
    rows = []
    port = args.port_start

    for decision_rec in decisions:
        ticker     = decision_rec["token"]
        trade_date = decision_rec["date"]
        decision   = decision_rec["decision"]

        block = resolve_block_for_date(trade_date)
        pool_key, routing = POOL_ROUTING[ticker]
        pool_cfg = UNISWAP_V3_POOLS[pool_key]

        eth_snapshot  = crypto.get_historical_crypto_snapshot("ETH", trade_date)
        eth_price_usd = eth_snapshot["current_price"]

        for notional_usd in NOTIONAL_SIZES_USD:
            port += 1
            tag = f"[{ticker} {trade_date} {decision} ${notional_usd:,}]"
            print(f"{tag} block={block}, forking on port {port}...")

            try:
                if routing == "eth_usdc":
                    estimate, actual = run_eth_case(
                        decision, block, notional_usd, port, eth_price_usd
                    )
                else:
                    estimate, actual = run_weth_pair_case(
                        ticker, decision, block, notional_usd, port, eth_price_usd
                    )

                pre_price    = actual.pop("pre_price", {})
                base_fee_wei = actual.pop("base_fee_wei", 0)

                spot_price_t1_per_t0 = pre_price.get("price_t1_per_t0")

                impact_pct = _compute_price_impact(
                    amount_in=actual.get("amount_in", 0) or 0,
                    amount_out=actual.get("amount_out", 0) or 0,
                    slot0_data=pre_price,
                    pool_cfg=pool_cfg,
                    side=decision.lower(),
                )

                gas_used     = actual["gas_used"]
                gas_cost_eth = gas_used * base_fee_wei / 1e18
                gas_cost_usd = gas_cost_eth * eth_price_usd

                impact_cost_usd = notional_usd * impact_pct / 100 if impact_pct is not None else None
                total_cost_usd  = (
                    gas_cost_usd + impact_cost_usd
                    if impact_cost_usd is not None else None
                )

                est_out  = estimate.get("amount_out_estimate")
                act_out  = actual["amount_out"]
                diff_pct = (
                    abs(act_out - est_out) / est_out * 100
                    if est_out else None
                )

                rows.append({
                    "token":                   ticker,
                    "trade_date":              trade_date,
                    "decision":                decision,
                    "notional_usd":            notional_usd,
                    "block":                   block,
                    "pool_key":                pool_key,
                    "spot_price_t1_per_t0":    spot_price_t1_per_t0,
                    "amount_in":               actual.get("amount_in"),
                    "amount_out":              act_out,
                    "estimate_amount_out":      est_out,
                    "estimate_diff_pct":        diff_pct,
                    "price_impact_pct":         impact_pct,
                    "gas_used":                 gas_used,
                    "gas_cost_eth":             gas_cost_eth,
                    "eth_price_usd":            eth_price_usd,
                    "gas_cost_usd":             gas_cost_usd,
                    "price_impact_cost_usd":    impact_cost_usd,
                    "total_execution_cost_usd": total_cost_usd,
                    "liquidity_at_block":       pre_price.get("liquidity_in_range"),
                    "tx_status":                actual.get("tx_status"),
                    "simulated":                True,
                })
                print(
                    f"  impact={impact_pct:.3f}% | gas={gas_used} | "
                    f"gas_usd=${gas_cost_usd:.2f} | total_usd=${total_cost_usd or 0:.2f}"
                )

            except Exception as exc:
                import traceback as tb
                print(f"  ERROR: {exc}")
                tb.print_exc()
                rows.append({
                    "token": ticker, "trade_date": trade_date, "decision": decision,
                    "notional_usd": notional_usd, "block": block, "pool_key": pool_key,
                    "error": str(exc), "simulated": True,
                })

    df = pd.DataFrame(rows)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)

    print(f"\n{'='*70}")
    print("EXECUTION COST SUMMARY")
    print(f"{'='*70}")
    numeric_df = df.dropna(subset=["price_impact_pct"])
    if not numeric_df.empty:
        print("\nMean price impact (%) by token × notional:")
        print(
            numeric_df.groupby(["token", "notional_usd"])["price_impact_pct"]
            .agg(["mean", "max", "count"])
            .to_string()
        )
        print("\nMean total execution cost (USD) by token × notional:")
        print(
            numeric_df.groupby(["token", "notional_usd"])["total_execution_cost_usd"]
            .agg(["mean", "max", "count"])
            .to_string()
        )
    print(f"\n(simulated=True on all rows — do NOT aggregate with real-trade cost data)")
    print(f"Saved {len(df)} rows to {out_path}")


if __name__ == "__main__":
    main()
