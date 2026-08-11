"""
Dune Analytics client for the on-chain data this project's own RPC layer
can't get cheaply -- holder concentration and DEX volume, both of which
need an indexer scanning full transaction/transfer history, not a handful
of contract reads.

Note on text parameters: Dune substitutes {{param}} directly into the SQL
text with no added quoting, so a hex address param must be wrapped in
single quotes in the SQL itself (from_hex('{{token_address}}')) and passed
without a leading "0x" -- confirmed by testing live (an unquoted address
was parsed as a varbinary literal by Dune's Trino engine and broke
string functions; a quoted one with a "0x" prefix was parsed as a bare,
unresolvable column identifier).

Setup:
1. Free account at dune.com, API key from Settings > API.
2. Write (or find a public) parameterized SQL query for the metric you want,
   save it, note its query ID. Creating a query via the API itself needs at
   least some paid plan tier on some accounts -- but this is account-specific,
   not a blanket free-tier restriction (confirmed 2026-06-21: this project's
   account can create+update queries via the API, see scripts/dune_queries.py).
3. Set DUNE_API_KEY in .env and pass the query ID to execute_query().
"""

import os
import time
from typing import Dict, Optional

import requests
from dotenv import load_dotenv

load_dotenv()

DUNE_API_BASE = "https://api.dune.com/api/v1"


class DuneError(Exception):
    pass


def execute_query(query_id: int, params: Optional[Dict] = None, poll_timeout_s: float = 60.0, poll_interval_s: float = 2.0) -> Dict:
    """Execute a saved Dune query by ID and return its latest result rows.

    Polls for completion -- these queries (full transfer/swap history scans)
    routinely take 10-30+ seconds, so a single immediate results fetch right
    after submitting (the original implementation) reliably saw
    QUERY_STATE_PENDING/EXECUTING and raised, even though the query itself
    was working correctly. Caught by testing live, not by inspection.
    """
    api_key = os.getenv("DUNE_API_KEY")
    if not api_key:
        raise DuneError(
            "DUNE_API_KEY not set. Get a free key at https://dune.com/settings/api "
            "and add it to .env. You'll also need a saved query ID -- see "
            "this module's docstring."
        )

    headers = {"X-DUNE-API-KEY": api_key}
    execute_resp = requests.post(
        f"{DUNE_API_BASE}/query/{query_id}/execute",
        headers=headers,
        json={"query_parameters": params or {}},
        timeout=30,
    )
    execute_resp.raise_for_status()
    execution_id = execute_resp.json()["execution_id"]

    deadline = time.monotonic() + poll_timeout_s
    payload = {}
    while time.monotonic() < deadline:
        result_resp = requests.get(
            f"{DUNE_API_BASE}/execution/{execution_id}/results",
            headers=headers,
            timeout=60,
        )
        result_resp.raise_for_status()
        payload = result_resp.json()
        if payload.get("is_execution_finished"):
            break
        time.sleep(poll_interval_s)

    state = payload.get("state")
    if state != "QUERY_STATE_COMPLETED":
        error_detail = payload.get("error", {}).get("message", "") if state == "QUERY_STATE_FAILED" else ""
        raise DuneError(f"Dune query {query_id} did not complete in {poll_timeout_s}s: {state} {error_detail}".strip())

    return {
        "query_id": query_id,
        "rows": payload.get("result", {}).get("rows", []),
        "metadata": payload.get("result", {}).get("metadata", {}),
    }
