#!/usr/bin/env python
"""
Pull and cache historical daily OHLCV for the research token set.

Usage:
    python scripts/fetch_historical_data.py --token ETH
    python scripts/fetch_historical_data.py --all
    python scripts/fetch_historical_data.py --all --force-refresh
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from datetime import datetime, timezone

from experiments.config import EXPERIMENT_TOKENS, TIME_PERIODS
from tradingagents.dataflows.historical_data import HistoricalDataCache, check_data_quality


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--token", help="Single token symbol to fetch (e.g. ETH). Default: all tokens.")
    parser.add_argument("--all", action="store_true", help="Fetch all tokens in EXPERIMENT_TOKENS.")
    parser.add_argument("--force-refresh", action="store_true", help="Ignore cache and re-fetch the full range.")
    parser.add_argument("--period", default="all_period", choices=list(TIME_PERIODS.keys()))
    return parser.parse_args()


def main():
    args = parse_args()

    if args.token:
        symbols = [args.token.upper()]
    elif args.all:
        symbols = list(EXPERIMENT_TOKENS.keys())
    else:
        print("Specify --token SYMBOL or --all", file=sys.stderr)
        sys.exit(1)

    period = TIME_PERIODS[args.period]
    start = datetime.strptime(period["start"], "%Y-%m-%d").replace(tzinfo=timezone.utc)
    end = datetime.strptime(period["end"], "%Y-%m-%d").replace(tzinfo=timezone.utc)

    cache = HistoricalDataCache()
    all_issues = []

    for symbol in symbols:
        if symbol not in EXPERIMENT_TOKENS:
            print(f"Skipping unknown token: {symbol}")
            continue

        yahoo_ticker = EXPERIMENT_TOKENS[symbol]["yahoo_ticker"]
        print(f"Fetching {symbol} ({yahoo_ticker}) {start.date()} -> {end.date()}...")

        df = cache.get(symbol, yahoo_ticker, start, end, source="yahoo", force_refresh=args.force_refresh)
        print(f"  {len(df)} daily bars cached for {symbol}")

        issues = check_data_quality(df, symbol, start, end)
        if issues:
            all_issues.extend(issues)
            for issue in issues:
                print(f"  WARNING: {issue}")
        else:
            print(f"  Data quality: clean")

    if all_issues:
        print(f"\n{len(all_issues)} data quality issue(s) found across {len(symbols)} token(s).")
        sys.exit(1)

    print(f"\nAll {len(symbols)} token(s) fetched and verified cleanly.")


if __name__ == "__main__":
    main()
