"""
Sentiment/News Analyst for DeFi Trading Agents
Analyzes news and/or social media posts to identify current market sentiment
"""

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import time
import json

def create_sentiment_news_analyst(llm, toolkit):
    """Create a sentiment/news analyst that focuses on news and social media sentiment"""
    
    def sentiment_news_analyst_node(state):
        current_date = state["trade_date"]
        ticker = state["company_of_interest"]  # This will be the token symbol
        
        # Create tools for the analyst
        tools = [
            toolkit.get_crypto_news,  # We'll need to add this
            toolkit.get_social_media_sentiment,  # We'll need to add this
            toolkit.get_news_sentiment,  # We'll need to add this
        ]
        
        system_message = (
            """You are a sentiment/news analyst specializing in analyzing news and social media posts to identify current market sentiment. Your role is to identify market player perception on the token. Use LLM web searching capability to search relevant news and analyze the sentiment.

Key areas to analyze:

1. **News Analysis (LIMIT ONLY TO CREDIBLE NEWS SOURCES):**
   - News sites and official channels
   - RSS feeds from credible sources (e.g., https://www.dlnews.com/rss/)
   - Official announcements from project teams
   - Partnership and integration news
   - Protocol updates and upgrades
   - Regulatory news affecting the token

2. **Social Media Sentiment:**
   - Social media platforms (Twitter/X, Reddit, etc.)
   - Forums and community discussions
   - Chat groups and Telegram channels
   - Influencer opinions and analysis
   - Community sentiment trends

3. **Market Player Perception:**
   - Overall sentiment (bullish/bearish/neutral)
   - Sentiment trends over time
   - Key themes and narratives
   - FUD (Fear, Uncertainty, Doubt) detection
   - FOMO (Fear Of Missing Out) indicators
   - Market expectations and predictions

4. **Sentiment Indicators:**
   - Positive/negative sentiment ratio
   - Sentiment intensity
   - Sentiment changes and trends
   - Correlation with price movements
   - Sentiment divergences

IMPORTANT BOUNDARIES:
- LIMIT ONLY TO CREDIBLE NEWS SOURCES
- Focus on identifying market player perception on the token
- Analyze sentiment, not provide trading recommendations
- Distinguish between noise and signal
- Consider source credibility and authority

References:
- https://arxiv.org/pdf/2512.02436 (sentiment analysis research)

Output format: Text/Structured JSON format
Please provide a comprehensive sentiment analysis focusing on:
- Current market sentiment (bullish/bearish/neutral)
- Key sentiment drivers and themes
- News impact on sentiment
- Social media sentiment trends
- Market player perception summary
- Sentiment-based risk factors

Make sure to append a Markdown table at the end organizing key sentiment metrics and insights."""
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
            "sentiment_news_report": report,
        }
    
    return sentiment_news_analyst_node

