"""
Main Experiment Script for DeFi Trading Agents Research
Complete experimental setup for FC26 DeFi Workshop submission

This script orchestrates the complete experimental pipeline:
1. Data collection and preprocessing
2. Baseline strategy execution
3. Agent-based strategy execution (role-based and function-based)
4. Performance evaluation
5. Visualization and reporting

Usage:
    python experiments/main.py --mode [full|quick|single]
    
Modes:
    - full: Run all experiments (all tokens, both architectures)
    - quick: Run quick test on single token
    - single: Run single token/architecture combination
"""

import argparse
import sys
import json
from pathlib import Path
from datetime import datetime

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from experiments.runner import ExperimentRunner
from experiments.visualizer import ExperimentVisualizer, ReportGenerator
from experiments.config import EXPERIMENT_TOKENS, AGENT_ARCHITECTURES


def print_banner():
    """Print experiment banner."""
    banner = """
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   DeFi Trading Agents: Multi-Agent Architecture Research     ║
║   Role-Based vs Function-Based Comparison                    ║
║                                                               ║
║   Tokens: BTC, ETH, SOL, UNI, AAVE, ZEC, XMR                ║
║   Period: Jan 2022 - Jun 2023 (Backtesting)                 ║
║   Baselines: 5 Rule-Based Strategies                         ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
"""
    print(banner)


def print_experiment_setup():
    """Print detailed experiment setup."""
    print("\n" + "="*70)
    print("EXPERIMENT CONFIGURATION")
    print("="*70)
    
    print("\n1. TOKENS:")
    for symbol, info in EXPERIMENT_TOKENS.items():
        print(f"   • {symbol}: {info['name']}")
        
    print("\n2. AGENT ARCHITECTURES:")
    for arch_type, info in AGENT_ARCHITECTURES.items():
        print(f"   • {arch_type}: {info['description']}")
        
    print("\n3. BASELINE STRATEGIES:")
    print("   • Buy and Hold")
    print("   • MACD (Moving Average Convergence Divergence)")
    print("   • KDJ + RSI (Combined Momentum)")
    print("   • ZMR (Zero Mean Reversion)")
    print("   • SMA Crossover (Simple Moving Average)")
    
    print("\n4. PERFORMANCE METRICS:")
    print("   • Cumulative Return")
    print("   • Annualized Return")
    print("   • Sharpe Ratio")
    print("   • Maximum Drawdown")
    print("   • Win Rate")
    print("   • Profit Factor")
    
    print("\n5. COST ANALYSIS:")
    print("   • Gas Fees (ETH)")
    print("   • Slippage Impact")
    print("   • MEV (Maximal Extractable Value)")
    print("   • API Costs (LLM)")
    print("   • Token Costs (LLM)")
    
    print("\n6. PREDICTION EVALUATION:")
    print("   • 24-Hour Direction Accuracy")
    print("   • Min Price Gap Assessment")
    print("   • Max Price Gap Assessment")
    print("   • Volatility Prediction Error")
    
    print("\n" + "="*70 + "\n")


def run_full_experiments():
    """Run complete experimental suite."""
    print("\n🚀 Starting FULL experimental suite...")
    print("⏱️  Estimated time: 2-4 hours (depending on API rate limits)\n")
    
    # Create runner
    runner = ExperimentRunner()
    
    # Run all experiments
    results = runner.run_all_experiments()
    
    # Generate visualizations
    print("\n📊 Generating visualizations...")
    visualizer = ExperimentVisualizer()
    visualizer.generate_all_visualizations(results)
    
    # Generate report
    print("\n📝 Generating research report...")
    reporter = ReportGenerator()
    reporter.generate_comprehensive_report(results)
    
    print("\n✅ Full experiments complete!")
    print(f"📁 Results: {runner.results_dir}")
    print(f"📊 Charts: {visualizer.charts_dir}")
    print(f"📝 Report: {reporter.reports_dir}")
    

