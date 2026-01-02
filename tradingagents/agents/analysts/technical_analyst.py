"""
Technical Analyst for DeFi Trading Agents
Performs technical analysis on important metrics, liquidity, trading volumes, and price movement
"""

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import time
import json
from tradingagents.dataflows.crypto_utils import CryptoDataProvider

def create_technical_analyst(llm, toolkit):
    """Create a technical analyst that focuses on technical analysis"""
    
    def technical_analyst_node(state):
        current_date = state["trade_date"]
        ticker = state["company_of_interest"]  # This will be the token symbol
        
        # Initialize crypto data provider
        crypto_provider = CryptoDataProvider()
        
        # Create tools for the analyst
        tools = [
            toolkit.get_crypto_price_data,
            toolkit.get_crypto_technical_indicators,
            toolkit.get_crypto_market_metrics,
            toolkit.get_crypto_volume_analysis,
            toolkit.get_orderbook_data,  # We'll need to add this
            toolkit.get_cvd_data,  # We'll need to add this
            toolkit.get_fear_greed_index,  # We'll need to add this
        ]
        
        system_message = (
            """You are a technical analyst specializing in cryptocurrency technical analysis. Your role is to perform technical analysis on important metrics, liquidity, trading volumes, and price movement. LLM is used to analyze the technical analysis metrics given and provide output recommendation of buy/sell and target price.

Key areas to analyze (SCOPE ON THE TECHNICAL ANALYSIS):

1. **Volume Analysis:**
   - Trading volume trends and patterns
   - Volume-price relationships
   - Volume spikes and their significance
   - Relative volume analysis

2. **Order Book Analysis:**
   - Bid/Ask spread analysis
   - Order book depth
   - Support and resistance levels from order book
   - Large order detection
   - Liquidity assessment

3. **Technical Indicators (use rule-based approach when metrics are available):**
   - RSI (Relative Strength Index) - overbought/oversold conditions
   - MACD (Moving Average Convergence Divergence) - momentum signals
   - Stochastic Oscillator - momentum indicator
   - Bollinger Bands - volatility and price bands
   - Ichimoku Cloud - support and resistance levels
   - Parabolic SAR - trend direction and reversal points
   - Additional indicators: ADX, ATR, CCI, Aroon, etc.

4. **CVD (Cumulative Volume Delta):**
   - Buy vs sell pressure
   - Volume imbalance analysis
   - Accumulation/distribution patterns

5. **Bid/Ask Spread & Depth:**
   - Current spread analysis
   - Spread trends
   - Market depth on both sides
   - Liquidity assessment

6. **Crypto Fear & Greed Index:**
   - Current market sentiment
   - Historical sentiment trends
   - Extremes (extreme fear/greed) and their significance

7. **Price Movement Analysis:**
   - Support and resistance levels
   - Trend identification
   - Pattern recognition
   - Price targets and stop-loss levels

IMPORTANT:
- Provide recommendation based on rule-based approach at given metrics
- Scope your analysis on technical analysis only
- Combine multiple indicators for confirmation
- Provide buy/sell recommendations with target price
- Include risk assessment (stop-loss levels)

References for algorithmic trading strategies:
- https://www.quantinsti.com/articles/algorithmic-trading-strategies/
- Algorithmic trading books and strategies

Output format: Text/Structured JSON format
Please provide a comprehensive technical analysis focusing on:
- Current technical position and signals
- Key support/resistance levels
- Entry/exit points with target prices
- Risk/reward assessment
- Trading recommendations (BUY/HOLD/SELL) with clear rationale

Make sure to append a Markdown table at the end organizing key technical metrics and signals."""
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
            "technical_report": report,
        }
    
    return technical_analyst_node 