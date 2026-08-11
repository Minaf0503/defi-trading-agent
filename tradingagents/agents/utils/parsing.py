"""
Deterministic, regex-based parsing of structured fields out of an LLM's
free-text decision -- kept separate from any LLM-based extraction (like
SignalProcessor's BUY/SELL/HOLD parsing) because a numeric confidence
feeding a downstream statistical calibration step (Stage 4, see
tradingagents/calibration/) needs to be exact, not another LLM's
paraphrase of a number.
"""

import re
from typing import Optional

CONFIDENCE_PATTERN = re.compile(
    r"FINAL TRANSACTION PROPOSAL:\s*\*{0,2}(BUY|HOLD|SELL)\*{0,2}\s*\(Confidence:\s*(\d{1,3})%\)",
    re.IGNORECASE,
)


def extract_confidence(full_signal: str) -> Optional[float]:
    """Extract the trader's self-reported confidence (0.0-1.0) from its
    'FINAL TRANSACTION PROPOSAL: **BUY/HOLD/SELL** (Confidence: NN%)' line.

    Returns None if the LLM didn't follow the required format -- callers
    must handle this explicitly (e.g. skip calibration for that decision)
    rather than substituting a guessed value.
    """
    match = CONFIDENCE_PATTERN.search(full_signal or "")
    if not match:
        return None
    pct = int(match.group(2))
    if not (0 <= pct <= 100):
        return None
    return pct / 100.0
