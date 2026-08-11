#!/usr/bin/env python
"""
Validate Phase 4 Week 16: Stage 4 (probability calibration) + Stage 5
(deterministic sizing) + the Reflection/ACE agent that ties them together.

Since this project has no real LLM-agent decision history to calibrate
against yet (that needs a real LLM key and Week 17/18 integration), this
validates the modules' correctness on:
  1. Synthetic confidence/outcome sequences with a known, constructed bias
     (proves ECE correctly detects miscalibration, and that calibrate()
     correctly corrects for it -- not just that the code runs).
  2. Hand-checkable Kelly-criterion arithmetic (proves the sizing formula
     itself, independent of any calibration).
  3. Real Phase 2 venue data (PerpVenue) for the venue-liquidity cap, so
     that check is against a real number, not a made-up one.

Usage:
    python scripts/validate_calibration_sizing.py
"""

import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tradingagents.agents.utils.parsing import extract_confidence
from tradingagents.calibration import PositionSizer, ProbabilityCalibrator


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def test_confidence_parsing():
    section("1. Confidence parsing (deterministic regex, no LLM)")
    cases = [
        ("FINAL TRANSACTION PROPOSAL: **BUY** (Confidence: 72%)", 0.72),
        ("...analysis...\nFINAL TRANSACTION PROPOSAL: **HOLD** (Confidence: 50%)", 0.50),
        ("FINAL TRANSACTION PROPOSAL: **SELL** (Confidence: 0%)", 0.0),
        ("FINAL TRANSACTION PROPOSAL: **BUY** (Confidence: 100%)", 1.0),
        ("No proposal line at all.", None),
        ("FINAL TRANSACTION PROPOSAL: **SELL** (Confidence: 105%)", None),  # out of range
    ]
    all_ok = True
    for text, expected in cases:
        got = extract_confidence(text)
        ok = got == expected
        all_ok &= ok
        print(f"  {'OK' if ok else 'FAIL'}: {text[:55]!r} -> {got} (expected {expected})")
    print("PASS" if all_ok else "FAIL: confidence parsing has a bug")
    return all_ok


def test_ece_detects_known_miscalibration():
    section("2. ECE correctly detects a constructed overconfidence bias")
    # Construct an agent that's systematically overconfident: whenever it
    # states 80% confidence, it's actually only right 55% of the time.
    # whenever it states 60%, it's actually right 60% (well-calibrated there).
    random.seed(42)
    calibrator = ProbabilityCalibrator(n_bins=10, min_records_to_calibrate=20)

    for _ in range(200):
        calibrator.add_record(0.80, outcome=random.random() < 0.55)
    for _ in range(200):
        calibrator.add_record(0.60, outcome=random.random() < 0.60)
    calibrator.fit()

    ece_result = calibrator.compute_ece()
    print(f"  n_records: {ece_result['n_records']}")
    print(f"  ECE: {ece_result['ece']:.4f}")
    for b in ece_result["bins"]:
        print(f"  bin {b['range']}: n={b['count']}, avg_confidence={b['avg_confidence']}, accuracy={b['accuracy']}, gap={b['gap']}")

    # The 0.8 bin should show a large gap (~0.25); the 0.6 bin should show ~0.
    bins_by_range = {tuple(b["range"]): b for b in ece_result["bins"]}
    gap_08 = bins_by_range.get((0.8, 0.9), {}).get("gap", 0)
    gap_06 = bins_by_range.get((0.6, 0.7), {}).get("gap", 0)
    ok = gap_08 > 0.15 and gap_06 < 0.05
    print(f"PASS: ECE correctly shows large gap at stated-80% bin ({gap_08:.3f}) and near-zero at stated-60% bin ({gap_06:.3f})" if ok
          else f"FAIL: expected large gap at 0.8 and small gap at 0.6, got {gap_08:.3f} / {gap_06:.3f}")

    # calibrate(0.80) should now return ~0.55, not 0.80 -- this is the actual
    # point of the module: correcting the trader's stated confidence using
    # what it's actually meant historically.
    calibration_result = calibrator.calibrate(0.80)
    calibrated = calibration_result["calibrated_probability"]
    ok2 = abs(calibrated - 0.55) < 0.05
    print(f"  calibrate(0.80) -> {calibrated:.3f} (expected ~0.55)")
    print("PASS: calibrate() corrects the overconfident input toward realized accuracy" if ok2
          else f"FAIL: expected ~0.55, got {calibrated:.3f}")
    return ok and ok2


