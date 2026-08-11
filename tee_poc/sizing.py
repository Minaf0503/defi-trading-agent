"""
Stage 5 of the Alpha Illusion-mapped pipeline (draft.md Section 3.1):
deterministic position sizing. See calibration.py's module docstring for
why this is called "Stage 5" rather than build-plan shorthand "P5" here.

Sizing is the fractional Kelly criterion -- standard, not novel -- applied
to the Stage 4 calibrated probability (not the trader's raw, uncalibrated
confidence; sizing off an uncalibrated number defeats the point of having
calibrated one). A safety multiplier (half-Kelly by default, common
practice since full Kelly is high-variance under any model misspecification)
and a hard fraction cap are both applied on top, and -- where real Phase 2
venue data is available -- a venue-liquidity cap, so sizing never proposes
a position the venue's own state shows it can't actually support without
material price impact.

Cost-aware cap (added after reviewing Solidus Labs' "The Ex Files" report,
literature/Solidus Labs Report - The Ex Files.pdf): that report's central
empirical finding is that execution cost is not a flat number -- it is a
function of size, and the function is super-linear for AMM and order-book
venues (their measured example: Uniswap goes from ~2 bps under $1K to 165
bps above $100K on BTC; a flat liquidity-fraction cap, which is what this
module had before, implicitly assumes cost scales linearly with size and so
systematically under-estimates cost at the top of the size range). The
`cost_estimator` parameter below lets a caller plug in the real venue's own
simulate_trade()-derived price-impact-in-bps function and have sizing
respect it directly, rather than only a static liquidity fraction. This
project only ever holds one spot venue, one perp venue, and one vault venue
per asset (no competing venues to route between), so the report's
venue-selection/routing and session/day-of-week findings don't have an
analog here yet -- the size-sensitivity finding is the one that transfers
regardless of how many venues you're choosing between.
"""

from typing import Callable, Dict, Optional


class PositionSizer:
    def __init__(self, max_position_fraction: float = 0.25, kelly_fraction_multiplier: float = 0.5):
        if not (0.0 < max_position_fraction <= 1.0):
            raise ValueError("max_position_fraction must be in (0, 1]")
        if not (0.0 < kelly_fraction_multiplier <= 1.0):
            raise ValueError("kelly_fraction_multiplier must be in (0, 1]")
        self.max_position_fraction = max_position_fraction
        self.kelly_fraction_multiplier = kelly_fraction_multiplier

    def size_position(
        self,
        calibrated_probability: float,
        payoff_ratio: float,
        capital: float,
        venue_liquidity_usd: Optional[float] = None,
        venue_liquidity_cap_fraction: float = 0.01,
        cost_estimator: Optional[Callable[[float], Optional[float]]] = None,
        max_execution_cost_bps: float = 50.0,
    ) -> Dict:
        """
        calibrated_probability: Stage 4 output, P(decision is profitable), 0-1.
        payoff_ratio: expected win amount / expected loss amount for this
            trade (b in the standard Kelly formula f* = p - (1-p)/b). This
            project does not yet have a principled per-decision estimate of
            this -- see Limitations -- so callers must supply one explicitly
            rather than this module silently assuming 1:1.
        capital: total capital available to size against, in USD.
        venue_liquidity_usd: if given (e.g. PerpVenue's available_liquidity_*_usd,
            or SpotDEXVenue's pool liquidity converted to USD), caps the
            position at venue_liquidity_cap_fraction of it, so sizing
            respects the venue's own real state rather than just the
            portfolio's risk budget.
        cost_estimator: optional callable, USD size -> estimated price impact
            in bps (or None if not computable), e.g. a closure around an
            already-fetched venue.get_state() result calling
            venue.simulate_trade(..., state=state) at the candidate size.
            Must be monotonically non-decreasing in size (true of AMM and
            order-book depth, per the cited report) -- if given, sizing
            bisects down to the largest size at or under
            max_execution_cost_bps rather than trusting a single flat
            estimate. Keep this cheap: it is called ~12 times per sizing
            decision.
        max_execution_cost_bps: the cost ceiling cost_estimator is bisected
            against. 50 bps is a conservative default placeholder, not a
            calibrated risk parameter -- callers running real capital should
            set this deliberately.
        """
        if not (0.0 <= calibrated_probability <= 1.0):
            raise ValueError(f"calibrated_probability must be in [0, 1], got {calibrated_probability}")
        if payoff_ratio <= 0:
            raise ValueError(f"payoff_ratio must be positive, got {payoff_ratio}")
        if capital < 0:
            raise ValueError(f"capital must be non-negative, got {capital}")

        kelly_fraction_raw = calibrated_probability - (1 - calibrated_probability) / payoff_ratio
        kelly_fraction_raw = max(kelly_fraction_raw, 0.0)  # negative edge -> no position, not a short

        kelly_fraction_applied = kelly_fraction_raw * self.kelly_fraction_multiplier
        capped_by = None

        if kelly_fraction_applied > self.max_position_fraction:
            kelly_fraction_applied = self.max_position_fraction
            capped_by = "max_position_fraction"

        position_size_usd = kelly_fraction_applied * capital

        if venue_liquidity_usd is not None:
            venue_cap_usd = venue_liquidity_usd * venue_liquidity_cap_fraction
            if position_size_usd > venue_cap_usd:
                position_size_usd = venue_cap_usd
                capped_by = "venue_liquidity"

        execution_cost_bps_estimate = None
        if cost_estimator is not None and position_size_usd > 0:
            execution_cost_bps_estimate = cost_estimator(position_size_usd)
            if execution_cost_bps_estimate is not None and execution_cost_bps_estimate > max_execution_cost_bps:
                position_size_usd = self._bisect_to_cost_ceiling(
                    cost_estimator, position_size_usd, max_execution_cost_bps
                )
                execution_cost_bps_estimate = cost_estimator(position_size_usd) if position_size_usd > 0 else 0.0
                capped_by = "execution_cost"

        return {
            "calibrated_probability": calibrated_probability,
            "payoff_ratio": payoff_ratio,
            "kelly_fraction_raw": kelly_fraction_raw,
            "kelly_fraction_multiplier": self.kelly_fraction_multiplier,
            "kelly_fraction_applied": kelly_fraction_applied,
            "position_size_usd": position_size_usd,
            "execution_cost_bps_estimate": execution_cost_bps_estimate,
            "max_execution_cost_bps": max_execution_cost_bps if cost_estimator is not None else None,
            "capped_by": capped_by,
        }

    @staticmethod
    def _bisect_to_cost_ceiling(
        cost_estimator: Callable[[float], Optional[float]],
        upper_bound_usd: float,
        max_execution_cost_bps: float,
        iterations: int = 12,
    ) -> float:
        """Largest size in [0, upper_bound_usd] with cost_estimator(size) <=
        max_execution_cost_bps, assuming cost is non-decreasing in size.
        12 iterations halves the search window each time -- well under 0.03%
        of upper_bound_usd, far finer than this cap needs to be."""
        lo, hi = 0.0, upper_bound_usd
        for _ in range(iterations):
            mid = (lo + hi) / 2
            cost = cost_estimator(mid) if mid > 0 else 0.0
            if cost is None or cost <= max_execution_cost_bps:
                lo = mid
            else:
                hi = mid
        return lo
