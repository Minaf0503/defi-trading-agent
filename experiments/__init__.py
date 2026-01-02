"""
DeFi Trading Agents - Experimental Framework

This package provides comprehensive experimental infrastructure for comparing
role-based and function-based multi-agent architectures in DeFi trading.

Key modules:
- config: Experiment configuration and parameters
- baselines: Rule-based trading strategy implementations
- metrics: Performance and cost analysis calculators
- runner: Experiment orchestration and execution
- visualizer: Chart generation and report creation
- main: Entry point for running experiments

Usage:
    # Quick test
    python experiments/main.py --mode quick
    
    # Full suite
    python experiments/main.py --mode full
    
    # Single experiment
    python experiments/main.py --mode single --token BTC --architecture role_based
"""

__version__ = "0.1.0"
__author__ = "DeFi Trading Agents Research Team"

from .config import (
    EXPERIMENT_TOKENS,
    TIME_PERIODS,
    BASELINE_STRATEGIES,
    AGENT_ARCHITECTURES,
    get_experiment_config,
    get_all_experiment_combinations
)

from .baselines import (
    BaselineStrategy,
    BuyAndHoldStrategy,
    MACDStrategy,
    KDJRSIStrategy,
    ZMRStrategy,
    SMACrossoverStrategy,
    get_baseline_strategy
)

from .metrics import (
    PerformanceMetrics,
    PerformanceCalculator,
    CostAnalyzer,
    PredictionEvaluator
)

from .runner import ExperimentRunner

from .visualizer import (
    ExperimentVisualizer,
    ReportGenerator
)

__all__ = [
    # Config
    'EXPERIMENT_TOKENS',
    'TIME_PERIODS',
    'BASELINE_STRATEGIES',
    'AGENT_ARCHITECTURES',
    'get_experiment_config',
    'get_all_experiment_combinations',
    
    # Baselines
    'BaselineStrategy',
    'BuyAndHoldStrategy',
    'MACDStrategy',
    'KDJRSIStrategy',
    'ZMRStrategy',
    'SMACrossoverStrategy',
    'get_baseline_strategy',
    
    # Metrics
    'PerformanceMetrics',
    'PerformanceCalculator',
    'CostAnalyzer',
    'PredictionEvaluator',
    
    # Runner
    'ExperimentRunner',
    
    # Visualizer
    'ExperimentVisualizer',
    'ReportGenerator',
]