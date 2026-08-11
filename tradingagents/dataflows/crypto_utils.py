"""
Crypto-specific data utilities for DeFi Trading Agents
Uses crypto price oracles (CoinGecko, DefiLlama) for market data. On-chain
data (liquidity, supply, holders) lives in tradingagents/dataflows/onchain/ --
see that package's modules, not this file.
"""

import requests
import json
from typing import Dict, List, Optional, Annotated
from datetime import datetime, timedelta, date
import pandas as pd
from pathlib import Path
import os

from tradingagents.dataflows.historical_data import HistoricalDataCache
from tradingagents.dataflows.onchain.block_resolver import resolve_block_for_date
from tradingagents.dataflows.onchain.token_data import get_token_supply

# Yahoo Finance tickers, mirrored from experiments/config.py's
# EXPERIMENT_TOKENS (kept local rather than imported, since
# tradingagents/dataflows/ should not depend on the experiments/ package).
HISTORICAL_YAHOO_TICKERS = {
    # Original panel
    "BTC":  "BTC-USD",
    "ETH":  "ETH-USD",
    "SOL":  "SOL-USD",
    "UNI":  "UNI7083-USD",
    "AAVE": "AAVE-USD",
    "ZEC":  "ZEC-USD",
    "XMR":  "XMR-USD",
    # FC27 panel additions (Tier 1)
    "WBTC": "WBTC-USD",
    "LINK": "LINK-USD",
    "MKR":  "MKR-USD",
    "CRV":  "CRV-USD",
    # FC27 panel additions (Tier 2 — limited history, post-launch dates only)
    "PEPE": "PEPE24478-USD",   # launched April 2023
    "ONDO": "ONDO-USD",        # Yahoo data from ~April 2024 (token launched Jan 2024)
    "ENA":  "ENA-USD",         # Yahoo data from ~June 2024 (token launched April 2024)
}

# Real on-chain ERC20.totalSupply() (UNI, AAVE) covers native-token supply
# exactly. BTC/ETH/SOL have no on-chain RPC source for *native*-asset supply
# in this project (WBTC/WETH's totalSupply() is the wrapped-token supply, a
# small fraction of the real asset's -- see get_onchain_supply_data's
# docstring) -- these are well-known circulating-supply figures as of
# 2022-01-01, held static across the whole backtest window as a disclosed
# approximation (real BTC/ETH/SOL supply grows ~2-4% over 2022-2025; this
# matters for the tier/order-of-magnitude market cap shown to the LLM, not
# for any of this project's actual financial calculations, which use real
# on-chain liquidity/sizing, not historical market cap). ZEC/XMR have no
# historical price or supply source found in this project's tooling --
# market cap is reported as unavailable for them, consistent with their
# role as the panel's deliberate non-EVM negative case.
_STATIC_CIRCULATING_SUPPLY = {
    "BTC": 18_932_556,
    "ETH": 118_549_000,
    "SOL": 297_500_000,
}

# Crypto price oracle APIs
class CryptoPriceOracle:
    """Crypto price oracle integration"""
    
    def __init__(self):
        self.coingecko_api = "https://api.coingecko.com/api/v3"
        self.binance_api = "https://api.binance.com/api/v3"
        self.defillama_api = "https://api.llama.fi"
        
    def get_token_price_coingecko(self, token_id: str, vs_currency: str = "usd") -> Dict:
        """Get token price from CoinGecko"""
        try:
            url = f"{self.coingecko_api}/simple/price"
            params = {
                "ids": token_id,
                "vs_currencies": vs_currency,
                "include_24hr_change": "true",
                "include_market_cap": "true",
                "include_24hr_vol": "true"
            }
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": f"CoinGecko API error: {str(e)}"}
    
    def get_token_market_data(self, token_id: str) -> Dict:
        """Get comprehensive market data from CoinGecko"""
        try:
            url = f"{self.coingecko_api}/coins/{token_id}"
            params = {
                "localization": "false",
                "tickers": "false",
                "market_data": "true",
                "community_data": "true",
                "developer_data": "true",
                "sparkline": "false"
            }
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": f"CoinGecko market data error: {str(e)}"}
    
    def get_token_price_history(self, token_id: str, days: int = 30, vs_currency: str = "usd") -> Dict:
        """Get historical price data"""
        try:
            url = f"{self.coingecko_api}/coins/{token_id}/market_chart"
            params = {
                "vs_currency": vs_currency,
                "days": days
            }
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": f"CoinGecko history error: {str(e)}"}
    
    def get_defi_protocol_data(self, protocol: str) -> Dict:
        """Get DeFi protocol data from DefiLlama"""
        try:
            url = f"{self.defillama_api}/protocol/{protocol}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": f"DefiLlama API error: {str(e)}"}

