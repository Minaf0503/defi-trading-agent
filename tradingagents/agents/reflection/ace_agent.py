"""
Reflection/ACE Agent (Week 16) -- ties together three things that were
previously separate or nonexistent:

  1. Existing qualitative reflection (tradingagents.graph.reflection.Reflector,
     unchanged) -- post-hoc, per-role lessons-learned written to memory.
  2. Stage 4: probability calibration (tradingagents.calibration.ProbabilityCalibrator)
  3. Stage 5: deterministic position sizing (tradingagents.calibration.PositionSizer)

Naming note: "ACE" is not defined anywhere else in this project -- it only
ever appeared as the unexpanded label "Reflection/ACE Agent" in
BUILD_PLAN.md/PROGRESS_LOG.md. Defined here as "Adaptive Calibration
Engine" to match what Stage 4 actually does (the calibration mapping
adapts as more decision outcomes accumulate). This is a naming decision
made during implementation, not a pre-existing requirement -- noted
explicitly since the term is otherwise undocumented.

Takes the Reflector as a constructor argument (dependency injection) rather
than importing tradingagents.graph.reflection directly: agents/ must not
import from graph/, since graph/trading_graph.py already imports
`from tradingagents.agents import *` -- a direct import the other way
would be circular. trading_graph.py, which already constructs a Reflector,
is expected to construct this with that same instance.
"""

from typing import Any, Callable, Dict, Optional

from tradingagents.calibration import PositionSizer, ProbabilityCalibrator


class ReflectionACEAgent:
    def __init__(
        self,
        reflector: Any,
        calibrator: Optional[ProbabilityCalibrator] = None,
        sizer: Optional[PositionSizer] = None,
    ):
        self.reflector = reflector
        self.calibrator = calibrator or ProbabilityCalibrator()
        self.sizer = sizer or PositionSizer()

    def calibrate_and_size(
        self,
        raw_confidence: Optional[float],
        payoff_ratio: float,
        capital: float,
        venue_liquidity_usd: Optional[float] = None,
        cost_estimator: Optional[Callable[[float], Optional[float]]] = None,
        max_execution_cost_bps: float = 50.0,
    ) -> Dict:
        """Decision-time: calibrate today's raw confidence using only
        bins fit from prior outcomes (no look-ahead -- see
        ProbabilityCalibrator's docstring), then size against it.

        raw_confidence=None (the trader didn't emit a parseable confidence)
        is passed through honestly rather than papered over with a guess --
        callers should skip sizing for that decision.

        cost_estimator/max_execution_cost_bps: passed straight through to
        PositionSizer.size_position() -- see its docstring. Added after
        reviewing literature/Solidus Labs Report - The Ex Files.pdf, whose
        central finding is that execution cost is conditional on size, not a
        flat number; a caller can pass a closure around the target venue's
        own simulate_trade() to have sizing respect that directly.
        """
        if raw_confidence is None:
            return {
                "raw_confidence": None,
                "calibrated_probability": None,
                "position_sizing": None,
                "reason": "trader did not emit a parseable confidence -- skipping calibration and sizing for this decision",
            }

        calibration_result = self.calibrator.calibrate(raw_confidence)
        sizing_result = self.sizer.size_position(
            calibrated_probability=calibration_result["calibrated_probability"],
            payoff_ratio=payoff_ratio,
            capital=capital,
            venue_liquidity_usd=venue_liquidity_usd,
            cost_estimator=cost_estimator,
            max_execution_cost_bps=max_execution_cost_bps,
        )
        return {
            "raw_confidence": raw_confidence,
            "calibration": calibration_result,
            "position_sizing": sizing_result,
        }

    def record_outcome_and_refit(self, raw_confidence: float, was_correct: bool, decision_id: Optional[str] = None) -> None:
        """Outcome-time (once a decision's realized result is known): add
        it to the calibration training set and refit, so it's available
        for future decisions' calibrate_and_size() calls. Must be called
        AFTER calibrate_and_size() used this same decision's confidence,
        never before -- adding it first would leak the outcome into its
        own calibration.
        """
        self.calibrator.add_record(raw_confidence, was_correct, decision_id)
        self.calibrator.fit()

    def reflect_and_remember(self, current_state: Dict, returns_losses, memories: Dict[str, Any]) -> None:
        """Delegates the existing qualitative reflection, unchanged --
        same five calls trading_graph.TradingAgentsGraph.reflect_and_remember
        already made directly. Kept here too so ACE can be the single
        post-hoc entry point if Week 17 integration wants one.

        memories: dict with keys bull_memory/bear_memory/trader_memory/
        invest_judge_memory/risk_manager_memory.
        """
        self.reflector.reflect_bull_researcher(current_state, returns_losses, memories["bull_memory"])
        self.reflector.reflect_bear_researcher(current_state, returns_losses, memories["bear_memory"])
        self.reflector.reflect_trader(current_state, returns_losses, memories["trader_memory"])
        self.reflector.reflect_invest_judge(current_state, returns_losses, memories["invest_judge_memory"])
        self.reflector.reflect_risk_manager(current_state, returns_losses, memories["risk_manager_memory"])

    def ece_summary(self) -> Dict:
        """Stage 4 diagnostic: how miscalibrated has the trader's raw
        confidence actually been, measured against realized outcomes.
        """
        return self.calibrator.compute_ece()
