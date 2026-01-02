"""
Baseline Trading Strategies for DeFi Trading Agents Research
Implements rule-based strategies for performance comparison
"""

import pandas as pd
import numpy as np
from typing import Dict, Tuple, List
from dataclasses import dataclass
from datetime import datetime


@dataclass
class TradeSignal:
    """Represents a trading signal."""
    timestamp: str
    action: str  # 'BUY', 'SELL', 'HOLD'
    price: float
    confidence: float = 1.0
    reason: str = ""


class BaselineStrategy:
    """Base class for all baseline strategies."""
    
    def __init__(self, name: str, params: Dict = None):
        self.name = name
        self.params = params or {}
        self.signals = []
        
    def generate_signals(self, price_data: pd.DataFrame) -> List[TradeSignal]:
        """Generate trading signals from price data."""
        raise NotImplementedError
        
    def backtest(self, price_data: pd.DataFrame, initial_capital: float = 10000) -> Dict:
        """Backtest the strategy."""
        signals = self.generate_signals(price_data)
        return self._calculate_performance(signals, price_data, initial_capital)
        
    def _calculate_performance(self, signals: List[TradeSignal], 
                               price_data: pd.DataFrame, 
                               initial_capital: float) -> Dict:
        """Calculate performance metrics."""
        portfolio_value = initial_capital
        cash = initial_capital
        position = 0
        trades = []
        portfolio_history = []
        
        for signal in signals:
            price = signal.price
            
            if signal.action == 'BUY' and cash > 0:
                # Buy with all available cash
                shares = cash / price
                position += shares
                cash = 0
                trades.append({
                    'timestamp': signal.timestamp,
                    'action': 'BUY',
                    'price': price,
                    'shares': shares
                })
                
            elif signal.action == 'SELL' and position > 0:
                # Sell all position
                cash = position * price
                trades.append({
                    'timestamp': signal.timestamp,
                    'action': 'SELL',
                    'price': price,
                    'shares': position
                })
                position = 0
                
            # Calculate current portfolio value
            current_value = cash + (position * price)
            portfolio_history.append({
                'timestamp': signal.timestamp,
                'value': current_value
            })
        
        # Calculate metrics
        final_value = cash + (position * price_data.iloc[-1]['close'])
        total_return = (final_value - initial_capital) / initial_capital
        
        return {
            'final_value': final_value,
            'total_return': total_return,
            'total_trades': len(trades),
            'portfolio_history': portfolio_history,
            'trades': trades
        }


class BuyAndHoldStrategy(BaselineStrategy):
    """Buy and hold strategy - buy at start, hold until end."""
    
    def __init__(self):
        super().__init__("Buy and Hold")
        
    def generate_signals(self, price_data: pd.DataFrame) -> List[TradeSignal]:
        signals = []
        
        # Buy at the first data point
        first_row = price_data.iloc[0]
        signals.append(TradeSignal(
            timestamp=str(first_row['timestamp']),
            action='BUY',
            price=first_row['close'],
            reason="Initial purchase"
        ))
        
        # Hold for all other points
        for idx, row in price_data.iloc[1:].iterrows():
            signals.append(TradeSignal(
                timestamp=str(row['timestamp']),
                action='HOLD',
                price=row['close'],
                reason="Holding position"
            ))
            
        return signals


