"""
Experiment Configuration for DeFi Trading Agents Research
Multi-token backtesting with baseline comparisons

Token selection criteria (formalized 2026-06-22, retroactively against an
already-existing panel -- see BUILD_PLAN.md and
writing/papers/PROGRESS_LOG.md for the full rationale and methodology
comparison against the Alpha Illusion paper's P2 "dynamic universe"
protocol, which names undocumented, ex-post-rationalized selection as a
named failure mode):

1. Liquidity-coverage first: a token only counts as having real on-chain
   coverage if it has a *verified* (queried on-chain, not assumed from an
   address existing) liquidity venue or supply source on a chain this
   project can directly RPC-query. BTC (via WBTC), ETH, UNI, and AAVE all
   verify this way (tradingagents/dataflows/onchain/contracts.py). SOL, ZEC,
   and XMR do not -- they are non-EVM by fundamental architecture (SOL is a
   different VM; ZEC/XMR have no smart-contract layer at all), not a gap to
   eventually fill. They are kept in this panel deliberately, as a negative
   case that exercises the on-chain analyst's graceful-degradation path
   (explicit "not configured" rather than silent failure or a fabricated
   number) -- removing them would remove that test coverage, not just
   simplify the panel.
2. Market-cap tier diversity, point-in-time, verified for 5 of 7 tokens
   without any paid plan: CoinGecko and CoinPaprika's own public APIs both
   reject historical queries older than 365 days on their free tiers
   (confirmed live, 2026-06-22), but Dune Analytics' curated `prices.day`
   table carries coinpaprika-sourced daily prices back to 2022-01-01
   regardless (real, queried: BTC $47,178.37, ETH $3,730.34, SOL $173.88,
   UNI $17.22, AAVE $258.02 on 2022-01-01 -- all consistent with known real
   historical prices for that date). Combined with real on-chain
   ERC20.totalSupply() at block 13916166 (2022-01-01 00:00:03 UTC, found via
   binary search on block timestamps) for UNI (1,000,000,000) and AAVE
   (16,000,000) -- both freshly verified via direct RPC, not assumed -- and
   well-known circulating-supply figures for BTC/ETH/SOL (NOT independently
   re-verified this session; native-asset circulating supply has no
   on-chain RPC source in this project's tooling, since WBTC/WETH's
   totalSupply() is the wrapped-token supply, a small fraction of the real
   asset's supply -- the same caveat already documented for
   get_onchain_supply_data("BTC"/"ETH")), this gives real point-in-time
   market caps: BTC ~$893.2B, ETH ~$442.2B, SOL ~$51.7B, UNI ~$17.2B (real
   supply was likely somewhat lower due to vesting not yet fully unlocked
   in Jan 2022; totalSupply is an upper bound, not circulating supply),
   AAVE ~$4.1B -- confirming the intended mega/large/mid-cap tiering exactly
   as labeled. ZEC and XMR remain unverified: Dune's prices.day has no
   coinpaprika rows for either on 2022-01-01 (itself a notable data-coverage
   finding, not investigated further), and no other free historical source
   was found -- their small/mid-cap label remains a general-knowledge
   characterization, consistent with their role as this panel's deliberate
   non-EVM negative case rather than a token this criterion was ever meant
   to fully close.
3. Full-history data-availability floor: daily OHLCV must be available from
   Yahoo Finance across the entire intended backtest window with no gaps --
   already enforced operationally since Phase 1 (1277 daily bars/token,
   2022-01-01 to 2025-06-30), just not previously stated as a named
   criterion.

What this is not: a claim that liquidity-coverage was checked this
rigorously *before* the original panel was chosen -- it wasn't (no written
rationale existed prior to this). This formalizes the criteria the existing
panel happens to satisfy and will govern any future additions, rather than
rationalizing the list after the fact without a falsifiable standard.
"""

from datetime import datetime
from typing import Dict, List

# Experiment Tokens
EXPERIMENT_TOKENS = {
    "BTC": {
        "name": "Bitcoin",
        "coingecko_id": "bitcoin",
        "yahoo_ticker": "BTC-USD",
        "addresses": {
            "ethereum": "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599",  # WBTC
        }
    },
    "ETH": {
        "name": "Ethereum",
        "coingecko_id": "ethereum",
        "yahoo_ticker": "ETH-USD",
        "addresses": {
            "ethereum": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",  # WETH
        }
    },
    "SOL": {
        "name": "Solana",
        "coingecko_id": "solana",
        "yahoo_ticker": "SOL-USD",
        "addresses": {
            "solana": "So11111111111111111111111111111111111111112",
        }
    },
    "UNI": {
        "name": "Uniswap",
        "coingecko_id": "uniswap",
        "yahoo_ticker": "UNI7083-USD",
        "addresses": {
            "ethereum": "0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984",
        }
    },
    "AAVE": {
        "name": "Aave",
        "coingecko_id": "aave",
        "yahoo_ticker": "AAVE-USD",
        "addresses": {
            "ethereum": "0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9",
        }
    },
    "ZEC": {
        "name": "Zcash",
        "coingecko_id": "zcash",
        "yahoo_ticker": "ZEC-USD",
        "addresses": {}
    },
    "XMR": {
        "name": "Monero",
        "coingecko_id": "monero",
        "yahoo_ticker": "XMR-USD",
        "addresses": {}
    }
}

