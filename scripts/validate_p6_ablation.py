#!/usr/bin/env python
"""
Validate Phase 5 Week 19: P6 (multi-agent disaggregation) ablation
instrumentation -- LLMCallTracker, role_similarity, and SingleAgentBaseline.

Deterministic, no real LLM calls or API cost: uses langchain_core's
FakeListChatModel throughout. This proves the instrumentation's mechanics
are correct (callback propagation through bind()/pipe composition, latency
measurement, confidence parsing, word-overlap arithmetic) -- it does not
and cannot validate whether the ablation's *findings* (does debate add
value, are roles actually differentiated) hold on real decisions. That
needs scripts/run_p6_ablation.py against a real LLM key.

Usage:
    python scripts/validate_p6_ablation.py
"""

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from langchain_core.language_models.fake_chat_models import FakeListChatModel

from tradingagents.ablation import LLMCallTracker, SingleAgentBaseline, compute_role_similarity, jaccard_word_overlap


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def test_tracker_call_counting():
    section("1. LLMCallTracker: call counting and latency, via a fake model")
    # NOTE (2026-06-22): this test's llm.with_config() -> llm.bind() ordering
    # does NOT reproduce ChatOpenAI's real .bind_tools() bug (see
    # trading_graph.py's __init__ comment) -- FakeListChatModel.bind() uses
    # the generic Runnable.bind(), which correctly preserves the outer
    # with_config()'s callbacks, while ChatOpenAI overrides .bind()/
    # .bind_tools() with logic that drops them in this exact order. This
    # test was previously (wrongly) cited as having verified the real
    # analyst-tool-calling path was safe; it only verifies the GENERIC
    # callback-through-.bind() mechanism, which was never the broken part.
    # The actual fix -- moving callback attachment to invoke-time
    # RunnableConfig instead of construction-time with_config() -- was
    # verified against a real ChatOpenAI + bind_tools() + LangGraph node
    # call (see PROGRESS_LOG.md), not against this fake model.
    tracker = LLMCallTracker()
    llm = FakeListChatModel(responses=["a", "b", "c"]).with_config({"callbacks": [tracker]})

    llm.invoke("hi")
    llm.invoke("hi")
    bound = llm.bind(stop=["x"])
    bound.invoke("hi")

    stats = tracker.summary()
    print(f"  stats after 3 calls (1 direct, 1 direct, 1 via .bind()): {stats}")
    ok = stats["call_count"] == 3 and stats["total_latency_s"] >= 0.0
    print("PASS: tracker counted all 3 calls including one routed through .bind()" if ok else "FAIL")

    tracker.reset()
    stats_after_reset = tracker.summary()
    ok2 = stats_after_reset["call_count"] == 0
    print(f"  stats after reset(): {stats_after_reset}")
    print("PASS: reset() clears counters" if ok2 else "FAIL")
    return ok and ok2


def test_tracker_missing_token_usage_reported_honestly():
    section("2. LLMCallTracker: missing token usage reported as None, not fabricated")
    tracker = LLMCallTracker()
    llm = FakeListChatModel(responses=["a"]).with_config({"callbacks": [tracker]})
    llm.invoke("hi")  # FakeListChatModel never populates usage_metadata
    stats = tracker.summary()
    print(f"  stats: {stats}")
    ok = stats["total_tokens"] is None and stats["call_count"] == 1
    print("PASS: total_tokens correctly reported as None when the model never provides usage data" if ok
          else "FAIL: should not fabricate a token count")
    return ok


def test_role_similarity_arithmetic():
    section("3. Role similarity: hand-checkable Jaccard word-overlap arithmetic")
    # Identical texts -> overlap 1.0
    ok1 = jaccard_word_overlap("buy ethereum now strong momentum", "buy ethereum now strong momentum") == 1.0
    print(f"  identical texts -> {jaccard_word_overlap('buy ethereum now strong momentum', 'buy ethereum now strong momentum')}")
    print("PASS: identical texts give overlap 1.0" if ok1 else "FAIL")

    # Completely disjoint significant words -> overlap 0.0
    disjoint = jaccard_word_overlap("bullish momentum breakout rally", "bearish capitulation crash decline")
    ok2 = disjoint == 0.0
    print(f"  disjoint texts -> {disjoint}")
    print("PASS: disjoint texts give overlap 0.0" if ok2 else "FAIL")

    # Empty text -> None, not a fabricated 0
    ok3 = jaccard_word_overlap("", "bullish momentum") is None
    print(f"  empty text -> {jaccard_word_overlap('', 'bullish momentum')}")
    print("PASS: empty text correctly returns None, not a fabricated 0" if ok3 else "FAIL")

    # Known partial overlap: {bullish, momentum, strong} vs {bullish, momentum, weak}
    # significant words (len>2, not stopword): both share {bullish, momentum} = 2;
    # union = {bullish, momentum, strong, weak} = 4 -> 2/4 = 0.5
    partial = jaccard_word_overlap("bullish momentum strong", "bullish momentum weak")
    ok4 = partial == 0.5
    print(f"  hand-checked partial overlap -> {partial} (expected 0.5)")
    print("PASS: matches hand-computed Jaccard overlap" if ok4 else f"FAIL: expected 0.5, got {partial}")

    result = compute_role_similarity(
        {"bull_history": "bullish momentum strong", "bear_history": "bullish momentum weak"},
        {"risky_history": "high reward worth it", "safe_history": "too risky avoid", "neutral_history": "balanced moderate position"},
    )
    print(f"\n  compute_role_similarity() full output: {result}")
    ok5 = result["bull_vs_bear_word_overlap"] == 0.5 and result["risk_debate_mean_word_overlap"] is not None
    print("PASS: compute_role_similarity aggregates correctly" if ok5 else "FAIL")
    return ok1 and ok2 and ok3 and ok4 and ok5


