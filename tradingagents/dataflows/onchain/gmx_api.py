"""
GMX v2 (Arbitrum) perpetuals data via GMX's public REST API
(https://arbitrum-api.gmxinfra.io) -- no API key needed.

Chosen over direct contract reads: GMX v2's storage is a generic
DataStore/Reader key-value pattern (much more involved to query correctly
than Uniswap v3's plain getters), and historical reads would hit the same
archive-RPC wall flagged for Uniswap in Phase 2 Week 5 anyway. The REST API
only exposes *current* state -- no historical-by-block queries.

Unit conventions, verified empirically on 2026-06-21 (see
writing/papers/PROGRESS_LOG.md):
- USD-denominated fields (openInterest*, availableLiquidity*) are 1e30-scaled.
- Token prices from /prices/tickers are scaled as raw / 10**(30 - decimals);
  cross-checked WETH price against the Chainlink ETH/USD feed from Week 5
  (gmx: $1715.46-$1716.82 vs chainlink: $1713.15, <0.3% deviation -- consistent).
- fundingRateLong/Short are 1e30-scaled. An initial implementation treated
  these as per-second factors (per the GMX SDK's getFundingFactorPerPeriod
  convention, which operates on a *different*, separately-fetched per-second
  contract value) and annualized by multiplying by SECONDS_PER_YEAR -- this
  produced nonsensical results (~-3,000,000% APR). Order-of-magnitude
  reasoning (real funding APRs are single/double/low-triple-digit percent,
  not millions) indicates the REST API's fundingRateLong/Short field is
  already on an annualized-equivalent scale: raw/1e30 alone gives ~-9.6%,
  which is plausible; further multiplying by SECONDS_PER_YEAR is wrong.
  This is an inference, not a confirmed spec -- GMX's public docs page is a
  JS app that couldn't be fetched as static text, and no independent source
  (CoinGlass, GMX app) could be reached to confirm directly. Treat
  `funding_rate_apr` as an estimate pending a manual cross-check against
  GMX's own UI before using in any final calibration result.
"""

from functools import lru_cache
from typing import Dict, List

import requests

GMX_API_BASE = "https://arbitrum-api.gmxinfra.io"
GMX_USD_PRECISION = 10 ** 30
SECONDS_PER_YEAR = 365 * 24 * 3600


def _get(path: str) -> dict:
    response = requests.get(f"{GMX_API_BASE}{path}", timeout=15)
    response.raise_for_status()
    return response.json()


@lru_cache(maxsize=1)
def _token_decimals() -> Dict[str, int]:
    """address (lowercased) -> decimals, from GMX's token list."""
    data = _get("/tokens")
    return {t["address"].lower(): t["decimals"] for t in data["tokens"]}


def get_markets_info() -> List[dict]:
    return _get("/markets/info")["markets"]


def get_token_price_usd(token_address: str) -> float:
    """Current GMX oracle price (mid of min/max) for a token, in USD."""
    decimals = _token_decimals()[token_address.lower()]
    tickers = _get("/prices/tickers")
    for t in tickers:
        if t["tokenAddress"].lower() == token_address.lower():
            raw_mid = (int(t["minPrice"]) + int(t["maxPrice"])) / 2
            return raw_mid / (10 ** (30 - decimals))
    raise ValueError(f"No ticker found for token {token_address}")


def find_market(symbol: str) -> dict:
    """Find a listed GMX v2 market by index-token symbol, e.g. 'ETH' -> the 'ETH/USD [...]' market."""
    markets = get_markets_info()
    matches = [m for m in markets if m["name"].split("/")[0] == symbol and m.get("isListed", True)]
    if not matches:
        raise ValueError(f"No listed GMX v2 market found for symbol {symbol!r}")
    return matches[0]