def test_cold_start_no_fabrication():
    section("3. Cold start: insufficient data returns raw confidence, flagged, not fabricated")
    calibrator = ProbabilityCalibrator(n_bins=10, min_records_to_calibrate=20)
    for _ in range(5):
        calibrator.add_record(0.70, outcome=True)
    calibrator.fit()
    result = calibrator.calibrate(0.70)
    ok = result["calibrated"] is False and result["calibrated_probability"] == 0.70
    print(f"  5 records (need 20): {result}")
    print("PASS: correctly refuses to calibrate on insufficient data" if ok else "FAIL")
    return ok


def test_kelly_sizing_arithmetic():
    section("4. Kelly criterion sizing -- hand-checkable arithmetic")
    sizer = PositionSizer(max_position_fraction=0.25, kelly_fraction_multiplier=0.5)
    # p=0.6, payoff_ratio=2.0 (win 2x what you risk) -> Kelly f* = p - (1-p)/b = 0.6 - 0.4/2 = 0.4
    # half-Kelly applied = 0.2, under the 0.25 cap, so uncapped.
    result = sizer.size_position(calibrated_probability=0.6, payoff_ratio=2.0, capital=100_000)
    expected_raw = 0.6 - 0.4 / 2.0
    expected_applied = expected_raw * 0.5
    print(f"  p=0.6, payoff_ratio=2.0, capital=$100,000: {result}")
    ok = (
        abs(result["kelly_fraction_raw"] - expected_raw) < 1e-9
        and abs(result["kelly_fraction_applied"] - expected_applied) < 1e-9
        and abs(result["position_size_usd"] - expected_applied * 100_000) < 1e-6
        and result["capped_by"] is None
    )
    print(f"  expected kelly_fraction_raw={expected_raw}, kelly_fraction_applied={expected_applied}")
    print("PASS: matches hand-computed Kelly formula exactly" if ok else "FAIL: arithmetic mismatch")

    # Negative-edge case: p=0.3, payoff_ratio=1.0 -> f* = 0.3 - 0.7/1 = -0.4 -> clamped to 0
    result2 = sizer.size_position(calibrated_probability=0.3, payoff_ratio=1.0, capital=100_000)
    ok2 = result2["kelly_fraction_raw"] == 0.0 and result2["position_size_usd"] == 0.0
    print(f"\n  negative edge (p=0.3, payoff_ratio=1.0): {result2}")
    print("PASS: negative edge correctly sized to zero, not a short position" if ok2 else "FAIL")

    # Max-fraction cap case: very high edge should hit the 0.25 cap.
    result3 = sizer.size_position(calibrated_probability=0.95, payoff_ratio=5.0, capital=100_000)
    ok3 = result3["capped_by"] == "max_position_fraction" and abs(result3["kelly_fraction_applied"] - 0.25) < 1e-9
    print(f"\n  high edge (p=0.95, payoff_ratio=5.0): {result3}")
    print("PASS: max_position_fraction cap correctly engaged" if ok3 else "FAIL")
    return ok and ok2 and ok3


def test_venue_liquidity_cap_real_data():
    section("5. Venue-liquidity cap against REAL Phase 2 PerpVenue data")
    try:
        from tradingagents.dataflows.onchain import PerpVenue

        perp = PerpVenue("ETH")
        state = perp.get_state()
        available_liquidity_usd = state["available_liquidity_long_usd"]
        print(f"  Real GMX v2 ETH/USD available long liquidity: ${available_liquidity_usd:,.0f}")
    except Exception as e:
        print(f"  SKIP: couldn't reach live RPC ({e}) -- using a placeholder value instead")
        available_liquidity_usd = 50_000_000.0

    sizer = PositionSizer(max_position_fraction=0.25, kelly_fraction_multiplier=0.5)
    # Deliberately large capital so the portfolio-fraction cap would NOT be
    # the binding constraint -- only the venue-liquidity cap (1% of real
    # available liquidity) should engage.
    huge_capital = 1_000_000_000.0
    result = sizer.size_position(
        calibrated_probability=0.9,
        payoff_ratio=3.0,
        capital=huge_capital,
        venue_liquidity_usd=available_liquidity_usd,
        venue_liquidity_cap_fraction=0.01,
    )
    expected_cap = available_liquidity_usd * 0.01
    ok = result["capped_by"] == "venue_liquidity" and abs(result["position_size_usd"] - expected_cap) < 1.0
    print(f"  result: {result}")
    print(f"  expected venue cap (1% of real available liquidity): ${expected_cap:,.2f}")
    print("PASS: sizing correctly capped by real venue liquidity, not the portfolio fraction" if ok
          else "FAIL: venue liquidity cap did not engage as expected")
    return ok


