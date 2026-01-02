"""
Test script for Sentiment News Analyst

This script tests:
1. RSS feed utilities
2. RSS feed tools
3. Sentiment news analyst in isolation
4. Sentiment news analyst as part of the trading graph
"""

import sys
import os
from datetime import datetime
from pathlib import Path

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tradingagents.dataflows.rss_utils import (
    fetch_rss_feed,
    parse_rss_entries,
    filter_articles_by_asset,
    fetch_dlnews_rss,
    fetch_article_content
)
from tradingagents.agents.utils.agent_utils import Toolkit
from tradingagents.agents.analysts.sentiment_news_analyst import create_sentiment_news_analyst
from tradingagents.default_config import DEFAULT_CONFIG
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage


def test_rss_feed_utilities():
    """Test RSS feed utility functions."""
    print("=" * 80)
    print("Test 1: RSS Feed Utilities")
    print("=" * 80)
    
    try:
        # Test fetching RSS feed
        print("\n1.1 Testing RSS feed fetch...")
        feed = fetch_rss_feed("https://www.dlnews.com/rss/")
        print(f"   ✓ Successfully fetched RSS feed")
        print(f"   - Feed title: {feed.feed.get('title', 'N/A')}")
        print(f"   - Number of entries: {len(feed.entries)}")
        
        # Test parsing entries
        print("\n1.2 Testing RSS entry parsing...")
        articles = parse_rss_entries(feed)
        print(f"   ✓ Successfully parsed {len(articles)} articles")
        if articles:
            print(f"   - First article title: {articles[0].get('title', 'N/A')[:80]}...")
            print(f"   - First article link: {articles[0].get('link', 'N/A')}")
        
        # Test filtering by asset
        print("\n1.3 Testing article filtering by asset...")
        btc_articles = filter_articles_by_asset(articles, "BTC", "Bitcoin")
        eth_articles = filter_articles_by_asset(articles, "ETH", "Ethereum")
        print(f"   ✓ Filtered articles:")
        print(f"   - BTC articles: {len(btc_articles)}")
        print(f"   - ETH articles: {len(eth_articles)}")
        
        # Test fetch_dlnews_rss convenience function
        print("\n1.4 Testing fetch_dlnews_rss convenience function...")
        btc_news = fetch_dlnews_rss(asset_symbol="BTC", days_back=7)
        print(f"   ✓ Fetched {len(btc_news)} BTC articles from last 7 days")
        
        return True
        
    except Exception as e:
        print(f"   ✗ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def test_rss_feed_tools():
    """Test RSS feed tools from Toolkit."""
    print("\n" + "=" * 80)
    print("Test 2: RSS Feed Tools")
    print("=" * 80)
    
    try:
        toolkit = Toolkit(config=DEFAULT_CONFIG)
        
        # Test get_dlnews_rss_feed tool
        print("\n2.1 Testing get_dlnews_rss_feed tool...")
        result = toolkit.get_dlnews_rss_feed.invoke({
            "token_symbol": "BTC",
            "token_name": "Bitcoin",
            "days_back": 7
        })
        print(f"   ✓ Tool executed successfully")
        print(f"   - Result length: {len(result)} characters")
        print(f"   - Result preview: {result[:200]}...")
        
        # Test get_crypto_news_sentiment tool
        print("\n2.2 Testing get_crypto_news_sentiment tool...")
        result = toolkit.get_crypto_news_sentiment.invoke({
            "token_symbol": "ETH",
            "days_back": 7
        })
        print(f"   ✓ Tool executed successfully")
        print(f"   - Result length: {len(result)} characters")
        print(f"   - Result preview: {result[:200]}...")
        
        return True
        
    except Exception as e:
        print(f"   ✗ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def test_sentiment_news_analyst_isolated():
    """Test sentiment news analyst in isolation."""
    print("\n" + "=" * 80)
    print("Test 3: Sentiment News Analyst (Isolated)")
    print("=" * 80)
    
    try:
        # Initialize LLM
        config = DEFAULT_CONFIG.copy()
        llm = ChatOpenAI(
            model=config["quick_think_llm"],
            base_url=config["backend_url"]
        )
        
        # Initialize toolkit
        toolkit = Toolkit(config=config)
        
        # Create sentiment news analyst
        analyst_node = create_sentiment_news_analyst(llm, toolkit)
        
        # Create test state
        test_state = {
            "trade_date": datetime.now().strftime("%Y-%m-%d"),
            "company_of_interest": "BTC",  # Bitcoin
            "messages": [
                HumanMessage(content=f"Analyze sentiment for BTC from DL News RSS feed and provide a trading recommendation.")
            ],
            "sentiment_news_report": ""
        }
        
        print("\n3.1 Running sentiment news analyst...")
        print(f"   - Token: {test_state['company_of_interest']}")
        print(f"   - Date: {test_state['trade_date']}")
        print("   - This may take a while as it fetches RSS feed and analyzes articles...")
        
        # Run analyst
        result = analyst_node(test_state)
        
        print(f"   ✓ Analyst executed successfully")
        print(f"   - Messages in result: {len(result.get('messages', []))}")
        
        # Check for tool calls
        if result.get('messages'):
            last_message = result['messages'][-1]
            if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
                print(f"   - Tool calls made: {len(last_message.tool_calls)}")
                for tool_call in last_message.tool_calls:
                    print(f"     * {tool_call.get('name', 'unknown')}")
        
        # Check report
        report = result.get('sentiment_news_report', '')
        if report:
            print(f"   - Report generated: {len(report)} characters")
            print(f"   - Report preview: {report[:300]}...")
        else:
            print("   - Note: Report will be generated after tool calls complete")
        
        return True
        
    except Exception as e:
        print(f"   ✗ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def test_sentiment_news_analyst_in_graph():
    """Test sentiment news analyst as part of the trading graph."""
    print("\n" + "=" * 80)
    print("Test 4: Sentiment News Analyst (In Trading Graph)")
    print("=" * 80)
    
    try:
        from tradingagents.graph.trading_graph import TradingAgentsGraph
        
        # Create config
        config = DEFAULT_CONFIG.copy()
        
        print("\n4.1 Initializing trading graph with sentiment_news analyst only...")
        graph = TradingAgentsGraph(
            selected_analysts=["sentiment_news"],
            debug=True,  # Enable debug to see output
            config=config
        )
        print("   ✓ Trading graph initialized")
        
        # Test with a token
        token = "ETH"  # Ethereum
        trade_date = datetime.now().strftime("%Y-%m-%d")
        
        print(f"\n4.2 Running analysis for {token} on {trade_date}...")
        print("   - This will fetch RSS feed, analyze articles, and provide recommendation")
        print("   - This may take several minutes...")
        
        final_state, signal = graph.propagate(token, trade_date)
        
        print(f"\n   ✓ Analysis completed")
        print(f"   - Final signal: {signal}")
        
        # Check sentiment report
        sentiment_report = final_state.get("sentiment_news_report", "")
        if sentiment_report:
            print(f"   - Sentiment report length: {len(sentiment_report)} characters")
            print(f"   - Report preview:\n{sentiment_report[:500]}...")
        
        return True
        
    except Exception as e:
        print(f"   ✗ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def run_all_tests():
    """Run all tests."""
    print("\n" + "=" * 80)
    print("SENTIMENT NEWS ANALYST TEST SUITE")
    print("=" * 80)
    print(f"Test started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    results = []
    
    # Run tests
    results.append(("RSS Feed Utilities", test_rss_feed_utilities()))
    results.append(("RSS Feed Tools", test_rss_feed_tools()))
    results.append(("Sentiment News Analyst (Isolated)", test_sentiment_news_analyst_isolated()))
    
    # Ask before running full graph test (it's slower and uses API calls)
    print("\n" + "=" * 80)
    response = input("Run full trading graph test? (This will use API calls and may take several minutes) [y/N]: ")
    if response.lower() == 'y':
        results.append(("Sentiment News Analyst (In Graph)", test_sentiment_news_analyst_in_graph()))
    else:
        print("Skipping full graph test.")
        results.append(("Sentiment News Analyst (In Graph)", None))
    
    # Print summary
    print("\n" + "=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)
    for test_name, result in results:
        if result is None:
            status = "SKIPPED"
        elif result:
            status = "PASSED ✓"
        else:
            status = "FAILED ✗"
        print(f"{test_name:50} {status}")
    
    print(f"\nTest completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)


if __name__ == "__main__":
    # Create tests directory if it doesn't exist
    os.makedirs("tests", exist_ok=True)
    
    # Run tests
    run_all_tests()

