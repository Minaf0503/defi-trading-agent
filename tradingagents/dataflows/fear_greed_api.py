"""
Crypto Fear & Greed Index (alternative.me) -- genuinely free, no API key.

Replaces the LunarCrush social sentiment integration: LunarCrush's free web
account does not include API access (confirmed empirically -- a real API key
returns 402 Payment Required, see writing/papers/PROGRESS_LOG.md 2026-06-21).

Trade-off vs. LunarCrush: this index is market-wide, not per-token. It serves
as a deterministic Stage 2 macro-sentiment feature; per-token sentiment
relies on the LLM reading real news/Reddit content qualitatively rather than
a quantitative per-token score.
"""

import time

import requests

FEAR_GREED_API = "https://api.alternative.me/fng/"
MAX_RETRIES = 3


class FearGreedError(Exception):
    pass


def get_fear_greed_index(limit: int = 1) -> list:
    """Fetch the most recent `limit` days of the Fear & Greed Index.

    Returns a list of dicts: value (0-100, 0=extreme fear, 100=extreme
    greed), value_classification (e.g. "Extreme Fear"), timestamp.

    Retries on transient failures (timeout, connection error, 5xx) -- a
    real 28-point historical panel run (2026-06-22) showed this call fail
    14/14 times it was attempted in that run's specific window, while a
    fresh standalone call afterward succeeded immediately, consistent with
    a brief outage/rate-limit on alternative.me's side rather than a code
    bug. With zero retries beforehand, any single transient hiccup during a
    run produced a 100% failure rate for that run -- this is the fix.
    """
    last_error = None
    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(FEAR_GREED_API, params={"limit": limit}, timeout=15)
            response.raise_for_status()
            payload = response.json()

            if payload.get("metadata", {}).get("error"):
                raise FearGreedError(payload["metadata"]["error"])

            return [
                {
                    "value": int(entry["value"]),
                    "value_classification": entry["value_classification"],
                    "timestamp": int(entry["timestamp"]),
                }
                for entry in payload["data"]
            ]
        except (requests.RequestException, FearGreedError) as e:
            last_error = e
            if attempt < MAX_RETRIES - 1:
                time.sleep(2 * (attempt + 1))
    raise last_error
