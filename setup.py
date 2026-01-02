"""
Setup script for the DeFi Trading Agents package.
"""

from setuptools import setup, find_packages

setup(
    name="defi-trading-agents",
    version="0.1.0",
    description="Multi-Agent LLM Framework for DeFi Trading",
    author="DeFi Trading Agents Team",
    author_email="",
    url="",
    packages=find_packages(),
    install_requires=[
        "langchain>=0.1.0",
        "langchain-openai>=0.0.2",
        "langchain-experimental>=0.0.40",
        "langgraph>=0.0.20",
        "numpy>=1.24.0",
        "pandas>=2.0.0",
        "coinbase-agentkit>=0.7.1",
        "requests>=2.32.4",
        "typer>=0.9.0",
        "rich>=13.0.0",
        "questionary>=2.0.1",
    ],
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "defi-trading-agents=cli.main:app",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Financial and Trading Industry",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Topic :: Office/Business :: Financial :: Investment",
    ],
)
