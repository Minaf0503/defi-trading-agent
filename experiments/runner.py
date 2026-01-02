"""
Experiment Runner for DeFi Trading Agents Research
Orchestrates experiments across tokens, architectures, and baselines
"""

import os
import json
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Tuple
from tqdm import tqdm

from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG
from experiments.config import (
    EXPERIMENT_TOKENS, TIME_PERIODS, BASELINE_STRATEGIES,
    get_experiment_config, get_all_experiment_combinations
)
from experiments.baselines import get_baseline_strategy
from experiments.metrics import PerformanceCalculator, CostAnalyzer, PredictionEvaluator


class ExperimentRunner:
    """Main experiment runner for DeFi trading agents research."""
    
    def __init__(self, config: Dict = None):
        """Initialize experiment runner."""
        self.config = config or DEFAULT_CONFIG.copy()
        self.results_dir = Path("./experiments/results")
        self.results_dir.mkdir(parents=True, exist_ok=True)
        
        self.performance_calculator = PerformanceCalculator()
        self.cost_analyzer = CostAnalyzer()
        self.prediction_evaluator = PredictionEvaluator()
        
    def run_all_experiments(self):
        """Run all experiment combinations."""
        combinations = get_all_experiment_combinations()
        
        print(f"Running {len(combinations)} experiment combinations...")
        
        all_results = []
        for combo in tqdm(combinations, desc="Experiments"):
            result = self.run_single_experiment(
                token=combo['token'],
                architecture=combo['architecture'],
                period=combo['period']
            )
            all_results.append(result)
            
        # Save aggregate results
        self._save_aggregate_results(all_results)
        
        return all_results
        
    def run_single_experiment(self, token: str, architecture: str, period: str) -> Dict:
        """
        Run a single experiment configuration.
        
        Args:
            token: Token symbol (e.g., 'BTC')
            architecture: 'role_based' or 'function_based'
            period: 'backtesting', 'training', or 'all_period'
            
        Returns:
            Dictionary with experiment results
        """
        print(f"\n{'='*80}")
        print(f"Running Experiment: {token} - {architecture} - {period}")
        print(f"{'='*80}\n")
        
        # Get experiment configuration
        exp_config = get_experiment_config(token, architecture, period)
        
        # Load price data
        price_data = self._load_price_data(token, exp_config['period'])
        
        # Run agent-based strategy
        agent_results = self._run_agent_strategy(
            token, architecture, price_data, exp_config
        )
        
        # Run baseline strategies
        baseline_results = self._run_baseline_strategies(price_data, exp_config)
        
        # Combine results
        experiment_result = {
            'token': token,
            'architecture': architecture,
            'period': period,
            'timestamp': datetime.now().isoformat(),
            'agent_results': agent_results,
            'baseline_results': baseline_results,
            'config': exp_config
        }
        
        # Save individual experiment result
        self._save_experiment_result(experiment_result)
        
        return experiment_result
        
    def _load_price_data(self, token: str, period: Dict) -> pd.DataFrame:
        """
        Load price data for the specified token and period.
        
        This is a placeholder - you'll need to implement actual data loading
        from your crypto data sources (CoinGecko, etc.)
        """
        # TODO: Implement actual data loading
        # For now, return dummy data structure
        print(f"Loading price data for {token} from {period['start']} to {period['end']}")
        
        # Create date range
        dates = pd.date_range(start=period['start'], end=period['end'], freq='1H')
        
        # Generate synthetic data (replace with actual data loading)
        np.random.seed(42)
        base_price = 50000 if token == 'BTC' else 3000 if token == 'ETH' else 100
        
        price_data = pd.DataFrame({
            'timestamp': dates,
            'open': base_price + np.random.randn(len(dates)) * base_price * 0.02,
            'high': base_price + np.random.randn(len(dates)) * base_price * 0.03,
            'low': base_price + np.random.randn(len(dates)) * base_price * 0.03,
            'close': base_price + np.random.randn(len(dates)) * base_price * 0.02,
            'volume': np.random.randint(1000000, 10000000, len(dates))
        })
        
        # Ensure high >= close >= low
        price_data['high'] = price_data[['high', 'close']].max(axis=1)
        price_data['low'] = price_data[['low', 'close']].min(axis=1)
        
        return price_data
        
    def _run_agent_strategy(self, token: str, architecture: str, 
                           price_data: pd.DataFrame, config: Dict) -> Dict:
        """Run the agent-based trading strategy."""
        print(f"Running {architecture} agent strategy for {token}...")
        
        # Initialize trading graph
        analysts = config['architecture']['analysts']
        trading_config = self.config.copy()
        trading_config['llm_provider'] = 'anthropic'  # Use Anthropic for experiments
        
        graph = TradingAgentsGraph(
            selected_analysts=analysts,
            debug=False,
            config=trading_config
        )
        
        # Run trading over the period
        portfolio_history = []
        trades = []
        predictions = []
        api_calls = 0
        total_tokens = 0
        
        initial_capital = 10000
        current_capital = initial_capital
        position = 0
        
        # Sample dates (daily instead of hourly for efficiency)
        trading_dates = price_data.resample('D', on='timestamp').first().index
        
        for trade_date in tqdm(trading_dates, desc=f"{token} {architecture}", leave=False):
            trade_date_str = trade_date.strftime('%Y-%m-%d')
            
            try:
                # Get agent decision
                final_state, decision = graph.propagate(token, trade_date_str)
                
                # Extract prediction
                prediction = {
                    'timestamp': trade_date_str,
                    'direction': 'UPWARD' if 'BUY' in decision else 'DOWNWARD',
                    'decision': decision
                }
                predictions.append(prediction)
                
                # Get current price
                current_price = price_data[price_data['timestamp'].dt.date == trade_date.date()]['close'].iloc[0]
                
                # Execute trade based on decision
                if 'BUY' in decision and position == 0:
                    shares = current_capital / current_price
                    position = shares
                    current_capital = 0
                    trades.append({
                        'timestamp': trade_date_str,
                        'action': 'BUY',
                        'price': current_price,
                        'shares': shares
                    })
                    
                elif 'SELL' in decision and position > 0:
                    current_capital = position * current_price
                    trades.append({
                        'timestamp': trade_date_str,
                        'action': 'SELL',
                        'price': current_price,
                        'shares': position
                    })
                    position = 0
                    
                # Track portfolio value
                portfolio_value = current_capital + (position * current_price)
                portfolio_history.append({
                    'timestamp': trade_date_str,
                    'value': portfolio_value
                })
                
                # Track API usage (estimate)
                api_calls += len(analysts) + 5  # Analysts + researchers + managers
                total_tokens += 10000  # Rough estimate
                
            except Exception as e:
                print(f"Error on {trade_date_str}: {e}")
                continue
                
        # Calculate performance metrics
        metrics = self.performance_calculator.calculate_metrics(
            portfolio_history, trades, initial_capital
        )
        
        # Calculate costs
        costs = self.cost_analyzer.calculate_costs(
            trades, api_calls, total_tokens
        )
        
        # Evaluate predictions
        prediction_eval = self.prediction_evaluator.evaluate_predictions(
            predictions, price_data
        )
        
        return {
            'metrics': metrics.to_dict(),
            'costs': costs,
            'prediction_evaluation': prediction_eval,
            'portfolio_history': portfolio_history,
            'trades': trades,
            'predictions': predictions
        }
        
    def _run_baseline_strategies(self, price_data: pd.DataFrame, config: Dict) -> Dict:
        """Run all baseline strategies."""
        print("Running baseline strategies...")
        
        baseline_results = {}
        
        for strategy_name, strategy_config in BASELINE_STRATEGIES.items():
            try:
                strategy = get_baseline_strategy(strategy_name, strategy_config['params'])
                result = strategy.backtest(price_data)
                
                # Calculate metrics
                metrics = self.performance_calculator.calculate_metrics(
                    result['portfolio_history'],
                    result['trades'],
                    initial_capital=10000
                )
                
                baseline_results[strategy_name] = {
                    'metrics': metrics.to_dict(),
                    'trades': result['trades']
                }
                
            except Exception as e:
                print(f"Error running {strategy_name}: {e}")
                baseline_results[strategy_name] = {'error': str(e)}
                
        return baseline_results
        
    def _save_experiment_result(self, result: Dict):
        """Save individual experiment result."""
        token = result['token']
        architecture = result['architecture']
        period = result['period']
        
        filename = f"{token}_{architecture}_{period}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = self.results_dir / filename
        
        # Convert to JSON-serializable format
        result_copy = result.copy()
        if 'agent_results' in result_copy:
            # Remove non-serializable data
            result_copy['agent_results'] = {
                'metrics': result_copy['agent_results']['metrics'],
                'costs': result_copy['agent_results']['costs'],
                'prediction_evaluation': result_copy['agent_results']['prediction_evaluation'],
                'num_trades': len(result_copy['agent_results']['trades'])
            }
            
        with open(filepath, 'w') as f:
            json.dump(result_copy, f, indent=2)
            
        print(f"Saved results to {filepath}")
        
    def _save_aggregate_results(self, all_results: List[Dict]):
        """Save aggregated results across all experiments."""
        summary_data = []
        
        for result in all_results:
            summary_data.append({
                'token': result['token'],
                'architecture': result['architecture'],
                'period': result['period'],
                **result['agent_results']['metrics'],
                'total_cost_usd': result['agent_results']['costs']['total_cost']['usd']
            })
            
        # Save as CSV for easy analysis
        df = pd.DataFrame(summary_data)
        df.to_csv(self.results_dir / 'summary_results.csv', index=False)
        
        print(f"\nSaved summary results to {self.results_dir / 'summary_results.csv'}")


def main():
    """Main function to run experiments."""
    runner = ExperimentRunner()
    results = runner.run_all_experiments()
    
    print("\n" + "="*80)
    print("Experiments Complete!")
    print("="*80)
    print(f"Results saved to: {runner.results_dir}")


if __name__ == "__main__":
    main()