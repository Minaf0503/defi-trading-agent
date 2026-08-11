"""
P6 (multi-agent disaggregation) ablation -- Alpha Illusion's named minimum
requirement: "Single-agent baseline" to isolate whether multi-agent debate
adds value beyond what one model, given the same information, would decide
alone (failure mode: "multi-agent consensus illusion").

Design choice: this baseline is given the SAME four analyst reports the
full pipeline produces (technical/onchain/tokenomics/sentiment_news) rather
than calling its own tools to gather fresh data. Letting it gather its own
data would confound two different variables -- "how much/which data does
it see" and "does it debate before deciding" -- when P6 specifically wants
to isolate the second one. Holding the input data identical between arms
means any difference in the final decision is attributable to the
debate/role structure itself, not to a difference in information access.

Also deliberately mirrors trader.py's interface as closely as possible:
same memory-lookup pattern (optional, same query construction), same
confidence-honesty instructions, same required output format
('FINAL TRANSACTION PROPOSAL: **BUY/HOLD/SELL** (Confidence: NN%)'), parsed
by the same deterministic regex (tradingagents.agents.utils.parsing). The
one thing this agent is NOT told is the debate-synthesized investment plan
trader.py actually conditions on (Section 3.1's bull/bear -> Research
Manager output) -- it sees only the raw analyst reports and must reach its
own investment view and trade decision in one shot, which is exactly the
capability the multi-agent debate exists to add on top of.
"""

import time
from typing import Dict, Optional

from tradingagents.agents.utils.parsing import extract_confidence


class SingleAgentBaseline:
    def __init__(self, llm, memory=None, tracker=None):
        """
        llm: should be the SAME LLM class the production Trader node uses
            (quick_thinking_llm as of this writing -- see graph/setup.py) for
            a fair cost/latency comparison; using a different/stronger model
            for this arm would confound the ablation.
        memory: optional FinancialSituationMemory instance (e.g.
            graph.trader_memory) -- if given, this agent gets the same
            past-lessons lookup trader.py uses, so the comparison isolates
            debate structure specifically, not "debate + memory access vs.
            neither."
        tracker: optional LLMCallTracker (e.g. graph.llm_call_tracker), passed
            explicitly at invoke time rather than via llm.with_config() --
            see trading_graph.py's __init__ comment for why construction-time
            with_config() is no longer used (it silently drops callbacks for
            any .bind_tools() caller; this class doesn't bind tools, but the
            same explicit-at-invoke-time convention is used everywhere now
            for consistency and to avoid double-counting on the graph side).
        """
        self.llm = llm
        self.memory = memory
        self.tracker = tracker

    def decide(
        self,
        ticker: str,
        trade_date: str,
        technical_report: str,
        onchain_report: str,
        tokenomics_report: str,
        sentiment_news_report: str,
    ) -> Dict:
        curr_situation = f"{technical_report}\n\n{onchain_report}\n\n{tokenomics_report}\n\n{sentiment_news_report}"

        past_memory_str = "No past memories found."
        if self.memory is not None:
            past_memories = self.memory.get_memories(curr_situation, n_matches=2)
            if past_memories:
                past_memory_str = "\n\n".join(rec["recommendation"] for rec in past_memories)

        system_message = f"""You are a single trading agent responsible for the entire investment decision on your own -- there is no analyst team, no bull/bear debate, and no separate risk committee to consult. You must read the raw analyst reports below yourself and decide. Based on your analysis, provide a specific recommendation to buy, sell, or hold. End with a firm decision and always conclude your response with 'FINAL TRANSACTION PROPOSAL: **BUY/HOLD/SELL** (Confidence: NN%)' -- the confidence is YOUR OWN self-assessed probability (0-100) that this decision will be profitable, not a measure of how strongly you phrased the recommendation. Be honest about uncertainty; a well-calibrated 55% means you genuinely think it's close to a coin flip, not a hedge to avoid commitment. This number feeds a downstream statistical calibration step, so it needs to be your real estimate, not decoration. Do not forget to utilize lessons from past decisions to learn from your mistakes. Here is some reflections from similar situations you traded in and the lessons learned: {past_memory_str}"""

        human_message = (
            f"Token: {ticker}\nDate: {trade_date}\n\n"
            f"Technical Analyst Report:\n{technical_report}\n\n"
            f"On-Chain Analyst Report:\n{onchain_report}\n\n"
            f"Tokenomics Analyst Report:\n{tokenomics_report}\n\n"
            f"Sentiment/News Analyst Report:\n{sentiment_news_report}\n\n"
            f"Make your trading decision now."
        )

        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": human_message},
        ]

        start = time.monotonic()
        invoke_config = {"callbacks": [self.tracker], "metadata": {"langgraph_node": "SingleAgentBaseline"}} if self.tracker else {}
        result = self.llm.invoke(messages, config=invoke_config)
        latency_s = time.monotonic() - start

        raw_confidence = extract_confidence(result.content)

        return {
            "full_response": result.content,
            "raw_confidence": raw_confidence,
            "latency_s": round(latency_s, 3),
        }
