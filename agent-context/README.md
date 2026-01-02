# Agent Context and Tool System

This directory contains the agent context management system that allows you to store knowledge, API configurations, and tools for each agent in the DeFi trading system.

## Overview

The agent context system provides two main components:

1. **AgentContextManager**: Manages knowledge base and API information for each agent
2. **ToolRegistry**: Manages tools for each agent, allowing dynamic registration and API querying

## Directory Structure

```
agent-context/
├── knowledge/          # Stored knowledge for each agent
│   ├── technical/
│   ├── onchain/
│   ├── tokenomics/
│   └── sentiment_news/
├── apis/              # API configurations for each agent
│   ├── technical/
│   ├── onchain/
│   └── ...
├── tools/             # Tool configurations for each agent
├── preferences/       # Agent preferences
└── history/           # Historical context data
```

## Usage

### 1. Storing Knowledge for an Agent

```python
from tradingagents.agents.utils.context_manager import AgentContextManager

context_manager = AgentContextManager(base_dir="agent-context")

# Store knowledge
knowledge_id = context_manager.store_knowledge(
    agent_name="technical",
    knowledge={
        "indicator_preferences": {
            "preferred_indicators": ["RSI", "MACD"],
            "timeframes": ["1h", "4h", "1d"]
        }
    },
    category="trading_strategy",
    metadata={"source": "manual_configuration"}
)
```

### 2. Retrieving Knowledge

```python
# Retrieve knowledge
results = context_manager.retrieve_knowledge(
    agent_name="technical",
    category="trading_strategy",
    query="RSI",  # Optional search query
    limit=10
)
```

### 3. Storing API Information

```python
# Store API configuration
context_manager.store_api_info(
    agent_name="technical",
    api_name="coingecko",
    api_config={
        "base_url": "https://api.coingecko.com/api/v3",
        "endpoints": [
            {
                "path": "/simple/price",
                "method": "GET",
                "description": "Get current price"
            }
        ]
    },
    credentials={
        "api_key": "your-api-key"
    }
)
```

### 4. Using Tools with Context

```python
from tradingagents.agents.utils.agent_utils import Toolkit

toolkit = Toolkit()

# Get all tools for an agent (includes context and API tools)
technical_tools = toolkit.get_agent_tools("technical")

# Tools automatically include:
# - Base crypto/DeFi tools
# - Context query tools (query_agent_context)
# - Context store tools (store_agent_context)
# - API query tools (based on stored API configurations)
```

### 5. Storing Agent Preferences

```python
# Store preferences
context_manager.store_preference("technical", "risk_tolerance", "moderate")
context_manager.store_preference("technical", "preferred_timeframe", "4h")

# Retrieve preferences
risk_tolerance = context_manager.get_preference("technical", "risk_tolerance")
```

## Agent Tools

Each agent automatically gets access to:

1. **Base Tools**: Standard crypto/DeFi analysis tools
2. **Context Query Tool**: `{agent_name}_context_query` - Query the agent's knowledge base
3. **Context Store Tool**: `{agent_name}_context_store` - Store information in the knowledge base
4. **API Query Tools**: Tools for each registered API endpoint

### Example: Using Context Tools in Agent Workflow

When an agent runs, it can use these tools:

```python
# Agent can query its own context
result = agent.invoke({
    "messages": [HumanMessage(content="What are my preferred indicators?")],
    # Agent will use technical_context_query tool
})

# Agent can store new information
result = agent.invoke({
    "messages": [HumanMessage(content="Remember that BTC showed strong support at $40k")],
    # Agent will use technical_context_store tool
})
```

## API Integration

### Registering a New API

1. Store API configuration:
```python
context_manager.store_api_info(
    agent_name="technical",
    api_name="my_api",
    api_config={
        "base_url": "https://api.example.com",
        "endpoints": [
            {
                "path": "/v1/data",
                "method": "GET",
                "description": "Get market data"
            }
        ],
        "api_key_header": "X-API-Key"  # Optional
    },
    credentials={
        "api_key": "your-key"
    }
)
```

2. The tool registry automatically creates query tools for each endpoint
3. Agents can use these tools in their workflows

## Best Practices

1. **Organize Knowledge by Category**: Use categories to organize knowledge (e.g., "trading_strategy", "market_data", "risk_rules")

2. **Store API Credentials Securely**: In production, use environment variables or secure credential storage instead of hardcoding

3. **Use Metadata**: Include metadata (source, timestamp, version) when storing knowledge for traceability

4. **Query Efficiently**: Use specific categories and queries to retrieve relevant knowledge quickly

5. **Update Preferences**: Store agent preferences separately from knowledge for easier management

## Examples

See `examples/agent_context_example.py` for complete usage examples.

## Integration with Trading Graph

The context manager and tool registry are automatically integrated with the trading graph. When you create a `TradingAgentsGraph`, it:

1. Initializes the context manager
2. Sets up tool registry
3. Automatically includes context and API tools for each agent
4. Allows agents to query and store context during execution

## File Format

All context data is stored as JSON files:

- **Knowledge**: `knowledge/{agent_name}/{category}/{knowledge_id}.json`
- **APIs**: `apis/{agent_name}/{api_name}.json`
- **Tools**: `tools/{agent_name}/{tool_name}.json`
- **Preferences**: `preferences/{agent_name}/preferences.json`