# Time Periods
TIME_PERIODS = {
    "all_period": {
        "start": "2022-01-01",
        "end": "2025-06-30"
    },
    "training": {
        "start": "2023-07-01",
        "end": "2024-12-31"
    },
    "backtesting": {
        "start": "2022-01-01",
        "end": "2023-06-30"
    }
}

# Baseline Strategies Configuration
BASELINE_STRATEGIES = {
    "buy_and_hold": {
        "name": "Buy and Hold",
        "description": "Buy at the start and hold until the end",
        "params": {}
    },
    "macd": {
        "name": "MACD Strategy",
        "description": "Buy when MACD crosses above signal, sell when crosses below",
        "params": {
            "fast_period": 12,
            "slow_period": 26,
            "signal_period": 9
        }
    },
    "kdj_rsi": {
        "name": "KDJ + RSI Combined",
        "description": "Combined momentum strategy using KDJ and RSI",
        "params": {
            "kdj_period": 9,
            "rsi_period": 14,
            "rsi_overbought": 70,
            "rsi_oversold": 30
        }
    },
    "zmr": {
        "name": "Zero Mean Reversion",
        "description": "Mean reversion strategy",
        "params": {
            "lookback_period": 20,
            "entry_threshold": 2.0,  # Standard deviations
            "exit_threshold": 0.5
        }
    },
    "sma_crossover": {
        "name": "SMA Crossover",
        "description": "Simple moving average crossover strategy",
        "params": {
            "short_window": 50,
            "long_window": 200
        }
    }
}

# Agent Architecture Types
AGENT_ARCHITECTURES = {
    "role_based": {
        "name": "Role-Based Multi-Agent",
        "description": "Specialized agents (TradingAgents framework)",
        "analysts": ["technical", "onchain", "tokenomics", "sentiment_news"]
    },
    "function_based": {
        "name": "Function-Based Orchestrator",
        "description": "Centralized orchestrator with worker functions",
        "analysts": ["technical", "onchain", "tokenomics", "sentiment_news"]
    }
}

# Performance Metrics
PERFORMANCE_METRICS = [
    "cumulative_return",
    "annualized_return",
    "sharpe_ratio",
    "max_drawdown",
    "win_rate",
    "profit_factor",
    "total_trades",
    "avg_trade_return"
]

# Cost Analysis Components
COST_COMPONENTS = {
    "gas_fees": {
        "description": "Ethereum gas costs for on-chain transactions",
        "unit": "ETH"
    },
    "slippage": {
        "description": "Price impact and slippage costs",
        "unit": "percentage"
    },
    "mev_impact": {
        "description": "MEV (Maximal Extractable Value) costs",
        "unit": "percentage"
    },
    "api_costs": {
        "description": "LLM API call costs",
        "unit": "USD"
    },
    "token_costs": {
        "description": "LLM token usage costs",
        "unit": "USD"
    }
}

# Evaluation Configuration
EVALUATION_CONFIG = {
    "llm_as_judge": {
        "enabled": True,
        "model": "claude-sonnet-4-20250514",
        "criteria": [
            "prediction_accuracy",
            "reasoning_quality",
            "risk_assessment",
            "recommendation_clarity"
        ]
    },
    "human_review": {
        "enabled": True,
        "sample_size": 50,  # Number of decisions to review
        "criteria": [
            "technical_soundness",
            "fundamental_analysis_quality",
            "risk_management",
            "overall_decision_quality"
        ]
    }
}

# Prediction Task Configuration
PREDICTION_TASK = {
    "type": "trend_prediction",
    "horizon": "24_hours",
    "targets": [
        "price_direction",  # upward/downward
        "min_price_next_24h",
        "max_price_next_24h",
        "volatility_estimate"
    ],
    "evaluation_metrics": [
        "direction_accuracy",
        "min_price_gap",  # Difference between predicted and actual min
        "max_price_gap",
        "volatility_prediction_error"
    ]
}

