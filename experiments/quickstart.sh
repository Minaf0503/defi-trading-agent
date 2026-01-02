#!/bin/bash
# Quick Start Script for DeFi Trading Agents Experiments
# Usage: ./experiments/quickstart.sh

set -e  # Exit on error

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║   DeFi Trading Agents - Experiment Quick Start               ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Check Python version
echo "🔍 Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "   Python version: $python_version"

# Check if in correct directory
if [ ! -f "experiments/main.py" ]; then
    echo "❌ Error: Must run from project root directory"
    echo "   cd /path/to/defi-trading-agent"
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source .venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -q --upgrade pip
pip install -q -r requirements.txt
pip install -q -r experiments/requirements.txt

# Check API keys
echo ""
echo "🔑 Checking API keys..."
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "⚠️  ANTHROPIC_API_KEY not set"
    echo "   Set it with: export ANTHROPIC_API_KEY='your-key-here'"
    echo "   Or add to .env file"
    read -p "   Continue anyway? [y/N]: " continue
    if [ "$continue" != "y" ]; then
        exit 1
    fi
else
    echo "✅ ANTHROPIC_API_KEY found"
fi

# Create necessary directories
echo ""
echo "📁 Creating directories..."
mkdir -p experiments/results
mkdir -p experiments/charts
mkdir -p experiments/reports
mkdir -p experiments/logs
mkdir -p experiments/data
echo "✅ Directories created"

# Run prerequisite check
echo ""
echo "🔍 Running prerequisite check..."
python3 experiments/main.py --check-only

# Ask user what to run
echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "What would you like to do?"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "1. Quick Test (5-10 min) - Test on BTC only"
echo "2. Single Experiment - Choose token and architecture"
echo "3. Full Suite (2-4 hours) - All tokens and architectures"
echo "4. Exit"
echo ""
read -p "Enter choice [1-4]: " choice

case $choice in
    1)
        echo ""
        echo "🏃 Running quick test..."
        python3 experiments/main.py --mode quick
        ;;
    2)
        echo ""
        echo "Available tokens: BTC, ETH, SOL, UNI, AAVE, ZEC, XMR"
        read -p "Enter token symbol: " token
        echo ""
        echo "Available architectures: role_based, function_based"
        read -p "Enter architecture: " arch
        echo ""
        echo "🎯 Running experiment: $token - $arch"
        python3 experiments/main.py --mode single --token $token --architecture $arch
        ;;
    3)
        echo ""
        echo "⚠️  This will run ALL experiments (2-4 hours)"
        read -p "Are you sure? [y/N]: " confirm
        if [ "$confirm" = "y" ]; then
            echo ""
            echo "🚀 Running full experimental suite..."
            python3 experiments/main.py --mode full
        else
            echo "Cancelled."
        fi
        ;;
    4)
        echo "Exiting."
        exit 0
        ;;
    *)
        echo "Invalid choice. Exiting."
        exit 1
        ;;
esac

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "✅ Complete!"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "📁 Results: experiments/results/"
echo "📊 Charts: experiments/charts/"
echo "📝 Report: experiments/reports/"
echo ""
echo "To view results:"
echo "   ls experiments/results/"
echo "   open experiments/charts/performance_comparison_BTC.png"
echo "   cat experiments/reports/experiment_report.md"
echo ""