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
python3 -m venv .venv
source .venv/bin/activate

# Install the package (editable -- pyproject.toml is the single source of
# dependency truth; there is no requirements.txt)
pip install -e .

# Foundry's anvil is needed for fork-simulated execution (Mode 2)
curl -L https://foundry.paradigm.xyz | bash && foundryup
```

### Required API Keys

Copy `.env.example` to `.env` and fill in keys for the services you want to use:

```bash
cp .env.example .env
```

At minimum, an LLM key is required to run the agent graph (`OPENAI_API_KEY` or `ANTHROPIC_API_KEY`). `COINGECKO_API_KEY`, `ONCHAIN_RPC_URL` (an archive-capable RPC endpoint, e.g. Alchemy's free tier), `DUNE_API_KEY`, and `REDDIT_*` unlock additional real data sources; see the comments in `.env.example` and the "Data Sources" section below for what each one enables.

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
_, decision = ta.propagate("ETH", "2026-06-22")
print(decision)
```

For the full pipeline (live debate -> Stage 4-5 calibration/sizing -> Stage 6 real fork-sim execution), see `scripts/run_e2e_pipeline.py` rather than the bare snippet above.

## Supported Tokens & Networks

The current experiment panel (`experiments/config.py`) is BTC, ETH, SOL, UNI, AAVE, ZEC, XMR. Real on-chain (direct RPC) data only covers tokens with an actual Ethereum mainnet ERC20 address -- BTC (via WBTC), ETH, UNI, AAVE. SOL is a different chain entirely; ZEC and XMR have no EVM presence. Live venues: Uniswap v3 (spot, Ethereum), GMX v2 (perps, Arbitrum), Morpho Vaults (Ethereum). Polygon/Base/Solana are not integrated despite occasionally being mentioned aspirationally in older docs -- if you see a claim like that elsewhere in this repo outside `archive/`, it's stale; this section is the current state.

## Data Sources

All of the following are real, live integrations (not aspirational):

- **Yahoo Finance** (`yfinance`): primary historical OHLCV source (free, no key, full history)
- **CoinGecko API**: current price/market data, and historical data within its free tier's 365-day window
- **DefiLlama API**: DeFi protocol TVL and metrics
- **Direct Ethereum/Arbitrum RPC** (`tradingagents/dataflows/onchain/`): live venue state -- Chainlink price feeds, Uniswap v3 pools, GMX v2 (via its public REST API), Morpho Vaults (ERC4626), plus ERC20 supply reads. Needs an archive-capable RPC URL (e.g. Alchemy's free tier) for historical-block queries.
- **Foundry/Anvil fork-simulated execution** (`tradingagents/dataflows/onchain/fork_sim.py`): real transactions (gas, slippage) against a forked copy of real historical or current chain state
- **Dune Analytics**: holder concentration and DEX volume (needs a one-time query setup -- see `DUNE_HOLDER_QUERY_ID`/`DUNE_VOLUME_QUERY_ID` in `.env.example`)
- **Crypto news RSS** (Cointelegraph, Decrypt, The Block) and the **Crypto Fear & Greed Index** (alternative.me, free, no key): sentiment/news pipeline
- **Reddit** (PRAW): real but typically unconfigured, since Reddit gates API access behind an approval process now

Coinbase AgentKit was investigated for on-chain data and for accelerating the Morpho Vault integration, but is **not used** -- the direct-RPC `tradingagents/dataflows/onchain/` module replaces it.

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

## Documentation

This repo has several scoped READMEs rather than one giant file -- start here, then go deeper as needed:

| Doc | Covers |
|---|---|
| `tests/README.md` | Sentiment/news analyst test suite |
| `experiments/README.md` | Backtest/experiment framework (baselines, metrics, token/period config) |
| `evaluation/README.md` | LLM-judge and human-review evaluation framework |
| `agent-context/README.md` | The agent context/tool-registry runtime system |
| `.claude/skills/README.md` | Claude Code skills used in this project |

## Acknowledgments

- Based on [TradingAgents](https://github.com/TauricResearch/TradingAgents) framework
- Integrates with CoinGecko, DefiLlama, Dune Analytics, and other crypto data providers

