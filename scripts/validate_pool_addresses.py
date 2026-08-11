#!/usr/bin/env python
"""
Validate all 10 Uniswap v3 pool addresses used in the FC27 panel.

For each pool in contracts.py UNISWAP_V3_POOLS:
1. Calls Factory.getPool(token0, token1, fee) to confirm the hardcoded address
   matches the on-chain deployment
2. Reads pool.token0() and pool.token1() to verify token ordering
3. Reads pool.liquidity() to confirm non-zero in-range depth

Usage:
    python scripts/validate_pool_addresses.py
    python scripts/validate_pool_addresses.py --block 20000000
"""

import argparse
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from dotenv import load_dotenv
from web3 import Web3

load_dotenv()

from tradingagents.dataflows.onchain.contracts import UNISWAP_V3_POOLS, ERC20_TOKENS

UNISWAP_V3_FACTORY = "0x1F98431c8aD98523631AE4a59f267346ea31F984"

FACTORY_ABI = [
    {
        "inputs": [
            {"name": "tokenA", "type": "address"},
            {"name": "tokenB", "type": "address"},
            {"name": "fee",    "type": "uint24"},
        ],
        "name": "getPool",
        "outputs": [{"name": "pool", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    }
]

POOL_META_ABI = [
    {"inputs": [], "name": "token0",    "outputs": [{"name": "", "type": "address"}], "stateMutability": "view", "type": "function"},
    {"inputs": [], "name": "token1",    "outputs": [{"name": "", "type": "address"}], "stateMutability": "view", "type": "function"},
    {"inputs": [], "name": "fee",       "outputs": [{"name": "", "type": "uint24"}],  "stateMutability": "view", "type": "function"},
    {"inputs": [], "name": "liquidity", "outputs": [{"name": "", "type": "uint128"}], "stateMutability": "view", "type": "function"},
    {
        "inputs": [],
        "name": "slot0",
        "outputs": [
            {"name": "sqrtPriceX96", "type": "uint160"},
            {"name": "tick", "type": "int24"},
            {"name": "observationIndex", "type": "uint16"},
            {"name": "observationCardinality", "type": "uint16"},
            {"name": "observationCardinalityNext", "type": "uint16"},
            {"name": "feeProtocol", "type": "uint8"},
            {"name": "unlocked", "type": "bool"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
]

# Build reverse lookup: address → symbol for all known ERC20s + USDC
_ADDR_TO_SYM: dict[str, str] = {
    v["address"].lower(): k for k, v in ERC20_TOKENS.items()
}
_ADDR_TO_SYM["0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"] = "USDC"


def _sym(addr: str) -> str:
    return _ADDR_TO_SYM.get(addr.lower(), addr[:8] + "...")


def validate_all(block: int | None = None) -> bool:
    rpc_url = os.getenv("ONCHAIN_RPC_URL")
    if not rpc_url:
        print("ERROR: ONCHAIN_RPC_URL not set in .env")
        return False

    w3 = Web3(Web3.HTTPProvider(rpc_url))
    if not w3.is_connected():
        print("ERROR: could not connect to RPC")
        return False

    factory = w3.eth.contract(
        address=Web3.to_checksum_address(UNISWAP_V3_FACTORY),
        abi=FACTORY_ABI,
    )

    block_kwarg = {"block_identifier": block} if block else {}
    current_block = block or w3.eth.block_number
    print(f"Validating {len(UNISWAP_V3_POOLS)} pools at block {current_block}\n")

    all_pass = True
    for pool_key, cfg in UNISWAP_V3_POOLS.items():
        hardcoded = Web3.to_checksum_address(cfg["address"])
        fee_bps   = cfg["fee_tier_bps"]
        fee_units = fee_bps * 100  # bps → Uniswap fee units (e.g., 30 bps → 3000)
        t0_sym    = cfg["token0_symbol"]
        t1_sym    = cfg["token1_symbol"]

        # Resolve token addresses for Factory call
        def _addr(sym: str) -> str:
            if sym == "USDC":
                return "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
            if sym == "WETH":
                sym = "ETH"
            return ERC20_TOKENS[sym]["address"]

        t0_addr = _addr(t0_sym)
        t1_addr = _addr(t1_sym)

        pool_contract = w3.eth.contract(address=hardcoded, abi=POOL_META_ABI)

        issues = []

        # 1. Factory address check
        try:
            factory_addr = factory.functions.getPool(
                Web3.to_checksum_address(t0_addr),
                Web3.to_checksum_address(t1_addr),
                fee_units,
            ).call(**block_kwarg)
            if factory_addr.lower() != hardcoded.lower():
                issues.append(f"Factory mismatch: expected {hardcoded}, got {factory_addr}")
        except Exception as e:
            issues.append(f"Factory call failed: {e}")

        # 2. On-chain token0/token1 ordering
        try:
            on_t0 = pool_contract.functions.token0().call(**block_kwarg)
            on_t1 = pool_contract.functions.token1().call(**block_kwarg)
            on_t0_sym = _sym(on_t0)
            on_t1_sym = _sym(on_t1)
            if on_t0.lower() != t0_addr.lower():
                issues.append(
                    f"token0 mismatch: config says {t0_sym} ({t0_addr[:8]}...), "
                    f"on-chain says {on_t0_sym} ({on_t0[:8]}...)"
                )
        except Exception as e:
            issues.append(f"token0/1 call failed: {e}")
            on_t0_sym, on_t1_sym = "?", "?"

        # 3. Liquidity check
        try:
            liq = pool_contract.functions.liquidity().call(**block_kwarg)
            if liq == 0:
                issues.append("liquidity() == 0 (no in-range liquidity at this block)")
        except Exception as e:
            issues.append(f"liquidity() call failed: {e}")
            liq = None

        # 4. Spot price sanity
        try:
            slot0 = pool_contract.functions.slot0().call(**block_kwarg)
            sqrt_p = slot0[0]
            raw = (sqrt_p / (2 ** 96)) ** 2
            price = raw * (10 ** (cfg["token0_decimals"] - cfg["token1_decimals"]))
        except Exception as e:
            issues.append(f"slot0 call failed: {e}")
            price = None

        status = "PASS" if not issues else "FAIL"
        liq_str   = f"{liq:,}" if liq is not None else "?"
        price_str = f"{price:.6g}" if price is not None else "?"

        print(f"[{status}] {pool_key}")
        print(f"       address:   {hardcoded}")
        print(f"       fee:       {fee_units} ({fee_bps} bps)")
        print(f"       on-chain:  {on_t0_sym}/{on_t1_sym}")
        print(f"       liq:       {liq_str}")
        print(f"       price(t1/t0): {price_str}")
        if issues:
            for iss in issues:
                print(f"       !! {iss}")
            all_pass = False
        print()

    print("=" * 60)
    print(f"Result: {'ALL PASS' if all_pass else 'FAILURES DETECTED'}")
    return all_pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--block", type=int, default=None,
                        help="Block number to validate at (default: latest)")
    args = parser.parse_args()
    ok = validate_all(args.block)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
