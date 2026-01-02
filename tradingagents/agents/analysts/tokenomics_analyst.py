"""
Tokenomics Analyst for DeFi Trading Agents
Analyzes tokenomics aspects: token supply, inflation/deflation, distribution, utility and demand
"""

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import time
import json
from tradingagents.dataflows.crypto_utils import CryptoDataProvider, OnchainAnalytics

def create_tokenomics_analyst(llm, toolkit):
    """Create a tokenomics analyst that focuses on tokenomics analysis"""
    
    def tokenomics_analyst_node(state):
        current_date = state["trade_date"]
        ticker = state["company_of_interest"]  # This will be the token symbol
        token_address = state.get("token_address", None)  # Token contract address
        
        # Initialize data providers
        crypto_provider = CryptoDataProvider()
        onchain_analytics = OnchainAnalytics() if token_address else None
        
        # Create tools for the analyst
        tools = [
            toolkit.get_onchain_supply_data,
            toolkit.get_onchain_holder_data,
            toolkit.get_crypto_market_metrics,
            toolkit.get_tokenomics_data,  # We'll need to add this tool
        ]
        
        system_message = (
            """You are a tokenomics analyst specializing in cryptocurrency tokenomics analysis. Your role is to analyze tokenomics aspects and provide insights for token evaluation.

Key areas to analyze (LIMIT YOUR ANALYSIS TO THESE TOKENOMICS ASPECTS ONLY):

1. **Token Supply Analysis:**
   - Current circulating supply vs total supply
   - Maximum supply (if applicable)
   - Supply growth/decline trends
   - Supply distribution across different categories
   - Historical supply changes

2. **Token Mint/Burn Cycle:**
   - Minting mechanisms and schedules
   - Burning mechanisms and schedules
   - Net supply changes over time
   - Inflation/deflation rates and trends
   - Future supply projections based on mechanisms

3. **Wallet Distribution:**
   - Total number of holders
   - Distribution concentration (top 10, top 100, top 1000 holders)
   - Gini coefficient or similar distribution metrics
   - Holder growth/decline trends
   - Average holding size
   - Whale concentration risks

4. **Token Utility and Demand Analysis:**
   - Primary use cases of the token
   - Token utility within protocols/platforms
   - Staking/rewards mechanisms
   - Governance participation requirements
   - Demand drivers and catalysts
   - Historical demand patterns
   - When demand for token is unclear, assume the demand is Moving average of last 30 days token circulation

5. **Tokenomics Index:**
   - Overall tokenomics health score
   - Supply dynamics score
   - Distribution fairness score
   - Utility and demand strength
   - Long-term sustainability assessment

6. **News Article Analysis (ONLY for token demand and utility):**
   - Collect and analyze ONLY news articles relevant to token demand and utility
   - Focus on announcements affecting token utility
   - Changes in tokenomics mechanisms
   - Protocol upgrades affecting token use
   - DO NOT analyze general price movements or market sentiment

IMPORTANT BOUNDARIES:
- Limit your analysis ONLY to tokenomics aspects
- When analyzing news, collect and analyze ONLY specific news articles relevant to token demand and utility
- Do not provide technical analysis, price predictions, or trading recommendations
- Focus on the fundamental tokenomics structure and mechanisms

Please provide a comprehensive tokenomics analysis focusing on:
- Token supply dynamics and sustainability
- Inflation/deflation prospects
- Distribution fairness and concentration risks
- Token utility strength and demand drivers
- Overall tokenomics health and risks
- Long-term tokenomics viability

Output format: Text/Structured JSON format
Make sure to append a Markdown table at the end organizing key tokenomics metrics and insights."""
        )
        
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a helpful AI assistant, collaborating with other assistants."
                    " Use the provided tools to progress towards answering the question."
                    " If you are unable to fully answer, that's OK; another assistant with different tools"
                    " will help where you left off. Execute what you can to make progress."
                    " If you or any other assistant has the FINAL TRANSACTION PROPOSAL: **BUY/HOLD/SELL** or deliverable,"
                    " prefix your response with FINAL TRANSACTION PROPOSAL: **BUY/HOLD/SELL** so the team knows to stop."
                    " You have access to the following tools: {tool_names}.\n{system_message}"
                    "For your reference, the current date is {current_date}. The crypto token we want to analyze is {ticker}",
                ),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )
        
        prompt = prompt.partial(system_message=system_message)
        prompt = prompt.partial(tool_names=", ".join([tool.name for tool in tools]))
        prompt = prompt.partial(current_date=current_date)
        prompt = prompt.partial(ticker=ticker)
        
        chain = prompt | llm.bind_tools(tools)
        
        result = chain.invoke(state["messages"])
        
        report = ""
        
        if len(result.tool_calls) == 0:
            report = result.content
        
        return {
            "messages": [result],
            "tokenomics_report": report,
        }
    
    return tokenomics_analyst_node

