"""
Fork-simulated execution (Mode 2) -- Phase 2 Week 7.

Spins up a local Anvil fork at a specific historical block and replays a
trade as a real transaction against real forked contract state: real gas,
real slippage, real revert behavior. This is what gives Alpha Illusion's P5
(realistic implementation) literal teeth, instead of a parametric cost model
or the same-tick approximation in venues.py's simulate_trade().

Requires Foundry (`anvil`) installed locally, and ONCHAIN_RPC_URL pointing at
an archive-capable RPC provider (Alchemy/Infura free tier) -- public RPC
endpoints only serve ~100 blocks of history (Phase 2 Week 5 finding) and
cannot fork at arbitrary historical blocks.
"""

import os
import subprocess
import time
from typing import Optional

from web3 import Web3

WETH9_ADDRESS = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
SWAP_ROUTER02_ADDRESS = "0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45"
USDC_ADDRESS = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"

POOL_SLOT0_ABI = [
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
    {
        "inputs": [],
        "name": "liquidity",
        "outputs": [{"name": "", "type": "uint128"}],
        "stateMutability": "view",
        "type": "function",
    },
]

# Binance hot wallet, used only as an impersonated USDC funding source for
# BUY-side (USDC->WETH) pilot trades on the fork. Verified to hold
# $179M-$292M USDC across the entire 2022-2023 backtest window (see
# PROGRESS_LOG.md 2026-06-21) -- not used for anything beyond funding a test
# account, never a real transaction on real mainnet.
USDC_WHALE_ADDRESS = "0x28C6c06298d514Db089934071355E5743bf21d60"

