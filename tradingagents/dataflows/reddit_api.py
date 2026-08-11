"""
Real Reddit search via PRAW (the official Reddit API).

Replaces the old search_reddit tool, which silently called
get_reddit_company_news/get_reddit_global_news -- functions that read from a
static local reddit_data/ directory that does not exist anywhere in this
repo, and always returned an empty string (see PROGRESS_LOG.md 2026-06-21).
`praw` was already a listed dependency but had never actually been imported
anywhere in the codebase until now.

Requires a free Reddit "script" app (https://www.reddit.com/prefs/apps) ->
REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT in .env.
"""

import os
from datetime import datetime, timedelta, timezone
from typing import Dict, List, Optional

import praw
from dotenv import load_dotenv

load_dotenv()

DEFAULT_SUBREDDITS = ["CryptoCurrency", "defi"]

TOKEN_SUBREDDITS = {
    "BTC": ["Bitcoin"],
    "ETH": ["ethereum", "ethtrader"],
    "SOL": ["solana"],
    "UNI": ["UniSwap"],
    "AAVE": ["Aave_Official"],
    "ZEC": ["zec"],
    "XMR": ["Monero"],
}


class RedditSearchError(Exception):
    pass


_client: Optional[praw.Reddit] = None


def _get_client() -> praw.Reddit:
    global _client
    if _client is not None:
        return _client

    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_CLIENT_SECRET")
    user_agent = os.getenv("REDDIT_USER_AGENT")
    if not (client_id and client_secret and user_agent):
        raise RedditSearchError(
            "REDDIT_CLIENT_ID/REDDIT_CLIENT_SECRET/REDDIT_USER_AGENT not set. "
            "Register a free 'script' app at https://www.reddit.com/prefs/apps and add them to .env."
        )

    _client = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent, read_only=True)
    return _client


def search_reddit_posts(
    token_symbol: str,
    token_name: Optional[str] = None,
    days_back: int = 7,
    max_posts: int = 10,
) -> List[Dict]:
    """Search token-relevant subreddits (plus r/CryptoCurrency, r/defi) for
    recent posts mentioning the token. Returns up to max_posts posts sorted
    by score, each with subreddit/title/score/num_comments/created_utc/
    permalink/selftext (truncated to 500 chars).
    """
    reddit = _get_client()
    subreddits = TOKEN_SUBREDDITS.get(token_symbol.upper(), []) + DEFAULT_SUBREDDITS
    cutoff = datetime.now(timezone.utc) - timedelta(days=days_back)
    query = token_name or token_symbol

    posts = []
    seen_ids = set()
    for subreddit_name in subreddits:
        try:
            subreddit = reddit.subreddit(subreddit_name)
            for submission in subreddit.search(query, sort="new", time_filter="month", limit=max_posts):
                if submission.id in seen_ids:
                    continue
                created = datetime.fromtimestamp(submission.created_utc, tz=timezone.utc)
                if created < cutoff:
                    continue
                seen_ids.add(submission.id)
                posts.append(
                    {
                        "subreddit": subreddit_name,
                        "title": submission.title,
                        "score": submission.score,
                        "num_comments": submission.num_comments,
                        "created_utc": created.isoformat(),
                        "permalink": f"https://reddit.com{submission.permalink}",
                        "selftext": (submission.selftext or "")[:500],
                    }
                )
        except Exception as e:
            posts.append({"subreddit": subreddit_name, "error": str(e)})

    errors = [p for p in posts if "error" in p]
    clean_posts = [p for p in posts if "error" not in p]
    clean_posts.sort(key=lambda p: p["score"], reverse=True)

    if errors and not clean_posts:
        raise RedditSearchError(f"All subreddit searches failed: {errors}")

    return clean_posts[:max_posts]
