"""
P6 (multi-agent disaggregation) instrumentation -- Alpha Illusion's P6
minimum reporting includes "debate-round cost" and "coordination latency".
This counts real LLM calls and measures real wall-clock latency across an
entire graph.propagate() run (or a single-agent baseline call), without
modifying any individual agent node file.

Mechanism: LangChain callbacks attached via `llm.with_config({"callbacks":
[tracker]})` at construction time propagate through `.bind()`,
`.bind_tools()`, and prompt-pipe (`prompt | llm`) composition -- verified
empirically against langchain_core's FakeListChatModel before relying on it
here (see PROGRESS_LOG.md), since this project's node files use several
different invocation styles (direct `.invoke()`, `.bind_tools()`, and pipe
composition) and the callback needs to survive all of them without each
node file being touched individually.

Token usage is reported best-effort: not every provider/model populates
`usage_metadata` (notably some streaming or third-party-routed calls don't).
When any call in a tracked window is missing it, `total_tokens` is reported
as None rather than a silently-undercounted number.
"""

import time
from typing import Dict, List, Optional
from uuid import UUID

from langchain_core.callbacks.base import BaseCallbackHandler


class LLMCallTracker(BaseCallbackHandler):
    def __init__(self):
        super().__init__()
        self._start_times: Dict[UUID, float] = {}
        self._pending: Dict[UUID, Dict] = {}
        self.call_count = 0
        self.total_latency_s = 0.0
        self.total_tokens = 0
        self._tokens_available = True
        self.calls: List[Dict] = []  # per-call record, in execution order

    def reset(self) -> None:
        self._start_times.clear()
        self._pending.clear()
        self.call_count = 0
        self.total_latency_s = 0.0
        self.total_tokens = 0
        self._tokens_available = True
        self.calls = []

    def on_chat_model_start(self, serialized, messages, *, run_id, tags=None, metadata=None, **kwargs) -> None:
        self._start_times[run_id] = time.monotonic()
        self._pending[run_id] = {
            "model": (metadata or {}).get("ls_model_name") or (serialized or {}).get("kwargs", {}).get("model_name"),
            "langgraph_node": (metadata or {}).get("langgraph_node"),
        }

    def on_llm_start(self, serialized, prompts, *, run_id, tags=None, metadata=None, **kwargs) -> None:
        self._start_times[run_id] = time.monotonic()
        self._pending[run_id] = {
            "model": (metadata or {}).get("ls_model_name") or (serialized or {}).get("kwargs", {}).get("model_name"),
            "langgraph_node": (metadata or {}).get("langgraph_node"),
        }

    def on_llm_end(self, response, *, run_id, **kwargs) -> None:
        self.call_count += 1
        start = self._start_times.pop(run_id, None)
        latency = (time.monotonic() - start) if start is not None else None
        if latency is not None:
            self.total_latency_s += latency

        input_tokens, output_tokens, total_tokens = self._extract_tokens(response)
        if total_tokens is None:
            self._tokens_available = False
        else:
            self.total_tokens += total_tokens

        record = self._pending.pop(run_id, {})
        record.update({
            "latency_s": round(latency, 3) if latency is not None else None,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "total_tokens": total_tokens,
        })
        self.calls.append(record)

    @staticmethod
    def _extract_tokens(response):
        """Returns (input_tokens, output_tokens, total_tokens), any of which may be None."""
        llm_output = getattr(response, "llm_output", None) or {}
        usage = llm_output.get("token_usage") or llm_output.get("usage")
        if usage and "total_tokens" in usage:
            return usage.get("prompt_tokens"), usage.get("completion_tokens"), usage["total_tokens"]

        for gen_list in getattr(response, "generations", []) or []:
            for gen in gen_list:
                message = getattr(gen, "message", None)
                meta = getattr(message, "usage_metadata", None) if message else None
                if meta and meta.get("total_tokens") is not None:
                    return meta.get("input_tokens"), meta.get("output_tokens"), meta["total_tokens"]
        return None, None, None

    def summary(self) -> Dict:
        return {
            "call_count": self.call_count,
            "total_latency_s": round(self.total_latency_s, 3),
            "total_tokens": self.total_tokens if self._tokens_available else None,
        }
