"""
Shared Web3 RPC connection for the on-chain data layer (Track B).

Defaults to a free public Ethereum RPC endpoint so the venue/data connectors
work with zero setup. Set ONCHAIN_RPC_URL in .env to point at a dedicated
provider (Alchemy/Infura/etc.) for production reliability -- public endpoints
are rate-limited and not guaranteed to stay up.
"""

import os
from functools import lru_cache

from dotenv import load_dotenv
from web3 import Web3

load_dotenv()

PUBLIC_RPC_FALLBACKS = [
    "https://ethereum-rpc.publicnode.com",
    "https://eth.llamarpc.com",
]


@lru_cache(maxsize=1)
def get_web3() -> Web3:
    """Return a connected Web3 instance, trying ONCHAIN_RPC_URL first, then public fallbacks."""
    candidates = [os.getenv("ONCHAIN_RPC_URL")] if os.getenv("ONCHAIN_RPC_URL") else []
    candidates += PUBLIC_RPC_FALLBACKS

    last_error = None
    for rpc_url in candidates:
        try:
            w3 = Web3(Web3.HTTPProvider(rpc_url, request_kwargs={"timeout": 10}))
            if w3.is_connected():
                return w3
        except Exception as e:
            last_error = e
            continue

    raise ConnectionError(f"Could not connect to any RPC endpoint (tried {candidates}). Last error: {last_error}")


def block_at_timestamp(w3: Web3, target_ts: int) -> int:
    """Binary search for the block whose timestamp is closest to (and not
    after) target_ts. Used to map a historical decision date to a concrete
    block number for fork-sim."""
    low, high = 1, w3.eth.block_number
    while low < high:
        mid = (low + high + 1) // 2
        if w3.eth.get_block(mid)["timestamp"] <= target_ts:
            low = mid
        else:
            high = mid - 1
    return low
