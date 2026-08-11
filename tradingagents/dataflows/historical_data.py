"""
Historical OHLCV data pipeline for DeFi Trading Agents research.

Primary source: Yahoo Finance (via yfinance) for daily OHLCV. It's free, has
no rate-limited API key, and covers the project's full 2022-2025 backtest
window natively at daily granularity.

CoinGecko is kept as a secondary/fallback source, but note its free "Demo" API
key tier only allows querying historical data within the past 365 days
(everything older returns a 401 with error_code 10012) -- it cannot serve this
project's multi-year backtest window without a paid plan. Its
/market_chart/range endpoint also only returns hourly granularity for spans
<= 90 days (daily-only, no OHLC, for longer spans), which is why the
CoinGecko path below chunks requests into <=90-day windows and resamples
hourly price+volume into daily bars itself.
"""

import os
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import List, Optional, Tuple

import pandas as pd
import requests
import yfinance as yf
from dotenv import load_dotenv

from tradingagents.dataflows.config import get_config

load_dotenv()

COINGECKO_API = "https://api.coingecko.com/api/v3"
MAX_CHUNK_DAYS = 89
REQUEST_DELAY_SECONDS = 1.5
MAX_RETRIES = 5
OHLCV_COLUMNS = ["timestamp", "open", "high", "low", "close", "volume"]
DEFAULT_SOURCE = "yahoo"


class CoinGeckoFetchError(Exception):
    pass


def _to_utc(dt: datetime) -> datetime:
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


def _chunk_date_range(start: datetime, end: datetime, max_days: int = MAX_CHUNK_DAYS) -> List[Tuple[datetime, datetime]]:
    chunks = []
    current = start
    while current < end:
        chunk_end = min(current + timedelta(days=max_days), end)
        chunks.append((current, chunk_end))
        current = chunk_end
    return chunks


def _coingecko_headers() -> dict:
    api_key = os.getenv("COINGECKO_API_KEY")
    if not api_key:
        return {}
    return {"x-cg-demo-api-key": api_key}


def _request_market_chart_range(coingecko_id: str, start: datetime, end: datetime, vs_currency: str) -> dict:
    url = f"{COINGECKO_API}/coins/{coingecko_id}/market_chart/range"
    params = {"vs_currency": vs_currency, "from": int(start.timestamp()), "to": int(end.timestamp())}

    for attempt in range(MAX_RETRIES):
        response = requests.get(url, params=params, headers=_coingecko_headers(), timeout=30)
        if response.status_code == 429:
            time.sleep(REQUEST_DELAY_SECONDS * (2 ** attempt))
            continue
        if response.status_code == 401:
            raise CoinGeckoFetchError(
                "401 Unauthorized from CoinGecko. Set COINGECKO_API_KEY in your .env file "
                "(sign up for a free Demo key at https://www.coingecko.com/en/api/pricing)."
            )
        if response.status_code == 404:
            raise CoinGeckoFetchError(f"Unknown CoinGecko id '{coingecko_id}'")
        response.raise_for_status()
        return response.json()

    raise CoinGeckoFetchError(f"Exceeded retries fetching {coingecko_id} {start.date()}–{end.date()}")


def _hourly_points_to_daily_ohlcv(prices: list, volumes: list) -> pd.DataFrame:
    if not prices:
        return pd.DataFrame(columns=OHLCV_COLUMNS)

    price_df = pd.DataFrame(prices, columns=["ts_ms", "price"])
    price_df["timestamp"] = pd.to_datetime(price_df["ts_ms"], unit="ms", utc=True)

    volume_df = pd.DataFrame(volumes, columns=["ts_ms", "volume"])
    volume_df["timestamp"] = pd.to_datetime(volume_df["ts_ms"], unit="ms", utc=True)

    merged = pd.merge_asof(
        price_df.sort_values("timestamp"),
        volume_df.sort_values("timestamp")[["timestamp", "volume"]],
        on="timestamp",
    )
    merged["date"] = merged["timestamp"].dt.floor("D")

    daily = merged.groupby("date").agg(
        open=("price", "first"),
        high=("price", "max"),
        low=("price", "min"),
        close=("price", "last"),
        volume=("volume", "sum"),
    ).reset_index()
    daily = daily.rename(columns={"date": "timestamp"})
    return daily[OHLCV_COLUMNS]


def fetch_historical_ohlcv_coingecko(coingecko_id: str, start: datetime, end: datetime, vs_currency: str = "usd") -> pd.DataFrame:
    """Fetch daily OHLCV for [start, end] by stitching <=90-day hourly chunks.

    Free CoinGecko Demo keys only serve the past 365 days of history -- use
    fetch_historical_ohlcv_yahoo for the project's full backtest window.
    """
    start, end = _to_utc(start), _to_utc(end)
    frames = []

    for chunk_start, chunk_end in _chunk_date_range(start, end):
        raw = _request_market_chart_range(coingecko_id, chunk_start, chunk_end, vs_currency)
        frame = _hourly_points_to_daily_ohlcv(raw.get("prices", []), raw.get("total_volumes", []))
        if not frame.empty:
            frames.append(frame)
        time.sleep(REQUEST_DELAY_SECONDS)

    if not frames:
        return pd.DataFrame(columns=OHLCV_COLUMNS)

    combined = pd.concat(frames, ignore_index=True)
    return combined.drop_duplicates(subset="timestamp").sort_values("timestamp").reset_index(drop=True)


