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
from tradingagents.dataflows.crypto_utils import CryptoDataProvider
from tradingagents.dataflows.onchain.token_data import get_token_supply as fetch_token_supply
from tradingagents.dataflows.onchain.venues import SpotDEXVenue
from tradingagents.dataflows.onchain.block_resolver import resolve_block_for_date
from tradingagents.dataflows.onchain.dune_api import execute_query as dune_execute_query, DuneError
from tradingagents.dataflows.onchain.contracts import ERC20_TOKENS, UNISWAP_V3_POOLS
from tradingagents.dataflows.technical_indicators import compute_technical_snapshot
from tradingagents.dataflows.rss_utils import (
    fetch_crypto_news_rss,
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
        Get crypto price data. Live mode: current data from CoinGecko.
        Historical-backtest mode (Toolkit._config["as_of_date"] set): real
        cached Yahoo Finance OHLCV as of that date, no look-ahead.
        Args:
            token_symbol (str): Token symbol (e.g., BTC, ETH, UNI)
            vs_currency (str): Quote currency (e.g., USD, EUR)
        Returns:
            str: Price data and market metrics
        """
        as_of_date = Toolkit._config.get("as_of_date")
        crypto_provider = CryptoDataProvider()
        if as_of_date:
            snapshot = crypto_provider.get_historical_crypto_snapshot(token_symbol, as_of_date)
            if "error" in snapshot:
                return f"Error getting historical price data for {token_symbol} as of {as_of_date}: {snapshot['error']}"
            return f"Price data for {token_symbol} as of {as_of_date} (historical, no look-ahead): {json.dumps(snapshot, indent=2)}"

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
        Get technical indicators for crypto token. Live mode: current data
        from CoinGecko. Historical-backtest mode (Toolkit._config["as_of_date"]
        set): real cached Yahoo Finance OHLCV as of that date, no look-ahead.
        Args:
            token_symbol (str): Token symbol (e.g., BTC, ETH, UNI)
        Returns:
            str: Technical analysis data
        """
        as_of_date = Toolkit._config.get("as_of_date")
        crypto_provider = CryptoDataProvider()
        if as_of_date:
            snapshot = crypto_provider.get_historical_crypto_snapshot(token_symbol, as_of_date)
            if "error" in snapshot:
                return f"Error getting historical technical data for {token_symbol} as of {as_of_date}: {snapshot['error']}"
            return f"Technical analysis for {token_symbol} as of {as_of_date} (historical, no look-ahead): {json.dumps(snapshot, indent=2)}"

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
        Get comprehensive market metrics for crypto token. Live mode:
        current data from CoinGecko. Historical-backtest mode
        (Toolkit._config["as_of_date"] set): real cached Yahoo Finance OHLCV
        price combined with real on-chain supply (UNI, AAVE) or a static
        circulating-supply estimate (BTC, ETH, SOL) for market cap -- see
        CryptoDataProvider.get_historical_crypto_snapshot's docstring.
        Args:
            token_symbol (str): Token symbol (e.g., BTC, ETH, UNI)
        Returns:
            str: Market metrics data
        """
        as_of_date = Toolkit._config.get("as_of_date")
        crypto_provider = CryptoDataProvider()
        if as_of_date:
            snapshot = crypto_provider.get_historical_crypto_snapshot(token_symbol, as_of_date)
            if "error" in snapshot:
                return f"Error getting historical market data for {token_symbol} as of {as_of_date}: {snapshot['error']}"
            return f"Market metrics for {token_symbol} as of {as_of_date} (historical, no look-ahead): {json.dumps(snapshot, indent=2)}"

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
        Get volume analysis for crypto token. Live mode: current data from
        CoinGecko. Historical-backtest mode (Toolkit._config["as_of_date"]
        set): real cached Yahoo Finance OHLCV as of that date, no look-ahead.
        Args:
            token_symbol (str): Token symbol (e.g., BTC, ETH, UNI)
        Returns:
            str: Volume analysis data
        """
        as_of_date = Toolkit._config.get("as_of_date")
        crypto_provider = CryptoDataProvider()
        if as_of_date:
            snapshot = crypto_provider.get_historical_crypto_snapshot(token_symbol, as_of_date)
            if "error" in snapshot:
                return f"Error getting historical volume data for {token_symbol} as of {as_of_date}: {snapshot['error']}"
            volume_24h = snapshot.get("volume_24h")
            market_cap = snapshot.get("market_cap")
            mc_str = f"${market_cap:,.0f}" if market_cap is not None else f"not available ({snapshot.get('market_cap_note')})"
            return f"Volume analysis for {token_symbol} as of {as_of_date} (historical, no look-ahead): 24h Volume: ${volume_24h:,.0f}, Market Cap: {mc_str}"

        market_data = crypto_provider.get_crypto_market_data(token_symbol)
        if "error" in market_data.get("price_data", {}):
            return f"Error getting volume data for {token_symbol}: {market_data['price_data']['error']}"
        price_data = market_data["price_data"]
        volume_24h = price_data.get("usd_24h_vol", 0)
        market_cap = price_data.get("usd_market_cap", 0)
        return f"Volume analysis for {token_symbol}: 24h Volume: ${volume_24h:,.0f}, Market Cap: ${market_cap:,.0f}"

    @staticmethod
    @tool
    def get_deterministic_technical_analysis(
        token_symbol: Annotated[str, "Token symbol (e.g., BTC, ETH, UNI, AAVE)"],
    ):
        """
        Compute a full deterministic technical analysis snapshot from historical daily OHLCV data.
        All indicators are computed in Python — the LLM must interpret, never recompute.

        Covers (Gaps 1–9):
          - Trend: EMA 8/21/50/200, EMA alignment, ADX/+DI/-DI, trend regime
          - Momentum: RSI-7/14 (adaptive period), StochRSI K/D, MACD line/signal/histogram/crossover, ROC-14
          - Volatility: ATR-14, ATR%, 30d hist vol, Bollinger Bands (upper/mid/lower/width/%B), BB squeeze, vol regime
          - Volume: OBV trend, 20d VWAP, volume ratio vs 20d avg, volume spike flag
          - Market structure: 20/50 support/resistance, pivot points (P/R1/R2/S1/S2), swing HH/HL detection
          - Candle patterns: doji, hammer, engulfing, pin bar
          - Weekly HTF bias: derived by resampling daily → weekly
          - BTC relative strength: 30d return differential vs BTC (for non-BTC tokens)
          - Pre-computed signal score, bias (STRONG_BULL/BULL/NEUTRAL/BEAR/STRONG_BEAR), conviction (0-1),
            conflicting signals list, regime warning

        Params are auto-adapted to 30d realised volatility so high-vol DeFi tokens
        don't produce noisy signals with equity-default RSI-14 / MACD 12-26-9.

        Returns: JSON snapshot with all indicators pre-computed. Use the signal_bias and
        conviction fields as your starting directional view and explain the WHY from
        the indicator values — do not recompute anything.
        """
        from tradingagents.dataflows.historical_data import HistoricalDataCache
        from tradingagents.dataflows.crypto_utils import HISTORICAL_YAHOO_TICKERS

        symbol = token_symbol.upper()
        yahoo_ticker = HISTORICAL_YAHOO_TICKERS.get(symbol)
        if yahoo_ticker is None:
            return f"No historical price source configured for {symbol}. Supported: {', '.join(HISTORICAL_YAHOO_TICKERS)}."

        as_of_date = Toolkit._config.get("as_of_date")
        try:
            if as_of_date:
                from datetime import date as _date, timedelta as _td
                end_dt = _date.fromisoformat(str(as_of_date))
            else:
                from datetime import date as _date, timedelta as _td
                end_dt = _date.today()
            start_dt = end_dt - _td(days=420)  # 420 cal days ≈ 400+ crypto bars — enough for EMA-200
            cache = HistoricalDataCache()
            df = cache.get(
                symbol, yahoo_ticker,
                datetime.combine(start_dt, datetime.min.time()),
                datetime.combine(end_dt, datetime.min.time()),
                source="yahoo",
            )
            if df.empty or len(df) < 60:
                return f"Insufficient historical data for {symbol} (got {len(df)} bars, need ≥ 60)."

            # Fetch BTC for relative-strength computation when token is not BTC
            btc_df = None
            if symbol not in ("BTC", "WBTC"):
                try:
                    btc_df = cache.get(
                        "BTC", "BTC-USD",
                        datetime.combine(start_dt, datetime.min.time()),
                        datetime.combine(end_dt, datetime.min.time()),
                        source="yahoo",
                    )
                    if btc_df.empty:
                        btc_df = None
                except Exception:
                    btc_df = None

            snapshot = compute_technical_snapshot(df, symbol, btc_df=btc_df)
            caveat = f" CAVEAT: as_of_date={as_of_date} (historical backtest, no look-ahead)." if as_of_date else ""
            return (
                f"Deterministic technical analysis for {symbol} ({len(df)} daily bars):{caveat}\n"
                f"{json.dumps(snapshot, indent=2)}"
            )
        except Exception as e:
            return f"Error computing deterministic technical analysis for {symbol}: {str(e)}"

    @staticmethod
    @tool
    def get_4h_technical_analysis(
        token_symbol: Annotated[str, "Token symbol (e.g., ETH, UNI, AAVE)"],
    ):
        """
        Compute a deterministic technical analysis snapshot on 4-hour candles built
        from on-chain DEX VWAP prices (Dune query 7822415, prices.hour).

        Complements get_deterministic_technical_analysis (daily) with an intraday
        timeframe. All the same indicator categories are returned: trend (EMA ribbon,
        ADX), momentum (RSI, StochRSI, MACD), volatility (ATR, BB), market structure
        (S/R, pivot points), candle patterns, and pre-computed signal_bias / conviction.

        NOTE: Volume is near-zero in prices.hour; OBV and volume_ratio signals are
        unreliable at this timeframe — weight price-based indicators only.

        Returns a JSON snapshot in the same format as get_deterministic_technical_analysis
        but labelled timeframe='4H'. Use alongside the daily snapshot for timeframe
        confluence: daily sets directional bias, 4H identifies entry timing.
        """
        from tradingagents.dataflows.onchain.contracts import ERC20_TOKENS

        symbol = token_symbol.upper()
        token = ERC20_TOKENS.get(symbol)
        if token is None:
            return f"No ERC20 address configured for {symbol}. Supported: {', '.join(ERC20_TOKENS)}."

        as_of_date = Toolkit._config.get("as_of_date")
        try:
            from datetime import date as _date, timedelta as _td
            import pandas as pd

            end_dt = _date.fromisoformat(str(as_of_date)) if as_of_date else _date.today()
            start_dt = end_dt - _td(days=90)  # 90 days × 6 candles/day = ~540 4H bars

            address = token["address"].lower()
            result = dune_execute_query(
                7822415,
                params={
                    "token_address": address,
                    "start_date": f"TIMESTAMP '{start_dt.isoformat()}'",
                    "end_date":   f"TIMESTAMP '{end_dt.isoformat()}'",
                },
            )
            rows = result.get("rows", [])
            if len(rows) < 60:
                return f"Insufficient 4H data for {symbol} ({len(rows)} candles returned, need ≥60)."

            df = pd.DataFrame(rows)
            df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)
            df = df.sort_values("timestamp").reset_index(drop=True)
            # Ensure numeric columns
            for col in ["open", "high", "low", "close", "volume"]:
                df[col] = pd.to_numeric(df[col], errors="coerce")
            # Fill any NaN volume with 0 (prices.hour volume is often 0)
            df["volume"] = df["volume"].fillna(0).replace(0, 1e-9)
            df = df.set_index("timestamp")

            snapshot = compute_technical_snapshot(df, symbol, btc_df=None)
            snapshot["timeframe"] = "4H"
            snapshot["data_bars_used"] = len(df)
            snapshot["volume_note"] = "prices.hour volume is near-zero; OBV/volume_ratio unreliable — use price indicators only"

            caveat = f" CAVEAT: as_of_date={as_of_date} (historical backtest, no look-ahead)." if as_of_date else ""
            return (
                f"4H technical analysis for {symbol} ({len(df)} candles, {start_dt} to {end_dt}):{caveat}\n"
                f"{json.dumps(snapshot, indent=2)}"
            )
        except DuneError as e:
            return f"Dune error fetching 4H candles for {symbol}: {str(e)}"
        except Exception as e:
            return f"Error computing 4H technical analysis for {symbol}: {str(e)}"

    @staticmethod
    @tool
    def get_eth_btc_ratio():
        """
        Fetch the daily ETH/BTC price ratio for the past 35 days (Dune query 7822417).
        Prices sourced from on-chain DEX trades (WETH / WBTC on Ethereum).

        Returns: daily ETH/BTC ratio with 7-day and 30-day percentage change.

        Interpretation guide (for the LLM):
          - Rising ratio (7d/30d change > 0): ETH outperforming BTC — altcoin-friendly
            macro, favourable for DeFi tokens.
          - Falling ratio: BTC dominance rising — risk-off rotation, generally headwind
            for altcoins.
          - Sustained move > +10% in 30d: altcoin season signal.
          - Sustained move < -10% in 30d: BTC dominance surge, reduce altcoin exposure.
        """
        as_of_date = Toolkit._config.get("as_of_date")
        try:
            from datetime import date as _date, timedelta as _td

            end_dt = _date.fromisoformat(str(as_of_date)) if as_of_date else _date.today()
            start_dt = end_dt - _td(days=65)  # extra buffer so LAG(30) has data

            result = dune_execute_query(
                7822417,
                params={
                    "start_date": f"TIMESTAMP '{start_dt.isoformat()}'",
                    "end_date":   f"TIMESTAMP '{end_dt.isoformat()}'",
                },
            )
            rows = result.get("rows", [])
            if not rows:
                return "No ETH/BTC ratio data returned from Dune."

            caveat = f" CAVEAT: as_of_date={as_of_date} (historical backtest, no look-ahead)." if as_of_date else ""
            return (
                f"ETH/BTC ratio — last {len(rows)} days:{caveat}\n"
                f"{json.dumps(rows, indent=2)}"
            )
        except DuneError as e:
            return f"Dune error fetching ETH/BTC ratio: {str(e)}"
        except Exception as e:
            return f"Error fetching ETH/BTC ratio: {str(e)}"

    @staticmethod
    @tool
    def get_peer_relative_strength(
        token_symbol: Annotated[str, "Token symbol (e.g., ETH, UNI, AAVE)"],
        days_back:    Annotated[int, "Lookback window in days (default 30)"] = 30,
    ):
        """
        Fetch indexed price performance of a token vs DeFi peers (ETH, UNI, AAVE)
        over a lookback window (Dune query 7822418, prices.hour aggregated daily).

        All assets are indexed to 0% at the start of the window. Returns daily
        cumulative return for each asset and the token's alpha vs each peer.

        Columns:
          token_perf_pct / eth_perf_pct / uni_perf_pct / aave_perf_pct:
            cumulative % return since window start
          vs_eth_alpha_pct / vs_uni_alpha_pct / vs_aave_alpha_pct:
            token's outperformance (+) or underperformance (-) vs that peer

        NOTE: When the queried token IS one of the peers (e.g. querying UNI), that
        peer's column will be NULL — the token is already captured as token_price.
        """
        from tradingagents.dataflows.onchain.contracts import ERC20_TOKENS

        symbol = token_symbol.upper()
        token = ERC20_TOKENS.get(symbol)
        if token is None:
            return f"No ERC20 address configured for {symbol}. Supported: {', '.join(ERC20_TOKENS)}."

        as_of_date = Toolkit._config.get("as_of_date")
        try:
            from datetime import date as _date, timedelta as _td

            end_dt = _date.fromisoformat(str(as_of_date)) if as_of_date else _date.today()
            start_dt = end_dt - _td(days=days_back)

            address = token["address"].lower()
            result = dune_execute_query(
                7822418,
                params={
                    "token_address": address,
                    "start_date": f"TIMESTAMP '{start_dt.isoformat()}'",
                    "end_date":   f"TIMESTAMP '{end_dt.isoformat()}'",
                },
            )
            rows = result.get("rows", [])
            if not rows:
                return f"No peer relative strength data returned for {symbol}."

            # Summary row (most recent day = first row since ORDER BY day DESC)
            latest = rows[0]
            summary = {
                "as_of": latest.get("day", ""),
                "token_perf_pct":    latest.get("token_perf_pct"),
                "eth_perf_pct":      latest.get("eth_perf_pct"),
                "uni_perf_pct":      latest.get("uni_perf_pct"),
                "aave_perf_pct":     latest.get("aave_perf_pct"),
                "vs_eth_alpha_pct":  latest.get("vs_eth_alpha_pct"),
                "vs_uni_alpha_pct":  latest.get("vs_uni_alpha_pct"),
                "vs_aave_alpha_pct": latest.get("vs_aave_alpha_pct"),
            }

            caveat = f" CAVEAT: as_of_date={as_of_date} (historical backtest, no look-ahead)." if as_of_date else ""
            return (
                f"Peer relative strength for {symbol} ({days_back}d window, {start_dt} to {end_dt}):{caveat}\n"
                f"SUMMARY (latest day): {json.dumps(summary, indent=2)}\n"
                f"DAILY SERIES: {json.dumps(rows, indent=2)}"
            )
        except DuneError as e:
            return f"Dune error fetching peer relative strength for {symbol}: {str(e)}"
        except Exception as e:
            return f"Error fetching peer relative strength for {symbol}: {str(e)}"

    @staticmethod
    @tool
    def get_onchain_liquidity_data(
        token_symbol: Annotated[str, "Token symbol, e.g. ETH, BTC, UNI, AAVE"],
    ):
        """
        Get real on-chain DEX liquidity for a token, read directly via RPC
        from its Uniswap v3 pool (no third-party data API). Configured pools:
        ETH (WETH/USDC), UNI (UNI/WETH), AAVE (AAVE/WETH) -- BTC, SOL, ZEC,
        XMR have no real liquidity venue here (BTC/WBTC has supply data only;
        SOL/ZEC/XMR are non-EVM and are kept in the experiment panel as a
        deliberate negative case for this exact graceful-degradation path,
        not an oversight -- see BUILD_PLAN.md token-selection-criteria entry).
        Returns:
            str: Pool state (price, liquidity, tick) or an explicit
            "not configured" message for other tokens.
        """
        pool_by_token = {"ETH": "WETH/USDC", "UNI": "UNI/WETH", "AAVE": "AAVE/WETH"}
        pool_key = pool_by_token.get(token_symbol.upper())
        if pool_key is None:
            return (
                f"No on-chain liquidity pool configured for {token_symbol} "
                f"(configured: {', '.join(pool_by_token)}). This is a real "
                f"limitation, not an error -- say so rather than guessing a number."
            )
        try:
            as_of_date = Toolkit._config.get("as_of_date")
            block = resolve_block_for_date(as_of_date) if as_of_date else None
            venue = SpotDEXVenue(pool_key)
            state = venue.get_state(block=block)
            label = f"as of {as_of_date} (block {block}, historical, no look-ahead)" if as_of_date else "current"
            liquidity_note = (
                "IMPORTANT: the 'liquidity' field below is Uniswap v3's abstract "
                "virtual-reserve unit (sqrt-price-scale), NOT a token balance and "
                "NOT denominated in either pool token -- do not describe it as "
                "'X WETH' or 'X UNI' etc. It is only meaningful as a relative "
                "comparison (e.g. this pool's liquidity now vs. earlier, or vs. "
                "another pool), not as an absolute token or dollar amount."
            )
            return f"On-chain liquidity (Uniswap v3, direct RPC, {label}): {json.dumps(state, indent=2)}\n\n{liquidity_note}"
        except Exception as e:
            return f"Error getting on-chain liquidity data: {str(e)}"

    @staticmethod
    @tool
    def get_onchain_holder_data(
        token_symbol: Annotated[str, "Token symbol, e.g. ETH, BTC, UNI, AAVE"],
    ):
        """
        Get holder concentration / whale data for a token via a saved Dune
        Analytics query (holder distribution needs an indexer scanning full
        transfer history -- not cheap via direct RPC). Requires DUNE_API_KEY
        and DUNE_HOLDER_QUERY_ID in .env; the query itself has to be authored
        once by hand in Dune's free web UI (Dune's API can execute a saved
        query on the free tier, but creating one via API needs a paid plan).
        Returns:
            str: Holder data, or a clear message if Dune isn't configured.
        """
        import os as _os

        query_id = _os.getenv("DUNE_HOLDER_QUERY_ID")
        if not query_id:
            return (
                "Holder data unavailable: DUNE_HOLDER_QUERY_ID not set in .env. "
                "Say so plainly rather than fabricating holder/whale data."
            )
        token = ERC20_TOKENS.get(token_symbol.upper())
        if token is None:
            return f"Holder data not available: {token_symbol} has no Ethereum mainnet ERC20 address tracked in this project."
        try:
            address_hex = token["address"].lower().removeprefix("0x")
            result = dune_execute_query(int(query_id), params={"token_address": address_hex})
            as_of_date = Toolkit._config.get("as_of_date")
            caveat = (
                f" CAVEAT: this query has no date filter and reflects CURRENT state, "
                f"not the simulated historical date ({as_of_date}) -- treat as a current-state "
                f"reference point only, not point-in-time evidence."
                if as_of_date else ""
            )
            return f"Holder data (Dune query {query_id}):{caveat} {json.dumps(result['rows'], indent=2)}"
        except Exception as e:
            return f"Error getting holder data: {str(e)}"

    @staticmethod
    @tool
    def get_onchain_transaction_data(
        token_symbol: Annotated[str, "Token symbol, e.g. ETH, BTC, UNI, AAVE"],
    ):
        """
        Get DEX transaction/volume data for a token via a saved Dune
        Analytics query. Requires DUNE_API_KEY and DUNE_VOLUME_QUERY_ID in
        .env -- see get_onchain_holder_data for why this can't be fully
        self-serve like the CoinGecko/Yahoo/Fear&Greed tools.
        Returns:
            str: Transaction/volume data, or a clear message if unconfigured.
        """
        import os as _os

        query_id = _os.getenv("DUNE_VOLUME_QUERY_ID")
        if not query_id:
            return (
                "Transaction/volume data unavailable: DUNE_VOLUME_QUERY_ID not set "
                "in .env. Say so plainly rather than fabricating volume data."
            )
        token = ERC20_TOKENS.get(token_symbol.upper())
        if token is None:
            return f"Transaction data not available: {token_symbol} has no Ethereum mainnet ERC20 address tracked in this project."
        try:
            address_hex = token["address"].lower().removeprefix("0x")
            result = dune_execute_query(int(query_id), params={"token_address": address_hex, "days_back": 7})
            as_of_date = Toolkit._config.get("as_of_date")
            caveat = (
                f" CAVEAT: this query has no date filter and reflects the CURRENT trailing "
                f"7 days, not the simulated historical date ({as_of_date}) -- treat as a "
                f"current-state reference point only, not point-in-time evidence."
                if as_of_date else ""
            )
            return f"Transaction data (Dune query {query_id}):{caveat} {json.dumps(result['rows'], indent=2)}"
        except Exception as e:
            return f"Error getting transaction data: {str(e)}"

    @staticmethod
    @tool
    def get_onchain_supply_data(
        token_symbol: Annotated[str, "Token symbol, e.g. ETH, BTC, UNI, AAVE"],
    ):
        """
        Get real on-chain total supply for a token via a direct
        ERC20.totalSupply() RPC call (no third-party data API). Only works
        for tokens with a tracked Ethereum mainnet ERC20 address (BTC via
        WBTC, ETH via WETH, UNI, AAVE) -- SOL/ZEC/XMR have none.
        Returns:
            str: Supply data, or an explicit "not available" message.
        """
        try:
            as_of_date = Toolkit._config.get("as_of_date")
            block = resolve_block_for_date(as_of_date) if as_of_date else None
            supply_data = fetch_token_supply(token_symbol, block=block)
            if not supply_data.get("available"):
                return f"Supply data not available: {supply_data.get('reason')}"
            label = f"as of {as_of_date} (block {block}, historical, no look-ahead)" if as_of_date else "current"
            return f"On-chain supply (direct RPC, {label}): {json.dumps(supply_data, indent=2)}"
        except Exception as e:
            return f"Error getting supply data: {str(e)}"

    @staticmethod
    @tool
    def get_dex_volume_flow_quality(
        token_symbol: Annotated[str, "Token symbol, e.g. ETH, BTC, UNI, AAVE"],
    ):
        """
        Module 1: DEX Volume & Flow Quality via Dune query 7811692.
        Provides DEX volume metrics and flow quality signals, including buy/sell
        pressure, volume composition, and organic vs. wash-trade indicators.
        Params passed to Dune: token_address (0x-prefixed varbinary), target_date (TIMESTAMP literal).
        Returns:
            str: DEX volume and flow quality data, or a clear error message.
        """
        from datetime import date as _date
        token = ERC20_TOKENS.get(token_symbol.upper())
        if token is None:
            return f"DEX volume/flow data not available: {token_symbol} has no Ethereum mainnet ERC20 address tracked in this project."
        try:
            as_of_date = Toolkit._config.get("as_of_date")
            date_str = str(as_of_date) if as_of_date else _date.today().isoformat()
            # Dune substitutes directly into SQL; address needs 0x prefix for varbinary literal,
            # date needs TIMESTAMP '...' for Trino date arithmetic.
            address = token["address"].lower()
            target_date = f"TIMESTAMP '{date_str}'"
            result = dune_execute_query(7811692, params={"token_address": address, "target_date": target_date})
            caveat = f" CAVEAT: target_date={date_str} (simulated historical date)." if as_of_date else ""
            return f"DEX Volume & Flow Quality (Dune query 7811692, date={date_str}):{caveat} {json.dumps(result['rows'], indent=2)}"
        except DuneError as e:
            return f"Dune error getting DEX volume/flow quality data: {str(e)}"
        except Exception as e:
            return f"Error getting DEX volume/flow quality data: {str(e)}"

    @staticmethod
    @tool
    def get_liquidity_depth_slippage(
        token_symbol: Annotated[str, "Token symbol, e.g. ETH, UNI, AAVE"],
    ):
        """
        Module 2: Liquidity Depth & Slippage Estimation via Dune query 7812804.
        Provides on-chain liquidity depth metrics and estimated slippage for
        various trade sizes across DEX pools. Uses the token's primary Uniswap
        v3 pool address (ETH→WETH/USDC, UNI→UNI/WETH, AAVE→AAVE/WETH).
        Params passed to Dune: pool_address (0x-prefixed varbinary).
        Returns:
            str: Liquidity depth and slippage data, or a clear error message.
        """
        _TOKEN_TO_POOL = {"ETH": "WETH/USDC", "UNI": "UNI/WETH", "AAVE": "AAVE/WETH"}
        pool_key = _TOKEN_TO_POOL.get(token_symbol.upper())
        if pool_key is None:
            return (
                f"Liquidity depth data not available: no Uniswap v3 pool configured for {token_symbol} "
                f"(configured: {', '.join(_TOKEN_TO_POOL)})."
            )
        try:
            pool_address = UNISWAP_V3_POOLS[pool_key]["address"].lower()
            result = dune_execute_query(7812804, params={"pool_address": pool_address})
            as_of_date = Toolkit._config.get("as_of_date")
            caveat = (
                f" CAVEAT: this query reflects current pool state, not the simulated historical date ({as_of_date})."
                if as_of_date else ""
            )
            return f"Liquidity Depth & Slippage Estimation (Dune query 7812804, pool={pool_key}):{caveat} {json.dumps(result['rows'], indent=2)}"
        except DuneError as e:
            return f"Dune error getting liquidity depth/slippage data: {str(e)}"
        except Exception as e:
            return f"Error getting liquidity depth/slippage data: {str(e)}"

    @staticmethod
    @tool
    def get_holder_concentration_whale_activity(
        token_symbol: Annotated[str, "Token symbol, e.g. ETH, BTC, UNI, AAVE"],
    ):
        """
        Module 3: Holder Concentration & Whale Activity via Dune query 7812812.
        Provides holder concentration metrics, top holder rankings, whale wallet
        movements, and accumulation/distribution patterns.
        Params passed to Dune: token_address (0x-prefixed varbinary), target_date (TIMESTAMP literal).
        NOTE: query 7812812 has a SQL bug (semicolon between M3A and M3B sub-queries);
        will fail until the query is fixed in Dune to remove the semicolon.
        Returns:
            str: Holder concentration and whale activity data, or a clear error message.
        """
        from datetime import date as _date
        token = ERC20_TOKENS.get(token_symbol.upper())
        if token is None:
            return f"Holder concentration data not available: {token_symbol} has no Ethereum mainnet ERC20 address tracked in this project."
        try:
            as_of_date = Toolkit._config.get("as_of_date")
            date_str = str(as_of_date) if as_of_date else _date.today().isoformat()
            address = token["address"].lower()
            target_date = f"TIMESTAMP '{date_str}'"
            result = dune_execute_query(7812812, params={"token_address": address, "target_date": target_date})
            caveat = f" CAVEAT: target_date={date_str} (simulated historical date)." if as_of_date else ""
            return f"Holder Concentration & Whale Activity (Dune query 7812812, date={date_str}):{caveat} {json.dumps(result['rows'], indent=2)}"
        except DuneError as e:
            return f"Dune error getting holder concentration/whale data: {str(e)}"
        except Exception as e:
            return f"Error getting holder concentration/whale data: {str(e)}"

    @staticmethod
    @tool
    def get_mev_execution_risk(
        token_symbol: Annotated[str, "Token symbol, e.g. ETH, BTC, UNI, AAVE"],
    ):
        """
        Module 4: MEV & Execution Risk Scoring via Dune query 7812866.
        Provides MEV exposure metrics, sandwich attack frequency, front-running
        indicators, and execution risk scores for the token's DEX activity.
        Params passed to Dune: token_address (0x-prefixed varbinary), target_date (TIMESTAMP literal).
        Returns:
            str: MEV and execution risk data, or a clear error message.
        """
        from datetime import date as _date
        token = ERC20_TOKENS.get(token_symbol.upper())
        if token is None:
            return f"MEV/execution risk data not available: {token_symbol} has no Ethereum mainnet ERC20 address tracked in this project."
        try:
            as_of_date = Toolkit._config.get("as_of_date")
            date_str = str(as_of_date) if as_of_date else _date.today().isoformat()
            address = token["address"].lower()
            target_date = f"TIMESTAMP '{date_str}'"
            result = dune_execute_query(7812866, params={"token_address": address, "target_date": target_date})
            caveat = f" CAVEAT: target_date={date_str} (simulated historical date)." if as_of_date else ""
            return f"MEV & Execution Risk Scoring (Dune query 7812866, date={date_str}):{caveat} {json.dumps(result['rows'], indent=2)}"
        except DuneError as e:
            return f"Dune error getting MEV/execution risk data: {str(e)}"
        except Exception as e:
            return f"Error getting MEV/execution risk data: {str(e)}"

    @staticmethod
    @tool
    def get_cross_protocol_leverage_pressure(
        token_symbol: Annotated[str, "Token symbol, e.g. ETH, BTC, UNI, AAVE"],
    ):
        """
        Module 5: Cross-Protocol Leverage Pressure via Dune query 7812868.
        Provides cross-protocol leverage metrics including lending protocol
        borrow rates, collateralization ratios, liquidation risk, and
        aggregate leverage pressure on the token.
        Params passed to Dune: token_address (0x-prefixed varbinary), target_date (TIMESTAMP literal).
        Returns:
            str: Cross-protocol leverage pressure data, or a clear error message.
        """
        from datetime import date as _date
        token = ERC20_TOKENS.get(token_symbol.upper())
        if token is None:
            return f"Leverage pressure data not available: {token_symbol} has no Ethereum mainnet ERC20 address tracked in this project."
        try:
            as_of_date = Toolkit._config.get("as_of_date")
            date_str = str(as_of_date) if as_of_date else _date.today().isoformat()
            address = token["address"].lower()
            target_date = f"TIMESTAMP '{date_str}'"
            result = dune_execute_query(7812868, params={"token_address": address, "target_date": target_date})
            caveat = f" CAVEAT: target_date={date_str} (simulated historical date)." if as_of_date else ""
            return f"Cross-Protocol Leverage Pressure (Dune query 7812868, date={date_str}):{caveat} {json.dumps(result['rows'], indent=2)}"
        except DuneError as e:
            return f"Dune error getting cross-protocol leverage data: {str(e)}"
        except Exception as e:
            return f"Error getting cross-protocol leverage data: {str(e)}"

    @staticmethod
    @tool
    def get_contamination_instrument_data(
        token_symbol: Annotated[str, "Token symbol, e.g. ETH, BTC, UNI, AAVE"],
        days_back: Annotated[int, "Lookback window in days (start_date = end_date - days_back)"] = 7,
    ):
        """
        Module 6: Contamination Instrument Data Pull via Dune query 7812879.
        Pulls daily DEX VWAP and directional flow for the token -- a deterministic
        historical ground truth useful for contamination baseline scoring.
        Params passed to Dune: token_address (0x-prefixed varbinary),
        start_date and end_date (TIMESTAMP literals).
        Returns:
            str: Contamination instrument data, or a clear error message.
        """
        from datetime import date as _date, timedelta as _timedelta
        token = ERC20_TOKENS.get(token_symbol.upper())
        if token is None:
            return f"Contamination instrument data not available: {token_symbol} has no Ethereum mainnet ERC20 address tracked in this project."
        try:
            as_of_date = Toolkit._config.get("as_of_date")
            end_dt = _date.fromisoformat(str(as_of_date)) if as_of_date else _date.today()
            start_dt = end_dt - _timedelta(days=days_back)
            address = token["address"].lower()
            start_date = f"TIMESTAMP '{start_dt.isoformat()}'"
            end_date = f"TIMESTAMP '{end_dt.isoformat()}'"
            result = dune_execute_query(7812879, params={"token_address": address, "start_date": start_date, "end_date": end_date})
            caveat = f" CAVEAT: end_date={end_dt} (simulated historical date)." if as_of_date else ""
            return f"Contamination Instrument Data (Dune query 7812879, {start_dt} to {end_dt}):{caveat} {json.dumps(result['rows'], indent=2)}"
        except DuneError as e:
            return f"Dune error getting contamination instrument data: {str(e)}"
        except Exception as e:
            return f"Error getting contamination instrument data: {str(e)}"

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
    def get_defillama_tvl(
        protocol_slug: Annotated[
            str,
            "DefiLlama protocol slug (e.g. 'uniswap-v3', 'aave-v3', 'lido', 'makerdao', 'curve-dex'). "
            "Common mappings: UNI→uniswap-v3, AAVE→aave-v3, ETH staking→lido.",
        ],
    ):
        """
        Fetch historical and current TVL for a DeFi protocol from DefiLlama
        (https://api.llama.fi/protocol/{slug}).

        Returns:
          - Current TVL with 1h / 1d / 7d / 30d percentage changes
          - mcap/TVL ratio (lower = more undervalued vs. protocol usage)
          - Per-chain TVL breakdown (top 5 chains)
          - Top tokens held in the protocol (by USD value)
          - 30-day daily TVL trend

        TVL momentum signals (for the LLM to apply):
          Rising TVL + rising price  → fundamental confirmation
          Falling TVL + rising price → price/TVL divergence (bearish)
          Falling TVL + falling price → capital flight
          Rising TVL + falling price → accumulation / TVL-led recovery

        In backtest mode (as_of_date set), the 30d trend is trimmed to
        as_of_date so the LLM only sees data available at that point in time.
        """
        import requests

        slug = protocol_slug.lower().strip()
        as_of_date = Toolkit._config.get("as_of_date")

        try:
            resp = requests.get(f"https://api.llama.fi/protocol/{slug}", timeout=15)
            if resp.status_code == 404:
                return (
                    f"Protocol '{slug}' not found on DefiLlama. "
                    "Browse slugs at https://defillama.com/protocols"
                )
            resp.raise_for_status()
            data = resp.json()

            name     = data.get("name", slug)
            symbol   = data.get("symbol", "")
            category = data.get("category", "")
            chain    = data.get("chain", "")
            mcap     = data.get("mcap")

            # Per-chain TVL breakdown → current total
            chain_tvls = data.get("currentChainTvls", {})
            total_tvl  = sum(chain_tvls.values()) if chain_tvls else 0
            if not total_tvl:
                series_last = (data.get("tvl") or [{}])[-1]
                total_tvl   = series_last.get("totalLiquidityUSD", 0)

            change_1h = data.get("change_1h")
            change_1d = data.get("change_1d")
            change_7d = data.get("change_7d")

            top_chains = [
                {"chain": c, "tvl_usd": round(v)}
                for c, v in sorted(chain_tvls.items(), key=lambda x: x[1], reverse=True)[:5]
            ]

            # 30-day TVL trend, trimmed to as_of_date in backtest mode
            tvl_series = data.get("tvl") or []
            if as_of_date:
                from datetime import date as _date
                cutoff_ts = int(_date.fromisoformat(str(as_of_date)).strftime("%s"))
                tvl_series = [e for e in tvl_series if e.get("date", 0) <= cutoff_ts]

            trend_30d = [
                {"date": e.get("date"), "tvl_usd": round(e.get("totalLiquidityUSD", 0))}
                for e in tvl_series[-30:]
            ]

            tvl_30d_ago = tvl_series[-30].get("totalLiquidityUSD") if len(tvl_series) >= 30 else None
            change_30d  = (
                round((total_tvl / tvl_30d_ago - 1) * 100, 2) if tvl_30d_ago else None
            )

            # Top tokens held
            tokens_usd_series = data.get("tokensInUsd") or []
            if as_of_date and tokens_usd_series:
                tokens_usd_series = [
                    e for e in tokens_usd_series
                    if e.get("date", 0) <= int(_date.fromisoformat(str(as_of_date)).strftime("%s"))
                ]
            latest_tokens = (tokens_usd_series[-1].get("tokens") or {}) if tokens_usd_series else {}
            top_tokens = [
                {"token": k, "usd": round(v)}
                for k, v in sorted(latest_tokens.items(), key=lambda x: x[1], reverse=True)[:8]
            ]

            snapshot = {
                "protocol":         name,
                "symbol":           symbol,
                "category":         category,
                "primary_chain":    chain,
                "tvl_usd":          round(total_tvl),
                "change_1h_pct":    round(change_1h, 2) if change_1h is not None else None,
                "change_1d_pct":    round(change_1d, 2) if change_1d is not None else None,
                "change_7d_pct":    round(change_7d, 2) if change_7d is not None else None,
                "change_30d_pct":   change_30d,
                "mcap_usd":         round(mcap) if mcap else None,
                "mcap_tvl_ratio":   round(mcap / total_tvl, 3) if (mcap and total_tvl) else None,
                "top_chains":       top_chains,
                "top_tokens_held":  top_tokens,
                "tvl_30d_trend":    trend_30d,
            }
            caveat = f" CAVEAT: as_of_date={as_of_date} — trend trimmed to that date." if as_of_date else ""
            return (
                f"DefiLlama TVL for {name} ({slug}):{caveat}\n"
                f"{json.dumps(snapshot, indent=2)}"
            )
        except requests.exceptions.Timeout:
            return f"Timeout fetching DefiLlama TVL for '{slug}'"
        except Exception as e:
            return f"Error fetching DefiLlama TVL for '{slug}': {str(e)}"

    @staticmethod
    @tool
    def get_dexscreener_flow(
        token_symbol: Annotated[str, "Token symbol (e.g., ETH, UNI, AAVE)"],
    ):
        """
        Fetch real-time DEX buy/sell flow and liquidity for a token from DexScreener
        (https://api.dexscreener.com/token-pairs/v1/ethereum/{address}).

        Aggregates across ALL active Ethereum DEX pairs for the token:
          - buys / sells / buy_ratio over m5, h1, h6, h24
          - total swap volume per window
          - total liquidity across all pairs
          - top 5 pairs by liquidity with per-pair buy ratio

        buy_ratio = buys / (buys + sells):
          > 0.60 → strong buy pressure (accumulation)
          0.45–0.60 → balanced / neutral
          < 0.40 → strong sell pressure (distribution)

        h1 buy_ratio diverging from h24 signals a recent shift in flow direction.
        High volume + high buy_ratio = conviction buying.
        High volume + low buy_ratio = conviction selling / exit.

        NOTE: DexScreener only covers DEX spot trading; no perpetuals/CEX data.
        Use get_perpetuals_data for futures-market sentiment.
        """
        import requests
        from tradingagents.dataflows.onchain.contracts import ERC20_TOKENS

        symbol = token_symbol.upper()
        token  = ERC20_TOKENS.get(symbol)
        if token is None:
            return f"No ERC20 address configured for {symbol}. Supported: {', '.join(ERC20_TOKENS)}."

        address = token["address"].lower()
        try:
            resp = requests.get(
                f"https://api.dexscreener.com/token-pairs/v1/ethereum/{address}",
                timeout=15,
            )
            resp.raise_for_status()
            pairs = resp.json()
            if not pairs:
                return f"No DEX pairs found for {symbol} on Ethereum via DexScreener."

            # Active = has h24 volume
            active = [p for p in pairs if (p.get("volume") or {}).get("h24", 0) > 0] or pairs

            # Aggregate flow across all active pairs
            agg = {tf: {"buys": 0, "sells": 0, "volume_usd": 0.0} for tf in ("m5", "h1", "h6", "h24")}
            total_liquidity = 0.0
            for p in active:
                txns   = p.get("txns") or {}
                volume = p.get("volume") or {}
                total_liquidity += (p.get("liquidity") or {}).get("usd", 0) or 0
                for tf in ("m5", "h1", "h6", "h24"):
                    agg[tf]["buys"]       += (txns.get(tf) or {}).get("buys", 0)
                    agg[tf]["sells"]      += (txns.get(tf) or {}).get("sells", 0)
                    agg[tf]["volume_usd"] += (volume.get(tf) or 0)

            flow = {}
            for tf, d in agg.items():
                total_txns = d["buys"] + d["sells"]
                flow[tf] = {
                    "buys":       d["buys"],
                    "sells":      d["sells"],
                    "total_txns": total_txns,
                    "buy_ratio":  round(d["buys"] / total_txns, 3) if total_txns else None,
                    "volume_usd": round(d["volume_usd"]),
                }

            # Top 5 pairs by liquidity
            top5 = sorted(active, key=lambda p: (p.get("liquidity") or {}).get("usd", 0) or 0, reverse=True)[:5]
            top_pairs = []
            for p in top5:
                h24_txns  = (p.get("txns") or {}).get("h24") or {}
                b, s      = h24_txns.get("buys", 0), h24_txns.get("sells", 0)
                top_pairs.append({
                    "pair":             (p.get("baseToken") or {}).get("symbol", "") + "/" + (p.get("quoteToken") or {}).get("symbol", ""),
                    "dex":              p.get("dexId", ""),
                    "price_usd":        p.get("priceUsd"),
                    "liquidity_usd":    (p.get("liquidity") or {}).get("usd"),
                    "volume_h24_usd":   (p.get("volume") or {}).get("h24"),
                    "h24_buy_ratio":    round(b / (b + s), 3) if (b + s) > 0 else None,
                    "price_change_h24_pct": (p.get("priceChange") or {}).get("h24"),
                })

            ref_price = top5[0].get("priceUsd") if top5 else None
            result = {
                "token":                symbol,
                "price_usd":            ref_price,
                "total_liquidity_usd":  round(total_liquidity),
                "active_pairs_count":   len(active),
                "flow_by_timeframe":    flow,
                "top_pairs":            top_pairs,
            }
            return (
                f"DexScreener DEX flow for {symbol} ({len(active)} active pairs, Ethereum):\n"
                f"{json.dumps(result, indent=2)}"
            )
        except requests.exceptions.Timeout:
            return f"Timeout fetching DexScreener data for {symbol}"
        except Exception as e:
            return f"Error fetching DexScreener flow for {symbol}: {str(e)}"

    @staticmethod
    @tool
    def get_binance_perpetuals(
        token_symbol: Annotated[str, "Token symbol (e.g., BTC, ETH, SOL, UNI, AAVE)"],
    ):
        """
        Fetch perpetual futures market data from OKX public API (no auth required).
        Data is sourced from OKX (source-agnostic naming retained for compatibility).

        Returns three signal categories:

        FUNDING RATE (last 8 settlements ≈ last 2.67 days at 8h intervals):
          Positive → longs pay shorts → market is net long / bullish bias
          Negative → shorts pay longs → market is net short / bearish bias
          |annualized rate| > 36% → extreme funding, often precedes mean-reversion
          current_rate_annualized_pct provided for easy cross-asset comparison

        OPEN INTEREST — current (contracts + USD) + 7-day daily trend:
          OI ↑ + price ↑ → strong uptrend (new capital entering longs)
          OI ↑ + price ↓ → short buildup (bearish pressure building)
          OI ↓ + price ↑ → short squeeze / weak rally (no new long conviction)
          OI ↓ + price ↓ → capitulation / deleveraging (selling exhaustion)

        LONG/SHORT RATIO — hourly last 24h (top-trader account ratio):
          ratio > 1.5 → crowded long — contrarian downside risk
          ratio < 0.7 → crowded short — potential squeeze setup
        """
        import requests

        # OKX USDT-margined perpetual instrument IDs
        OKX_INST = {
            "BTC":   "BTC-USDT-SWAP",
            "ETH":   "ETH-USDT-SWAP",
            "SOL":   "SOL-USDT-SWAP",
            "UNI":   "UNI-USDT-SWAP",
            "AAVE":  "AAVE-USDT-SWAP",
            "BNB":   "BNB-USDT-SWAP",
            "ARB":   "ARB-USDT-SWAP",
            "OP":    "OP-USDT-SWAP",
            "LINK":  "LINK-USDT-SWAP",
            "MATIC": "MATIC-USDT-SWAP",
        }

        symbol  = token_symbol.upper()
        inst_id = OKX_INST.get(symbol)
        if inst_id is None:
            return (
                f"No OKX perpetual configured for {symbol}. "
                f"Supported: {', '.join(OKX_INST)}."
            )

        base = "https://www.okx.com"
        ccy  = symbol  # base currency for rubik endpoints

        try:
            def get(path, params):
                r = requests.get(f"{base}{path}", params=params, timeout=12)
                r.raise_for_status()
                body = r.json()
                if body.get("code") != "0":
                    raise ValueError(f"OKX error {body.get('code')}: {body.get('msg')}")
                return body["data"]

            funding_hist = get("/api/v5/public/funding-rate-history",
                               {"instId": inst_id, "limit": 8})
            funding_now  = get("/api/v5/public/funding-rate",
                               {"instId": inst_id})
            oi_now       = get("/api/v5/public/open-interest",
                               {"instId": inst_id})
            oi_hist      = get("/api/v5/rubik/stat/contracts/open-interest-volume",
                               {"ccy": ccy, "period": "1D", "limit": 7})
            ls_hist      = get("/api/v5/rubik/stat/contracts/long-short-account-ratio-contract-top-trader",
                               {"instId": inst_id, "period": "1H", "limit": 24})

            # Funding rate — current + recent history
            current_fr   = float((funding_now[0] if funding_now else {}).get("fundingRate", 0))
            fr_history   = [
                {"time": int(x["fundingTime"]), "rate": float(x["realizedRate"])}
                for x in funding_hist
            ]
            recent_rates = [float(x["realizedRate"]) for x in funding_hist[:3]]
            avg_fr_24h   = round(sum(recent_rates) / len(recent_rates), 7) if recent_rates else None
            # OKX settles every 8h → annualized = rate * 3 * 365
            annualized   = round(current_fr * 3 * 365 * 100, 2)

            # Open interest — current snapshot
            oi_snap      = oi_now[0] if oi_now else {}
            oi_ccy       = float(oi_snap.get("oiCcy", 0))   # in base currency units
            oi_usd       = float(oi_snap.get("oiUsd", 0))   # notional USD

            # OI history — [timestamp, oi_usd, volume_usd]
            oi_trend = [
                {"date": int(row[0]), "oi_usd": float(row[1]), "volume_usd": float(row[2])}
                for row in reversed(oi_hist)  # oldest→newest
            ]
            oi_7d_change = None
            if len(oi_trend) >= 2 and oi_trend[0]["oi_usd"]:
                oi_7d_change = round(
                    (oi_trend[-1]["oi_usd"] / oi_trend[0]["oi_usd"] - 1) * 100, 2
                )

            # Long/short ratio — [[timestamp, ratio], ...]
            ls_series = [
                {"time": int(row[0]), "long_short_ratio": float(row[1])}
                for row in ls_hist
            ]
            ls_now    = float(ls_hist[-1][1]) if ls_hist else 0.0

            snapshot = {
                "instrument":    inst_id,
                "data_source":   "OKX",
                "funding_rate": {
                    "current_rate_8h":             round(current_fr, 7),
                    "current_rate_annualized_pct": annualized,
                    "avg_rate_last_24h":           avg_fr_24h,
                    "bias":                        "net_long" if current_fr > 0 else "net_short",
                    "extreme_rate":                abs(annualized) > 36,
                    "history_last_8_settlements":  fr_history,
                },
                "open_interest": {
                    "current_oi_ccy":  round(oi_ccy, 4),
                    "current_oi_usd":  round(oi_usd),
                    "oi_7d_change_pct": oi_7d_change,
                    "trend_7d_daily":  oi_trend,
                },
                "long_short_ratio": {
                    "current_ratio":    round(ls_now, 3),
                    "crowded_long":     ls_now > 1.5,
                    "crowded_short":    ls_now < 0.7,
                    "trend_24h_hourly": ls_series,
                },
            }
            return (
                f"Perpetuals data for {inst_id} (OKX) — funding rate, OI, L/S ratio:\n"
                f"{json.dumps(snapshot, indent=2)}"
            )
        except requests.exceptions.Timeout:
            return f"Timeout fetching perpetuals data for {inst_id}"
        except Exception as e:
            return f"Error fetching perpetuals data for {inst_id}: {str(e)}"

    @staticmethod
    @tool
    def get_crypto_news_rss_feed(
        token_symbol: Annotated[str, "Token symbol (e.g., BTC, ETH, UNI)"],
        token_name: Annotated[Optional[str], "Optional token name (e.g., Bitcoin, Ethereum)"] = None,
        days_back: Annotated[int, "Number of days to look back for articles"] = 7,
    ):
        """
        Fetch and filter articles for a specific token from active crypto news
        RSS feeds (Cointelegraph, Decrypt, The Block).

        Args:
            token_symbol (str): Token symbol to filter for
            token_name (str): Optional token name to filter for
            days_back (int): Number of days to look back

        Returns:
            str: JSON string of filtered articles with titles, links, summaries, and dates
        """
        try:
            articles = fetch_crypto_news_rss(
                asset_symbol=token_symbol,
                asset_name=token_name,
                days_back=days_back
            )

            if not articles:
                return f"No articles found for {token_symbol} in crypto news RSS feeds (last {days_back} days)"

            # Format articles for output
            formatted_articles = []
            for article in articles:
                formatted_articles.append({
                    "title": article.get("title", ""),
                    "link": article.get("link", ""),
                    "summary": article.get("summary", "")[:500],  # Limit summary length
                    "published": article.get("published", ""),
                    "source": article.get("source", ""),
                    "tags": article.get("tags", [])
                })

            return f"Found {len(formatted_articles)} articles for {token_symbol}:\n{json.dumps(formatted_articles, indent=2)}"

        except Exception as e:
            return f"Error fetching crypto news RSS feeds for {token_symbol}: {str(e)}"

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
        days_back: Annotated[int, "Number of days to look back (default 7)"] = 7,
    ):
        """
        Fetch crypto news articles and return a FULLY PRE-COMPUTED sentiment snapshot.

        Sources: Cointelegraph, Decrypt, The Block (RSS feeds).

        All scoring is done deterministically in Python — the LLM must interpret
        pre-computed fields only. It must NOT re-score articles from raw text.
        This follows the same principle as get_deterministic_technical_analysis.

        Snapshot fields (all pre-computed):
          sentiment_score     : −1.0 (very bearish) → +1.0 (very bullish)
                                Weighted by recency decay × source credibility
                                × event-category relevance boost.
          sentiment_bias      : STRONG_BULL / BULL / NEUTRAL / BEAR / STRONG_BEAR
          conviction          : 0.0 → 1.0 (signal strength)
          sentiment_momentum  : improving / stable / deteriorating
                                (recent half of window vs early half)
          event_breakdown     : {category: count} — exploit_hack, regulatory,
                                protocol_upgrade, adoption, governance, etc.
          high_impact_events  : event categories with relevance weight ≥ 1.4
          top_articles        : top 5 by |weighted_score| with per-article scores
                                and event tags — for qualitative LLM read-through
          bullish_themes / bearish_themes : top 3 article titles per direction

        COMPUTATION RULE: Do NOT re-score articles from their title/summary text.
        Read sentiment_score, sentiment_bias, and conviction directly.
        """
        from tradingagents.dataflows.sentiment_indicators import compute_sentiment_snapshot

        as_of_date = Toolkit._config.get("as_of_date")
        try:
            articles = fetch_crypto_news_rss(
                asset_symbol=token_symbol,
                asset_name=token_name,
                days_back=days_back,
            )
            snapshot = compute_sentiment_snapshot(
                articles, token_symbol.upper(), as_of_date=as_of_date
            )
            caveat = (
                f" CAVEAT: as_of_date={as_of_date} (backtest — recency weights relative to that date)."
                if as_of_date else ""
            )
            return (
                f"Pre-computed news sentiment for {token_symbol.upper()} "
                f"({len(articles)} articles, {days_back}d):{caveat}\n"
                f"{json.dumps(snapshot, indent=2)}"
            )
        except Exception as e:
            return f"Error computing news sentiment for {token_symbol}: {str(e)}"

    @staticmethod
    @tool
    def get_fear_greed_index(
        days_back: Annotated[int, "Number of days of history to retrieve (default 7)"] = 7,
    ):
        """
        Get the crypto Fear & Greed Index (alternative.me) -- a real,
        deterministic, market-wide sentiment score (0-100, 0=extreme fear,
        100=extreme greed). This replaces the old search_internet/search_twitter
        tools (silently broken) and a LunarCrush integration that turned out to
        require a paid plan for API access. Note this index is market-wide,
        not specific to any one token.

        Returns:
            str: JSON of recent Fear & Greed Index readings.
        """
        try:
            from tradingagents.dataflows.fear_greed_api import get_fear_greed_index as fetch_fear_greed_index

            readings = fetch_fear_greed_index(limit=days_back)
            return f"Crypto Fear & Greed Index (market-wide, last {days_back} day(s)):\n{json.dumps(readings, indent=2)}"

        except Exception as e:
            return f"Error getting Fear & Greed Index: {str(e)}"

    @staticmethod
    @tool
    def get_coingecko_trending():
        """
        Fetch the top trending coins on CoinGecko in the last 24 hours
        (https://api.coingecko.com/api/v3/search/trending).

        Returns up to 15 coins ranked by search volume on CoinGecko, each with:
          - symbol, name, market_cap_rank
          - price_change_24h_pct (if available)
          - score (CoinGecko internal trending rank, 0 = hottest)

        Interpretation:
          - A token in the trending list = elevated retail attention / FOMO risk
          - Token NOT in trending list during a price rally = institutional-driven,
            lower retail FOMO component (more sustainable)
          - Many DeFi tokens trending simultaneously = sector rotation signal
          - Trending + negative news = retail capitulation risk

        This is a market-wide retail attention gauge, not a directional signal.
        Combine with sentiment_bias from get_crypto_news_sentiment.
        """
        import requests

        try:
            resp = requests.get(
                "https://api.coingecko.com/api/v3/search/trending",
                timeout=10,
            )
            resp.raise_for_status()
            data = resp.json()

            coins = data.get("coins", [])
            trending = []
            for entry in coins:
                item = entry.get("item", {})
                trending.append({
                    "symbol":              item.get("symbol", ""),
                    "name":                item.get("name", ""),
                    "market_cap_rank":     item.get("market_cap_rank"),
                    "score":               item.get("score", 0),  # 0 = hottest
                    "price_change_24h_pct": (
                        item.get("data", {}).get("price_change_percentage_24h", {}).get("usd")
                    ),
                })

            # Sort by score ascending (0 is hottest)
            trending.sort(key=lambda x: x["score"])

            return (
                f"CoinGecko trending coins (top {len(trending)}, last 24h):\n"
                f"{json.dumps(trending, indent=2)}"
            )
        except requests.exceptions.Timeout:
            return "Timeout fetching CoinGecko trending data"
        except Exception as e:
            return f"Error fetching CoinGecko trending: {str(e)}"

    @staticmethod
    @tool
    def get_snapshot_governance(
        token_symbol: Annotated[str, "Token symbol (UNI or AAVE — both have active Snapshot spaces)"],
    ):
        """
        Fetch recent governance proposals and vote results from Snapshot.org
        (https://hub.snapshot.org/graphql) — free public GraphQL API, no auth required.

        Covers: UNI (space: 'uniswap'), AAVE (space: 'aave.eth').
        Returns last 5 proposals (active + closed) with vote totals and outcomes.

        Governance signals:
          - Active proposals with high participation = healthy community engagement
          - Passed proposals for fee switches / token burns = direct bullish fundamental
          - Failed quorum = governance apathy, bearish for protocol health
          - Contentious votes (close split) = community uncertainty, headwind

        Only relevant for UNI and AAVE. For BTC/ETH/SOL returns a clear
        "not applicable" rather than fabricating data.
        """
        import requests

        SNAPSHOT_SPACES = {
            "UNI":  "uniswap",
            "AAVE": "aave.eth",
        }

        symbol = token_symbol.upper()
        space  = SNAPSHOT_SPACES.get(symbol)
        if space is None:
            return (
                f"Snapshot governance not applicable for {symbol}. "
                f"Only UNI and AAVE have tracked Snapshot spaces in this pipeline."
            )

        query = """
        query($space: String!) {
          proposals(
            first: 5,
            where: { space_in: [$space] },
            orderBy: "created",
            orderDirection: desc
          ) {
            id
            title
            state
            start
            end
            votes
            quorum
            scores_total
            scores
            choices
          }
        }
        """
        try:
            resp = requests.post(
                "https://hub.snapshot.org/graphql",
                json={"query": query, "variables": {"space": space}},
                timeout=12,
            )
            resp.raise_for_status()
            body = resp.json()

            if "errors" in body:
                return f"Snapshot GraphQL error for {symbol}: {body['errors']}"

            proposals_raw = (body.get("data") or {}).get("proposals", [])
            proposals = []
            for p in proposals_raw:
                scores   = p.get("scores") or []
                choices  = p.get("choices") or []
                total    = p.get("scores_total") or 0
                top_idx  = scores.index(max(scores)) if scores else None
                outcome  = choices[top_idx] if (top_idx is not None and top_idx < len(choices)) else None
                win_pct  = round(max(scores) / total * 100, 1) if total else None

                proposals.append({
                    "title":        p.get("title", "")[:100],
                    "state":        p.get("state"),
                    "votes_cast":   p.get("votes"),
                    "quorum":       p.get("quorum"),
                    "scores_total": round(total),
                    "leading_choice": outcome,
                    "leading_pct":  win_pct,
                    "start_ts":     p.get("start"),
                    "end_ts":       p.get("end"),
                })

            active   = [p for p in proposals if p["state"] == "active"]
            closed   = [p for p in proposals if p["state"] == "closed"]

            result = {
                "token":            symbol,
                "snapshot_space":   space,
                "active_proposals": len(active),
                "recent_proposals": proposals,
                "governance_note": (
                    f"{len(active)} proposal(s) currently active."
                    if active else "No active proposals — governance is quiet."
                ),
            }
            return (
                f"Snapshot governance for {symbol} (space: {space}):\n"
                f"{json.dumps(result, indent=2)}"
            )
        except requests.exceptions.Timeout:
            return f"Timeout fetching Snapshot governance for {symbol}"
        except Exception as e:
            return f"Error fetching Snapshot governance for {symbol}: {str(e)}"

    @staticmethod
    @tool
    def search_reddit(
        token_symbol: Annotated[str, "Token symbol (e.g., BTC, ETH, UNI)"],
        token_name: Annotated[Optional[str], "Optional token name"] = None,
        days_back: Annotated[int, "Number of days to look back"] = 7,
        max_posts: Annotated[int, "Maximum number of posts to retrieve"] = 10,
    ):
        """
        Search Reddit for recent posts and discussions about a cryptocurrency token,
        via the real Reddit API (PRAW). Searches token-relevant subreddits plus
        r/CryptoCurrency and r/defi.

        Args:
            token_symbol: Token symbol to search for
            token_name: Optional token name
            days_back: Number of days to look back
            max_posts: Maximum number of posts to retrieve

        Returns:
            str: JSON list of real Reddit posts (title, score, comments, link, text excerpt)
        """
        try:
            from tradingagents.dataflows.reddit_api import search_reddit_posts

            posts = search_reddit_posts(token_symbol, token_name, days_back, max_posts)
            if not posts:
                return f"No Reddit posts found for {token_symbol} in the last {days_back} days"
            return f"Found {len(posts)} Reddit posts for {token_symbol}:\n{json.dumps(posts, indent=2)}"

        except Exception as e:
            return f"Error searching Reddit for {token_symbol}: {str(e)}"
    
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

