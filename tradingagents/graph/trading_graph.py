# DeFi Trading Agents/graph/trading_graph.py

import os
from pathlib import Path
import json
from datetime import date
from typing import Dict, Any, Tuple, List, Optional

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI

from langgraph.prebuilt import ToolNode

from tradingagents.agents import *
from tradingagents.default_config import DEFAULT_CONFIG
from tradingagents.agents.utils.memory import FinancialSituationMemory
from tradingagents.agents.utils.agent_states import (
    AgentState,
    InvestDebateState,
    RiskDebateState,
)
from tradingagents.dataflows.config import set_config
from tradingagents.ablation import LLMCallTracker, SingleAgentBaseline

from .conditional_logic import ConditionalLogic
from .setup import GraphSetup
from .propagation import Propagator
from .reflection import Reflector
from .signal_processing import SignalProcessor


class TradingAgentsGraph:
    """Main class that orchestrates the trading agents framework."""

    def __init__(
        self,
        selected_analysts=["technical", "onchain", "tokenomics", "sentiment_news"],
        debug=False,
        config: Dict[str, Any] = None,
    ):
        """Initialize the trading agents graph and components.

        Args:
            selected_analysts: List of analyst types to include
            debug: Whether to run in debug mode
            config: Configuration dictionary. If None, uses default config
        """
        self.debug = debug
        self.config = config or DEFAULT_CONFIG

        # Update the interface's config
        set_config(self.config)

        # Create necessary directories
        os.makedirs(
            os.path.join(self.config["project_dir"], "dataflows/data_cache"),
            exist_ok=True,
        )

        # Initialize LLMs
        if self.config["llm_provider"].lower() == "openai" or self.config["llm_provider"] == "ollama" or self.config["llm_provider"] == "openrouter":
            self.deep_thinking_llm = ChatOpenAI(model=self.config["deep_think_llm"], base_url=self.config["backend_url"])
            self.quick_thinking_llm = ChatOpenAI(model=self.config["quick_think_llm"], base_url=self.config["backend_url"])
        elif self.config["llm_provider"].lower() == "anthropic":
            self.deep_thinking_llm = ChatAnthropic(model=self.config["deep_think_llm"], base_url=self.config["backend_url"])
            self.quick_thinking_llm = ChatAnthropic(model=self.config["quick_think_llm"], base_url=self.config["backend_url"])
        elif self.config["llm_provider"].lower() == "google":
            self.deep_thinking_llm = ChatGoogleGenerativeAI(model=self.config["deep_think_llm"])
            self.quick_thinking_llm = ChatGoogleGenerativeAI(model=self.config["quick_think_llm"])
        else:
            raise ValueError(f"Unsupported LLM provider: {self.config['llm_provider']}")

        # P6 instrumentation (Alpha Illusion: "debate-round cost",
        # "coordination latency"). IMPORTANT (found 2026-06-22, see
        # PROGRESS_LOG.md): attaching this via llm.with_config({"callbacks":
        # [...]}) at construction time -- the original design -- silently
        # drops the callback for any node that later calls .bind_tools() on
        # the wrapped object (all 4 analyst nodes), because ChatOpenAI's
        # .bind()/.bind_tools() override constructs a fresh binding that
        # does not inherit the outer with_config()'s callbacks. Verified
        # empirically: a real ChatOpenAI call fires the callback when
        # .with_config() is applied AFTER .bind_tools(), but not before --
        # and this project's analyst factories take the LLM already-wrapped
        # and call .bind_tools() on it themselves, so construction-time
        # wrapping silently undercounted every analyst's calls (Week 19's
        # reported call counts/tokens were missing all 4 analysts' calls).
        # Fix: do NOT wrap the LLM objects at all. Pass callbacks once, at
        # graph-invocation time (propagate()) via the top-level RunnableConfig
        # -- LangGraph/LangChain's own callback-manager propagation correctly
        # reaches every nested call, including .bind_tools()-bound ones,
        # because it threads through the run tree rather than through the
        # bound object's own config. SingleAgentBaseline's direct .invoke()
        # call gets the same tracker passed explicitly (see
        # build_single_agent_baseline() and ablation/single_agent_baseline.py).
        self.llm_call_tracker = LLMCallTracker()

        self.toolkit = Toolkit(config=self.config)

        # Initialize memories
        self.bull_memory = FinancialSituationMemory("bull_memory", self.config)
        self.bear_memory = FinancialSituationMemory("bear_memory", self.config)
        self.trader_memory = FinancialSituationMemory("trader_memory", self.config)
        self.invest_judge_memory = FinancialSituationMemory("invest_judge_memory", self.config)
        self.risk_manager_memory = FinancialSituationMemory("risk_manager_memory", self.config)

        # Create tool nodes
        self.tool_nodes = self._create_tool_nodes()

        # Initialize components
        self.conditional_logic = ConditionalLogic()
        self.graph_setup = GraphSetup(
            self.quick_thinking_llm,
            self.deep_thinking_llm,
            self.toolkit,
            self.tool_nodes,
            self.bull_memory,
            self.bear_memory,
            self.trader_memory,
            self.invest_judge_memory,
            self.risk_manager_memory,
            self.conditional_logic,
        )

        self.propagator = Propagator()
        self.reflector = Reflector(self.quick_thinking_llm)
        self.signal_processor = SignalProcessor(self.quick_thinking_llm)
        # Week 16: Stage 4 (calibration) + Stage 5 (sizing), see
        # tradingagents/agents/reflection/ace_agent.py. Not yet wired into
        # the graph itself (no in-graph node calls it) -- that's Week 17
        # integration; for now it's available for post-hoc, out-of-band use
        # the same way self.reflector already is via reflect_and_remember().
        self.ace_agent = ReflectionACEAgent(self.reflector)

        # State tracking
        self.curr_state = None
        self.ticker = None
        self.log_states_dict = {}  # date to full state dict

        # Set up the graph
        self.graph = self.graph_setup.setup_graph(selected_analysts)

    def _create_tool_nodes(self) -> Dict[str, ToolNode]:
        """Create tool nodes for different data sources."""
        # Define base tools for each analyst type
        technical_base_tools = [
            self.toolkit.get_crypto_price_data,
            self.toolkit.get_crypto_technical_indicators,
            self.toolkit.get_crypto_market_metrics,
            self.toolkit.get_crypto_volume_analysis,
        ]
        
        onchain_base_tools = [
            self.toolkit.get_onchain_liquidity_data,
            self.toolkit.get_onchain_holder_data,
            self.toolkit.get_onchain_transaction_data,
            self.toolkit.get_onchain_supply_data,
        ]
        
        tokenomics_base_tools = [
            self.toolkit.get_onchain_supply_data,
            self.toolkit.get_onchain_holder_data,
            self.toolkit.get_crypto_market_metrics,
        ]
        
        sentiment_base_tools = [
            self.toolkit.get_crypto_news_rss_feed,
            self.toolkit.analyze_article_sentiment,
            self.toolkit.get_crypto_news_sentiment,
            self.toolkit.get_fear_greed_index,
            self.toolkit.search_reddit,
        ]
        
        # Get enhanced tools for each agent (includes context and API tools)
        technical_tools = self.toolkit.get_agent_tools("technical", technical_base_tools)
        onchain_tools = self.toolkit.get_agent_tools("onchain", onchain_base_tools)
        tokenomics_tools = self.toolkit.get_agent_tools("tokenomics", tokenomics_base_tools)
        sentiment_tools = self.toolkit.get_agent_tools("sentiment_news", sentiment_base_tools)
        
        return {
            # Technical analyst tools
            "technical": ToolNode(technical_tools),
            # Onchain analyst tools
            "onchain": ToolNode(onchain_tools),
            # Tokenomics analyst tools
            "tokenomics": ToolNode(tokenomics_tools),
            # Sentiment/News analyst tools
            "sentiment_news": ToolNode(sentiment_tools),
        }

    def propagate(self, company_name, trade_date, historical_mode=None):
        """Run the trading agents graph for a company on a specific date.

        historical_mode (None = auto-detect from trade_date): when True,
        analyst tools that support it (technical price/indicators,
        on-chain liquidity/supply, tokenomics market cap) read real
        point-in-time data as of trade_date instead of live current data --
        see Toolkit's "as_of_date"-aware tools in agent_utils.py and
        BUILD_PLAN.md's Week 18 entry. Auto-detected as True whenever
        trade_date is strictly before today (ISO date string comparison).
        Note: Toolkit._config is class-level, shared state -- this method
        sets/clears it on every call, so sequential propagate() calls (the
        only usage pattern in this codebase) are safe, but concurrent calls
        across multiple graph instances are not.
        """
        if historical_mode is None:
            historical_mode = trade_date < date.today().isoformat()
        Toolkit.update_config({"as_of_date": trade_date if historical_mode else None})

        self.ticker = company_name

        # Initialize state
        init_agent_state = self.propagator.create_initial_state(
            company_name, trade_date
        )
        args = self.propagator.get_graph_args()
        args["config"]["callbacks"] = [self.llm_call_tracker]

        if self.debug:
            # Debug mode with tracing
            trace = []
            for chunk in self.graph.stream(init_agent_state, **args):
                if len(chunk["messages"]) == 0:
                    pass
                else:
                    chunk["messages"][-1].pretty_print()
                    trace.append(chunk)

            final_state = trace[-1]
        else:
            # Standard mode without tracing
            final_state = self.graph.invoke(init_agent_state, **args)

        # Store current state for reflection
        self.curr_state = final_state

        # Log state
        self._log_state(trade_date, final_state)

        # Return decision and processed signal
        return final_state, self.process_signal(final_state["final_trade_decision"])

    def _log_state(self, trade_date, final_state):
        """Log the final state to a JSON file."""
        self.log_states_dict[str(trade_date)] = {
            "company_of_interest": final_state["company_of_interest"],
            "trade_date": final_state["trade_date"],
            "technical_report": final_state["technical_report"],
            "onchain_report": final_state["onchain_report"],
            "tokenomics_report": final_state["tokenomics_report"],
            "sentiment_news_report": final_state["sentiment_news_report"],
            "investment_debate_state": {
                "bull_history": final_state["investment_debate_state"]["bull_history"],
                "bear_history": final_state["investment_debate_state"]["bear_history"],
                "history": final_state["investment_debate_state"]["history"],
                "current_response": final_state["investment_debate_state"][
                    "current_response"
                ],
                "judge_decision": final_state["investment_debate_state"][
                    "judge_decision"
                ],
            },
            "trader_investment_decision": final_state["trader_investment_plan"],
            "risk_debate_state": {
                "risky_history": final_state["risk_debate_state"]["risky_history"],
                "safe_history": final_state["risk_debate_state"]["safe_history"],
                "neutral_history": final_state["risk_debate_state"]["neutral_history"],
                "history": final_state["risk_debate_state"]["history"],
                "judge_decision": final_state["risk_debate_state"]["judge_decision"],
            },
            "investment_plan": final_state["investment_plan"],
            "final_trade_decision": final_state["final_trade_decision"],
        }

        # Save to file
        directory = Path(f"eval_results/{self.ticker}/DeFiTradingAgents_logs/")
        directory.mkdir(parents=True, exist_ok=True)

        with open(
            f"eval_results/{self.ticker}/DeFiTradingAgents_logs/full_states_log_{trade_date}.json",
            "w",
        ) as f:
            json.dump(self.log_states_dict, f, indent=4)

    def reflect_and_remember(self, returns_losses):
        """Reflect on decisions and update memory based on returns."""
        self.reflector.reflect_bull_researcher(
            self.curr_state, returns_losses, self.bull_memory
        )
        self.reflector.reflect_bear_researcher(
            self.curr_state, returns_losses, self.bear_memory
        )
        self.reflector.reflect_trader(
            self.curr_state, returns_losses, self.trader_memory
        )
        self.reflector.reflect_invest_judge(
            self.curr_state, returns_losses, self.invest_judge_memory
        )
        self.reflector.reflect_risk_manager(
            self.curr_state, returns_losses, self.risk_manager_memory
        )

    def calibrate_and_size(
        self, payoff_ratio, capital, venue_liquidity_usd=None, cost_estimator=None, max_execution_cost_bps=50.0
    ):
        """Stage 4 + 5: calibrate the most recent propagate() call's trader
        confidence and size a position against it. Call this after
        propagate(), before reflect_and_remember() records the outcome
        (recording first would leak this decision's own outcome into its
        own calibration -- see ReflectionACEAgent.record_outcome_and_refit).

        cost_estimator: optional USD-size -> bps callable (e.g. a closure
        around the target venue's simulate_trade(), see PositionSizer's
        docstring) so sizing respects real, size-conditional execution cost
        rather than only the flat venue_liquidity_usd fraction -- see
        literature/Solidus Labs Report - The Ex Files.pdf.
        """
        raw_confidence = self.curr_state.get("raw_confidence") if self.curr_state else None
        return self.ace_agent.calibrate_and_size(
            raw_confidence, payoff_ratio, capital, venue_liquidity_usd, cost_estimator, max_execution_cost_bps
        )

    def record_outcome_and_refit(self, was_correct):
        """Outcome-time: feed the most recent decision's confidence + realized
        outcome back into the Stage 4 calibrator. Call after the outcome is
        actually known (e.g. alongside reflect_and_remember(), not before).
        """
        raw_confidence = self.curr_state.get("raw_confidence") if self.curr_state else None
        if raw_confidence is None:
            return
        self.ace_agent.record_outcome_and_refit(raw_confidence, was_correct)

    def process_signal(self, full_signal):
        """Process a signal to extract the core decision."""
        return self.signal_processor.process_signal(full_signal)

    def get_llm_call_stats(self):
        """P6 instrumentation: call count, cumulative latency, and total
        tokens (if the provider reports usage_metadata) across every LLM
        call made since the last reset_llm_call_stats() -- i.e. typically
        one full propagate() run's worth of analyst tool-calling loops,
        debate rounds, trader, and risk judge calls combined."""
        return self.llm_call_tracker.summary()

    def get_llm_call_details(self):
        """Per-call breakdown (model, langgraph_node if available, input/
        output/total tokens, latency), in execution order, since the last
        reset_llm_call_stats()."""
        return list(self.llm_call_tracker.calls)

    def reset_llm_call_stats(self):
        """Call before propagate() if you want stats scoped to exactly that
        run (the tracker is otherwise cumulative across the graph object's
        lifetime, which would conflate multiple decisions)."""
        self.llm_call_tracker.reset()

    def build_single_agent_baseline(self, use_memory=True):
        """P6 ablation: construct a SingleAgentBaseline using the same LLM
        class the production Trader node uses (quick_thinking_llm -- see
        graph/setup.py's create_trader call) for a fair cost/latency
        comparison, sharing this graph's LLM call tracker so both arms'
        stats are captured the same way. use_memory=True (default) gives it
        the same trader_memory past-lessons lookup trader.py uses, so the
        comparison isolates debate structure, not "debate + memory vs.
        neither" -- see tradingagents/ablation/single_agent_baseline.py.
        """
        return SingleAgentBaseline(
            self.quick_thinking_llm,
            memory=self.trader_memory if use_memory else None,
            tracker=self.llm_call_tracker,
        )
