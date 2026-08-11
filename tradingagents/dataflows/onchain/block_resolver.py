"""
Resolve a calendar date to the closest Ethereum mainnet block, via binary
search on block timestamps (real direct-RPC calls, no third-party API).

Used by Phase 5 Week 18's historical Mode 1 backtest panel to give the
on-chain analyst's tools (liquidity, supply) a genuine point-in-time read
instead of always reading current chain state -- the same method already
used and verified (2026-06-22) for the token-selection market-cap check, now
made reusable.
"""

from datetime import date, datetime, timezone
from functools import lru_cache
from typing import Union

from tradingagents.dataflows.onchain.rpc import get_web3


@lru_cache(maxsize=512)
def resolve_block_for_date(target_date: Union[str, date]) -> int:
    """Return the first Ethereum block whose timestamp is >= midnight UTC on
    target_date. Cached -- repeated calls for the same date cost one cache
    hit, not one binary search."""
    if isinstance(target_date, str):
        target_date = date.fromisoformat(target_date)

    target_ts = int(datetime(target_date.year, target_date.month, target_date.day, tzinfo=timezone.utc).timestamp())

    w3 = get_web3()
    lo, hi = 1, w3.eth.block_number
    while lo < hi:
        mid = (lo + hi) // 2
        if w3.eth.get_block(mid).timestamp < target_ts:
            lo = mid + 1
        else:
            hi = mid
    return lo
