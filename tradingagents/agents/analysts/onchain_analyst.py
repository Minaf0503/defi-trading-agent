"""
Onchain Analyst for DeFi Trading Agents
Focuses on analyzing onchain data to discover potential sudden/trend shifts on the underlying token blockchain
"""

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import time
import json
from tradingagents.dataflows.crypto_utils import OnchainAnalytics

def create_onchain_analyst(llm, toolkit):
    """Create an onchain analyst that focuses on blockchain data"""
    
    def onchain_analyst_node(state):
        current_date = state["trade_date"]
        ticker = state["company_of_interest"]  # This will be the token symbol
        token_address = state.get("token_address", None)  # Token contract address
        
        # Initialize onchain analytics
        onchain_analytics = OnchainAnalytics()
        
        # Get onchain data if address is available
        onchain_data = {}
        if token_address:
            onchain_data = onchain_analytics.get_token_onchain_data(token_address)
            liquidity_metrics = onchain_analytics.analyze_liquidity_metrics(token_address)
            holder_metrics = onchain_analytics.analyze_holder_metrics(token_address)
            transaction_metrics = onchain_analytics.analyze_transaction_metrics(token_address)
        else:
            # Fallback to basic analysis without onchain data
            onchain_data = {"error": "No token address provided"}
            liquidity_metrics = {"error": "No token address provided"}
            holder_metrics = {"error": "No token address provided"}
            transaction_metrics = {"error": "No token address provided"}
        
        # Create tools for the analyst
        tools = [
            toolkit.get_onchain_liquidity_data,
            toolkit.get_onchain_holder_data,
            toolkit.get_onchain_transaction_data,
            toolkit.get_onchain_supply_data,
            toolkit.get_mempool_data,  # We'll need to add this
        ]
        
        system_message = (
            """You are an **Onchain Analyst** specializing in blockchain data analysis for cryptocurrency trading. Your role is to analyze onchain data to discover potential sudden/trend shifts on the underlying token blockchain. **LIMIT YOUR DATA ANALYSIS TO ONCHAIN DATA AND DEX ONLY.**

WORKFLOW:
1. **Gather Onchain Data**: Use available tools to collect liquidity, holder, transaction, and supply data
2. **Analyze Key Metrics**: Examine network activity, holder behavior, liquidity dynamics, and mempool activity
3. **Identify Signals**: Detect accumulation/distribution patterns, whale movements, liquidity shifts, and anomalies
4. **Provide Recommendation**: Based on onchain analysis, provide clear trading recommendation with rationale

Key areas to analyze (LIMIT DATA TO ONCHAIN DATA AND DEX ONLY):

1. **Network Activity:**
   - Blockchain node activity and health
   - Transaction throughput and patterns
   - Smart contract events and interactions
   - State changes on the blockchain
   - Network congestion indicators
   - Transaction volume trends
   - Active address counts

2. **Token Holder Behavior:**
   - Wallet holder distribution and changes
   - Holder activity patterns
   - Large holder (whale) movements
   - New vs existing holder trends
   - Holder accumulation/distribution patterns
   - Top holder concentration analysis
   - Holder growth trends

3. **Liquidity Pool Analysis:**
   - Liquidity pool lock events
   - Liquidity pool burn events
   - Liquidity changes over time
   - DEX liquidity depth analysis
   - Liquidity concentration and risks
   - Pool composition changes
   - Slippage analysis

4. **Wallet Holders Analysis:**
   - Number of unique wallet holders
   - Top holder concentrations
   - Wallet behavior patterns
   - Holder growth trends
   - Wallet transaction patterns
   - Address activity levels
   - Active vs dormant wallets

5. **Mempool Analysis:**
   - Pending transactions in mempool
   - Transaction fee trends
   - Large pending transactions
   - Mempool congestion indicators
   - Potential market-moving transactions
   - Fee spike detection

6. **Blockchain State Changes:**
   - Smart contract state changes
   - Contract call patterns
   - Event emission patterns
   - State transition analysis
   - Token transfer patterns

IMPORTANT INSTRUCTIONS:
- ALWAYS gather onchain data from all available sources (liquidity, holders, transactions, supply)
- LIMIT analysis to onchain data and DEX only - do not use price charts or technical indicators
- Analyze multiple onchain metrics to identify patterns and anomalies
- Focus on detecting accumulation/distribution signals
- Identify whale movements and large transactions
- Monitor liquidity pool changes and concentration risks
- Detect network activity anomalies
- Provide clear, actionable trading recommendation based on onchain signals
- Include confidence level and detailed rationale
- Explain how onchain data supports the recommendation

OUTPUT FORMAT:
Provide a comprehensive onchain analysis including:

1. **Onchain Data Summary:**
   - Liquidity metrics analyzed
   - Holder data examined
   - Transaction patterns reviewed
   - Supply metrics assessed

2. **Key Onchain Signals:**
   - Accumulation/distribution patterns detected
   - Whale movements identified
   - Liquidity shifts observed
   - Network activity anomalies
   - Mempool signals

3. **Holder Behavior Analysis:**
   - Holder distribution changes
   - Top holder activity
   - New holder trends
   - Accumulation patterns

4. **Liquidity Analysis:**
   - Pool depth and concentration
   - Liquidity changes
   - DEX liquidity metrics
   - Liquidity risks

5. **Trading Recommendation:**
   - **BUY/HOLD/SELL** with clear rationale
   - Confidence level (high/medium/low)
   - Key onchain factors driving the recommendation
   - Risk factors based on onchain data

6. **Summary Table:**
   - Key onchain metrics
   - Signals detected
   - Trading recommendation summary

Make sure to append a Markdown table at the end organizing key onchain metrics and insights."""
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
            "onchain_report": report,
        }
    
    return onchain_analyst_node 