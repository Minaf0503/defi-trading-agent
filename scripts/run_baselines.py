#!/usr/bin/env python
"""
Run the 5 rule-based baseline strategies against real cached OHLCV data and
produce a performance table. This is Phase 1 Weeks 3-4: validate the existing
experiments/baseline.py + experiments/metrics.py code end-to-end on real data
before any agent is built on top of it.

Usage:
    python scripts/run_baselines.py
    python scripts/run_baselines.py --period all_period
    python scripts/run_baselines.py --token ETH
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from datetime import datetime, timezone

import pandas as pd

from experiments.config import EXPERIMENT_TOKENS, TIME_PERIODS, BASELINE_STRATEGIES, EXPERIMENT_PATHS
from experiments.baseline import get_baseline_strategy
from experiments.metrics import PerformanceCalculator
from tradingagents.dataflows.historical_data import HistoricalDataCache


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--token", help="Single token symbol (e.g. ETH). Default: all tokens.")
    parser.add_argument("--period", default="backtesting", choices=list(TIME_PERIODS.keys()))
    return parser.parse_args()


def run_for_token(symbol: str, price_data: pd.DataFrame, calculator: PerformanceCalculator) -> list:
    rows = []
    for strategy_name, strategy_config in BASELINE_STRATEGIES.items():
        strategy = get_baseline_strategy(strategy_name, strategy_config["params"] or None)
        result = strategy.backtest(price_data, initial_capital=10000)
        metrics = calculator.calculate_metrics(result["portfolio_history"], result["trades"], initial_capital=10000)

        row = {"token": symbol, "strategy": strategy_config["name"]}
        row.update(metrics.to_dict())
        rows.append(row)
    return rows


def main():
    args = parse_args()
    symbols = [args.token.upper()] if args.token else list(EXPERIMENT_TOKENS.keys())
    period = TIME_PERIODS[args.period]
    start = datetime.strptime(period["start"], "%Y-%m-%d").replace(tzinfo=timezone.utc)
    end = datetime.strptime(period["end"], "%Y-%m-%d").replace(tzinfo=timezone.utc)

    cache = HistoricalDataCache()
    calculator = PerformanceCalculator()
    all_rows = []

    for symbol in symbols:
        if symbol not in EXPERIMENT_TOKENS:
            print(f"Skipping unknown token: {symbol}")
            continue

        yahoo_ticker = EXPERIMENT_TOKENS[symbol]["yahoo_ticker"]
        price_data = cache.get(symbol, yahoo_ticker, start, end, source="yahoo")
        if price_data.empty:
            print(f"No cached data for {symbol} in range {start.date()}-{end.date()} -- run scripts/fetch_historical_data.py first.")
            continue

        print(f"Running baselines for {symbol} ({len(price_data)} bars, {args.period})...")
        all_rows.extend(run_for_token(symbol, price_data, calculator))

    if not all_rows:
        print("No results produced.")
        sys.exit(1)

    summary = pd.DataFrame(all_rows)
    results_dir = Path(EXPERIMENT_PATHS["results_dir"])
    results_dir.mkdir(parents=True, exist_ok=True)
    out_path = results_dir / f"baseline_performance_{args.period}.csv"
    summary.to_csv(out_path, index=False)

    pd.set_option("display.float_format", lambda x: f"{x:.4f}")
    print(f"\n{summary.to_string(index=False)}")
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()
