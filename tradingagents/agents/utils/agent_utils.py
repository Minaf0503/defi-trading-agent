from langchain_core.messages import BaseMessage, HumanMessage, ToolMessage, AIMessage
from typing import List, Optional
from typing import Annotated
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import RemoveMessage
from langchain_core.tools import tool
from datetime import date, timedelta, datetime
import functools
import pandas as pd
import os
import json
from dateutil.relativedelta import relativedelta
from langchain_openai import ChatOpenAI
from tradingagents.dataflows.crypto_utils import CryptoDataProvider, OnchainAnalytics
from tradingagents.dataflows.rss_utils import (
    fetch_dlnews_rss,
    fetch_article_content,
    filter_articles_by_asset,
    filter_articles_by_date
)
from tradingagents.default_config import DEFAULT_CONFIG
from langchain_core.messages import HumanMessage
from tradingagents.agents.utils.context_manager import AgentContextManager
from tradingagents.agents.utils.tool_registry import ToolRegistry


def create_msg_delete():
    def delete_messages(state):
        """Clear messages and add placeholder for Anthropic compatibility"""
        messages = state["messages"]
        
        # Remove all messages
        removal_operations = [RemoveMessage(id=m.id) for m in messages]
        
        # Add a minimal placeholder message
        placeholder = HumanMessage(content="Continue")
        
        return {"messages": removal_operations + [placeholder]}
    
    return delete_messages


