#!/usr/bin/env python
"""Deterministic validation for the LLM-as-judge module (no real LLM calls,
zero cost) -- specifically the de-anonymization logic in judge_decision_pair,
since a bug there would silently mislabel which arm "won" every comparison."""

import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tradingagents.ablation.llm_judge import judge_decision_pair


class FakeJudgeLLM:
    """Always says 'A is better' with fixed, asymmetric scores -- lets us
    check relabeling is correct regardless of which real arm landed on A."""

    def invoke(self, messages):
        class FakeResult:
            def model_dump(self):
                return {
                    "evidence_grounding_a": 9, "evidence_grounding_b": 3,
                    "logical_coherence_a": 8, "logical_coherence_b": 2,
                    "uncertainty_engagement_a": 7, "uncertainty_engagement_b": 1,
                    "overall_preference": "A",
                    "justification": "A is more grounded.",
                }
        return FakeResult()


def test_relabeling_both_orderings():
    section = "1. De-anonymization: correct regardless of random A/B assignment"
    print(f"\n{'='*70}\n{section}\n{'='*70}")

    fake_llm = FakeJudgeLLM()
    ok = True

    # Force multi_agent -> A (rng.random() < 0.5 is True)
    rng_a = random.Random()
    rng_a.random = lambda: 0.1
    result_a = judge_decision_pair("tech report", "onchain report", "tokenomics report",
                                    "MULTI AGENT TEXT", "SINGLE AGENT TEXT", rng_a, judge_llm=fake_llm)
    print("multi_agent forced to A:", result_a)
    if result_a["evidence_grounding_multi_agent"] != 9 or result_a["evidence_grounding_single_agent"] != 3:
        print("FAIL: scores not correctly relabeled when multi_agent=A")
        ok = False
    if result_a["overall_preference"] != "multi_agent":
        print("FAIL: preference should map to multi_agent when judge picked A and multi_agent=A")
        ok = False

    # Force multi_agent -> B (rng.random() < 0.5 is False)
    rng_b = random.Random()
    rng_b.random = lambda: 0.9
    result_b = judge_decision_pair("tech report", "onchain report", "tokenomics report",
                                    "MULTI AGENT TEXT", "SINGLE AGENT TEXT", rng_b, judge_llm=fake_llm)
    print("multi_agent forced to B:", result_b)
    if result_b["evidence_grounding_multi_agent"] != 3 or result_b["evidence_grounding_single_agent"] != 9:
        print("FAIL: scores not correctly relabeled when multi_agent=B")
        ok = False
    if result_b["overall_preference"] != "single_agent":
        print("FAIL: preference should map to single_agent when judge picked A but multi_agent=B")
        ok = False

    print("PASS: relabeling correct in both random orderings" if ok else "FAIL")
    return ok


class FakeTieLLM:
    def invoke(self, messages):
        class FakeResult:
            def model_dump(self):
                return {
                    "evidence_grounding_a": 5, "evidence_grounding_b": 5,
                    "logical_coherence_a": 5, "logical_coherence_b": 5,
                    "uncertainty_engagement_a": 5, "uncertainty_engagement_b": 5,
                    "overall_preference": "tie",
                    "justification": "Comparable.",
                }
        return FakeResult()


def test_tie_passthrough():
    section = "2. Tie verdict passes through regardless of A/B assignment"
    print(f"\n{'='*70}\n{section}\n{'='*70}")
    rng = random.Random()
    rng.random = lambda: 0.1
    result = judge_decision_pair("t", "o", "tok", "M", "S", rng, judge_llm=FakeTieLLM())
    ok = result["overall_preference"] == "tie"
    print(result)
    print("PASS: tie correctly passes through" if ok else "FAIL")
    return ok


def main():
    results = [test_relabeling_both_orderings(), test_tie_passthrough()]
    print(f"\n{'='*70}\nSummary\n{'='*70}")
    print(f"{sum(results)}/{len(results)} test groups passed")
    sys.exit(0 if all(results) else 1)


if __name__ == "__main__":
    main()
