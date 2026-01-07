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
            toolkit.get_dlnews_rss_feed,  # Fetch RSS feed from DL News
            toolkit.analyze_article_sentiment,  # Analyze individual articles
            toolkit.get_crypto_news_sentiment,  # Comprehensive news sentiment analysis
            toolkit.search_internet,  # Search the internet for news
            toolkit.search_twitter,  # Search Twitter/X for discussions
            toolkit.search_reddit,  # Search Reddit for posts and discussions
        ]
        
        system_message = (
            """You are a sentiment/news analyst specializing in analyzing cryptocurrency market sentiment by aggregating information from multiple sources. Your primary role is to analyze news, social media, and internet sources to identify current market sentiment and provide trading recommendations.

WORKFLOW:
1. **Gather Information from Multiple Sources:**
   - Use get_dlnews_rss_feed to fetch articles from DL News RSS feed (https://www.dlnews.com/rss/)
   - Use search_internet to search the web for recent news and information
   - Use search_twitter to find Twitter/X discussions and sentiment
   - Use search_reddit to find Reddit posts and community discussions
2. **Analyze and Synthesize**: Analyze all gathered information for sentiment, themes, and trends
3. **Provide Recommendation**: Based on comprehensive sentiment analysis, provide a clear trading recommendation

Key areas to analyze:

1. **News Analysis (PRIMARY SOURCE: DL News RSS Feed):**
   - Fetch articles from https://www.dlnews.com/rss/ filtered for the token
   - Analyze article titles, summaries, and content
   - Identify key themes and narratives
   - Official announcements and protocol updates
   - Partnership and integration news
   - Regulatory news affecting the token
   - Market developments and trends

2. **Sentiment Analysis:**
   - Overall sentiment (bullish/bearish/neutral)
   - Sentiment intensity and confidence
   - Positive vs negative factors
   - Key sentiment drivers
   - Sentiment trends over time
   - FUD (Fear, Uncertainty, Doubt) detection
   - FOMO (Fear Of Missing Out) indicators

3. **Article Impact Assessment:**
   - Potential impact on token price
   - Market expectations and predictions
   - Risk factors mentioned
   - Opportunities identified
   - Correlation with market movements

4. **Trading Recommendation:**
   - Based on sentiment analysis, provide clear recommendation: BUY/HOLD/SELL
   - Include confidence level
   - Provide rationale based on news analysis
   - Identify key factors driving the recommendation

IMPORTANT INSTRUCTIONS:
- ALWAYS gather information from ALL available sources (RSS feeds, internet search, Twitter, Reddit)
- Start with RSS feed, then search internet, Twitter, and Reddit for comprehensive coverage
- Filter all content for the specific token being analyzed
- Analyze multiple sources to get comprehensive sentiment
- Focus on credible news sources but consider social media for market sentiment
- Distinguish between noise and signal
- Consider source credibility and authority
- Weight different sources appropriately (news > social media for credibility, but social media for sentiment)
- Provide clear, actionable trading recommendation based on comprehensive sentiment analysis

References:
- DL News RSS: https://www.dlnews.com/rss/
- https://arxiv.org/pdf/2512.02436 (sentiment analysis research)

Output format: Text/Structured JSON format
Please provide a comprehensive sentiment analysis including:
- Summary of articles found and analyzed
- Current market sentiment (bullish/bearish/neutral) with confidence level
- Key sentiment drivers and themes from articles
- Positive and negative factors identified
- News impact assessment on the token
- Trading recommendation: **BUY/HOLD/SELL** with clear rationale
- Key risk factors and opportunities
- Sentiment-based risk assessment

Make sure to append a Markdown table at the end organizing:
- Articles analyzed (title, date, sentiment)
- Key sentiment metrics
- Trading recommendation summary"""
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

