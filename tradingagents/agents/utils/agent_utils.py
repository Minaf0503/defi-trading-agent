from langchain_core.messages import BaseMessage, HumanMessage, ToolMessage, AIMessage
from typing import List
from typing import Annotated
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import RemoveMessage
from langchain_core.tools import tool
from datetime import date, timedelta, datetime
import functools
import pandas as pd
import os
from dateutil.relativedelta import relativedelta
from langchain_openai import ChatOpenAI
from tradingagents.dataflows.crypto_utils import CryptoDataProvider, OnchainAnalytics
from tradingagents.default_config import DEFAULT_CONFIG
from langchain_core.messages import HumanMessage


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