class MACDStrategy(BaselineStrategy):
    """MACD crossover strategy."""
    
    def __init__(self, fast_period=12, slow_period=26, signal_period=9):
        params = {
            'fast_period': fast_period,
            'slow_period': slow_period,
            'signal_period': signal_period
        }
        super().__init__("MACD", params)
        
    def generate_signals(self, price_data: pd.DataFrame) -> List[TradeSignal]:
        df = price_data.copy()
        
        # Calculate MACD
        exp1 = df['close'].ewm(span=self.params['fast_period'], adjust=False).mean()
        exp2 = df['close'].ewm(span=self.params['slow_period'], adjust=False).mean()
        df['macd'] = exp1 - exp2
        df['signal_line'] = df['macd'].ewm(span=self.params['signal_period'], adjust=False).mean()
        df['macd_diff'] = df['macd'] - df['signal_line']
        
        signals = []
        position = None
        
        for idx, row in df.iterrows():
            if pd.isna(row['macd_diff']):
                continue
                
            # Buy when MACD crosses above signal line
            if row['macd_diff'] > 0 and position != 'LONG':
                signals.append(TradeSignal(
                    timestamp=str(row['timestamp']),
                    action='BUY',
                    price=row['close'],
                    reason=f"MACD ({row['macd']:.2f}) crossed above signal ({row['signal_line']:.2f})"
                ))
                position = 'LONG'
                
            # Sell when MACD crosses below signal line
            elif row['macd_diff'] < 0 and position == 'LONG':
                signals.append(TradeSignal(
                    timestamp=str(row['timestamp']),
                    action='SELL',
                    price=row['close'],
                    reason=f"MACD ({row['macd']:.2f}) crossed below signal ({row['signal_line']:.2f})"
                ))
                position = None
            else:
                signals.append(TradeSignal(
                    timestamp=str(row['timestamp']),
                    action='HOLD',
                    price=row['close']
                ))
                
        return signals


class KDJRSIStrategy(BaselineStrategy):
    """Combined KDJ and RSI momentum strategy."""
    
    def __init__(self, kdj_period=9, rsi_period=14, rsi_overbought=70, rsi_oversold=30):
        params = {
            'kdj_period': kdj_period,
            'rsi_period': rsi_period,
            'rsi_overbought': rsi_overbought,
            'rsi_oversold': rsi_oversold
        }
        super().__init__("KDJ + RSI", params)
        
    def _calculate_rsi(self, prices: pd.Series, period: int) -> pd.Series:
        """Calculate RSI indicator."""
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi
        
    def _calculate_kdj(self, df: pd.DataFrame, period: int) -> Tuple[pd.Series, pd.Series, pd.Series]:
        """Calculate KDJ indicator."""
        low_min = df['low'].rolling(window=period).min()
        high_max = df['high'].rolling(window=period).max()
        
        rsv = (df['close'] - low_min) / (high_max - low_min) * 100
        k = rsv.ewm(com=2, adjust=False).mean()
        d = k.ewm(com=2, adjust=False).mean()
        j = 3 * k - 2 * d
        
        return k, d, j
        
    def generate_signals(self, price_data: pd.DataFrame) -> List[TradeSignal]:
        df = price_data.copy()
        
        # Calculate RSI
        df['rsi'] = self._calculate_rsi(df['close'], self.params['rsi_period'])
        
        # Calculate KDJ
        df['k'], df['d'], df['j'] = self._calculate_kdj(df, self.params['kdj_period'])
        
        signals = []
        position = None
        
        for idx, row in df.iterrows():
            if pd.isna(row['rsi']) or pd.isna(row['k']):
                continue
                
            # Buy when RSI oversold and K crosses above D
            if (row['rsi'] < self.params['rsi_oversold'] and 
                row['k'] > row['d'] and position != 'LONG'):
                signals.append(TradeSignal(
                    timestamp=str(row['timestamp']),
                    action='BUY',
                    price=row['close'],
                    reason=f"RSI oversold ({row['rsi']:.2f}) and K>D"
                ))
                position = 'LONG'
                
            # Sell when RSI overbought and K crosses below D
            elif (row['rsi'] > self.params['rsi_overbought'] and 
                  row['k'] < row['d'] and position == 'LONG'):
                signals.append(TradeSignal(
                    timestamp=str(row['timestamp']),
                    action='SELL',
                    price=row['close'],
                    reason=f"RSI overbought ({row['rsi']:.2f}) and K<D"
                ))
                position = None
            else:
                signals.append(TradeSignal(
                    timestamp=str(row['timestamp']),
                    action='HOLD',
                    price=row['close']
                ))
                
        return signals