class CryptoDataProvider:
    """Main crypto data provider combining multiple sources"""

    def __init__(self, network: str = "ethereum"):
        self.network = network
        self.price_oracle = CryptoPriceOracle()

    def get_crypto_market_data(self, token_symbol: str) -> Dict:
        """Get comprehensive crypto market data"""
        # Map common symbols to CoinGecko IDs
        symbol_to_id = {
            "BTC": "bitcoin",
            "ETH": "ethereum",
            "USDC": "usd-coin",
            "USDT": "tether",
            "DAI": "dai",
            "UNI": "uniswap",
            "LINK": "chainlink",
            "AAVE": "aave",
            "COMP": "compound-governance-token",
            "CRV": "curve-dao-token",
            "SUSHI": "sushi",
            "YFI": "yearn-finance",
            "BAL": "balancer",
            "SNX": "havven",
            "MKR": "maker",
            "REN": "republic-protocol",
            "BAND": "band-protocol",
            "ZRX": "0x",
            "BAT": "basic-attention-token",
            "REP": "augur",
        }
        
        token_id = symbol_to_id.get(token_symbol.upper(), token_symbol.lower())
        
        # Get price data
        price_data = self.price_oracle.get_token_price_coingecko(token_id)
        market_data = self.price_oracle.get_token_market_data(token_id)
        price_history = self.price_oracle.get_token_price_history(token_id, days=30)

        return {
            "symbol": token_symbol,
            "token_id": token_id,
            "price_data": price_data,
            "market_data": market_data,
            "price_history": price_history,
        }
    
    def get_crypto_technical_analysis(self, token_symbol: str) -> Dict:
        """Get technical analysis for crypto"""
        token_id = token_symbol.lower()
        
        # Get price history for technical analysis
        price_history = self.price_oracle.get_token_price_history(token_id, days=90)
        
        if "error" in price_history:
            return price_history
        
        # Calculate technical indicators
        prices = price_history.get("prices", [])
        if not prices:
            return {"error": "No price data available"}
        
        # Convert to DataFrame for analysis
        df = pd.DataFrame(prices, columns=["timestamp", "price"])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
        df.set_index("timestamp", inplace=True)
        
        # Calculate moving averages
        df["sma_20"] = df["price"].rolling(window=20).mean()
        df["sma_50"] = df["price"].rolling(window=50).mean()
        df["ema_12"] = df["price"].ewm(span=12).mean()
        df["ema_26"] = df["price"].ewm(span=26).mean()
        
        # Calculate RSI
        delta = df["price"].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        df["rsi"] = 100 - (100 / (1 + rs))
        
        # Calculate Bollinger Bands
        df["bb_middle"] = df["price"].rolling(window=20).mean()
        bb_std = df["price"].rolling(window=20).std()
        df["bb_upper"] = df["bb_middle"] + (bb_std * 2)
        df["bb_lower"] = df["bb_middle"] - (bb_std * 2)
        
        # Calculate MACD
        df["macd"] = df["ema_12"] - df["ema_26"]
        df["macd_signal"] = df["macd"].ewm(span=9).mean()
        df["macd_histogram"] = df["macd"] - df["macd_signal"]
        
        # Get latest values
        latest = df.iloc[-1]
        
        return {
            "current_price": latest["price"],
            "sma_20": latest["sma_20"],
            "sma_50": latest["sma_50"],
            "rsi": latest["rsi"],
            "bb_upper": latest["bb_upper"],
            "bb_middle": latest["bb_middle"],
            "bb_lower": latest["bb_lower"],
            "macd": latest["macd"],
            "macd_signal": latest["macd_signal"],
            "macd_histogram": latest["macd_histogram"],
            "price_data": df.tail(30).to_dict("records")
        }
    
    def get_historical_crypto_snapshot(self, token_symbol: str, as_of_date: str) -> Dict:
        """Point-in-time equivalent of get_crypto_market_data +
        get_crypto_technical_analysis, sourced from real cached Yahoo
        Finance OHLCV (Phase 1's existing 2022-01-01..2025-06-30 panel) --
        no look-ahead, since the trailing window always ends at as_of_date.

        Market cap uses real on-chain supply (UNI, AAVE) or a static
        well-known circulating-supply figure (BTC, ETH, SOL); see
        _STATIC_CIRCULATING_SUPPLY's comment for the disclosed caveat.
        ZEC/XMR have no historical price source -- returns an explicit
        "not available" rather than a fabricated number.
        """
        symbol = token_symbol.upper()
        yahoo_ticker = HISTORICAL_YAHOO_TICKERS.get(symbol)
        if yahoo_ticker is None:
            return {"error": f"No historical price source configured for {symbol}"}

        as_of = as_of_date if isinstance(as_of_date, date) else date.fromisoformat(as_of_date)
        window_start = as_of - timedelta(days=180)  # >90 trading days of buffer for indicator warmup

        cache = HistoricalDataCache()
        df = cache.get(symbol, yahoo_ticker, datetime.combine(window_start, datetime.min.time()), datetime.combine(as_of, datetime.min.time()), source="yahoo")
        if df.empty:
            return {"error": f"No historical OHLCV available for {symbol} as of {as_of_date}"}

        df = df.rename(columns={"close": "price"}).set_index("timestamp")

        df["sma_20"] = df["price"].rolling(window=20).mean()
        df["sma_50"] = df["price"].rolling(window=50).mean()
        df["ema_12"] = df["price"].ewm(span=12).mean()
        df["ema_26"] = df["price"].ewm(span=26).mean()

        delta = df["price"].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        df["rsi"] = 100 - (100 / (1 + rs))

        df["bb_middle"] = df["price"].rolling(window=20).mean()
        bb_std = df["price"].rolling(window=20).std()
        df["bb_upper"] = df["bb_middle"] + (bb_std * 2)
        df["bb_lower"] = df["bb_middle"] - (bb_std * 2)

        df["macd"] = df["ema_12"] - df["ema_26"]
        df["macd_signal"] = df["macd"].ewm(span=9).mean()
        df["macd_histogram"] = df["macd"] - df["macd_signal"]

        latest = df.iloc[-1]
        prev = df.iloc[-2] if len(df) > 1 else latest
        price_change_24h_pct = ((latest["price"] - prev["price"]) / prev["price"] * 100) if prev["price"] else None

        market_cap, market_cap_note = self._historical_market_cap(symbol, as_of, float(latest["price"]))

        return {
            "symbol": symbol,
            "as_of_date": str(as_of),
            "current_price": float(latest["price"]),
            "price_change_24h_pct": price_change_24h_pct,
            "volume_24h": float(latest["volume"]),
            "market_cap": market_cap,
            "market_cap_note": market_cap_note,
            "sma_20": float(latest["sma_20"]) if pd.notna(latest["sma_20"]) else None,
            "sma_50": float(latest["sma_50"]) if pd.notna(latest["sma_50"]) else None,
            "rsi": float(latest["rsi"]) if pd.notna(latest["rsi"]) else None,
            "bb_upper": float(latest["bb_upper"]) if pd.notna(latest["bb_upper"]) else None,
            "bb_middle": float(latest["bb_middle"]) if pd.notna(latest["bb_middle"]) else None,
            "bb_lower": float(latest["bb_lower"]) if pd.notna(latest["bb_lower"]) else None,
            "macd": float(latest["macd"]) if pd.notna(latest["macd"]) else None,
            "macd_signal": float(latest["macd_signal"]) if pd.notna(latest["macd_signal"]) else None,
            "macd_histogram": float(latest["macd_histogram"]) if pd.notna(latest["macd_histogram"]) else None,
            "data_source": "Yahoo Finance (cached historical OHLCV, no look-ahead)",
        }

    @staticmethod
    def _historical_market_cap(symbol: str, as_of: date, price: float):
        if symbol in ("UNI", "AAVE"):
            try:
                block = resolve_block_for_date(as_of)
                supply_data = get_token_supply(symbol, block=block)
                if supply_data.get("available"):
                    supply = supply_data["total_supply"]
                    return price * supply, f"real on-chain totalSupply() at block {block} ({as_of})"
            except Exception as e:
                return None, f"on-chain supply lookup failed: {e}"
        if symbol in _STATIC_CIRCULATING_SUPPLY:
            supply = _STATIC_CIRCULATING_SUPPLY[symbol]
            return price * supply, "static circulating-supply estimate, not point-in-time (see code comment)"
        return None, f"no historical supply source configured for {symbol}"

    def get_defi_protocol_analysis(self, protocol: str) -> Dict:
        """Analyze DeFi protocol data"""
        protocol_data = self.price_oracle.get_defi_protocol_data(protocol)
        
        if "error" in protocol_data:
            return protocol_data
        
        # Extract key metrics
        tvl = protocol_data.get("tvl", 0)
        tvl_change_1d = protocol_data.get("change_1d", 0)
        tvl_change_7d = protocol_data.get("change_7d", 0)
        
        return {
            "protocol": protocol,
            "tvl": tvl,
            "tvl_change_1d": tvl_change_1d,
            "tvl_change_7d": tvl_change_7d,
            "protocol_data": protocol_data
        } 