# Experiment Output Paths
EXPERIMENT_PATHS = {
    "base_dir": "./experiments",
    "results_dir": "./experiments/results",
    "data_dir": "./experiments/data",
    "reports_dir": "./experiments/reports",
    "charts_dir": "./experiments/charts",
    "logs_dir": "./experiments/logs"
}

def get_experiment_config(token: str, architecture: str, period: str) -> Dict:
    """Get complete experiment configuration for a specific setup."""
    return {
        "token": EXPERIMENT_TOKENS[token],
        "architecture": AGENT_ARCHITECTURES[architecture],
        "period": TIME_PERIODS[period],
        "baselines": BASELINE_STRATEGIES,
        "metrics": PERFORMANCE_METRICS,
        "costs": COST_COMPONENTS,
        "evaluation": EVALUATION_CONFIG,
        "prediction": PREDICTION_TASK,
        "paths": EXPERIMENT_PATHS
    }

def get_all_experiment_combinations() -> List[Dict]:
    """Generate all experiment combinations."""
    combinations = []
    for token in EXPERIMENT_TOKENS.keys():
        for arch in AGENT_ARCHITECTURES.keys():
            for period in ["backtesting"]:  # Focus on backtesting period
                combinations.append({
                    "token": token,
                    "architecture": arch,
                    "period": period,
                    "config": get_experiment_config(token, arch, period)
                })
    return combinations


# ─── FC27 Panel Design (experiment_design_and_token_selection.md) ─────────────

