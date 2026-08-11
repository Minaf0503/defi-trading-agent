"""
Phase 5 Week 19: LLM-as-judge evaluation -- the second half of Week 19,
alongside the P6 single-agent ablation (single_agent_baseline.py).

Pairwise, not absolute scoring: shown two candidate decision texts side by
side and asked to compare, rather than scoring each in isolation. Standard
LLM-as-judge practice (Zheng et al. 2023, "Judging LLM-as-a-Judge with
MT-Bench and Chatbot Arena") finds pairwise comparison more reliable than
absolute scoring, and it directly answers this project's actual question --
is the multi-agent debate's reasoning better, not just "is it an 8/10."

Bias mitigations applied, and their limits, disclosed rather than hidden:
- Blind: the judge sees "Response A"/"Response B", never told which arm
  (multi-agent vs. single-agent) produced which, or which is "the debate
  pipeline" vs. "the baseline".
- Order-randomized per point (not double-run with both orderings per point,
  which would be the stronger mitigation against position bias -- not done
  here for cost/scope reasons; randomization across 28 points still
  averages out *aggregate* position bias even though it can't catch
  per-point order sensitivity).
- Judge model (gpt-4o) is deliberately neither of the two models that wrote
  the candidate text: o4-mini writes the multi-agent arm's final decision
  (Risk Judge), gpt-4o-mini writes the single-agent arm's. Using either of
  those as judge would risk self-preference bias specifically toward the
  arm sharing its model. gpt-4o is still the same provider/family as both
  -- a real, disclosed limitation, not a fully independent third-party
  judge (this project only has an OpenAI key configured).
- Judge never sees realized outcomes -- this is a reasoning-quality
  judgment, scored independently of whether the decision turned out to be
  right. Correlating judge preference with realized correctness happens
  separately, after scoring, not as part of the judge's prompt.
- Given the SAME underlying analyst reports as both arms, the judge can
  check claims against the actual source data, not just reward fluent
  prose -- it doesn't have to take either response's claims on faith.
"""

import random
import time
from typing import Dict, Literal

from langchain_openai import ChatOpenAI
from openai import RateLimitError
from pydantic import BaseModel, Field

JUDGE_MODEL = "gpt-4o"
MAX_RETRIES = 5


class PairwiseJudgment(BaseModel):
    evidence_grounding_a: int = Field(description="1-10: how well Response A cites specific facts from the provided analyst reports, vs. vague generalities")
    evidence_grounding_b: int = Field(description="Same scale, Response B")
    logical_coherence_a: int = Field(description="1-10: does Response A's conclusion actually follow from its stated premises")
    logical_coherence_b: int = Field(description="Same scale, Response B")
    uncertainty_engagement_a: int = Field(description="1-10: does Response A acknowledge counter-evidence/risks, or is it one-sided")
    uncertainty_engagement_b: int = Field(description="Same scale, Response B")
    overall_preference: Literal["A", "B", "tie"] = Field(description="Which response is better-reasoned overall, or tie if genuinely comparable")
    justification: str = Field(description="2-4 sentences explaining the verdict, citing specifics from each response")


JUDGE_SYSTEM_PROMPT = """You are an impartial judge evaluating the QUALITY OF REASONING in two trading-decision write-ups for the same token and date. You are not told which system produced which response, and you should not try to guess -- judge only what is written.

You are given the same underlying analyst reports (technical, on-chain, tokenomics) that both responses were based on. Use them to check whether each response's claims are actually grounded in that data, not just plausible-sounding.

Do NOT consider which response's ultimate trade call (BUY/SELL/HOLD) "sounds more confident" or "sounds more decisive" as a virtue in itself -- a well-reasoned HOLD that honestly says the evidence is mixed is not worse than a confident BUY that ignores counter-evidence. Judge the REASONING, not the decisiveness or the eventual real-world outcome (you don't know the outcome and shouldn't guess at it)."""


def judge_pairwise(
    technical_report: str,
    onchain_report: str,
    tokenomics_report: str,
    response_a_text: str,
    response_b_text: str,
    judge_llm=None,
) -> Dict:
    llm = judge_llm or ChatOpenAI(model=JUDGE_MODEL).with_structured_output(PairwiseJudgment)

    human_message = (
        f"Technical Analyst Report:\n{technical_report}\n\n"
        f"On-Chain Analyst Report:\n{onchain_report}\n\n"
        f"Tokenomics Analyst Report:\n{tokenomics_report}\n\n"
        f"--- Response A ---\n{response_a_text}\n\n"
        f"--- Response B ---\n{response_b_text}\n\n"
        f"Evaluate both responses' reasoning quality per the rubric."
    )

    messages = [
        {"role": "system", "content": JUDGE_SYSTEM_PROMPT},
        {"role": "user", "content": human_message},
    ]
    for attempt in range(MAX_RETRIES):
        try:
            result = llm.invoke(messages)
            return result.model_dump() if hasattr(result, "model_dump") else dict(result)
        except RateLimitError:
            if attempt == MAX_RETRIES - 1:
                raise
            time.sleep(5 * (attempt + 1))  # org TPM limits reset on a rolling per-minute window


def judge_decision_pair(
    technical_report: str,
    onchain_report: str,
    tokenomics_report: str,
    multi_agent_text: str,
    single_agent_text: str,
    rng: random.Random,
    judge_llm=None,
) -> Dict:
    """Randomizes which arm is "A" vs "B" before calling judge_pairwise, then
    de-anonymizes the result -- so the judge never sees which arm is which,
    but the caller gets back arm-labeled scores."""
    multi_agent_is_a = rng.random() < 0.5
    response_a = multi_agent_text if multi_agent_is_a else single_agent_text
    response_b = single_agent_text if multi_agent_is_a else multi_agent_text

    raw = judge_pairwise(technical_report, onchain_report, tokenomics_report, response_a, response_b, judge_llm=judge_llm)

    def relabel(key_a, key_b):
        return (raw[key_a], raw[key_b]) if multi_agent_is_a else (raw[key_b], raw[key_a])

    eg_multi, eg_single = relabel("evidence_grounding_a", "evidence_grounding_b")
    lc_multi, lc_single = relabel("logical_coherence_a", "logical_coherence_b")
    ue_multi, ue_single = relabel("uncertainty_engagement_a", "uncertainty_engagement_b")

    if raw["overall_preference"] == "tie":
        preference = "tie"
    elif (raw["overall_preference"] == "A") == multi_agent_is_a:
        preference = "multi_agent"
    else:
        preference = "single_agent"

    return {
        "multi_agent_was_response": "A" if multi_agent_is_a else "B",
        "evidence_grounding_multi_agent": eg_multi,
        "evidence_grounding_single_agent": eg_single,
        "logical_coherence_multi_agent": lc_multi,
        "logical_coherence_single_agent": lc_single,
        "uncertainty_engagement_multi_agent": ue_multi,
        "uncertainty_engagement_single_agent": ue_single,
        "overall_preference": preference,
        "justification": raw["justification"],
    }