WETH9_ABI = [
    {"inputs": [], "name": "deposit", "outputs": [], "stateMutability": "payable", "type": "function"},
    {
        "inputs": [{"name": "spender", "type": "address"}, {"name": "amount", "type": "uint256"}],
        "name": "approve",
        "outputs": [{"name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"name": "account", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
]

ERC20_ABI = [
    {
        "inputs": [{"name": "account", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"name": "to", "type": "address"}, {"name": "amount", "type": "uint256"}],
        "name": "transfer",
        "outputs": [{"name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"name": "spender", "type": "address"}, {"name": "amount", "type": "uint256"}],
        "name": "approve",
        "outputs": [{"name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]

SWAP_ROUTER02_ABI = [
    {
        "inputs": [
            {
                "components": [
                    {"name": "tokenIn", "type": "address"},
                    {"name": "tokenOut", "type": "address"},
                    {"name": "fee", "type": "uint24"},
                    {"name": "recipient", "type": "address"},
                    {"name": "amountIn", "type": "uint256"},
                    {"name": "amountOutMinimum", "type": "uint256"},
                    {"name": "sqrtPriceLimitX96", "type": "uint160"},
                ],
                "name": "params",
                "type": "tuple",
            }
        ],
        "name": "exactInputSingle",
        "outputs": [{"name": "amountOut", "type": "uint256"}],
        "stateMutability": "payable",
        "type": "function",
    },
]


class AnvilFork:
    """Context manager: spins up `anvil --fork-url ... --fork-block-number ...`,
    yields a connected Web3 instance, tears the process down on exit."""

    def __init__(self, fork_block: int, port: int = 8546, rpc_url: Optional[str] = None):
        self.fork_block = fork_block
        self.port = port
        self.rpc_url = rpc_url or os.getenv("ONCHAIN_RPC_URL")
        if not self.rpc_url:
            raise ValueError("AnvilFork needs an archive-capable RPC URL (set ONCHAIN_RPC_URL in .env)")
        self.process: Optional[subprocess.Popen] = None

    def __enter__(self) -> Web3:
        self.process = subprocess.Popen(
            [
                "anvil",
                "--fork-url", self.rpc_url,
                "--fork-block-number", str(self.fork_block),
                "--port", str(self.port),
                "--silent",
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        w3 = Web3(Web3.HTTPProvider(f"http://127.0.0.1:{self.port}"))
        for _ in range(60):
            if self.process.poll() is not None:
                raise RuntimeError(f"anvil exited early with code {self.process.returncode}")
            try:
                if w3.is_connected():
                    w3.eth.block_number
                    return w3
            except Exception:
                pass
            time.sleep(0.5)
        raise RuntimeError("Anvil fork did not become ready in time")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.process:
            self.process.terminate()
            try:
                self.process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                self.process.kill()


def spot_price_from_slot0(
    w3: Web3,
    pool_address: str,
    token0_decimals: int,
    token1_decimals: int,
) -> dict:
    """Read the current tick price from a Uniswap v3 pool's slot0.

    Returns the instant price (token1 per token0 and token0 per token1 in human
    units) plus raw in-range liquidity. This is the pre-trade reference price
    the experiment design calls spot_price_at_block.

    Note: this is an instant price from slot0, not a TWAP. A proper 30-min
    TWAP would require pool.observe() with two timestamps, which needs the pool
    to have oracle observations stored -- not guaranteed for all pools at all
    historical blocks. The instant price is the correct approach for fork-sim
    where we control the exact block and can compare pre-swap vs post-swap.
    """
    pool = w3.eth.contract(
        address=Web3.to_checksum_address(pool_address),
        abi=POOL_SLOT0_ABI,
    )
    sqrt_price_x96, tick, *_ = pool.functions.slot0().call()
    liquidity = pool.functions.liquidity().call()

    raw_price_t1_per_t0 = (sqrt_price_x96 / (2 ** 96)) ** 2
    price_t1_per_t0 = raw_price_t1_per_t0 * (10 ** (token0_decimals - token1_decimals))
    price_t0_per_t1 = 1 / price_t1_per_t0 if price_t1_per_t0 else None

    return {
        "sqrt_price_x96": sqrt_price_x96,
        "tick": tick,
        "price_t1_per_t0": price_t1_per_t0,
        "price_t0_per_t1": price_t0_per_t1,
        "liquidity_in_range": liquidity,
    }


def _impersonate_with_gas(w3: Web3, address: str, eth_for_gas: float = 1.0) -> None:
    w3.provider.make_request("anvil_impersonateAccount", [address])
    w3.provider.make_request("anvil_setBalance", [address, hex(w3.to_wei(eth_for_gas, "ether"))])


def simulate_spot_trade(w3: Web3, sell_token: str, amount_in: float, fee_tier: int = 500) -> dict:
    """Replay a WETH<->USDC swap as a real transaction on a forked chain.

    sell_token="WETH": funds the trader by wrapping ETH (anvil's dev account
    is pre-funded with 10000 ETH, no impersonation needed).
    sell_token="USDC": funds the trader by impersonating USDC_WHALE_ADDRESS
    and transferring USDC -- only ever used against a local fork, never a
    real transaction on real mainnet.

    fee_tier is in Uniswap's units (hundredths of a bip): 500 = 0.05%.
    amount_in is in human units of sell_token (ETH or USDC).
    """
    trader = w3.eth.accounts[0]
    weth = w3.eth.contract(address=Web3.to_checksum_address(WETH9_ADDRESS), abi=WETH9_ABI)
    usdc = w3.eth.contract(address=Web3.to_checksum_address(USDC_ADDRESS), abi=ERC20_ABI)
    router = w3.eth.contract(address=Web3.to_checksum_address(SWAP_ROUTER02_ADDRESS), abi=SWAP_ROUTER02_ABI)

    if sell_token == "WETH":
        token_in, token_out = WETH9_ADDRESS, USDC_ADDRESS
        amount_in_wei = w3.to_wei(amount_in, "ether")
        in_contract, out_contract, out_decimals = weth, usdc, 6

        tx_hash = weth.functions.deposit().transact({"from": trader, "value": amount_in_wei})
        w3.eth.wait_for_transaction_receipt(tx_hash)

    elif sell_token == "USDC":
        token_in, token_out = USDC_ADDRESS, WETH9_ADDRESS
        amount_in_wei = int(amount_in * 1e6)
        in_contract, out_contract, out_decimals = usdc, weth, 18

        whale = Web3.to_checksum_address(USDC_WHALE_ADDRESS)
        _impersonate_with_gas(w3, whale)
        whale_balance = usdc.functions.balanceOf(whale).call()
        if whale_balance < amount_in_wei:
            raise RuntimeError(f"USDC whale balance ({whale_balance / 1e6:.2f}) insufficient for trade ({amount_in})")
        tx_hash = usdc.functions.transfer(trader, amount_in_wei).transact({"from": whale})
        w3.eth.wait_for_transaction_receipt(tx_hash)

    else:
        raise ValueError(f"sell_token must be 'WETH' or 'USDC', got {sell_token!r}")

    tx_hash = in_contract.functions.approve(SWAP_ROUTER02_ADDRESS, amount_in_wei).transact({"from": trader})
    w3.eth.wait_for_transaction_receipt(tx_hash)

    amount_out_before = out_contract.functions.balanceOf(trader).call()

    params = (
        Web3.to_checksum_address(token_in),
        Web3.to_checksum_address(token_out),
        fee_tier,
        trader,
        amount_in_wei,
        0,  # amountOutMinimum -- fine for a measurement harness, never for real funds
        0,  # sqrtPriceLimitX96 -- no limit
    )
    tx_hash = router.functions.exactInputSingle(params).transact({"from": trader})
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    amount_out_after = out_contract.functions.balanceOf(trader).call()
    amount_out = (amount_out_after - amount_out_before) / (10 ** out_decimals)

    return {
        "sell_token": sell_token,
        "amount_in": amount_in,
        "amount_out": amount_out,
        "gas_used": receipt["gasUsed"],
        "tx_status": receipt["status"],
    }


def simulate_weth_pair_trade(
    w3: Web3,
    token_address: str,
    token_decimals: int,
    side: str,
    amount_in: float,
    fee_tier: int,
    amount_in_token_units: Optional[int] = None,
) -> dict:
    """Replay a WETH<->TOKEN swap as a real transaction on a forked chain,
    for any ERC20 paired against WETH (generalizes simulate_spot_trade,
    which is WETH/USDC-specific, to UNI/WETH, AAVE/WETH, etc. -- Phase 5
    Week 18 Mode 2).

    side="buy": acquire `token` by selling WETH, funded by wrapping ETH
        (anvil's dev account is pre-funded, no impersonation needed).
    side="sell": sell `token` for WETH. No whale impersonation -- this is
        designed to be called with the trader's EXISTING token balance from
        a prior "buy" leg in the same fork session (amount_in_token_units
        lets the caller pass the exact wei-precision output of that buy leg
        rather than a human-units float subject to rounding). Finding and
        verifying a real UNI/AAVE whale address at each specific historical
        block was judged unnecessary complexity for a case-study scope; a
        buy-then-sell round trip gives equally real gas/slippage data for
        the sell leg without it.
    """
    trader = w3.eth.accounts[0]
    weth = w3.eth.contract(address=Web3.to_checksum_address(WETH9_ADDRESS), abi=WETH9_ABI)
    token = w3.eth.contract(address=Web3.to_checksum_address(token_address), abi=ERC20_ABI)
    router = w3.eth.contract(address=Web3.to_checksum_address(SWAP_ROUTER02_ADDRESS), abi=SWAP_ROUTER02_ABI)

    if side == "buy":
        token_in, token_out = WETH9_ADDRESS, token_address
        amount_in_wei = w3.to_wei(amount_in, "ether")
        in_contract, out_contract, out_decimals = weth, token, token_decimals

        tx_hash = weth.functions.deposit().transact({"from": trader, "value": amount_in_wei})
        w3.eth.wait_for_transaction_receipt(tx_hash)

    elif side == "sell":
        token_in, token_out = token_address, WETH9_ADDRESS
        amount_in_wei = amount_in_token_units if amount_in_token_units is not None else int(amount_in * (10 ** token_decimals))
        in_contract, out_contract, out_decimals = token, weth, 18

    else:
        raise ValueError(f"side must be 'buy' or 'sell', got {side!r}")

    tx_hash = in_contract.functions.approve(SWAP_ROUTER02_ADDRESS, amount_in_wei).transact({"from": trader})
    w3.eth.wait_for_transaction_receipt(tx_hash)

    amount_out_before = out_contract.functions.balanceOf(trader).call()

    params = (
        Web3.to_checksum_address(token_in),
        Web3.to_checksum_address(token_out),
        fee_tier,
        trader,
        amount_in_wei,
        0,  # amountOutMinimum -- fine for a measurement harness, never for real funds
        0,  # sqrtPriceLimitX96 -- no limit
    )
    tx_hash = router.functions.exactInputSingle(params).transact({"from": trader})
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    amount_out_after = out_contract.functions.balanceOf(trader).call()
    amount_out_raw = amount_out_after - amount_out_before
    amount_out = amount_out_raw / (10 ** out_decimals)

    return {
        "side": side,
        "amount_in": amount_in_wei / (10 ** (18 if side == "buy" else token_decimals)),
        "amount_out": amount_out,
        "amount_out_raw": amount_out_raw,
        "gas_used": receipt["gasUsed"],
        "tx_status": receipt["status"],
    }
