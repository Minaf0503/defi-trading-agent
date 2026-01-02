"""
Example: Using Agent Context Manager and Tool Registry

This script demonstrates how to:
1. Store knowledge/APIs for each agent
2. Register tools for querying external APIs
3. Use the context in agent workflows
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tradingagents.agents.utils.context_manager import AgentContextManager
from tradingagents.agents.utils.tool_registry import ToolRegistry
from tradingagents.agents.utils.agent_utils import Toolkit


def example_store_knowledge():
    """Example: Store knowledge for an agent."""
    print("=" * 60)
    print("Example 1: Storing Knowledge for Agents")
    print("=" * 60)
    
    # Initialize context manager
    context_manager = AgentContextManager(base_dir="agent-context")
    
    # Store knowledge for technical analyst
    knowledge_id = context_manager.store_knowledge(
        agent_name="technical",
        knowledge={
            "indicator_preferences": {
                "preferred_indicators": ["RSI", "MACD", "Bollinger Bands"],
                "timeframes": ["1h", "4h", "1d"],
                "overbought_threshold": 70,
                "oversold_threshold": 30
            },
            "trading_rules": [
                "RSI > 70 indicates overbought condition",
                "MACD crossover signals trend change",
                "Volume confirmation required for all signals"
            ]
        },
        category="trading_strategy",
        metadata={
            "source": "manual_configuration",
            "version": "1.0"
        }
    )
    
    print(f"✓ Stored knowledge with ID: {knowledge_id}")
    
    # Store knowledge for onchain analyst
    context_manager.store_knowledge(
        agent_name="onchain",
        knowledge={
            "important_addresses": {
                "whale_wallets": [
                    "0x1234...",
                    "0x5678..."
                ],
                "exchange_addresses": [
                    "0xabcd...",
                    "0xefgh..."
                ]
            },
            "monitoring_rules": [
                "Track large transfers (>$1M)",
                "Monitor exchange inflows/outflows",
                "Watch for unusual activity patterns"
            ]
        },
        category="addresses",
        metadata={"source": "manual_configuration"}
    )
    
    print("✓ Stored knowledge for onchain analyst")
    
    # Retrieve knowledge
    results = context_manager.retrieve_knowledge(
        agent_name="technical",
        category="trading_strategy"
    )
    
    print(f"\n✓ Retrieved {len(results)} knowledge entries for technical analyst")
    for result in results:
        print(f"  - ID: {result['id']}, Category: {result['category']}")


def example_store_api():
    """Example: Store API information for an agent."""
    print("\n" + "=" * 60)
    print("Example 2: Storing API Information")
    print("=" * 60)
    
    context_manager = AgentContextManager(base_dir="agent-context")
    
    # Store API configuration for technical analyst
    context_manager.store_api_info(
        agent_name="technical",
        api_name="coingecko",
        api_config={
            "base_url": "https://api.coingecko.com/api/v3",
            "endpoints": [
                {
                    "path": "/simple/price",
                    "method": "GET",
                    "description": "Get current price for cryptocurrencies"
                },
                {
                    "path": "/coins/{id}/market_chart",
                    "method": "GET",
                    "description": "Get historical market data"
                }
            ]
        },
        credentials={
            "api_key": "your-api-key-here"  # In production, use secure storage
        }
    )
    
    print("✓ Stored CoinGecko API configuration")
    
    # Store another API
    context_manager.store_api_info(
        agent_name="onchain",
        api_name="etherscan",
        api_config={
            "base_url": "https://api.etherscan.io/api",
            "endpoints": [
                {
                    "path": "",
                    "method": "GET",
                    "description": "Query Ethereum blockchain data"
                }
            ],
            "api_key_header": "apikey"
        },
        credentials={
            "api_key": "your-etherscan-api-key"
        }
    )
    
    print("✓ Stored Etherscan API configuration")
    
    # Retrieve API info
    apis = context_manager.get_api_info("technical")
    print(f"\n✓ Retrieved {len(apis)} API configurations for technical analyst")
    for api in apis:
        print(f"  - API: {api['api_name']}, Endpoints: {len(api['config'].get('endpoints', []))}")


def example_use_tools():
    """Example: Using tools with context manager."""
    print("\n" + "=" * 60)
    print("Example 3: Using Tools with Context")
    print("=" * 60)
    
    # Initialize toolkit (which includes context manager and tool registry)
    toolkit = Toolkit()
    
    # Get tools for technical analyst (includes context and API tools)
    technical_tools = toolkit.get_agent_tools("technical")
    
    print(f"✓ Retrieved {len(technical_tools)} tools for technical analyst")
    print("\nAvailable tools:")
    for tool in technical_tools:
        print(f"  - {tool.name}: {tool.description[:80]}...")


def example_query_context():
    """Example: Query agent context."""
    print("\n" + "=" * 60)
    print("Example 4: Querying Agent Context")
    print("=" * 60)
    
    context_manager = AgentContextManager(base_dir="agent-context")
    
    # Query knowledge
    results = context_manager.retrieve_knowledge(
        agent_name="technical",
        query="RSI",
        limit=5
    )
    
    print(f"✓ Found {len(results)} results for query 'RSI'")
    for result in results:
        print(f"  - Category: {result['category']}")
        print(f"    Knowledge: {str(result['knowledge'])[:100]}...")


def example_store_preferences():
    """Example: Store agent preferences."""
    print("\n" + "=" * 60)
    print("Example 5: Storing Agent Preferences")
    print("=" * 60)
    
    context_manager = AgentContextManager(base_dir="agent-context")
    
    # Store preferences
    context_manager.store_preference("technical", "risk_tolerance", "moderate")
    context_manager.store_preference("technical", "preferred_timeframe", "4h")
    context_manager.store_preference("onchain", "min_transfer_threshold", 1000000)
    
    print("✓ Stored preferences for agents")
    
    # Retrieve preferences
    risk_tolerance = context_manager.get_preference("technical", "risk_tolerance")
    timeframe = context_manager.get_preference("technical", "preferred_timeframe")
    
    print(f"\n✓ Technical analyst preferences:")
    print(f"  - Risk tolerance: {risk_tolerance}")
    print(f"  - Preferred timeframe: {timeframe}")


def example_get_all_context():
    """Example: Get all context for an agent."""
    print("\n" + "=" * 60)
    print("Example 6: Getting All Context for an Agent")
    print("=" * 60)
    
    context_manager = AgentContextManager(base_dir="agent-context")
    
    # Get all context
    all_context = context_manager.get_all_context("technical")
    
    print(f"✓ Retrieved all context for technical analyst:")
    print(f"  - Knowledge entries: {len(all_context['knowledge'])}")
    print(f"  - API configurations: {len(all_context['apis'])}")
    print(f"  - Tool configurations: {len(all_context['tools'])}")
    print(f"  - Preferences: {len(all_context['preferences'])}")


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("Agent Context Manager and Tool Registry Examples")
    print("=" * 60 + "\n")
    
    # Run examples
    example_store_knowledge()
    example_store_api()
    example_use_tools()
    example_query_context()
    example_store_preferences()
    example_get_all_context()
    
    print("\n" + "=" * 60)
    print("Examples completed!")
    print("=" * 60 + "\n")

