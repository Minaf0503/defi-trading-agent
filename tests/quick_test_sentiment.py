"""
Quick test for Sentiment News Analyst

A simplified test script for quick verification of RSS feed functionality.
"""

import sys
import os
from datetime import datetime

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tradingagents.dataflows.rss_utils import fetch_dlnews_rss
from tradingagents.agents.utils.agent_utils import Toolkit
from tradingagents.default_config import DEFAULT_CONFIG


def quick_test():
    """Quick test of RSS feed functionality."""
    print("=" * 60)
    print("Quick Test: Sentiment News Analyst RSS Feed")
    print("=" * 60)
    
    # Test 1: Fetch RSS feed
    print("\n1. Testing RSS feed fetch for BTC...")
    try:
        articles = fetch_dlnews_rss(asset_symbol="BTC", days_back=7)
        print(f"   ✓ Success! Found {len(articles)} articles mentioning BTC")
        if articles:
            print(f"   - Latest article: {articles[0].get('title', 'N/A')[:60]}...")
            print(f"   - Published: {articles[0].get('published', 'N/A')}")
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False
    
    # Test 2: Test toolkit tool
    print("\n2. Testing toolkit RSS feed tool...")
    try:
        toolkit = Toolkit(config=DEFAULT_CONFIG)
        result = toolkit.get_dlnews_rss_feed.invoke({
            "token_symbol": "ETH",
            "days_back": 7
        })
        print(f"   ✓ Success! Tool executed")
        print(f"   - Result preview: {result[:150]}...")
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False
    
    print("\n" + "=" * 60)
    print("Quick test completed successfully! ✓")
    print("=" * 60)
    return True


if __name__ == "__main__":
    quick_test()

