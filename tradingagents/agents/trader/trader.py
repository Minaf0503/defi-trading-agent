import functools
import time
import json

from tradingagents.agents.utils.parsing import extract_confidence


def create_trader(llm, memory):
    def trader_node(state, name):
        company_name = state["company_of_interest"]
        investment_plan = state["investment_plan"]
        technical_report = state["technical_report"]
        onchain_report = state["onchain_report"]
        tokenomics_report = state["tokenomics_report"]
        sentiment_news_report = state["sentiment_news_report"]

        curr_situation = f"{technical_report}\n\n{onchain_report}\n\n{tokenomics_report}\n\n{sentiment_news_report}"
        past_memories = memory.get_memories(curr_situation, n_matches=2)

        past_memory_str = ""
        if past_memories:
            for i, rec in enumerate(past_memories, 1):
                past_memory_str += rec["recommendation"] + "\n\n"
        else:
            past_memory_str = "No past memories found."

        context = {
            "role": "user",
            "content": f"Based on a comprehensive analysis by a team of analysts, here is an investment plan tailored for {company_name}. This plan incorporates insights from current technical market trends, macroeconomic indicators, and social media sentiment. Use this plan as a foundation for evaluating your next trading decision.\n\nProposed Investment Plan: {investment_plan}\n\nLeverage these insights to make an informed and strategic decision.",
        }

        messages = [
            {
                "role": "system",
                "content": f"""You are a trading agent analyzing market data to make investment decisions. Based on your analysis, provide a specific recommendation to buy, sell, or hold. End with a firm decision and always conclude your response with 'FINAL TRANSACTION PROPOSAL: **BUY/HOLD/SELL** (Confidence: NN%)' -- the confidence is YOUR OWN self-assessed probability (0-100) that this decision will be profitable, not a measure of how strongly you phrased the recommendation. Be honest about uncertainty; a well-calibrated 55% means you genuinely think it's close to a coin flip, not a hedge to avoid commitment. This number feeds a downstream statistical calibration step, so it needs to be your real estimate, not decoration. Do not forget to utilize lessons from past decisions to learn from your mistakes. Here is some reflections from similar situatiosn you traded in and the lessons learned: {past_memory_str}""",
            },
            context,
        ]

        result = llm.invoke(messages)
        raw_confidence = extract_confidence(result.content)

        return {
            "messages": [result],
            "trader_investment_plan": result.content,
            "raw_confidence": raw_confidence,
            "sender": name,
        }

    return functools.partial(trader_node, name="Trader")