def run_quick_test():
    """Run quick test on single token."""
    print("\n🏃 Running QUICK test on BTC (role-based)...")
    print("⏱️  Estimated time: 5-10 minutes\n")
    
    runner = ExperimentRunner()
    
    # Run single experiment
    result = runner.run_single_experiment(
        token='BTC',
        architecture='role_based',
        period='backtesting'
    )
    
    print("\n✅ Quick test complete!")
    print(f"📁 Results: {runner.results_dir}")
    

def run_single_experiment(token: str, architecture: str):
    """Run single token/architecture experiment."""
    print(f"\n🎯 Running experiment: {token} - {architecture}...")
    
    runner = ExperimentRunner()
    
    result = runner.run_single_experiment(
        token=token,
        architecture=architecture,
        period='backtesting'
    )
    
    print(f"\n✅ Experiment complete!")
    print(f"📁 Results: {runner.results_dir}")


def check_prerequisites():
    """Check if prerequisites are met."""
    print("\n🔍 Checking prerequisites...")
    
    issues = []
    
    # Check API keys
    import os
    if not os.getenv('ANTHROPIC_API_KEY'):
        issues.append("❌ ANTHROPIC_API_KEY not set")
    else:
        print("✅ ANTHROPIC_API_KEY found")
        
    # Check directories
    required_dirs = ['./experiments', './data', './results']
    for dir_path in required_dirs:
        path = Path(dir_path)
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            print(f"✅ Created directory: {dir_path}")
        else:
            print(f"✅ Directory exists: {dir_path}")
            
    # Check dependencies
    try:
        import pandas
        import matplotlib
        import seaborn
        print("✅ Required packages installed")
    except ImportError as e:
        issues.append(f"❌ Missing package: {e.name}")
        
    if issues:
        print("\n⚠️  Issues found:")
        for issue in issues:
            print(f"   {issue}")
        print("\nPlease fix these issues before running experiments.")
        return False
    else:
        print("\n✅ All prerequisites met!\n")
        return True


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description='DeFi Trading Agents Experiment Runner',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run full experimental suite
  python experiments/main.py --mode full
  
  # Run quick test
  python experiments/main.py --mode quick
  
  # Run single experiment
  python experiments/main.py --mode single --token BTC --architecture role_based
  
  # Check setup only
  python experiments/main.py --check-only
"""
    )
    
    parser.add_argument(
        '--mode',
        choices=['full', 'quick', 'single'],
        default='quick',
        help='Experiment mode: full (all experiments), quick (test), single (one experiment)'
    )
    
    parser.add_argument(
        '--token',
        choices=list(EXPERIMENT_TOKENS.keys()),
        help='Token symbol (for single mode)'
    )
    
    parser.add_argument(
        '--architecture',
        choices=['role_based', 'function_based'],
        help='Agent architecture (for single mode)'
    )
    
    parser.add_argument(
        '--check-only',
        action='store_true',
        help='Only check prerequisites, do not run experiments'
    )
    
    args = parser.parse_args()
    
    # Print banner
    print_banner()
    
    # Check prerequisites
    if not check_prerequisites():
        sys.exit(1)
        
    if args.check_only:
        print("Setup check complete. Use --mode to run experiments.")
        sys.exit(0)
        
    # Print setup
    print_experiment_setup()
    
    # Confirm before running
    if args.mode == 'full':
        response = input("⚠️  This will run ALL experiments (2-4 hours). Continue? [y/N]: ")
        if response.lower() != 'y':
            print("Cancelled.")
            sys.exit(0)
    
    # Run experiments based on mode
    try:
        if args.mode == 'full':
            run_full_experiments()
        elif args.mode == 'quick':
            run_quick_test()
        elif args.mode == 'single':
            if not args.token or not args.architecture:
                print("❌ Error: --token and --architecture required for single mode")
                sys.exit(1)
            run_single_experiment(args.token, args.architecture)
            
        print("\n" + "="*70)
        print("NEXT STEPS:")
        print("="*70)
        print("\n1. Review results in ./experiments/results/")
        print("2. View charts in ./experiments/charts/")
        print("3. Read report in ./experiments/reports/")
        print("4. For paper writing, see ./writing/papers/fc26-defi/")
        print("\n" + "="*70 + "\n")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user. Partial results may be saved.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()