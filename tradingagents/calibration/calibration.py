"""
Stage 4 of the Alpha Illusion-mapped pipeline (draft.md Section 3.1):
probability calibration.

Naming note: BUILD_PLAN.md/PROGRESS_LOG.md call this "P4" as build-plan
shorthand, which happens to agree with the paper's own P4 claim label
("epistemic calibration"). The build plan's "P5" for the sizing module
(sizing.py) does NOT agree with the paper's P5 ("realistic implementation",
already claimed via fork-sim -- see draft.md Section 3.4) -- to avoid that
collision, this code and PROGRESS_LOG.md from 2026-06-22 onward refer to
"Stage 4"/"Stage 5" rather than "P4"/"P5".

An LLM's self-reported confidence is not a calibrated probability -- there
is no reason to expect "I'm 70% confident" actually means "this class of
decision is profitable 70% of the time" without checking, and a wide
literature on LLM calibration says it usually doesn't. This module checks,
using the standard reliability-diagram / binning approach (not a learned
model like isotonic regression, so the mapping stays simple enough to
inspect and explain) rather than assuming raw confidence is usable as-is.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


@dataclass
class CalibrationRecord:
    raw_confidence: float  # 0.0-1.0, the trader's self-reported confidence
    outcome: bool  # True if the decision was profitable/correct
    decision_id: Optional[str] = None


@dataclass
class _Bin:
    lower: float
    upper: float
    confidences: List[float] = field(default_factory=list)
    outcomes: List[bool] = field(default_factory=list)

    @property
    def count(self) -> int:
        return len(self.confidences)

    @property
    def avg_confidence(self) -> Optional[float]:
        return sum(self.confidences) / self.count if self.count else None

    @property
    def accuracy(self) -> Optional[float]:
        return sum(self.outcomes) / self.count if self.count else None


class ProbabilityCalibrator:
    """Bins (raw_confidence, outcome) pairs and maps a new raw confidence to
    the empirical accuracy of its bin -- i.e. "decisions where the trader
    said ~70% confident were actually profitable X% of the time".

    Sequential/no-look-ahead usage (required -- mirrors this project's P1
    temporal-integrity discipline elsewhere): call calibrate() to get a
    probability for TODAY's decision using only bins fit from PRIOR
    outcomes, then once today's outcome is known, call add_record() +
    fit() so it's included for future decisions. Don't fit() on a record
    and then calibrate() that same record -- that's look-ahead.
    """

    def __init__(self, n_bins: int = 10, min_records_to_calibrate: int = 20):
        if not (1 <= n_bins <= 100):
            raise ValueError("n_bins must be between 1 and 100")
        self.n_bins = n_bins
        self.min_records_to_calibrate = min_records_to_calibrate
        self.records: List[CalibrationRecord] = []
        self._bins: List[_Bin] = self._empty_bins()

    def _empty_bins(self) -> List[_Bin]:
        width = 1.0 / self.n_bins
        return [_Bin(lower=i * width, upper=(i + 1) * width) for i in range(self.n_bins)]

    def _bin_index(self, confidence: float) -> int:
        idx = int(confidence * self.n_bins)
        return min(idx, self.n_bins - 1)

    def add_record(self, raw_confidence: float, outcome: bool, decision_id: Optional[str] = None) -> None:
        if not (0.0 <= raw_confidence <= 1.0):
            raise ValueError(f"raw_confidence must be in [0, 1], got {raw_confidence}")
        self.records.append(CalibrationRecord(raw_confidence, outcome, decision_id))

    def fit(self) -> None:
        """Rebuild bins from all records added so far."""
        self._bins = self._empty_bins()
        for rec in self.records:
            b = self._bins[self._bin_index(rec.raw_confidence)]
            b.confidences.append(rec.raw_confidence)
            b.outcomes.append(rec.outcome)

    def calibrate(self, raw_confidence: float) -> Dict:
        """Map a raw confidence to a calibrated probability using bins
        fit so far. Falls back to the raw confidence, explicitly flagged,
        if there isn't enough data yet -- a fabricated calibrated number
        from a near-empty bin would be worse than admitting the gap.
        """
        if not (0.0 <= raw_confidence <= 1.0):
            raise ValueError(f"raw_confidence must be in [0, 1], got {raw_confidence}")

        if len(self.records) < self.min_records_to_calibrate:
            return {
                "raw_confidence": raw_confidence,
                "calibrated_probability": raw_confidence,
                "calibrated": False,
                "reason": f"only {len(self.records)} historical records (need {self.min_records_to_calibrate}) -- returning raw confidence unchanged",
            }

        own_bin = self._bins[self._bin_index(raw_confidence)]
        if own_bin.count > 0:
            return {
                "raw_confidence": raw_confidence,
                "calibrated_probability": own_bin.accuracy,
                "calibrated": True,
                "bin_count": own_bin.count,
            }

        # Own bin is empty even though we have enough total records -- fall
        # back to the nearest non-empty bin rather than the global average,
        # since confidence-dependent miscalibration is exactly what this
        # module exists to catch (a global average would wash that out).
        nonempty = [(abs(b.lower - raw_confidence), b) for b in self._bins if b.count > 0]
        if not nonempty:
            return {
                "raw_confidence": raw_confidence,
                "calibrated_probability": raw_confidence,
                "calibrated": False,
                "reason": "no non-empty bins -- returning raw confidence unchanged",
            }
        _, nearest = min(nonempty, key=lambda t: t[0])
        return {
            "raw_confidence": raw_confidence,
            "calibrated_probability": nearest.accuracy,
            "calibrated": True,
            "bin_count": nearest.count,
            "reason": f"own bin [{own_bin.lower:.1f}, {own_bin.upper:.1f}) empty -- used nearest non-empty bin instead",
        }

    def compute_ece(self) -> Dict:
        """Expected Calibration Error: weighted average gap between each
        bin's mean stated confidence and its empirical accuracy. 0 = perfect
        calibration; standard diagnostic, not something we invented.
        """
        n = len(self.records)
        if n == 0:
            return {"ece": None, "n_records": 0, "bins": []}

        ece = 0.0
        bin_diagnostics = []
        for b in self._bins:
            if b.count == 0:
                continue
            weight = b.count / n
            gap = abs(b.avg_confidence - b.accuracy)
            ece += weight * gap
            bin_diagnostics.append(
                {
                    "range": [round(b.lower, 2), round(b.upper, 2)],
                    "count": b.count,
                    "avg_confidence": round(b.avg_confidence, 4),
                    "accuracy": round(b.accuracy, 4),
                    "gap": round(gap, 4),
                }
            )
        return {"ece": ece, "n_records": n, "bins": bin_diagnostics}
