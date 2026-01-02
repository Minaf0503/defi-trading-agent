# Testing Sentiment News Analyst

This directory contains tests for the sentiment news analyst functionality.

## Quick Start

Run the test script:

```bash
python tests/test_sentiment_news_analyst.py
```

## Test Structure

The test script includes four test suites:

### 1. RSS Feed Utilities Test
Tests the core RSS feed functionality:
- Fetching RSS feeds from DL News
- Parsing RSS entries
- Filtering articles by asset
- Date filtering

**What it tests:**
- `fetch_rss_feed()` - RSS feed fetching
- `parse_rss_entries()` - Entry parsing
- `filter_articles_by_asset()` - Asset filtering
- `fetch_dlnews_rss()` - Convenience function

### 2. RSS Feed Tools Test
Tests the LangChain tools:
- `get_dlnews_rss_feed` tool
- `get_crypto_news_sentiment` tool

**What it tests:**
- Tool invocation
- Tool output format
- Error handling

### 3. Sentiment News Analyst (Isolated) Test
Tests the analyst node in isolation:
- Analyst initialization
- State processing
- Tool calling
- Report generation

**What it tests:**
- `create_sentiment_news_analyst()` function
- Analyst node execution
- Message handling
- Tool integration

### 4. Sentiment News Analyst (In Trading Graph) Test
Tests the analyst as part of the full trading graph:
- Graph initialization
- Full workflow execution
- State propagation
- Final report generation

**What it tests:**
- Integration with TradingAgentsGraph
- End-to-end workflow
- Report generation
- Signal processing

## Running Individual Tests

You can modify the test script to run only specific tests:

```python
# Run only RSS utilities test
test_rss_feed_utilities()

# Run only tools test
test_rss_feed_tools()

# Run only isolated analyst test
test_sentiment_news_analyst_isolated()

# Run only graph integration test
test_sentiment_news_analyst_in_graph()
```

## Expected Output

### Successful Test Output:
```
================================================================================
SENTIMENT NEWS ANALYST TEST SUITE
================================================================================
Test started at: 2025-01-15 10:30:00

================================================================================
Test 1: RSS Feed Utilities
================================================================================

1.1 Testing RSS feed fetch...
   ✓ Successfully fetched RSS feed
   - Feed title: DL News
   - Number of entries: 20

1.2 Testing RSS entry parsing...
   ✓ Successfully parsed 20 articles
   - First article title: Article Title...

[... more test output ...]

================================================================================
TEST SUMMARY
================================================================================
RSS Feed Utilities                              PASSED ✓
RSS Feed Tools                                  PASSED ✓
Sentiment News Analyst (Isolated)               PASSED ✓
Sentiment News Analyst (In Graph)               PASSED ✓

Test completed at: 2025-01-15 10:35:00
================================================================================
```

## Configuration

Make sure your `DEFAULT_CONFIG` is set up correctly:

```python
DEFAULT_CONFIG = {
    "llm_provider": "openai",  # or "anthropic", "google"
    "quick_think_llm": "gpt-4o-mini",
    "backend_url": "https://api.openai.com/v1",
    # ... other config
}
```

## Troubleshooting

### RSS Feed Fetching Fails
- Check internet connection
- Verify DL News RSS feed is accessible: https://www.dlnews.com/rss/
- Check if feedparser is installed: `pip install feedparser`

### Tool Execution Fails
- Verify toolkit initialization
- Check if all dependencies are installed
- Review error messages for specific issues

### Analyst Test Fails
- Check LLM configuration (API keys, model names)
- Verify backend URL is correct
- Check if rate limits are being hit

### Graph Test Fails
- Ensure all required analysts are available
- Check graph setup and dependencies
- Review state propagation logic

## Dependencies

Required packages (should be in requirements.txt):
- `feedparser` - RSS feed parsing
- `beautifulsoup4` - HTML parsing
- `requests` - HTTP requests
- `langchain-openai` - LangChain OpenAI integration
- `langgraph` - Graph execution

Install dependencies:
```bash
pip install -r requirements.txt
```

## Notes

- The full graph test uses API calls and may incur costs
- Tests may take several minutes to complete
- Some tests require internet connection
- RSS feed content may vary, so article counts may differ

