# DeFi Trading Agents: Multi-Agent LLM Framework for DeFi Trading

> 🚀 **DeFi Trading Agents** - A specialized multi-agent framework for DeFi and cryptocurrency trading analysis.

## Overview

DeFi Trading Agents is a multi-agent trading framework specifically designed for DeFi and cryptocurrency markets. It deploys specialized LLM-powered agents to collaboratively analyze crypto markets, onchain data, and DeFi protocols to inform trading decisions.

> ⚠️ **Disclaimer**: This framework is designed for research purposes. Trading performance may vary based on many factors, including the chosen language models, model temperature, trading periods, data quality, and other non-deterministic factors. It is not intended as financial, investment, or trading advice.

## Framework Architecture

Our framework decomposes complex DeFi trading tasks into specialized roles, ensuring a robust and scalable approach to crypto market analysis and decision-making.

### Analyst Team

- **Technical Analyst**: Performs technical analysis on important metrics, liquidity, trading volumes, and price movement using indicators like RSI, MACD, Stochastic Oscillator, Bollinger Bands, Ichimoku Cloud, Parabolic SAR, CVD, and more.
- **Onchain Analyst**: Analyzes onchain data to discover potential sudden/trend shifts, including network activity, token holder behavior, liquidity pool burn/lock analysis, wallet holders, and MEMpool.
- **Tokenomics Analyst**: Analyzes tokenomics aspects including token supply, inflation/deflation trends, token distribution, token utility and demand analysis, and tokenomics index.
- **Sentiment/News Analyst**: Analyzes news and social media posts to identify current market sentiment and market player perception on the token.

### Researcher Team

- Comprises both bullish and bearish researchers who critically assess the insights provided by the Analyst Team. Through structured debates, they balance potential gains against inherent risks.

### Trader Agent

- Composes reports from the analysts and researchers to make informed trading decisions. It determines the timing and magnitude of trades based on comprehensive market insights.

### Risk Management and Portfolio Manager

- Continuously evaluates portfolio risk by assessing market volatility, liquidity, and DeFi-specific risks (smart contract risks, oracle risks, etc.). The risk management team evaluates and adjusts trading strategies, providing assessment reports to the Portfolio Manager for final decision.

## Installation

### Prerequisites

- Python 3.10+
- OpenAI API key (or other supported LLM provider)

### Setup

```bash
# Clone the repository
git clone <repository-url>
cd defi-trading-agent

# Create a virtual environment
conda create -n defi-trading python=3.10
conda activate defi-trading

# Install dependencies
pip install -r requirements.txt
```

### Required API Keys

Set your OpenAI API key (or other LLM provider):

```bash
export OPENAI_API_KEY=$YOUR_OPENAI_API_KEY
```

## Usage

### CLI Usage

Run the CLI interface:

```bash
python -m cli.main
```

You will see an interface where you can:
- Select crypto token symbols (e.g., BTC, ETH, UNI)
- Choose analysis date
- Select analyst teams (Crypto Market, Crypto Onchain, Crypto DeFi)
- Configure LLM models and research depth

### Python API

```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

# Create a custom config
config = DEFAULT_CONFIG.copy()
config["deep_think_llm"] = "gpt-4o-mini"
config["quick_think_llm"] = "gpt-4o-mini"
config["max_debate_rounds"] = 1
config["online_tools"] = True

# Initialize with custom config
ta = TradingAgentsGraph(
    selected_analysts=["technical", "onchain", "tokenomics", "sentiment_news"],
    debug=True,
    config=config
)

# Analyze a crypto token
_, decision = ta.propagate("BTC", "2024-05-10")
print(decision)
```

## Supported Tokens & Networks

### Major Cryptocurrencies
- **BTC** - Bitcoin
- **ETH** - Ethereum
- **USDC** - USD Coin
- **USDT** - Tether
- **DAI** - Dai

### DeFi Tokens
- **UNI** - Uniswap
- **LINK** - Chainlink
- **AAVE** - Aave
- **COMP** - Compound
- **CRV** - Curve DAO
- **SUSHI** - SushiSwap
- **YFI** - Yearn Finance
- **BAL** - Balancer
- **SNX** - Synthetix
- **MKR** - Maker

### Networks Supported
- **Ethereum** - Mainnet and testnets
- **Polygon** - Layer 2 scaling
- **Base** - Coinbase's L2
- **Solana** - High-performance blockchain

## Data Sources

The framework integrates with multiple crypto data providers:

- **CoinGecko API**: Real-time crypto prices, market data, and historical data
- **DefiLlama API**: DeFi protocol TVL and metrics
- **Binance API**: Additional price data source
- **Coinbase AgentKit**: Blockchain data integration for onchain analysis

## Features

- **Multi-Agent Architecture**: Specialized agents for different aspects of DeFi analysis
- **Onchain Analytics**: Blockchain data analysis including liquidity, holders, and transactions
- **DeFi Protocol Analysis**: TVL trends, yield opportunities, and governance analysis
- **Technical Analysis**: Crypto-specific technical indicators and market metrics
- **Risk Assessment**: DeFi-specific risk analysis including smart contract and oracle risks

## Configuration

You can customize the framework by modifying `tradingagents/default_config.py` or passing a custom config dictionary. Key configuration options include:

- `deep_think_llm`: Model for deep reasoning tasks
- `quick_think_llm`: Model for fast inference tasks
- `max_debate_rounds`: Number of debate rounds between researchers
- `online_tools`: Whether to use online data sources or cached data
- `llm_provider`: LLM provider (openai, anthropic, google, etc.)

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

Apache-2.0 License

## Acknowledgments

- Based on [TradingAgents](https://github.com/TauricResearch/TradingAgents) framework
- Uses [Coinbase AgentKit](https://github.com/coinbase/agentkit) for blockchain data integration
- Integrates with CoinGecko, DefiLlama, and other crypto data providers

