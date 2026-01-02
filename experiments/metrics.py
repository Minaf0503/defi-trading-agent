"""
Performance Metrics Calculator for DeFi Trading Agents Research
Calculates comprehensive trading performance metrics
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple
from dataclasses import dataclass
from datetime import datetime


@dataclass
class PerformanceMetrics:
    """Container for performance metrics."""
    cumulative_return: float
    annualized_return: float
    sharpe_ratio: float
    max_drawdown: float
    win_rate: float
    profit_factor: float
    total_trades: int
    avg_trade_return: float
    volatility: float
    calmar_ratio: float
    sortino_ratio: float
    
    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        return {
            'cumulative_return': self.cumulative_return,
            'annualized_return': self.annualized_return,
            'sharpe_ratio': self.sharpe_ratio,
            'max_drawdown': self.max_drawdown,
            'win_rate': self.win_rate,
            'profit_factor': self.profit_factor,
            'total_trades': self.total_trades,
            'avg_trade_return': self.avg_trade_return,
            'volatility': self.volatility,
            'calmar_ratio': self.calmar_ratio,
            'sortino_ratio': self.sortino_ratio
        }


class PerformanceCalculator:
    """Calculate comprehensive performance metrics for trading strategies."""
    
    def __init__(self, risk_free_rate: float = 0.02):
        """
        Initialize calculator.
        
        Args:
            risk_free_rate: Annual risk-free rate for Sharpe ratio calculation
        """
        self.risk_free_rate = risk_free_rate
        
    def calculate_metrics(self, portfolio_history: List[Dict], 
                         trades: List[Dict],
                         initial_capital: float = 10000) -> PerformanceMetrics:
        """
        Calculate all performance metrics.
        
        Args:
            portfolio_history: List of portfolio values over time
            trades: List of executed trades
            initial_capital: Starting capital
            
        Returns:
            PerformanceMetrics object
        """
        # Convert to DataFrame for easier calculation
        df = pd.DataFrame(portfolio_history)
        df['returns'] = df['value'].pct_change()
        
        # Calculate metrics
        cumulative_return = self._calculate_cumulative_return(df, initial_capital)
        annualized_return = self._calculate_annualized_return(df)
        sharpe_ratio = self._calculate_sharpe_ratio(df)
        max_drawdown = self._calculate_max_drawdown(df)
        win_rate = self._calculate_win_rate(trades)
        profit_factor = self._calculate_profit_factor(trades)
        total_trades = len([t for t in trades if t['action'] in ['BUY', 'SELL']])
        avg_trade_return = self._calculate_avg_trade_return(trades)
        volatility = self._calculate_volatility(df)
        calmar_ratio = self._calculate_calmar_ratio(annualized_return, max_drawdown)
        sortino_ratio = self._calculate_sortino_ratio(df)
        
        return PerformanceMetrics(
            cumulative_return=cumulative_return,
            annualized_return=annualized_return,
            sharpe_ratio=sharpe_ratio,
            max_drawdown=max_drawdown,
            win_rate=win_rate,
            profit_factor=profit_factor,
            total_trades=total_trades,
            avg_trade_return=avg_trade_return,
            volatility=volatility,
            calmar_ratio=calmar_ratio,
            sortino_ratio=sortino_ratio
        )
        
    def _calculate_cumulative_return(self, df: pd.DataFrame, initial_capital: float) -> float:
        """Calculate cumulative return."""
        final_value = df['value'].iloc[-1]
        return (final_value - initial_capital) / initial_capital
        
    def _calculate_annualized_return(self, df: pd.DataFrame) -> float:
        """Calculate annualized return."""
        total_return = (df['value'].iloc[-1] / df['value'].iloc[0]) - 1
        num_periods = len(df)
        # Assuming daily data, 365 days per year
        years = num_periods / 365
        if years > 0:
            annualized = (1 + total_return) ** (1 / years) - 1
            return annualized
        return 0.0
        
    def _calculate_sharpe_ratio(self, df: pd.DataFrame) -> float:
        """Calculate Sharpe ratio."""
        returns = df['returns'].dropna()
        if len(returns) == 0 or returns.std() == 0:
            return 0.0
            
        # Annualize returns and volatility (assuming daily data)
        excess_returns = returns.mean() * 365 - self.risk_free_rate
        volatility = returns.std() * np.sqrt(365)
        
        return excess_returns / volatility if volatility > 0 else 0.0
        
    def _calculate_max_drawdown(self, df: pd.DataFrame) -> float:
        """Calculate maximum drawdown."""
        cumulative = df['value']
        running_max = cumulative.expanding().max()
        drawdown = (cumulative - running_max) / running_max
        return abs(drawdown.min())
        
    def _calculate_win_rate(self, trades: List[Dict]) -> float:
        """Calculate win rate (percentage of profitable trades)."""
        if len(trades) < 2:
            return 0.0
            
        # Pair buy and sell trades
        buy_trades = [t for t in trades if t['action'] == 'BUY']
        sell_trades = [t for t in trades if t['action'] == 'SELL']
        
        wins = 0
        total_pairs = min(len(buy_trades), len(sell_trades))
        
        for i in range(total_pairs):
            if sell_trades[i]['price'] > buy_trades[i]['price']:
                wins += 1
                
        return wins / total_pairs if total_pairs > 0 else 0.0
        
    def _calculate_profit_factor(self, trades: List[Dict]) -> float:
        """Calculate profit factor (gross profit / gross loss)."""
        if len(trades) < 2:
            return 0.0
            
        buy_trades = [t for t in trades if t['action'] == 'BUY']
        sell_trades = [t for t in trades if t['action'] == 'SELL']
        
        total_profit = 0.0
        total_loss = 0.0
        total_pairs = min(len(buy_trades), len(sell_trades))
        
        for i in range(total_pairs):
            pnl = (sell_trades[i]['price'] - buy_trades[i]['price']) * buy_trades[i]['shares']
            if pnl > 0:
                total_profit += pnl
            else:
                total_loss += abs(pnl)
                
        return total_profit / total_loss if total_loss > 0 else 0.0
        
    def _calculate_avg_trade_return(self, trades: List[Dict]) -> float:
        """Calculate average return per trade."""
        if len(trades) < 2:
            return 0.0
            
        buy_trades = [t for t in trades if t['action'] == 'BUY']
        sell_trades = [t for t in trades if t['action'] == 'SELL']
        
        total_return = 0.0
        total_pairs = min(len(buy_trades), len(sell_trades))
        
        for i in range(total_pairs):
            trade_return = (sell_trades[i]['price'] - buy_trades[i]['price']) / buy_trades[i]['price']
            total_return += trade_return
            
        return total_return / total_pairs if total_pairs > 0 else 0.0
        
    def _calculate_volatility(self, df: pd.DataFrame) -> float:
        """Calculate annualized volatility."""
        returns = df['returns'].dropna()
        # Annualize (assuming daily data)
        return returns.std() * np.sqrt(365)
        
    def _calculate_calmar_ratio(self, annualized_return: float, max_drawdown: float) -> float:
        """Calculate Calmar ratio (annualized return / max drawdown)."""
        return annualized_return / max_drawdown if max_drawdown > 0 else 0.0
        
    def _calculate_sortino_ratio(self, df: pd.DataFrame) -> float:
        """Calculate Sortino ratio (uses downside deviation instead of total volatility)."""
        returns = df['returns'].dropna()
        if len(returns) == 0:
            return 0.0
            
        # Calculate downside deviation (only negative returns)
        negative_returns = returns[returns < 0]
        downside_deviation = negative_returns.std() * np.sqrt(365)
        
        if downside_deviation == 0:
            return 0.0
            
        excess_returns = returns.mean() * 365 - self.risk_free_rate
        return excess_returns / downside_deviation


class CostAnalyzer:
    """Analyze trading costs including gas fees, slippage, and MEV."""
    
    def __init__(self):
        # Average costs (these would be updated based on actual data)
        self.avg_gas_price_gwei = 50  # Average gas price in Gwei
        self.eth_price_usd = 3000  # ETH price in USD
        self.swap_gas_units = 150000  # Average gas units for a DEX swap
        
    def calculate_costs(self, trades: List[Dict], api_calls: int, 
                       total_tokens: int, token_cost_per_1k: float = 0.01) -> Dict:
        """
        Calculate comprehensive trading costs.
        
        Args:
            trades: List of executed trades
            api_calls: Number of LLM API calls
            total_tokens: Total tokens used
            token_cost_per_1k: Cost per 1000 tokens
            
        Returns:
            Dictionary of cost breakdowns
        """
        num_trades = len([t for t in trades if t['action'] in ['BUY', 'SELL']])
        
        # Calculate gas fees
        gas_cost_eth = (self.avg_gas_price_gwei / 1e9) * self.swap_gas_units * num_trades
        gas_cost_usd = gas_cost_eth * self.eth_price_usd
        
        # Estimate slippage (0.1% per trade on average)
        total_volume = sum(t.get('price', 0) * t.get('shares', 0) 
                          for t in trades if t['action'] in ['BUY', 'SELL'])
        slippage_cost = total_volume * 0.001
        
        # Estimate MEV impact (0.05% per trade on average)
        mev_cost = total_volume * 0.0005
        
        # Calculate API costs
        api_cost = (total_tokens / 1000) * token_cost_per_1k
        
        # Total costs
        total_cost = gas_cost_usd + slippage_cost + mev_cost + api_cost
        
        return {
            'gas_fees': {
                'eth': gas_cost_eth,
                'usd': gas_cost_usd,
                'percentage': (gas_cost_usd / total_volume * 100) if total_volume > 0 else 0
            },
            'slippage': {
                'usd': slippage_cost,
                'percentage': 0.1  # 0.1% assumed
            },
            'mev_impact': {
                'usd': mev_cost,
                'percentage': 0.05  # 0.05% assumed
            },
            'api_costs': {
                'usd': api_cost,
                'calls': api_calls,
                'tokens': total_tokens
            },
            'total_cost': {
                'usd': total_cost,
                'percentage': (total_cost / total_volume * 100) if total_volume > 0 else 0
            }
        }


class PredictionEvaluator:
    """Evaluate prediction accuracy for 24-hour price forecasts."""
    
    def evaluate_predictions(self, predictions: List[Dict], 
                            actual_prices: pd.DataFrame) -> Dict:
        """
        Evaluate prediction accuracy.
        
        Args:
            predictions: List of predictions with timestamp, predicted_min, predicted_max
            actual_prices: DataFrame with actual prices
            
        Returns:
            Dictionary of evaluation metrics
        """
        direction_correct = 0
        min_price_errors = []
        max_price_errors = []
        
        for pred in predictions:
            timestamp = pred['timestamp']
            pred_direction = pred.get('direction', 'HOLD')
            
            # Find actual prices in next 24 hours
            pred_time = pd.to_datetime(timestamp)
            next_24h = actual_prices[
                (actual_prices['timestamp'] >= pred_time) &
                (actual_prices['timestamp'] < pred_time + pd.Timedelta(hours=24))
            ]
            
            if len(next_24h) == 0:
                continue
                
            actual_min = next_24h['low'].min()
            actual_max = next_24h['high'].max()
            
            # Evaluate direction
            price_change = (actual_max - actual_min) / actual_min
            actual_direction = 'UPWARD' if price_change > 0 else 'DOWNWARD'
            if pred_direction == actual_direction:
                direction_correct += 1
                
            # Evaluate min/max predictions
            if 'predicted_min' in pred:
                min_error = abs(pred['predicted_min'] - actual_min) / actual_min
                min_price_errors.append(min_error)
                
            if 'predicted_max' in pred:
                max_error = abs(pred['predicted_max'] - actual_max) / actual_max
                max_price_errors.append(max_error)
                
        return {
            'direction_accuracy': direction_correct / len(predictions) if predictions else 0,
            'avg_min_price_error': np.mean(min_price_errors) if min_price_errors else 0,
            'avg_max_price_error': np.mean(max_price_errors) if max_price_errors else 0,
            'total_predictions': len(predictions)
        }