class Toolkit:
    _config = DEFAULT_CONFIG.copy()

    @classmethod
    def update_config(cls, config):
        """Update the class-level configuration."""
        cls._config.update(config)

    @property
    def config(self):
        """Access the configuration."""
        return self._config

    def __init__(self, config=None):
        if config:
            self.update_config(config)
        
        # Initialize context manager and tool registry
        context_dir = config.get("agent_context_dir", "agent-context") if config else "agent-context"
        self.context_manager = AgentContextManager(base_dir=context_dir, config=config)
        self.tool_registry = ToolRegistry(context_manager=self.context_manager)

    # DeFi/Crypto-specific tools
    @staticmethod
    @tool
    def get_crypto_price_data(
        token_symbol: Annotated[str, "Token symbol (e.g., BTC, ETH, UNI)"],
        vs_currency: Annotated[str, "Quote currency (e.g., USD, EUR)"] = "usd",
    ):
        """
        Get current crypto price data from CoinGecko
        Args:
            token_symbol (str): Token symbol (e.g., BTC, ETH, UNI)
            vs_currency (str): Quote currency (e.g., USD, EUR)
        Returns:
            str: Current price data and market metrics
        """
        crypto_provider = CryptoDataProvider()
        market_data = crypto_provider.get_crypto_market_data(token_symbol)
        
        if "error" in market_data.get("price_data", {}):
            return f"Error getting price data for {token_symbol}: {market_data['price_data']['error']}"
        
        price_data = market_data["price_data"]
        return f"Price data for {token_symbol}: {json.dumps(price_data, indent=2)}"

    @staticmethod
    @tool
    def get_crypto_technical_indicators(
        token_symbol: Annotated[str, "Token symbol (e.g., BTC, ETH, UNI)"],
    ):
        """
        Get technical indicators for crypto token
        Args:
            token_symbol (str): Token symbol (e.g., BTC, ETH, UNI)
        Returns:
            str: Technical analysis data
        """
        crypto_provider = CryptoDataProvider()
        technical_data = crypto_provider.get_crypto_technical_analysis(token_symbol)
        
        if "error" in technical_data:
            return f"Error getting technical data for {token_symbol}: {technical_data['error']}"
        
        return f"Technical analysis for {token_symbol}: {json.dumps(technical_data, indent=2)}"

    @staticmethod
    @tool
    def get_crypto_market_metrics(
        token_symbol: Annotated[str, "Token symbol (e.g., BTC, ETH, UNI)"],
    ):
        """
        Get comprehensive market metrics for crypto token
        Args:
            token_symbol (str): Token symbol (e.g., BTC, ETH, UNI)
        Returns:
            str: Market metrics data
        """
        crypto_provider = CryptoDataProvider()
        market_data = crypto_provider.get_crypto_market_data(token_symbol)
        
        if "error" in market_data.get("market_data", {}):
            return f"Error getting market data for {token_symbol}: {market_data['market_data']['error']}"
        
        return f"Market metrics for {token_symbol}: {json.dumps(market_data['market_data'], indent=2)}"

    @staticmethod
    @tool
    def get_crypto_volume_analysis(
        token_symbol: Annotated[str, "Token symbol (e.g., BTC, ETH, UNI)"],
    ):
        """
        Get volume analysis for crypto token
        Args:
            token_symbol (str): Token symbol (e.g., BTC, ETH, UNI)
        Returns:
            str: Volume analysis data
        """
        crypto_provider = CryptoDataProvider()
        market_data = crypto_provider.get_crypto_market_data(token_symbol)
        
        if "error" in market_data.get("price_data", {}):
            return f"Error getting volume data for {token_symbol}: {market_data['price_data']['error']}"
        
        price_data = market_data["price_data"]
        volume_24h = price_data.get("usd_24h_vol", 0)
        market_cap = price_data.get("usd_market_cap", 0)
        
        return f"Volume analysis for {token_symbol}: 24h Volume: ${volume_24h:,.0f}, Market Cap: ${market_cap:,.0f}"

    @staticmethod
    @tool
    def get_onchain_liquidity_data(
        token_address: Annotated[str, "Token contract address"],
        network: Annotated[str, "Blockchain network (e.g., ethereum, polygon)"] = "ethereum",
    ):
        """
        Get onchain liquidity data for token
        Args:
            token_address (str): Token contract address
            network (str): Blockchain network
        Returns:
            str: Liquidity analysis data
        """
        onchain_analytics = OnchainAnalytics(network)
        liquidity_data = onchain_analytics.analyze_liquidity_metrics(token_address)
        
        if "error" in liquidity_data:
            return f"Error getting liquidity data: {liquidity_data['error']}"
        
        return f"Liquidity analysis: {json.dumps(liquidity_data, indent=2)}"

    @staticmethod
    @tool
    def get_onchain_holder_data(
        token_address: Annotated[str, "Token contract address"],
        network: Annotated[str, "Blockchain network (e.g., ethereum, polygon)"] = "ethereum",
    ):
        """
        Get onchain holder data for token
        Args:
            token_address (str): Token contract address
            network (str): Blockchain network
        Returns:
            str: Holder analysis data
        """
        onchain_analytics = OnchainAnalytics(network)
        holder_data = onchain_analytics.analyze_holder_metrics(token_address)
        
        if "error" in holder_data:
            return f"Error getting holder data: {holder_data['error']}"
        
        return f"Holder analysis: {json.dumps(holder_data, indent=2)}"

    @staticmethod
    @tool
    def get_onchain_transaction_data(
        token_address: Annotated[str, "Token contract address"],
        network: Annotated[str, "Blockchain network (e.g., ethereum, polygon)"] = "ethereum",
    ):
        """
        Get onchain transaction data for token
        Args:
            token_address (str): Token contract address
            network (str): Blockchain network
        Returns:
            str: Transaction analysis data
        """
        onchain_analytics = OnchainAnalytics(network)
        transaction_data = onchain_analytics.analyze_transaction_metrics(token_address)
        
        if "error" in transaction_data:
            return f"Error getting transaction data: {transaction_data['error']}"
        
        return f"Transaction analysis: {json.dumps(transaction_data, indent=2)}"

    @staticmethod
    @tool
    def get_onchain_supply_data(
        token_address: Annotated[str, "Token contract address"],
        network: Annotated[str, "Blockchain network (e.g., ethereum, polygon)"] = "ethereum",
    ):
        """
        Get onchain supply data for token
        Args:
            token_address (str): Token contract address
            network (str): Blockchain network
        Returns:
            str: Supply analysis data
        """
        onchain_analytics = OnchainAnalytics(network)
        onchain_data = onchain_analytics.get_token_onchain_data(token_address)
        
        if "error" in onchain_data:
            return f"Error getting supply data: {onchain_data['error']}"
        
        supply_data = onchain_data.get("supply", {})
        return f"Supply analysis: {json.dumps(supply_data, indent=2)}"

    @staticmethod
    @tool
    def get_defi_protocol_data(
        protocol: Annotated[str, "DeFi protocol name (e.g., uniswap, aave, compound)"],
    ):
        """
        Get DeFi protocol data
        Args:
            protocol (str): DeFi protocol name
        Returns:
            str: Protocol analysis data
        """
        crypto_provider = CryptoDataProvider()
        protocol_data = crypto_provider.get_defi_protocol_analysis(protocol)
        
        if "error" in protocol_data:
            return f"Error getting protocol data for {protocol}: {protocol_data['error']}"
        
        return f"Protocol analysis for {protocol}: {json.dumps(protocol_data, indent=2)}"

    @staticmethod
    @tool
    def get_defi_yield_data(
        protocol: Annotated[str, "DeFi protocol name (e.g., uniswap, aave, compound)"],
    ):
        """
        Get DeFi yield opportunities
        Args:
            protocol (str): DeFi protocol name
        Returns:
            str: Yield analysis data
        """
        crypto_provider = CryptoDataProvider()
        protocol_data = crypto_provider.get_defi_protocol_analysis(protocol)
        
        if "error" in protocol_data:
            return f"Error getting yield data for {protocol}: {protocol_data['error']}"
        
        return f"Yield analysis for {protocol}: {json.dumps(protocol_data, indent=2)}"

    @staticmethod
    @tool
    def get_defi_tvl_data(
        protocol: Annotated[str, "DeFi protocol name (e.g., uniswap, aave, compound)"],
    ):
        """
        Get DeFi TVL data
        Args:
            protocol (str): DeFi protocol name
        Returns:
            str: TVL analysis data
        """
        crypto_provider = CryptoDataProvider()
        protocol_data = crypto_provider.get_defi_protocol_analysis(protocol)
        
        if "error" in protocol_data:
            return f"Error getting TVL data for {protocol}: {protocol_data['error']}"
        
        tvl = protocol_data.get("tvl", 0)
        tvl_change_1d = protocol_data.get("tvl_change_1d", 0)
        tvl_change_7d = protocol_data.get("tvl_change_7d", 0)
        
        return f"TVL analysis for {protocol}: Current TVL: ${tvl:,.0f}, 1d change: {tvl_change_1d:.2f}%, 7d change: {tvl_change_7d:.2f}%"

    @staticmethod
    @tool
    def get_defi_governance_data(
        protocol: Annotated[str, "DeFi protocol name (e.g., uniswap, aave, compound)"],
    ):
        """
        Get DeFi governance data
        Args:
            protocol (str): DeFi protocol name
        Returns:
            str: Governance analysis data
        """
        crypto_provider = CryptoDataProvider()
        protocol_data = crypto_provider.get_defi_protocol_analysis(protocol)
        
        if "error" in protocol_data:
            return f"Error getting governance data for {protocol}: {protocol_data['error']}"
        
        return f"Governance analysis for {protocol}: {json.dumps(protocol_data, indent=2)}"

    @staticmethod
    @tool
    def get_defi_risk_data(
        protocol: Annotated[str, "DeFi protocol name (e.g., uniswap, aave, compound)"],
    ):
        """
        Get DeFi risk assessment
        Args:
            protocol (str): DeFi protocol name
        Returns:
            str: Risk analysis data
        """
        crypto_provider = CryptoDataProvider()
        protocol_data = crypto_provider.get_defi_protocol_analysis(protocol)
        
        if "error" in protocol_data:
            return f"Error getting risk data for {protocol}: {protocol_data['error']}"
        
        return f"Risk analysis for {protocol}: {json.dumps(protocol_data, indent=2)}"

    @staticmethod
    @tool
    def get_dlnews_rss_feed(
        token_symbol: Annotated[str, "Token symbol (e.g., BTC, ETH, UNI)"],
        token_name: Annotated[Optional[str], "Optional token name (e.g., Bitcoin, Ethereum)"] = None,
        days_back: Annotated[int, "Number of days to look back for articles"] = 7,
    ):
        """
        Fetch and filter articles from DL News RSS feed for a specific token.
        DL News is a credible DeFi news source: https://www.dlnews.com/rss/
        
        Args:
            token_symbol (str): Token symbol to filter for
            token_name (str): Optional token name to filter for
            days_back (int): Number of days to look back
        
        Returns:
            str: JSON string of filtered articles with titles, links, summaries, and dates
        """
        try:
            articles = fetch_dlnews_rss(
                asset_symbol=token_symbol,
                asset_name=token_name,
                days_back=days_back
            )
            
            if not articles:
                return f"No articles found for {token_symbol} in DL News RSS feed (last {days_back} days)"
            
            # Format articles for output
            formatted_articles = []
            for article in articles:
                formatted_articles.append({
                    "title": article.get("title", ""),
                    "link": article.get("link", ""),
                    "summary": article.get("summary", "")[:500],  # Limit summary length
                    "published": article.get("published", ""),
                    "tags": article.get("tags", [])
                })
            
            return f"Found {len(formatted_articles)} articles for {token_symbol} from DL News:\n{json.dumps(formatted_articles, indent=2)}"
        
        except Exception as e:
            return f"Error fetching DL News RSS feed for {token_symbol}: {str(e)}"

    @staticmethod
    @tool
    def analyze_article_sentiment(
        article_url: Annotated[str, "URL of the article to analyze"],
        token_symbol: Annotated[str, "Token symbol being analyzed"],
    ):
        """
        Fetch and analyze the sentiment of a news article for a specific token.
        
        Args:
            article_url (str): URL of the article
            token_symbol (str): Token symbol being analyzed
        
        Returns:
            str: Analysis of article sentiment and key points
        """
        try:
            # Fetch article content
            content = fetch_article_content(article_url)
            
            if not content:
                return f"Could not fetch article content from {article_url}"
            
            # Limit content length for analysis
            content_preview = content[:3000] if len(content) > 3000 else content
            
            # Return structured information for LLM analysis
            return f"""Article URL: {article_url}
Token: {token_symbol}

Article Content (preview):
{content_preview}

Please analyze this article for:
1. Overall sentiment (bullish/bearish/neutral) regarding {token_symbol}
2. Key points and themes
3. Potential impact on {token_symbol}
4. Risk factors mentioned
5. Recommendations or predictions mentioned
"""
        
        except Exception as e:
            return f"Error analyzing article from {article_url}: {str(e)}"

    @staticmethod
    @tool
    def get_crypto_news_sentiment(
        token_symbol: Annotated[str, "Token symbol (e.g., BTC, ETH, UNI)"],
        token_name: Annotated[Optional[str], "Optional token name"] = None,
        days_back: Annotated[int, "Number of days to look back"] = 7,
    ):
        """
        Get comprehensive news sentiment analysis for a token from DL News RSS feed.
        Fetches articles, filters for the token, and provides sentiment summary.
        
        Args:
            token_symbol (str): Token symbol
            token_name (str): Optional token name
            days_back (int): Number of days to look back
        
        Returns:
            str: Comprehensive sentiment analysis based on news articles
        """
        try:
            # Fetch articles
            articles = fetch_dlnews_rss(
                asset_symbol=token_symbol,
                asset_name=token_name,
                days_back=days_back
            )
            
            if not articles:
                return f"No news articles found for {token_symbol} in DL News (last {days_back} days). This may indicate low news coverage or neutral sentiment."
            
            # Format articles summary
            articles_summary = []
            for article in articles[:10]:  # Limit to top 10 articles
                articles_summary.append({
                    "title": article.get("title", ""),
                    "link": article.get("link", ""),
                    "summary": article.get("summary", "")[:300],
                    "published": article.get("published", "")
                })
            
            summary = f"""Found {len(articles)} articles for {token_symbol} from DL News (last {days_back} days):

Articles Summary:
{json.dumps(articles_summary, indent=2)}

Please analyze these articles to provide:
1. Overall sentiment trend (bullish/bearish/neutral)
2. Key themes and narratives
3. Positive and negative factors mentioned
4. Potential impact on {token_symbol}
5. Risk factors identified
6. Trading recommendation based on sentiment (BUY/HOLD/SELL)
"""
            
            return summary
        
        except Exception as e:
            return f"Error getting news sentiment for {token_symbol}: {str(e)}"
    
    def get_agent_tools(self, agent_name: str, base_tools: List = None) -> List:
        """
        Get all tools for a specific agent, including base tools, context tools, and API tools.
        
        Args:
            agent_name: Name of the agent
            base_tools: Optional list of base tools to include
        
        Returns:
            List of all tools for the agent
        """
        # Get base tools from this toolkit
        if base_tools is None:
            base_tools = [
                self.get_crypto_price_data,
                self.get_crypto_technical_indicators,
                self.get_crypto_market_metrics,
                self.get_crypto_volume_analysis,
                self.get_onchain_liquidity_data,
                self.get_onchain_holder_data,
                self.get_onchain_transaction_data,
                self.get_onchain_supply_data,
                self.get_defi_protocol_data,
                self.get_defi_yield_data,
                self.get_defi_tvl_data,
                self.get_defi_governance_data,
                self.get_defi_risk_data,
            ]
        
        # Setup agent tools with context and API tools
        return self.tool_registry.setup_agent_tools(
            agent_name=agent_name,
            context_manager=self.context_manager,
            base_tools=base_tools
        )