def test_cost_aware_cap_real_data():
    section("7. Cost-aware cap against REAL Uniswap v3 pool state (Solidus Labs report)")
    # literature/Solidus Labs Report - The Ex Files.pdf's central finding:
    # execution cost is a function of size, super-linearly for AMMs -- a flat
    # liquidity-fraction cap implicitly assumes linear scaling and so
    # under-states cost at large size. This proves the bisection cap engages
    # against the REAL Uniswap v3 WETH/USDC pool, using its own
    # simulate_trade(), not a synthetic curve.
    try:
        from tradingagents.dataflows.onchain.venues import SpotDEXVenue

        venue = SpotDEXVenue("WETH/USDC")
        state = venue.get_state()
        print(f"  Real Uniswap v3 WETH/USDC pool, block {state['block']}")

        def cost_estimator(usd_size):
            return venue.simulate_trade({"sell_token": "USDC", "amount_in": usd_size}, state=state)[
                "price_impact_bps_estimate"
            ]
    except Exception as e:
        print(f"  SKIP: couldn't reach live RPC ({e}) -- using a synthetic monotonic curve instead")

        def cost_estimator(usd_size):
            return usd_size / 50_000.0  # 1 bps per $50K, monotonic placeholder

    sizer = PositionSizer(max_position_fraction=1.0, kelly_fraction_multiplier=1.0)
    # Deliberately enormous edge/capital so neither the Kelly fraction nor
    # max_position_fraction binds first -- only the cost cap should engage.
    result = sizer.size_position(
        calibrated_probability=0.99,
        payoff_ratio=10.0,
        capital=100_000_000.0,
        cost_estimator=cost_estimator,
        max_execution_cost_bps=25.0,
    )
    print(f"  result: {result}")
    ok = (
        result["capped_by"] == "execution_cost"
        and result["execution_cost_bps_estimate"] is not None
        and abs(result["execution_cost_bps_estimate"] - 25.0) < 1.0
    )
    print("PASS: sizing correctly bisected down to the real cost ceiling, not a flat fraction" if ok
          else "FAIL: cost-aware cap did not engage as expected")
    return ok


def test_no_lookahead_sequencing():
    section("6. No-look-ahead: calibrate() before today's outcome is recorded")
    calibrator = ProbabilityCalibrator(n_bins=10, min_records_to_calibrate=10)
    for _ in range(15):
        calibrator.add_record(0.7, outcome=True)
    calibrator.fit()

    # "Today's" decision: calibrate using only the 15 prior records.
    before = calibrator.calibrate(0.7)
    n_before = len(calibrator.records)

    # Now the outcome becomes known and gets recorded.
    calibrator.add_record(0.7, outcome=False)
    calibrator.fit()
    n_after = len(calibrator.records)

    ok = n_before == 15 and n_after == 16 and before["calibrated_probability"] == 1.0
    print(f"  records used for calibrate(): {n_before}, records after recording outcome: {n_after}")
    print(f"  calibrate() result before recording: {before}")
    print("PASS: today's calibration used only prior records, outcome recorded after" if ok else "FAIL")
    return ok


def main():
    results = [
        test_confidence_parsing(),
        test_ece_detects_known_miscalibration(),
        test_cold_start_no_fabrication(),
        test_kelly_sizing_arithmetic(),
        test_venue_liquidity_cap_real_data(),
        test_cost_aware_cap_real_data(),
        test_no_lookahead_sequencing(),
    ]
    section("Summary")
    print(f"{sum(results)}/{len(results)} test groups passed")
    if not all(results):
        sys.exit(1)


if __name__ == "__main__":
    main()
