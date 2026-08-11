# RSS Feed Integration for Sentiment News Analyst

## Overview

The sentiment news analyst has been enhanced to fetch and analyze articles from DL News RSS feed (https://www.dlnews.com/rss/), filter them for the asset in scope, and provide trading recommendations based on sentiment analysis.

## Implementation

### 1. RSS Feed Utilities (`tradingagents/dataflows/rss_utils.py`)

New utilities for fetching and processing RSS feeds:

- **`fetch_rss_feed()`**: Fetches and parses RSS feeds with retry logic
- **`parse_rss_entries()`**: Parses RSS entries into structured format
- **`filter_articles_by_asset()`**: Filters articles mentioning specific assets (by symbol or name)
- **`filter_articles_by_date()`**: Filters articles by date range
- **`fetch_dlnews_rss()`**: Convenience function to fetch DL News RSS feed with filtering
- **`fetch_article_content()`**: Fetches full article content from URLs

### 2. New Tools in Toolkit (`tradingagents/agents/utils/agent_utils.py`)

Three new tools for the sentiment news analyst:

#### `get_dlnews_rss_feed`
- Fetches articles from DL News RSS feed
- Filters articles for a specific token symbol/name
- Returns structured article data (title, link, summary, date, tags)

#### `analyze_article_sentiment`
- Fetches full article content from a URL
- Prepares article for sentiment analysis
- Returns structured information for LLM analysis

#### `get_crypto_news_sentiment`
- Comprehensive news sentiment analysis tool
- Fetches articles, filters for token, and provides sentiment summary
- Returns formatted analysis ready for trading recommendations

### 3. Updated Sentiment News Analyst

The sentiment news analyst (`tradingagents/agents/analysts/sentiment_news_analyst.py`) now:

1. **Fetches RSS Feed**: Uses `get_dlnews_rss_feed` to get articles from DL News filtered for the token
2. **Analyzes Articles**: Uses `get_crypto_news_sentiment` for comprehensive analysis or `analyze_article_sentiment` for individual articles
3. **Provides Recommendations**: Based on sentiment analysis, provides clear BUY/HOLD/SELL recommendations

### 4. Workflow

```
1. Agent receives token symbol (e.g., "BTC", "ETH", "UNI")
2. Agent calls get_dlnews_rss_feed(token_symbol, days_back=7)
   → Fetches RSS feed from https://www.dlnews.com/rss/
   → Filters articles mentioning the token
   → Returns filtered articles
3. Agent analyzes articles using get_crypto_news_sentiment
   → Analyzes sentiment from all articles
   → Identifies key themes and narratives
   → Assesses impact on token
4. Agent provides recommendation
   → Overall sentiment (bullish/bearish/neutral)
   → Trading recommendation: BUY/HOLD/SELL
   → Rationale based on news analysis
```

## Features

### Asset Filtering
- Filters articles by token symbol (e.g., "BTC", "ETH")
- Supports filtering by token name (e.g., "Bitcoin", "Ethereum")
- Uses word boundaries to avoid partial matches
- Case-insensitive matching

### Date Filtering
- Filters articles by date range
- Configurable lookback period (default: 7 days)
- Handles various date formats from RSS feeds

### Article Analysis
- Fetches full article content when needed
- Extracts main content from HTML
- Prepares structured data for LLM analysis
- Handles various article page structures

### Sentiment Analysis
- Analyzes overall sentiment from multiple articles
- Identifies key themes and narratives
- Detects positive and negative factors
- Assesses potential impact on token price
- Provides trading recommendations with rationale

## Usage Example

```python
from tradingagents.graph.trading_graph import TradingAgentsGraph

# Initialize the trading graph
graph = TradingAgentsGraph(
    selected_analysts=["sentiment_news"],
    config=config
)

# Run analysis for a token
final_state, signal = graph.propagate("BTC", "2025-01-15")

# The sentiment news analyst will:
# 1. Fetch articles from DL News RSS feed for BTC
# 2. Filter articles mentioning Bitcoin/BTC
# 3. Analyze sentiment from articles
# 4. Provide trading recommendation
```

## Dependencies

Added to `requirements.txt`:
- `feedparser`: For parsing RSS feeds
- `beautifulsoup4`: For parsing HTML content (already used, now explicitly listed)

## Configuration

The RSS feed integration uses default settings but can be customized:

- **RSS Feed URL**: Currently hardcoded to `https://www.dlnews.com/rss/`
- **Default Lookback**: 7 days (configurable per tool call)
- **Article Limit**: Top 10 articles for comprehensive analysis
- **Content Preview**: 3000 characters for article analysis

## Error Handling

- Retry logic for RSS feed fetching (3 attempts with exponential backoff)
- Graceful handling of missing article content
- Error messages returned as strings for LLM processing
- Continues processing even if some articles fail

## Future Enhancements

Potential improvements:
1. Support for multiple RSS feed sources
2. Caching of RSS feed data
3. More sophisticated sentiment analysis models
4. Integration with other news sources
5. Historical sentiment tracking
6. Sentiment trend analysis over time

## References

- DL News RSS Feed: https://www.dlnews.com/rss/
- DL News Terms: https://www.dlnews.com/rss/ (see Terms & Conditions section)

