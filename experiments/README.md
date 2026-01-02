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

## 🎯 Overview

This experimental framework implements comprehensive backtesting to compare:

1. **Role-Based Multi-Agent Architecture** (TradingAgents framework)
2. **Function-Based Orchestrator Architecture** (Centralized approach)
3. **5 Baseline Rule-Based Strategies** (MACD, KDJ+RSI, ZMR, SMA, Buy & Hold)

Across **7 major tokens**: BTC, ETH, SOL, UNI, AAVE, ZEC, XMR

## 🔬 Experiment Design

### Time Periods

- **All Period**: Jan 2022 - Jun 2025
- **Training Data**: Jul 2023 - Dec 2024
- **Backtesting Period**: Jan 2022 - Jun 2023

### Prediction Task

- **Objective**: Predict upward/downward trend in next 24 hours
- **Metrics**: 
  - Direction accuracy
  - Min/Max price gap assessment
  - Volatility prediction error

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
pip install -r requirements.txt

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

### 2. Run Single Experiment

Run a specific token/architecture combination:

```bash
python experiments/main.py --mode single --token BTC --architecture role_based
```

Available options:
- **Tokens**: BTC, ETH, SOL, UNI, AAVE, ZEC, XMR
- **Architectures**: role_based, function_based

### 3. Run Full Experimental Suite (2-4 hours)

Run all experiments:

```bash
python experiments/main.py --mode full
```

This will:
- Run 14 agent experiments (7 tokens × 2 architectures)
- Run 35 baseline experiments (7 tokens × 5 baselines)
- Generate comprehensive visualizations
- Create research report

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
pip install -r requirements.txt
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

## 📝 For Your Research Paper

### Key Results to Report

1. **Performance Comparison Table**
   - Location: `experiments/reports/experiment_report.md`
   - Shows: Cumulative return, Sharpe ratio, Max drawdown for all strategies

2. **Cost Analysis Table**
   - Location: Same report
   - Shows: Gas fees, slippage, MEV, API costs breakdown

3. **Architecture Comparison**
   - Find in: Performance comparison charts
   - Compare: Role-based vs Function-based across all tokens

4. **Statistical Significance**
   - Run multiple trials
   - Calculate confidence intervals
   - Perform t-tests for performance differences

### Citations

When using this framework, cite:

```bibtex
@article{your_paper_2025,
  title={Comparing Role-Based and Function-Based Multi-Agent Architectures for DeFi Trading},
  author={Your Name},
  journal={FC26 DeFi Workshop},
  year={2025}
}

@misc{tradingagents2024,
  title={TradingAgents: Multi-Agent Framework for Financial Trading},
  author={Xiao et al.},
  year={2024}
}
```

## 🎓 Next Steps

1. **Run Experiments**: Start with `--mode quick` to test
2. **Review Results**: Check charts and reports
3. **Iterate**: Adjust parameters and re-run
4. **Analyze**: Deep dive into specific tokens or strategies
5. **Write**: Use results for your FC26 submission

## 📧 Support

For questions or issues:
- Check this README first
- Review troubleshooting section
- Check experiment logs in `experiments/logs/`
- Review error messages carefully


