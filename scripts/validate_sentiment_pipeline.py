#!/usr/bin/env python
"""
Phase 3 validation: confirm the rebuilt sentiment/news pipeline's real data
sources actually work, after finding (2026-06-21) that half the old tools
silently returned fake/empty data (and that the other half's primary source,
DL News, had separately shut down in May 2026). Tests, for a sample token:
  1. Crypto news RSS feeds -- Cointelegraph, Decrypt, The Block (new, replaces dead DL News)
  2. Crypto Fear & Greed Index -- alternative.me, free, no key (replaces LunarCrush,
     which turned out to require a paid plan for API access despite a free web tier)
  3. Reddit search via PRAW (new, replaces the dead static-dataset stub; likely
     unconfigured since Reddit replaced instant self-serve app creation with an
     approval process in 2026)

Each source reports its own pass/fail rather than the whole script crashing
on a missing/unapproved credential, since REDDIT_* is independent of
COINGECKO_API_KEY / ONCHAIN_RPC_URL.

Usage:
    python scripts/validate_sentiment_pipeline.py --token ETH
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--token", default="ETH")
    return parser.parse_args()


def main():
    args = parse_args()
    token = args.token.upper()

    from experiments.config import EXPERIMENT_TOKENS

    token_info = EXPERIMENT_TOKENS.get(token)
    token_name = token_info["name"] if token_info else None

    print(f"-- 1. Crypto news RSS feeds (Cointelegraph, Decrypt, The Block) for {token} --")
    try:
        from tradingagents.dataflows.rss_utils import fetch_crypto_news_rss

        articles = fetch_crypto_news_rss(asset_symbol=token, asset_name=token_name, days_back=14)
        print(f"OK: {len(articles)} articles found")
        for a in articles[:3]:
            print(f"  - {a.get('title')}")
    except Exception as e:
        print(f"FAIL: {e}")

    print(f"\n-- 2. Crypto Fear & Greed Index (market-wide, not {token}-specific) --")
    try:
        from tradingagents.dataflows.fear_greed_api import get_fear_greed_index

        readings = get_fear_greed_index(limit=3)
        print("OK:")
        print(json.dumps(readings, indent=2))
    except Exception as e:
        print(f"FAIL: {e}")

    print(f"\n-- 3. Reddit search for {token} (via PRAW) --")
    try:
        from tradingagents.dataflows.reddit_api import search_reddit_posts

        posts = search_reddit_posts(token, token_name, days_back=30, max_posts=5)
        print(f"OK: {len(posts)} posts found")
        for p in posts[:3]:
            print(f"  - [{p['subreddit']}] {p['title']} (score={p['score']})")
    except Exception as e:
        print(f"FAIL (expected if REDDIT_CLIENT_ID/SECRET/USER_AGENT are not set yet): {e}")


if __name__ == "__main__":
    main()
