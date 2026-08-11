"""
P6 (multi-agent disaggregation) instrumentation -- Alpha Illusion's P6
minimum reporting includes "role similarity" and "disagreement rate":
evidence for or against the "multi-agent consensus illusion" concern, where
debate participants drawn from the same underlying model converge on
similar reasoning rather than genuinely disagreeing as independent experts
would.

This is a deliberately coarse, deterministic proxy -- lexical (word-level)
Jaccard overlap between debate participants' conversation histories, not a
semantic or stance-classification model. No embedding infrastructure exists
in this project, and adding one solely for this metric would be more
machinery than the ablation needs; this is flagged as a real limitation
(see draft.md Limitations), not presented as a sophisticated NLP technique.
Low overlap is read as evidence of differentiation (not an echo chamber);
high overlap is read as a noteworthy signal worth a closer qualitative
read, not proof of groupthink on its own.
"""

import re
from typing import Dict, Optional

_STOPWORDS = frozenset(
    """
    a an the and or but if while of to in on at by for with about against
    between into through during before after above below from up down out
    off over under again further then once here there all any both each
    few more most other some such no nor not only own same so than too very
    s t can will just don should now is are was were be been being have has
    had do does did doing this that these those i you he she it we they
    them his her its our your their as
    """.split()
)


def jaccard_word_overlap(text_a: str, text_b: str) -> Optional[float]:
    """0.0 (no shared significant words) to 1.0 (identical word sets).
    None if either text is empty (no debate occurred -- e.g. a single-round
    "debate" or a node that never ran), not a fabricated 0."""
    words_a = _significant_words(text_a)
    words_b = _significant_words(text_b)
    if not words_a or not words_b:
        return None
    union = words_a | words_b
    intersection = words_a & words_b
    return len(intersection) / len(union)


def _significant_words(text: str) -> set:
    tokens = re.findall(r"[a-zA-Z']+", (text or "").lower())
    return {t for t in tokens if t not in _STOPWORDS and len(t) > 2}


def compute_role_similarity(investment_debate_state: Dict, risk_debate_state: Dict) -> Dict:
    """investment_debate_state/risk_debate_state: the same dicts already
    present in AgentState after propagate() -- bull_history/bear_history,
    and risky_history/safe_history/neutral_history.
    """
    bull = investment_debate_state.get("bull_history", "")
    bear = investment_debate_state.get("bear_history", "")
    risky = risk_debate_state.get("risky_history", "")
    safe = risk_debate_state.get("safe_history", "")
    neutral = risk_debate_state.get("neutral_history", "")

    risk_pairs = {
        "risky_vs_safe": jaccard_word_overlap(risky, safe),
        "risky_vs_neutral": jaccard_word_overlap(risky, neutral),
        "safe_vs_neutral": jaccard_word_overlap(safe, neutral),
    }
    available_risk_pairs = [v for v in risk_pairs.values() if v is not None]

    return {
        "bull_vs_bear_word_overlap": jaccard_word_overlap(bull, bear),
        "risk_debate_pairwise_word_overlap": risk_pairs,
        "risk_debate_mean_word_overlap": (
            sum(available_risk_pairs) / len(available_risk_pairs) if available_risk_pairs else None
        ),
        "caveat": (
            "Lexical (word-overlap) proxy, not semantic similarity -- low overlap is "
            "evidence of differentiation; high overlap is a signal worth a closer "
            "qualitative read, not proof of groupthink on its own. See Limitations."
        ),
    }
