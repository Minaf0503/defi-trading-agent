# How to Test Sentiment News Analyst

## Quick Test (Recommended for First Run)

Run the quick test to verify basic functionality:

```bash
python tests/quick_test_sentiment.py
```

This will:
- Fetch RSS feed from DL News for BTC
- Test the toolkit RSS feed tool for ETH
- Verify basic functionality works

**Expected time:** ~10-30 seconds

## Full Test Suite

Run the comprehensive test suite:

```bash
python tests/test_sentiment_news_analyst.py
```

This will run:
1. RSS Feed Utilities Test
2. RSS Feed Tools Test
3. Sentiment News Analyst (Isolated) Test
4. Sentiment News Analyst (In Trading Graph) Test - *optional, uses API calls*

**Expected time:** 2-5 minutes (longer if running full graph test)

## Testing Individual Components

### Test RSS Feed Utilities Only

```python
from tradingagents.dataflows.rss_utils import fetch_dlnews_rss

# Fetch articles for BTC
articles = fetch_dlnews_rss(asset_symbol="BTC", days_back=7)
print(f"Found {len(articles)} articles")
```

### Test RSS Feed Tools Only

```python
from tradingagents.agents.utils.agent_utils import Toolkit
from tradingagents.default_config import DEFAULT_CONFIG

toolkit = Toolkit(config=DEFAULT_CONFIG)

# Test RSS feed tool
result = toolkit.get_dlnews_rss_feed.invoke({
    "token_symbol": "ETH",
    "days_back": 7
})
print(result)
```

### Test Sentiment News Analyst Only

```python
from tradingagents.agents.analysts.sentiment_news_analyst import create_sentiment_news_analyst
from tradingagents.agents.utils.agent_utils import Toolkit
from tradingagents.default_config import DEFAULT_CONFIG
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from datetime import datetime

# Initialize
config = DEFAULT_CONFIG.copy()
llm = ChatOpenAI(model=config["quick_think_llm"], base_url=config["backend_url"])
toolkit = Toolkit(config=config)

# Create analyst
analyst = create_sentiment_news_analyst(llm, toolkit)

# Test state
state = {
    "trade_date": datetime.now().strftime("%Y-%m-%d"),
    "company_of_interest": "BTC",
    "messages": [HumanMessage(content="Analyze sentiment for BTC")],
    "sentiment_news_report": ""
}

# Run
result = analyst(state)
print(result)
```

## Testing with Trading Graph

```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG
from datetime import datetime

# Initialize graph with only sentiment_news analyst
config = DEFAULT_CONFIG.copy()
graph = TradingAgentsGraph(
    selected_analysts=["sentiment_news"],
    debug=True,  # See detailed output
    config=config
)

# Run analysis
token = "ETH"
date = datetime.now().strftime("%Y-%m-%d")
final_state, signal = graph.propagate(token, date)

# Check results
print(f"Signal: {signal}")
print(f"Report: {final_state.get('sentiment_news_report', '')[:500]}")
```

## Common Issues

### "Module not found" errors
```bash
# Make sure you're in the project root directory
cd /path/to/defi-trading-agent

# Install dependencies
pip install -r requirements.txt
```

### RSS feed fetch fails
- Check internet connection
- Verify DL News is accessible: https://www.dlnews.com/rss/
- Check if feedparser is installed: `pip install feedparser`

### LLM API errors
- Verify API keys are set correctly
- Check backend_url in config
- Ensure you have API credits/quota

### No articles found
- This is normal if there are no recent articles about the token
- Try a different token (BTC, ETH usually have more coverage)
- Increase `days_back` parameter

## Expected Output

### Successful Quick Test:
```
============================================================
Quick Test: Sentiment News Analyst RSS Feed
============================================================

1. Testing RSS feed fetch for BTC...
   ✓ Success! Found 5 articles mentioning BTC
   - Latest article: Bitcoin price surges as institutional...
   - Published: 2025-01-15T10:30:00

2. Testing toolkit RSS feed tool...
   ✓ Success! Tool executed
   - Result preview: Found 3 articles for ETH from DL News:...

============================================================
Quick test completed successfully! ✓
============================================================
```

## Next Steps

After running tests successfully:
1. Review the test output to understand what's being tested
2. Check the generated reports for quality
3. Try different tokens (BTC, ETH, UNI, etc.)
4. Adjust `days_back` parameter to get more/fewer articles
5. Integrate into your trading workflow

## Additional Resources

- See `tests/README.md` for detailed test documentation
- See `RSS_FEED_INTEGRATION.md` for implementation details
- See `agent-context/README.md` for context management features

