# DeFi Trading Agents: Experimental Framework

Complete experimental setup for comparing role-based and function-based multi-agent architectures in DeFi trading.

## 📋 Table of Contents

- [Overview](#overview)
- [Experiment Design](#experiment-design)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Detailed Usage](#detailed-usage)
- [Understanding Results](#understanding-results)
- [Troubleshooting](#troubleshooting)

## Overview

This experimental framework implements the FC27 DeFi Workshop evaluation panel. It compares:

1. **Role-Based Multi-Agent Architecture** — four analysts (on-chain, technical, tokenomics, sentiment) feeding a bull/bear debate → research manager → trader pipeline
2. **Single-Agent Ablation (P6 baseline)** — identical analyst reports, single synthesis step, no debate
3. **5 Baseline Rule-Based Strategies** — MACD, KDJ+RSI, ZMR, SMA Crossover, Buy & Hold

The primary instrument is `experiments/panel_runner.py` (`PanelRunner`), not `experiments/main.py`. See `experiments/config.py` for the full panel definition.

## Panel Design

### Token Panel (10 EVM-native tokens, 2 tiers)

**Tier-1 (7 tokens — used in RQ1, RQ2, RQ3):** ETH, WBTC, LINK, AAVE, UNI, MKR, CRV

All have verified Uniswap v3 pools and complete history from 2022-06-15. Appear at all 8 panel dates.

**Tier-2 (3 tokens — used in RQ2 execution cost analysis only):** PEPE (from 2023-09-15), ONDO (from 2024-06-15), ENA (from 2024-06-15)

Post-launch tokens with shallow-to-mid liquidity; provide the extreme contrast points for the execution cost scaling curve at $500k notional. Excluded from RQ1 (McNemar's test) and RQ3 (contamination stratification) — their post-launch restriction prevents pre-cutoff bucket coverage.

### Panel Dates (8 dates, contamination-stratified)

| Bucket | Dates | Tier-1 points |
|--------|-------|--------------|
| pre\_cutoff | 2022-06-15, 2022-11-10, 2023-03-15, 2023-09-15 | 28 |
| partial | 2024-01-15, 2024-06-15 | 14 |
| post\_cutoff | 2024-11-10, 2025-03-15 | 14 |

Total: 56 Tier-1 + 11 Tier-2 = **67 decision points**. Dates pre-committed before any panel execution.

### Research Questions

- **RQ1 (Architecture):** McNemar's test — does multi-agent debate change decisions, and is any change an improvement? Runs on 56 Tier-1 points (paired role-based vs. single-agent decisions).
- **RQ2 (Execution):** Anvil fork-simulated costs at $10k / $50k / $100k / $500k notional across all 10 tokens. See `scripts/run_fork_sim_mode2.py`.
- **RQ3 (Contamination):** Two-sample proportion test on Tier-1 pre-cutoff vs. post-cutoff directional hit rates. Model cutoffs: gpt-4o-mini Oct 2023, o4-mini Sep 2024.

### Ground Truth

7-day forward return from Yahoo Finance. BUY correct if > +2%, SELL correct if < -2%, HOLD excluded from directional hit rate.

### Prediction Task

- **Objective**: Point-in-time BUY/HOLD/SELL decision at each (token, date) panel point
- **Metrics**:
  - Directional hit rate (BUY/SELL only), stratified by contamination bucket
  - McNemar's test statistic (RQ1)
  - Two-sample proportion z-test (RQ3)
  - Execution cost by notional size (RQ2)

### Performance Evaluation

#### Quantitative Metrics
- Cumulative Return
- Annualized Return
- Sharpe Ratio
- Maximum Drawdown
- Win Rate
- Profit Factor
- Calmar Ratio
- Sortino Ratio

#### Cost Analysis
- **Gas Fees**: Ethereum transaction costs
- **Slippage**: Price impact costs
- **MEV Impact**: Maximal Extractable Value costs
- **API Costs**: LLM API call expenses
- **Token Costs**: LLM token usage expenses

#### Qualitative Evaluation
- **LLM-as-Judge**: Automated quality assessment
- **Human Expert Review**: Sample of 50 decisions

## 🚀 Installation

### Prerequisites

```bash
# Python 3.10+
python --version

# Required packages
pip install -e .

# Additional experiment dependencies
pip install matplotlib seaborn tabulate
```

### Environment Setup

```bash
# Set API keys
export ANTHROPIC_API_KEY="your-anthropic-api-key"
export OPENAI_API_KEY="your-openai-api-key"  # Optional

# Verify setup
python experiments/main.py --check-only
```

## ⚡ Quick Start

### 1. Run Quick Test (5-10 minutes)

Test the framework on a single token:

```bash
python experiments/main.py --mode quick
```

This runs BTC with role-based architecture as a test.

### 2. Run the FC27 Panel (primary path)

Run a single panel point:

```bash
.venv/bin/python3 -c "
from experiments.panel_runner import PanelRunner
runner = PanelRunner()
result = runner.run_panel_point('ETH', '2024-06-15')
print(result['decision'], result['fwd_return_7d'])
"
```

Run the full panel (skip already-completed points):

```bash
.venv/bin/python3 -c "
from experiments.panel_runner import PanelRunner
runner = PanelRunner()
results = runner.run_panel(skip_existing=True)
runner.print_summary(results)
stats = runner.run_statistical_analysis(results)
"
```

Available tokens (Tier-1): ETH, WBTC, LINK, AAVE, UNI, MKR, CRV

Available tokens (Tier-2, post-launch dates only): PEPE, ONDO, ENA

### 3. Run the P6 Single-Agent Ablation (RQ1)

Run the same panel points with the single-agent baseline:

```bash
.venv/bin/python3 scripts/run_p6_ablation.py
```

Then run the McNemar's test:

```bash
.venv/bin/python3 -c "
from experiments.panel_runner import PanelRunner
runner = PanelRunner()
multi = runner.load_all_results('role_based')
single = runner.load_all_results('single_agent')
paired = [(m,s) for m in multi for s in single if m['token']==s['token'] and m['date']==s['date']]
result = runner.mcnemar_test([p[0]['decision'] for p in paired], [p[1]['decision'] for p in paired])
print(result)
"
```

### 4. Run Fork Simulation (RQ2)

After the panel produces directional decisions, run Mode 2:

```bash
.venv/bin/python3 scripts/run_fork_sim_mode2.py --results-dir experiments/panel_results
```

This replays every BUY/SELL across 4 notional sizes ($10k/$50k/$100k/$500k) using Anvil (Foundry) against real historical Uniswap v3 state. Requires `ONCHAIN_RPC_URL` (archive-capable) in `.env` and `anvil` installed via Foundry.

### 5. Validate Pool Addresses

Before the first panel run, confirm all 10 Uniswap v3 pool addresses are live:

```bash
.venv/bin/python3 scripts/validate_pool_addresses.py
```

Expected output: `ALL PASS` for all 10 pools.

## 📊 Understanding Results

### Directory Structure

```
experiments/
├── config.py              # Experiment configuration
├── baselines.py           # Baseline strategy implementations
├── metrics.py             # Performance calculators
├── runner.py              # Experiment orchestrator
├── visualizer.py          # Chart and report generators
├── main.py                # Entry point
├── results/               # Raw experiment results (JSON)
├── charts/                # Generated visualizations (PNG)
└── reports/               # Research reports (Markdown)
```

### Key Outputs

#### 1. Performance Comparison Charts

`experiments/charts/performance_comparison_{TOKEN}.png`

Shows side-by-side comparison of:
- Cumulative returns
- Sharpe ratios
- Maximum drawdowns

For agents vs all baselines.

#### 2. Agent Signal Charts

`experiments/charts/agent_signals_{TOKEN}_{ARCHITECTURE}.png`

Time series showing when agents:
- Buy (green bars)
- Hold (gray bars)
- Sell (red bars)

#### 3. Cost Breakdown Charts

`experiments/charts/cost_breakdown.png`

Stacked bar charts showing:
- Gas fees as % of volume
- Slippage impact
- MEV costs
- API costs in USD

#### 4. Portfolio Trajectories

`experiments/charts/portfolio_trajectory_{TOKEN}_{ARCHITECTURE}.png`

Line charts comparing portfolio value over time for:
- Agent strategy
- Top baseline strategies

#### 5. Research Report

`experiments/reports/experiment_report.md`

Comprehensive markdown report with:
- Executive summary
- Performance comparison tables
- Cost analysis tables
- Prediction accuracy tables
- Conclusions and recommendations

### Sample Results Interpretation

```json
{
  "token": "BTC",
  "architecture": "role_based",
  "agent_results": {
    "metrics": {
      "cumulative_return": 0.45,      // 45% return
      "sharpe_ratio": 1.8,             // Risk-adjusted return
      "max_drawdown": -0.15,           // 15% max loss
      "win_rate": 0.62                 // 62% winning trades
    },
    "costs": {
      "total_cost": {
        "usd": 1250.50,                // Total trading costs
        "percentage": 0.85             // 0.85% of volume
      },
      "gas_fees": {
        "percentage": 0.15             // 0.15% in gas
      },
      "api_costs": {
        "usd": 450.30                  // LLM API costs
      }
    },
    "prediction_evaluation": {
      "direction_accuracy": 0.68,      // 68% correct direction
      "avg_min_price_error": 0.025     // 2.5% price error
    }
  }
}
```

## 📈 Detailed Usage

### Custom Configuration

Modify `experiments/config.py` to customize:

```python
# Adjust time periods
TIME_PERIODS = {
    "backtesting": {
        "start": "2022-01-01",
        "end": "2023-06-30"
    }
}

# Adjust baseline parameters
BASELINE_STRATEGIES = {
    "macd": {
        "params": {
            "fast_period": 12,
            "slow_period": 26,
            "signal_period": 9
        }
    }
}

# Adjust cost assumptions
class CostAnalyzer:
    def __init__(self):
        self.avg_gas_price_gwei = 50  # Adjust gas price
        self.eth_price_usd = 3000      # Adjust ETH price
```

### Adding Custom Baselines

Create new strategy in `experiments/baselines.py`:

```python
class MyCustomStrategy(BaselineStrategy):
    def __init__(self, param1=10, param2=20):
        params = {'param1': param1, 'param2': param2}
        super().__init__("My Strategy", params)
        
    def generate_signals(self, price_data: pd.DataFrame) -> List[TradeSignal]:
        signals = []
        
        # Your strategy logic here
        for idx, row in price_data.iterrows():
            # Generate buy/sell/hold signal
            signal = TradeSignal(...)
            signals.append(signal)
            
        return signals
```

Then add to `BASELINE_STRATEGIES` in config.

### Analyzing Specific Metrics

```python
# Load results
import json
from pathlib import Path

results_dir = Path("./experiments/results")
results = []
for f in results_dir.glob("*.json"):
    with open(f) as file:
        results.append(json.load(file))

# Compare Sharpe ratios
for r in results:
    if r['token'] == 'BTC':
        sharpe = r['agent_results']['metrics']['sharpe_ratio']
        print(f"{r['architecture']}: {sharpe:.2f}")

# Compare costs
for r in results:
    total_cost = r['agent_results']['costs']['total_cost']['usd']
    print(f"{r['token']} - {r['architecture']}: ${total_cost:.2f}")
```

### Generating Custom Visualizations

```python
from experiments.visualizer import ExperimentVisualizer

# Load results
visualizer = ExperimentVisualizer()

# Generate specific chart
visualizer.plot_performance_comparison(results)
visualizer.plot_cost_breakdown(results)
```

## 🔧 Troubleshooting

### Common Issues

#### 1. API Rate Limits

**Problem**: `429 Too Many Requests` errors

**Solution**: 
- Add delays between experiments
- Use lower-cost models (Haiku instead of Sonnet)
- Run experiments in batches

```python
# In runner.py, add delays
import time
time.sleep(2)  # 2 second delay between API calls
```

#### 2. Insufficient Data

**Problem**: `No data found for token X`

**Solution**:
- Implement actual data loading in `_load_price_data()`
- Use CoinGecko API or local CSV files
- Check date ranges match available data

#### 3. Memory Issues

**Problem**: `MemoryError` during backtesting

**Solution**:
- Reduce backtesting period
- Use daily data instead of hourly
- Process tokens sequentially instead of in parallel

#### 4. Import Errors

**Problem**: `ModuleNotFoundError`

**Solution**:
```bash
# Ensure you're in the project root
cd /path/to/defi-trading-agent

# Install all dependencies
pip install -e .
pip install matplotlib seaborn tabulate

# Run from project root
python experiments/main.py
```

### Debugging

Enable debug mode:

```python
# In runner.py
graph = TradingAgentsGraph(
    selected_analysts=analysts,
    debug=True,  # Enable debug output
    config=trading_config
)
```

Check logs:

```bash
# Logs are in experiments/logs/
tail -f experiments/logs/experiment_*.log
```


