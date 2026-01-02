"""
Experiment Configuration for DeFi Trading Agents Research
Multi-token backtesting with baseline comparisons
"""

from datetime import datetime
from typing import Dict, List

# Experiment Tokens
EXPERIMENT_TOKENS = {
    "BTC": {
        "name": "Bitcoin",
        "coingecko_id": "bitcoin",
        "addresses": {
            "ethereum": "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599",  # WBTC
        }
    },
    "ETH": {
        "name": "Ethereum",
        "coingecko_id": "ethereum",
        "addresses": {
            "ethereum": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",  # WETH
        }
    },
    "SOL": {
        "name": "Solana",
        "coingecko_id": "solana",
        "addresses": {
            "solana": "So11111111111111111111111111111111111111112",
        }
    },
    "UNI": {
        "name": "Uniswap",
        "coingecko_id": "uniswap",
        "addresses": {
            "ethereum": "0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984",
        }
    },
    "AAVE": {
        "name": "Aave",
        "coingecko_id": "aave",
        "addresses": {
            "ethereum": "0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9",
        }
    },
    "ZEC": {
        "name": "Zcash",
        "coingecko_id": "zcash",
        "addresses": {}
    },
    "XMR": {
        "name": "Monero",
        "coingecko_id": "monero",
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
            "kdj_signal_period": 3,
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