PANEL_TOKENS = {
    # Tier 1 — long history, all 8 dates
    "ETH":  {"name": "Ethereum",       "tier": 1, "yahoo_ticker": "ETH-USD",      "erc20": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2", "defillama_slug": None,           "uniswap_v3_pool": "0x88e6A0c2dDD26FEEb64F039a2c41296FcB3f5640", "pool_key": "WETH/USDC",  "liquidity_tier": "deep"},
    "WBTC": {"name": "Wrapped Bitcoin", "tier": 1, "yahoo_ticker": "WBTC-USD",     "erc20": "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599", "defillama_slug": None,           "uniswap_v3_pool": "0xCBCdF9626bC03E24f779434178A73a0B4bad62eD", "pool_key": "WBTC/WETH",  "liquidity_tier": "deep"},
    "LINK": {"name": "Chainlink",       "tier": 1, "yahoo_ticker": "LINK-USD",     "erc20": "0x514910771AF9Ca656af840dff83E8264EcF986CA", "defillama_slug": None,           "uniswap_v3_pool": "0xa6Cc3C2531FdaA6Ae1A3CA84c2855806728693e8", "pool_key": "LINK/WETH", "liquidity_tier": "mid"},
    "AAVE": {"name": "Aave",            "tier": 1, "yahoo_ticker": "AAVE-USD",     "erc20": "0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9", "defillama_slug": "aave-v3",      "uniswap_v3_pool": "0x5aB53EE1d50eeF2C1DD3d5402789cd27bB52c1bB", "pool_key": "AAVE/WETH", "liquidity_tier": "mid-shallow"},
    "UNI":  {"name": "Uniswap",         "tier": 1, "yahoo_ticker": "UNI7083-USD",  "erc20": "0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984", "defillama_slug": "uniswap-v3",   "uniswap_v3_pool": "0x1d42064Fc4Beb5F8aAF85F4617AE8b3b5B8Bd801", "pool_key": "UNI/WETH",  "liquidity_tier": "mid"},
    "MKR":  {"name": "Maker",           "tier": 1, "yahoo_ticker": "MKR-USD",      "erc20": "0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2", "defillama_slug": "makerdao",      "uniswap_v3_pool": "0xe8c6c9227491C0a8156A0106A0204d881BB7E531", "pool_key": "MKR/WETH",  "liquidity_tier": "shallow-mid"},
    "CRV":  {"name": "Curve DAO",       "tier": 1, "yahoo_ticker": "CRV-USD",      "erc20": "0xD533a949740bb3306d119CC777fa900bA034cd52", "defillama_slug": "curve-dex",    "uniswap_v3_pool": "0x919Fa96e88d67499339577Fa202345436bcDaf79", "pool_key": "CRV/WETH",  "liquidity_tier": "very-shallow"},
    # Tier 2 — post-launch dates only
    "PEPE": {"name": "Pepe",            "tier": 2, "yahoo_ticker": "PEPE24478-USD","erc20": "0x6982508145454Ce325dDbE47a25d4ec3d2311933", "defillama_slug": None,           "uniswap_v3_pool": "0x11950d141EcB863F01007AdD7D1A342041227b58", "pool_key": "PEPE/WETH", "liquidity_tier": "shallow",
             "first_panel_date": "2023-09-15", "note": "Launched April 2023"},
    "ONDO": {"name": "Ondo Finance",    "tier": 2, "yahoo_ticker": "ONDO-USD",     "erc20": "0xfAbA6f8e4a5E8Ab82F62fe7C39859FA577269BE3", "defillama_slug": "ondo-finance", "uniswap_v3_pool": "0x7b1E5D984A43eE732de195628d20d05CFaBc3cC7", "pool_key": "ONDO/WETH", "liquidity_tier": "shallow-mid",
             "first_panel_date": "2024-06-15", "note": "Yahoo data from ~April 2024; design doc Jan 2024"},
    "ENA":  {"name": "Ethena",          "tier": 2, "yahoo_ticker": "ENA-USD",      "erc20": "0x57e114B691Db790C35207b2e685D4A43181e6061", "defillama_slug": "ethena",       "uniswap_v3_pool": "0xc3Db44ADC1fCdFd5671f555236eae49f4A8EEa18", "pool_key": "ENA/WETH",  "liquidity_tier": "mid-shallow",
             "first_panel_date": "2024-06-15", "note": "Launched April 2024; Yahoo data from June 2024"},
}

PANEL_DATES = [
    # Date            Market regime          DeFi context                         Cutoff status          Tier-2 tokens
    {"date": "2022-06-15", "regime": "deep_bear",    "context": "Post-Terra/LUNA collapse; peak TVL drawdown",     "cutoff": "pre_all",     "tier2": []},
    {"date": "2022-11-10", "regime": "capitulation", "context": "FTX collapse; extreme fear; liquidity crisis",    "cutoff": "pre_all",     "tier2": []},
    {"date": "2023-03-15", "regime": "recovery",     "context": "SVB banking crisis; USDC depeg; DeFi stress",    "cutoff": "pre_all",     "tier2": []},
    {"date": "2023-09-15", "regime": "consolidation","context": "Pre-ETF speculation; Dencun prep",                "cutoff": "pre_all",     "tier2": ["PEPE"]},
    {"date": "2024-01-15", "regime": "bull_onset",   "context": "Bitcoin ETF approval; strong inflows; risk-on",  "cutoff": "partial",     "tier2": ["PEPE"]},
    {"date": "2024-06-15", "regime": "mid_cycle",    "context": "ETH ETF anticipation; DeFi TVL recovery",        "cutoff": "partial",     "tier2": ["PEPE", "ONDO", "ENA"]},
    {"date": "2024-11-10", "regime": "peak_bull",    "context": "US election; BTC ATH; extreme sentiment",        "cutoff": "post_all",    "tier2": ["PEPE", "ONDO", "ENA"]},
    {"date": "2025-03-15", "regime": "post_peak",    "context": "Market correction; tariff uncertainty",           "cutoff": "post_all",    "tier2": ["PEPE", "ONDO", "ENA"]},
]

# Contamination stratification for RQ3
CONTAMINATION_BUCKETS = {
    "pre_cutoff":  ["2022-06-15", "2022-11-10", "2023-03-15", "2023-09-15"],  # all models contaminated
    "partial":     ["2024-01-15", "2024-06-15"],                               # only o4-mini contaminated
    "post_cutoff": ["2024-11-10", "2025-03-15"],                               # no models contaminated
}

# Ground truth thresholds (Section 8.1 of design doc)
GROUND_TRUTH_CONFIG = {
    "forward_days": 7,
    "buy_threshold":  0.02,   # +2% → BUY correct
    "sell_threshold": -0.02,  # -2% → SELL correct
    "hold_evaluation": "reasoning_quality",  # HOLDs excluded from hit rate
}

def get_panel_tokens_for_date(date_str: str) -> List[str]:
    """Return tokens eligible for a given panel date."""
    tokens = []
    for symbol, info in PANEL_TOKENS.items():
        first = info.get("first_panel_date")
        if first and date_str < first:
            continue
        tokens.append(symbol)
    return tokens

def get_panel_points() -> List[Dict]:
    """Enumerate all valid (token, date) panel points."""
    points = []
    for date_info in PANEL_DATES:
        date_str = date_info["date"]
        for symbol in get_panel_tokens_for_date(date_str):
            token_info = PANEL_TOKENS[symbol]
            points.append({
                "token":       symbol,
                "date":        date_str,
                "regime":      date_info["regime"],
                "context":     date_info["context"],
                "cutoff":      date_info["cutoff"],
                "tier":        token_info["tier"],
                "liquidity":   token_info["liquidity_tier"],
                "yahoo_ticker":token_info["yahoo_ticker"],
            })
    return points