def test_single_agent_baseline_parsing_and_latency():
    section("4. SingleAgentBaseline: prompt construction, confidence parsing, latency capture")
    canned_response = "Given the bullish technical setup and healthy on-chain liquidity, I recommend entering a position.\n\nFINAL TRANSACTION PROPOSAL: **BUY** (Confidence: 65%)"
    tracker = LLMCallTracker()
    llm = FakeListChatModel(responses=[canned_response]).with_config({"callbacks": [tracker]})

    baseline = SingleAgentBaseline(llm)
    result = baseline.decide(
        ticker="ETH",
        trade_date="2026-06-22",
        technical_report="Price up 3%, RSI neutral.",
        onchain_report="Liquidity deep, no unusual flows.",
        tokenomics_report="Supply stable.",
        sentiment_news_report="Mildly positive news flow.",
    )
    print(f"  result: {result}")
    ok1 = result["raw_confidence"] == 0.65
    print("PASS: confidence parsed correctly from the canned response" if ok1 else "FAIL")
    ok2 = result["latency_s"] >= 0.0
    print("PASS: latency captured" if ok2 else "FAIL")

    stats = tracker.summary()
    ok3 = stats["call_count"] == 1
    print(f"  tracker stats after one decide() call: {stats}")
    print("PASS: exactly one LLM call made (no debate, no extra rounds)" if ok3 else "FAIL")
    return ok1 and ok2 and ok3


def test_single_agent_baseline_handles_unparseable_response():
    section("5. SingleAgentBaseline: unparseable response -> None, not a guessed confidence")
    llm = FakeListChatModel(responses=["I think this could go either way, hard to say."])
    baseline = SingleAgentBaseline(llm)
    result = baseline.decide("ETH", "2026-06-22", "report1", "report2", "report3", "report4")
    print(f"  result: {result}")
    ok = result["raw_confidence"] is None
    print("PASS: correctly returns None rather than fabricating a confidence" if ok else "FAIL")
    return ok


def test_graph_shares_tracker_between_arms():
    section("6. TradingAgentsGraph: single-agent baseline shares the SAME tracker as the full pipeline")
    import os

    os.environ.setdefault("OPENAI_API_KEY", "dummy-key-for-construction-only")
    from tradingagents.graph.trading_graph import TradingAgentsGraph

    graph = TradingAgentsGraph(debug=False)
    baseline = graph.build_single_agent_baseline()
    ok1 = baseline.llm is graph.quick_thinking_llm
    ok2 = baseline.memory is graph.trader_memory
    ok3 = baseline.tracker is graph.llm_call_tracker
    print(f"  baseline.llm is graph.quick_thinking_llm: {ok1}")
    print(f"  baseline.memory is graph.trader_memory: {ok2}")
    print(f"  baseline.tracker is graph.llm_call_tracker: {ok3}")
    print("PASS: single-agent baseline uses the same LLM class and tracker as the production Trader node, for a fair comparison"
          if (ok1 and ok2 and ok3) else "FAIL")
    return ok1 and ok2 and ok3


def main():
    results = [
        test_tracker_call_counting(),
        test_tracker_missing_token_usage_reported_honestly(),
        test_role_similarity_arithmetic(),
        test_single_agent_baseline_parsing_and_latency(),
        test_single_agent_baseline_handles_unparseable_response(),
        test_graph_shares_tracker_between_arms(),
    ]
    section("Summary")
    print(f"{sum(results)}/{len(results)} test groups passed")
    if not all(results):
        sys.exit(1)


if __name__ == "__main__":
    main()