class ZMRStrategy(BaselineStrategy):
    """Zero Mean Reversion strategy."""
    
    def __init__(self, lookback_period=20, entry_threshold=2.0, exit_threshold=0.5):
        params = {
            'lookback_period': lookback_period,
            'entry_threshold': entry_threshold,
            'exit_threshold': exit_threshold
        }
        super().__init__("ZMR", params)
        
    def generate_signals(self, price_data: pd.DataFrame) -> List[TradeSignal]:
        df = price_data.copy()
        
        # Calculate rolling mean and standard deviation
        df['mean'] = df['close'].rolling(window=self.params['lookback_period']).mean()
        df['std'] = df['close'].rolling(window=self.params['lookback_period']).std()
        df['z_score'] = (df['close'] - df['mean']) / df['std']
        
        signals = []
        position = None
        
        for idx, row in df.iterrows():
            if pd.isna(row['z_score']):
                continue
                
            # Buy when price is significantly below mean
            if row['z_score'] < -self.params['entry_threshold'] and position != 'LONG':
                signals.append(TradeSignal(
                    timestamp=str(row['timestamp']),
                    action='BUY',
                    price=row['close'],
                    reason=f"Price below mean by {abs(row['z_score']):.2f} std dev"
                ))
                position = 'LONG'
                
            # Sell when price returns to near mean
            elif abs(row['z_score']) < self.params['exit_threshold'] and position == 'LONG':
                signals.append(TradeSignal(
                    timestamp=str(row['timestamp']),
                    action='SELL',
                    price=row['close'],
                    reason=f"Price returned to mean (z={row['z_score']:.2f})"
                ))
                position = None
            else:
                signals.append(TradeSignal(
                    timestamp=str(row['timestamp']),
                    action='HOLD',
                    price=row['close']
                ))
                
        return signals


class SMACrossoverStrategy(BaselineStrategy):
    """Simple Moving Average crossover strategy."""
    
    def __init__(self, short_window=50, long_window=200):
        params = {
            'short_window': short_window,
            'long_window': long_window
        }
        super().__init__("SMA Crossover", params)
        
    def generate_signals(self, price_data: pd.DataFrame) -> List[TradeSignal]:
        df = price_data.copy()
        
        # Calculate SMAs
        df['sma_short'] = df['close'].rolling(window=self.params['short_window']).mean()
        df['sma_long'] = df['close'].rolling(window=self.params['long_window']).mean()
        
        signals = []
        position = None
        
        for idx, row in df.iterrows():
            if pd.isna(row['sma_short']) or pd.isna(row['sma_long']):
                continue
                
            # Buy when short SMA crosses above long SMA (Golden Cross)
            if row['sma_short'] > row['sma_long'] and position != 'LONG':
                signals.append(TradeSignal(
                    timestamp=str(row['timestamp']),
                    action='BUY',
                    price=row['close'],
                    reason=f"Golden cross: SMA{self.params['short_window']} > SMA{self.params['long_window']}"
                ))
                position = 'LONG'
                
            # Sell when short SMA crosses below long SMA (Death Cross)
            elif row['sma_short'] < row['sma_long'] and position == 'LONG':
                signals.append(TradeSignal(
                    timestamp=str(row['timestamp']),
                    action='SELL',
                    price=row['close'],
                    reason=f"Death cross: SMA{self.params['short_window']} < SMA{self.params['long_window']}"
                ))
                position = None
            else:
                signals.append(TradeSignal(
                    timestamp=str(row['timestamp']),
                    action='HOLD',
                    price=row['close']
                ))
                
        return signals


def get_baseline_strategy(strategy_name: str, params: Dict = None) -> BaselineStrategy:
    """Factory function to get baseline strategy instance."""
    strategies = {
        'buy_and_hold': BuyAndHoldStrategy,
        'macd': MACDStrategy,
        'kdj_rsi': KDJRSIStrategy,
        'zmr': ZMRStrategy,
        'sma_crossover': SMACrossoverStrategy
    }
    
    if strategy_name not in strategies:
        raise ValueError(f"Unknown strategy: {strategy_name}")
        
    if params:
        return strategies[strategy_name](**params)
    else:
        return strategies[strategy_name]()