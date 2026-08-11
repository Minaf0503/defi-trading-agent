"""
Generic ERC20 token reads (direct RPC, no third-party data API) -- the
real replacement for the get_token_onchain_data/get_token_supply pieces of
the fictional AgentKit-based OnchainAnalytics class (removed 2026-06-21,
see writing/papers/PROGRESS_LOG.md). Only covers tokens with a real
Ethereum mainnet ERC20 address -- see ERC20_TOKENS in contracts.py.
"""

from typing import Dict, Optional

from web3 import Web3

from tradingagents.dataflows.onchain.contracts import ERC20_ABI, ERC20_TOKENS
from tradingagents.dataflows.onchain.rpc import get_web3


def get_token_supply(token_symbol: str, block: Optional[int] = None) -> Dict:
    """Real on-chain total supply for a token, via direct ERC20.totalSupply() RPC call.

    Returns {"available": False, "reason": ...} for tokens with no Ethereum
    mainnet ERC20 address (SOL, ZEC, XMR in this project's token list) rather
    than guessing or erroring.
    """
    token = ERC20_TOKENS.get(token_symbol.upper())
    if token is None:
        return {
            "available": False,
            "reason": f"{token_symbol} has no Ethereum mainnet ERC20 address tracked in this project.",
        }

    w3 = get_web3()
    contract = w3.eth.contract(address=Web3.to_checksum_address(token["address"]), abi=ERC20_ABI)
    call_kwargs = {"block_identifier": block} if block is not None else {}
    raw_supply = contract.functions.totalSupply().call(**call_kwargs)

    return {
        "available": True,
        "token": token_symbol.upper(),
        "address": token["address"],
        "block": block if block is not None else w3.eth.block_number,
        "total_supply": raw_supply / (10 ** token["decimals"]),
        "note": token.get("note"),
    }