def fetch_historical_ohlcv_yahoo(yahoo_ticker: str, start: datetime, end: datetime) -> pd.DataFrame:
    """Fetch daily OHLCV for [start, end] from Yahoo Finance. No API key, no
    chunking needed -- yfinance returns clean daily bars natively."""
    start, end = _to_utc(start), _to_utc(end)
    # yfinance's `end` is exclusive; bump by a day to include the requested end date.
    raw = yf.Ticker(yahoo_ticker).history(start=start, end=end + timedelta(days=1))
    if raw.empty:
        return pd.DataFrame(columns=OHLCV_COLUMNS)

    df = raw.reset_index()[["Date", "Open", "High", "Low", "Close", "Volume"]]
    df.columns = OHLCV_COLUMNS
    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)
    return df.drop_duplicates(subset="timestamp").sort_values("timestamp").reset_index(drop=True)


def fetch_historical_ohlcv(symbol_or_id: str, start: datetime, end: datetime, source: str = DEFAULT_SOURCE, vs_currency: str = "usd") -> pd.DataFrame:
    """Dispatch to the configured source. `symbol_or_id` is a Yahoo ticker
    (e.g. "ETH-USD") when source="yahoo", or a CoinGecko id (e.g. "ethereum")
    when source="coingecko"."""
    if source == "yahoo":
        return fetch_historical_ohlcv_yahoo(symbol_or_id, start, end)
    if source == "coingecko":
        return fetch_historical_ohlcv_coingecko(symbol_or_id, start, end, vs_currency)
    raise ValueError(f"Unknown source: {source!r} (expected 'yahoo' or 'coingecko')")


class HistoricalDataCache:
    """CSV-backed cache for daily OHLCV history; only fetches date ranges missing from disk."""

    def __init__(self, cache_dir: Optional[str] = None):
        config = get_config()
        self.cache_dir = Path(cache_dir or config["data_cache_dir"]) / "historical_ohlcv"
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _cache_path(self, symbol: str) -> Path:
        return self.cache_dir / f"{symbol.upper()}.csv"

    def _load_cached(self, symbol: str) -> pd.DataFrame:
        path = self._cache_path(symbol)
        if not path.exists():
            return pd.DataFrame(columns=OHLCV_COLUMNS)
        df = pd.read_csv(path, parse_dates=["timestamp"])
        df["timestamp"] = df["timestamp"].dt.tz_localize("UTC") if df["timestamp"].dt.tz is None else df["timestamp"]
        return df

    def _missing_ranges(self, cached: pd.DataFrame, start: datetime, end: datetime) -> List[Tuple[datetime, datetime]]:
        start, end = _to_utc(start), _to_utc(end)
        if cached.empty:
            return [(start, end)]

        cached_start = cached["timestamp"].min().to_pydatetime()
        cached_end = cached["timestamp"].max().to_pydatetime()
        ranges = []
        if start < cached_start:
            ranges.append((start, cached_start))
        if end > cached_end:
            ranges.append((cached_end, end))
        return ranges

    def get(
        self,
        symbol: str,
        ticker_or_id: str,
        start: datetime,
        end: datetime,
        source: str = DEFAULT_SOURCE,
        vs_currency: str = "usd",
        force_refresh: bool = False,
    ) -> pd.DataFrame:
        cached = pd.DataFrame(columns=OHLCV_COLUMNS) if force_refresh else self._load_cached(symbol)
        missing_ranges = self._missing_ranges(cached, start, end)

        new_frames = [fetch_historical_ohlcv(ticker_or_id, r_start, r_end, source, vs_currency) for r_start, r_end in missing_ranges]
        new_frames = [f for f in new_frames if not f.empty]

        if new_frames:
            non_empty = [f for f in [cached] + new_frames if not f.empty]
            combined = pd.concat(non_empty, ignore_index=True)
            combined["timestamp"] = pd.to_datetime(combined["timestamp"], utc=True)
            combined = combined.drop_duplicates(subset="timestamp").sort_values("timestamp").reset_index(drop=True)
            combined.to_csv(self._cache_path(symbol), index=False)
        else:
            combined = cached

        start, end = _to_utc(start), _to_utc(end)
        mask = (combined["timestamp"] >= pd.Timestamp(start)) & (combined["timestamp"] <= pd.Timestamp(end))
        return combined.loc[mask].reset_index(drop=True)


def check_data_quality(df: pd.DataFrame, symbol: str, expected_start: datetime, expected_end: datetime) -> List[str]:
    """Return a list of human-readable data quality issues found in df. Empty list = clean."""
    issues = []
    if df.empty:
        return [f"{symbol}: no data returned"]

    full_range = pd.date_range(_to_utc(expected_start).date(), _to_utc(expected_end).date(), freq="D", tz="UTC")
    missing_days = full_range.difference(df["timestamp"].dt.normalize())
    if len(missing_days) > 0:
        issues.append(f"{symbol}: {len(missing_days)} missing day(s), e.g. {list(missing_days[:3].astype(str))}")

    for col in ["open", "high", "low", "close"]:
        if (df[col] <= 0).any():
            issues.append(f"{symbol}: non-positive values in '{col}'")
        if df[col].isna().any():
            issues.append(f"{symbol}: NaN values in '{col}'")

    bad_bars = df[(df["high"] < df["low"]) | (df["high"] < df["open"]) | (df["high"] < df["close"]) | (df["low"] > df["open"]) | (df["low"] > df["close"])]
    if not bad_bars.empty:
        issues.append(f"{symbol}: {len(bad_bars)} bar(s) with high/low inconsistent against open/close")

    if not df["timestamp"].is_monotonic_increasing:
        issues.append(f"{symbol}: timestamps not sorted")

    return issues
