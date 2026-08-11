"""
Phase 5 Week 20: TEE PoC -- execution-layer attestation, feasibility demo
only (1 venue, short window, per the build plan's own scope). Deployed via
Phala Cloud / dstack (https://github.com/Dstack-TEE/dstack).

Scope, stated precisely because it's easy to overclaim with TEE demos: this
attests that the POSITION-SIZING/EXECUTION-DISPATCH code ran unmodified
given a specific input and produced a specific output. It does NOT attest
the LLM's reasoning -- that's a remote call to OpenAI's API, a black box
this project has no way to run inside a TEE or get attested without
OpenAI's own cooperation. The claim here is narrower and real: "this code,
this input, this output, inside this enclave" -- not "this decision was
reasoned about correctly."

sizing.py in this directory is a byte-for-byte vendored copy of
tradingagents/calibration/sizing.py -- copied rather than imported so the
container doesn't need the rest of the tradingagents package's heavier
dependencies (web3, langchain, etc.) inside the enclave. The code_hash
computed below is over THIS copy; scripts/run_tee_poc_demo.py separately
verifies it still matches the canonical source before trusting a quote.
"""

import hashlib
import inspect
import json
import os
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from sizing import PositionSizer

app = FastAPI()

_SIZING_SOURCE = inspect.getsource(PositionSizer)
CODE_HASH = hashlib.sha256(_SIZING_SOURCE.encode()).hexdigest()


class SizingRequest(BaseModel):
    decision_id: str
    calibrated_probability: float
    payoff_ratio: float
    capital: float
    venue_liquidity_usd: Optional[float] = None
    venue_liquidity_cap_fraction: float = 0.01


def _get_quote(report_data: bytes) -> dict:
    """Returns the real TDX quote when running inside dstack (real Phala
    Cloud deployment or the local dstack-simulator with
    DSTACK_SIMULATOR_ENDPOINT set) -- and an explicit, clearly-flagged
    "unavailable" response otherwise, rather than fabricating one. A caller
    must check attestation_available before trusting a quote field."""
    try:
        from dstack_sdk import DstackClient
        client = DstackClient()
        quote = client.get_quote(report_data)
        return {
            "attestation_available": True,
            "quote": quote.quote,
            "event_log": quote.event_log,
            "report_data": quote.report_data,
        }
    except Exception as e:
        return {
            "attestation_available": False,
            "reason": f"no TEE runtime reachable ({type(e).__name__}: {e})",
        }


@app.post("/attest_sizing")
def attest_sizing(req: SizingRequest):
    sizer = PositionSizer()
    result = sizer.size_position(
        calibrated_probability=req.calibrated_probability,
        payoff_ratio=req.payoff_ratio,
        capital=req.capital,
        venue_liquidity_usd=req.venue_liquidity_usd,
        venue_liquidity_cap_fraction=req.venue_liquidity_cap_fraction,
    )

    # report_data binds the attestation to THIS specific (input, output,
    # code_hash) triple -- a tampered host returning a different output
    # can't reuse a genuine quote, since the quote itself commits to a
    # hash that would no longer match.
    commitment = {
        "decision_id": req.decision_id,
        "input": req.model_dump(),
        "output": result,
        "code_hash": CODE_HASH,
    }
    report_data = hashlib.sha256(json.dumps(commitment, sort_keys=True).encode()).digest()
    attestation = _get_quote(report_data)

    return {
        "decision_id": req.decision_id,
        "input": req.model_dump(),
        "output": result,
        "code_hash": CODE_HASH,
        "commitment_hash": report_data.hex(),
        "attestation": attestation,
    }


@app.get("/health")
def health():
    return {"status": "ok", "code_hash": CODE_HASH, "in_tee": os.path.exists("/var/run/dstack.sock")}
