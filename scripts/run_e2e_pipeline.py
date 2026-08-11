#!/usr/bin/env python
"""
Phase 4 Week 17: wire every built piece into one pipeline and run a single,
genuinely live end-to-end test on ETH.

This is a LIVE decision, not a backtest replay: the four analysts pull
CURRENT data (current price, current on-chain state, current news/Fear&Greed,
current Dune holder/volume snapshots) -- there is no historical-as-of-date
parameter threaded through those tools. That makes this the right test for
"does the full wiring work end to end", but the wrong test for "was the
decision good" (Phase 1's baseline backtests and Phase 2 Week 8's fork-sim
pilot already cover known-outcome historical replay; this script doesn't
duplicate that).

Pipeline, in order:
  Stage 1-3 (LLM debate, existing)  -- TradingAgentsGraph.propagate()
  Stage 4-5 (Week 16, post-hoc)     -- graph.calibrate_and_size(), now
                                       cost-aware: sizing is capped against
                                       the real Uniswap pool's own
                                       simulate_trade()-estimated price
                                       impact, not just a flat liquidity
                                       fraction -- see
                                       literature/Solidus Labs Report - The
                                       Ex Files.pdf, whose central finding is
                                       that execution cost is a function of
                                       size (super-linearly, for AMMs), not a
                                       flat number.
  Stage 6 (Mode 2, Phase 2 Week 7)  -- real Anvil fork-sim execution, if the
                                       decision is BUY/SELL (skipped for HOLD),
                                       now also reporting realized execution
                                       quality in bps (pre-trade reference
                                       price vs. realized fill price) in the
                                       same units the cited report uses, so
                                       Stage 5's cost estimate and Stage 6's
                                       realized cost are directly comparable.

What's deliberately NOT done here: graph.record_outcome_and_refit() and
graph.reflect_and_remember() both need a REALIZED outcome (was the decision
actually profitable) -- which doesn't exist for a same-day live decision.
Calling them with a fabricated outcome would defeat the entire point of
Week 16's no-look-ahead design. They're left for the historical-replay
pilots, which already have real, known outcomes to use.

Usage:
    python scripts/run_e2e_pipeline.py --ticker ETH
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
    parser.add_argument("--capital", type=float, default=10_000.0)
    parser.add_argument(
        "--payoff-ratio",
        type=float,
        default=1.5,
        help="Assumed win/loss payoff ratio for Kelly sizing -- this project has no "
        "principled per-decision estimator yet (Week 16 limitation), so this is a "
        "placeholder, not a computed value. Flagged in the output.",
    )
    parser.add_argument("--llm-provider", default="anthropic")
    parser.add_argument("--deep-think-llm", default="claude-sonnet-4-6")
    parser.add_argument("--quick-think-llm", default="claude-haiku-4-5-20251001")
    parser.add_argument(
        "--max-execution-cost-bps",
        type=float,
        default=50.0,
        help="Cost ceiling Stage 5 sizing bisects against using the real Uniswap pool's "
        "simulate_trade()-estimated price impact. 50 bps is a conservative placeholder, "
        "not a calibrated risk parameter -- see literature/Solidus Labs Report - The Ex Files.pdf.",
    )
    return parser.parse_args()


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

    trade_date = date.today().isoformat()
    print(f"=== Stage 1-3: live agent debate for {args.ticker} on {trade_date} ===")
    graph = TradingAgentsGraph(debug=False, config=config)
    final_state, processed_signal = graph.propagate(args.ticker, trade_date)

    print(f"\nProcessed signal: {processed_signal}")
    print(f"Raw confidence: {final_state.get('raw_confidence')}")
    print(f"\n--- Final trade decision (truncated) ---\n{final_state.get('final_trade_decision', '')[:500]}")

    print(f"\n=== Stage 4-5: calibration + sizing ===")
    try:
        from tradingagents.dataflows.onchain import PerpVenue

        venue_liquidity_usd = PerpVenue(args.ticker).get_state()["available_liquidity_long_usd"]
        print(f"Real venue liquidity (GMX v2 {args.ticker}/USD, long side): ${venue_liquidity_usd:,.0f}")
    except Exception as e:
        print(f"Could not fetch real venue liquidity ({e}) -- proceeding without a venue cap")
        venue_liquidity_usd = None

    # Cost-aware cap (literature/Solidus Labs Report - The Ex Files.pdf): fetch
    # the real Uniswap pool's state ONCE and reuse it both for sizing's
    # cost_estimator closure (called ~12x during bisection -- must be cheap,
    # see PositionSizer docstring) and for Stage 6 execution below, so this
    # only costs one RPC round-trip rather than one per call site.
    spot_venue = None
    spot_state = None
    usdc_per_weth = None
    cost_estimator = None
    if processed_signal in ("BUY", "SELL"):
        try:
            from tradingagents.dataflows.onchain.venues import SpotDEXVenue

            spot_venue = SpotDEXVenue("WETH/USDC")
            spot_state = spot_venue.get_state()
            usdc_per_weth = spot_state["price"]["USDC_per_WETH"]

            def cost_estimator(usd_size, _signal=processed_signal):
                if _signal == "BUY":
                    intent = {"sell_token": "USDC", "amount_in": usd_size}
                else:
                    intent = {"sell_token": "WETH", "amount_in": usd_size / usdc_per_weth}
                return spot_venue.simulate_trade(intent, state=spot_state)["price_impact_bps_estimate"]

            print(f"Cost estimator wired to real Uniswap v3 WETH/USDC pool state (block {spot_state['block']}).")
        except Exception as e:
            print(f"Could not fetch real pool state for cost-aware sizing ({e}) -- proceeding without it")

    calibration_sizing = graph.calibrate_and_size(
        payoff_ratio=args.payoff_ratio,
        capital=args.capital,
        venue_liquidity_usd=venue_liquidity_usd,
        cost_estimator=cost_estimator,
        max_execution_cost_bps=args.max_execution_cost_bps,
    )
    print(json.dumps(calibration_sizing, indent=2))

    print(f"\n=== Stage 6: execution (Mode 2 fork-sim) ===")
    execution_result = None
    realized_execution_quality_bps = None
    if processed_signal not in ("BUY", "SELL"):
        print(f"Decision is {processed_signal} -- no execution to run.")
    elif calibration_sizing.get("position_sizing") is None:
        print("No position size available (raw_confidence was unparseable) -- skipping execution.")
    else:
        from tradingagents.dataflows.onchain.fork_sim import AnvilFork, simulate_spot_trade
        from tradingagents.dataflows.onchain.rpc import get_web3

        w3 = get_web3()
        latest_block = w3.eth.block_number
        fee_tier = spot_venue.pool_config["fee_tier_bps"] * 100

        notional_usd = calibration_sizing["position_sizing"]["position_size_usd"]
        if notional_usd <= 0:
            print(f"Sized position is ${notional_usd:.2f} (non-positive edge) -- skipping execution.")
        else:
            if processed_signal == "BUY":
                sell_token, amount_in = "USDC", notional_usd
            else:
                sell_token, amount_in = "WETH", notional_usd / usdc_per_weth

            print(f"Forking at current block {latest_block}, executing {processed_signal} (${notional_usd:,.2f} notional)...")
            with AnvilFork(fork_block=latest_block, port=8560) as w3_fork:
                execution_result = simulate_spot_trade(w3_fork, sell_token=sell_token, amount_in=amount_in, fee_tier=fee_tier)
            print(json.dumps(execution_result, indent=2))

            # Realized execution quality in bps -- same unit/methodology as
            # literature/Solidus Labs Report - The Ex Files.pdf's core metric
            # (realized price vs. a pre-trade reference, in bps), but measured
            # against this single real fork-sim fill rather than a pooled
            # candle: this is the ground-truth counterpart to Stage 5's
            # simulate_trade()-based cost *estimate* above.
            if processed_signal == "BUY":
                realized_price = execution_result["amount_in"] / execution_result["amount_out"]  # USDC per WETH
            else:
                realized_price = execution_result["amount_out"] / execution_result["amount_in"]  # USDC per WETH
            realized_execution_quality_bps = abs(realized_price - usdc_per_weth) / usdc_per_weth * 10000
            print(
                f"Realized execution quality: {realized_execution_quality_bps:.2f} bps "
                f"(reference {usdc_per_weth:.4f} USDC/WETH vs. realized {realized_price:.4f} USDC/WETH)"
            )

    print(f"\n=== Stage 4-5 outcome recording: DEFERRED ===")
    print(
        "graph.record_outcome_and_refit() / graph.reflect_and_remember() need a realized "
        "outcome -- not available for a same-day live decision. Not called here; see "
        "scripts/run_fork_sim_pilot.py for the historical-replay path where outcomes are known."
    )

    out_dir = Path("eval_results") / args.ticker
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"e2e_pipeline_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json"
    artifact = {
        "ticker": args.ticker,
        "trade_date": trade_date,
        "config": config,
        "reports": {
            "technical_report": final_state.get("technical_report"),
            "onchain_report": final_state.get("onchain_report"),
            "tokenomics_report": final_state.get("tokenomics_report"),
            "sentiment_news_report": final_state.get("sentiment_news_report"),
        },
        "trader_investment_plan": final_state.get("trader_investment_plan"),
        "raw_confidence": final_state.get("raw_confidence"),
        "final_trade_decision": final_state.get("final_trade_decision"),
        "processed_signal": processed_signal,
        "calibration_sizing": calibration_sizing,
        "execution_result": execution_result,
        "realized_execution_quality_bps": realized_execution_quality_bps,
        "payoff_ratio_note": f"payoff_ratio={args.payoff_ratio} is an assumed placeholder, not computed -- see Week 16 limitation",
    }
    with open(out_path, "w") as f:
        json.dump(artifact, f, indent=2, default=str)
    print(f"\nSaved full artifact to {out_path}")


if __name__ == "__main__":
    main()
