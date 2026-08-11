"""
Venue abstraction for Track B (live on-chain state) -- see
writing/papers/draft.md Section 3.3-3.4.

Each Venue exposes get_state(block), simulate_trade(intent, block), and
cost_model(). `block=None` means "latest"; passing a specific block number
queries historical contract state as of that block, which is what the
fork-simulated execution layer (Phase 2 Week 7) and any backtest-time
on-chain feature will rely on.
"""

from abc import ABC, abstractmethod
from typing import Dict, Optional

from web3 import Web3

from tradingagents.dataflows.onchain import gmx_api
from tradingagents.dataflows.onchain.contracts import (
    CHAINLINK_AGGREGATOR_ABI,
    CHAINLINK_FEEDS,
    ERC4626_VAULT_ABI,
    MORPHO_VAULTS,
    UNISWAP_V3_POOL_ABI,
    UNISWAP_V3_POOLS,
)
from tradingagents.dataflows.onchain.rpc import get_web3


class Venue(ABC):
    @abstractmethod
    def get_state(self, block: Optional[int] = None) -> Dict:
        """Return the venue's current (or historical, if block is given) on-chain state."""

    @abstractmethod
    def simulate_trade(self, intent: Dict, block: Optional[int] = None) -> Dict:
        """Estimate the outcome of a trade intent against the venue's state at `block`."""

    @abstractmethod
    def cost_model(self) -> Dict:
        """Describe the venue's fee structure and what this estimate does/doesn't capture."""


class ChainlinkPriceFeed:
    """Reads a Chainlink price feed, optionally as of a historical block."""

    def __init__(self, pair: str):
        if pair not in CHAINLINK_FEEDS:
            raise ValueError(f"Unknown Chainlink feed: {pair!r}. Known: {list(CHAINLINK_FEEDS)}")
        self.pair = pair
        self.config = CHAINLINK_FEEDS[pair]
        self.w3 = get_web3()
        self.contract = self.w3.eth.contract(
            address=Web3.to_checksum_address(self.config["address"]),
            abi=CHAINLINK_AGGREGATOR_ABI,
        )

    def get_price(self, block: Optional[int] = None) -> Dict:
        call_kwargs = {"block_identifier": block} if block is not None else {}
        decimals = self.contract.functions.decimals().call(**call_kwargs)
        round_id, answer, started_at, updated_at, answered_in_round = self.contract.functions.latestRoundData().call(**call_kwargs)
        return {
            "pair": self.pair,
            "block": block if block is not None else self.w3.eth.block_number,
            "price": answer / (10 ** decimals),
            "updated_at": updated_at,
        }


class SpotDEXVenue(Venue):
    """Uniswap v3 pool, read directly via RPC (no subgraph dependency)."""

    def __init__(self, pool_key: str):
        if pool_key not in UNISWAP_V3_POOLS:
            raise ValueError(f"Unknown pool: {pool_key!r}. Known: {list(UNISWAP_V3_POOLS)}")
        self.pool_key = pool_key
        self.pool_config = UNISWAP_V3_POOLS[pool_key]
        self.w3 = get_web3()
        self.pool = self.w3.eth.contract(
            address=Web3.to_checksum_address(self.pool_config["address"]),
            abi=UNISWAP_V3_POOL_ABI,
        )

    def get_state(self, block: Optional[int] = None) -> Dict:
        call_kwargs = {"block_identifier": block} if block is not None else {}
        sqrt_price_x96, tick, *_ = self.pool.functions.slot0().call(**call_kwargs)
        liquidity = self.pool.functions.liquidity().call(**call_kwargs)

        d0 = self.pool_config["token0_decimals"]
        d1 = self.pool_config["token1_decimals"]
        sym0 = self.pool_config["token0_symbol"]
        sym1 = self.pool_config["token1_symbol"]

        raw_price_t1_per_t0 = (sqrt_price_x96 / (2 ** 96)) ** 2
        price_t1_per_t0 = raw_price_t1_per_t0 * (10 ** (d0 - d1))
        price_t0_per_t1 = 1 / price_t1_per_t0 if price_t1_per_t0 else None

        return {
            "venue": "uniswap_v3",
            "pool": self.pool_key,
            "block": block if block is not None else self.w3.eth.block_number,
            "sqrt_price_x96": sqrt_price_x96,
            "tick": tick,
            "liquidity": liquidity,
            "price": {
                f"{sym1}_per_{sym0}": price_t1_per_t0,
                f"{sym0}_per_{sym1}": price_t0_per_t1,
            },
        }

    def simulate_trade(self, intent: Dict, block: Optional[int] = None, state: Optional[Dict] = None) -> Dict:
        """Approximate a swap using the same-tick virtual-reserve constant
        product relationship x*y = L^2. This ignores tick-crossing, so it
        understates price impact for trades large enough to move out of the
        current tick. Real execution realism (gas, exact slippage,
        tick-crossing) comes from the Anvil fork-sim harness (Phase 2 Week 7)
        -- this is a cheap estimate for venue-selection logic, not a result.

        intent: {"sell_token": <symbol>, "amount_in": <float, human units>}
        state: pass an already-fetched get_state() result to skip the RPC
            call -- e.g. when a caller (sizing's cost-aware cap, Stage 5)
            needs to evaluate several candidate sizes against the same pool
            state in a tight loop. Per the Solidus Labs "Ex Files" report
            (literature/), execution cost at a venue is a function of size,
            not a flat number -- this is what makes repeated same-state
            calls at different sizes a normal, expected access pattern.
        """
        state = state if state is not None else self.get_state(block=block)
        d0 = self.pool_config["token0_decimals"]
        d1 = self.pool_config["token1_decimals"]
        sym0 = self.pool_config["token0_symbol"]
        sym1 = self.pool_config["token1_symbol"]
        fee_bps = self.pool_config["fee_tier_bps"]

        sqrt_price = state["sqrt_price_x96"] / (2 ** 96)
        liquidity = state["liquidity"]
        x_virtual = liquidity / sqrt_price
        y_virtual = liquidity * sqrt_price

        sell_token = intent["sell_token"]
        amount_in_human = intent["amount_in"]
        amount_in_after_fee = amount_in_human * (1 - fee_bps / 10000)

        if sell_token == sym0:
            dx = amount_in_after_fee * (10 ** d0)
            dy = y_virtual * dx / (x_virtual + dx)
            amount_out_human = dy / (10 ** d1)
            buy_token = sym1
            execution_price = amount_out_human / amount_in_human  # sym1 per sym0
            reference_price = state["price"][f"{sym1}_per_{sym0}"]
        elif sell_token == sym1:
            dy = amount_in_after_fee * (10 ** d1)
            dx = x_virtual * dy / (y_virtual + dy)
            amount_out_human = dx / (10 ** d0)
            buy_token = sym0
            execution_price = amount_in_human / amount_out_human  # sym1 per sym0
            reference_price = state["price"][f"{sym1}_per_{sym0}"]
        else:
            raise ValueError(f"sell_token must be {sym0!r} or {sym1!r}, got {sell_token!r}")

        price_impact_bps = abs(execution_price - reference_price) / reference_price * 10000 if reference_price else None

        return {
            "venue": "uniswap_v3",
            "pool": self.pool_key,
            "block": state["block"],
            "sell_token": sell_token,
            "buy_token": buy_token,
            "amount_in": amount_in_human,
            "amount_out_estimate": amount_out_human,
            "fee_bps": fee_bps,
            "price_impact_bps_estimate": price_impact_bps,
            "caveat": "Same-tick constant-product approximation; ignores tick-crossing. Use fork-sim for ground truth.",
        }

    def cost_model(self) -> Dict:
        return {
            "fee_tier_bps": self.pool_config["fee_tier_bps"],
            "description": (
                "Uniswap v3 LP fee only. Gas and slippage/MEV beyond the LP fee "
                "are not captured here -- see Mode 2 fork-simulated execution "
                "for real cost measurement."
            ),
        }


class PerpVenue(Venue):
    """GMX v2 (Arbitrum) perpetual market, read via GMX's public REST API.

    Unlike SpotDEXVenue, state comes from a REST API rather than direct RPC
    calls (GMX v2's DataStore/Reader storage pattern is much more involved to
    query correctly than Uniswap v3's plain getters). `block` is therefore
    not supported -- the API only exposes current state.
    """

    def __init__(self, symbol: str):
        self.symbol = symbol
        self._market = None

    def _resolve_market(self) -> dict:
        if self._market is None:
            self._market = gmx_api.find_market(self.symbol)
        return self._market

    def get_state(self, block: Optional[int] = None) -> Dict:
        if block is not None:
            raise NotImplementedError(
                "GMX v2 REST API only exposes current state; historical block queries "
                "would need direct archive-RPC contract reads against DataStore."
            )

        market = self._resolve_market()
        index_price_usd = gmx_api.get_token_price_usd(market["indexToken"])

        # NOTE: GMX_USD_PRECISION-scaled value only, NOT further annualized --
        # see gmx_api.py module docstring for why. Unconfirmed against an
        # independent source; treat as an estimate.
        funding_long = int(market["fundingRateLong"]) / gmx_api.GMX_USD_PRECISION
        funding_short = int(market["fundingRateShort"]) / gmx_api.GMX_USD_PRECISION

        return {
            "venue": "gmx_v2",
            "market": market["name"],
            "index_price_usd": index_price_usd,
            "open_interest_long_usd": int(market["openInterestLong"]) / gmx_api.GMX_USD_PRECISION,
            "open_interest_short_usd": int(market["openInterestShort"]) / gmx_api.GMX_USD_PRECISION,
            "available_liquidity_long_usd": int(market["availableLiquidityLong"]) / gmx_api.GMX_USD_PRECISION,
            "available_liquidity_short_usd": int(market["availableLiquidityShort"]) / gmx_api.GMX_USD_PRECISION,
            "funding_rate_apr_estimate": {
                "long": funding_long,
                "short": funding_short,
            },
        }

    def simulate_trade(self, intent: Dict, block: Optional[int] = None, state: Optional[Dict] = None) -> Dict:
        """Rough estimate of opening a position: entry price = current oracle
        price, price impact approximated as size / available-liquidity ratio.
        GMX v2's real price-impact formula is imbalance-based and more
        complex -- this is a coarse estimate for venue-selection logic, not a
        substitute for fork-sim ground truth (Phase 2 Week 7).

        intent: {"side": "long"|"short", "size_usd": float}
        state: pass an already-fetched get_state() result to skip the REST
            call (see SpotDEXVenue.simulate_trade's docstring for why this
            matters -- a cost-aware sizing cap evaluates several candidate
            sizes against the same state).
        """
        if block is not None:
            raise NotImplementedError("See get_state(): GMX v2 REST API has no historical block support.")

        side = intent["side"]
        if side not in ("long", "short"):
            raise ValueError(f"side must be 'long' or 'short', got {side!r}")

        state = state if state is not None else self.get_state()
        size_usd = intent["size_usd"]
        available_liquidity = state[f"available_liquidity_{side}_usd"]
        price_impact_bps_estimate = (size_usd / available_liquidity * 10000) if available_liquidity else None

        return {
            "venue": "gmx_v2",
            "market": state["market"],
            "side": side,
            "size_usd": size_usd,
            "entry_price_estimate": state["index_price_usd"],
            "price_impact_bps_estimate": price_impact_bps_estimate,
            "funding_rate_apr_estimate": state["funding_rate_apr_estimate"][side],
            "caveat": (
                "Price impact is a coarse size/available-liquidity estimate, not GMX v2's "
                "real imbalance-based formula. Use fork-sim for ground truth."
            ),
        }

    def cost_model(self) -> Dict:
        return {
            "description": (
                "GMX v2 perp costs: funding (paid/received between long and short, "
                "varies continuously with imbalance), borrowing fee (paid to the pool), "
                "and price impact on open/close. Funding/borrowing rates are dynamic "
                "state, not a flat fee tier -- query get_state() for current values."
            ),
        }


class VaultVenue(Venue):
    """Morpho Vault (ERC4626), read directly via RPC -- no Morpho-specific
    SDK or AgentKit dependency needed, since ERC4626 is a standard interface
    most vaults (including Morpho's) implement directly. Considered using
    real Coinbase AgentKit for this (its EthAccountWalletProvider supports a
    custom RPC URL, so it could in principle target this project's Anvil
    fork) -- but Morpho Vaults turned out to be plain ERC4626, simpler than
    expected, so direct RPC (matching SpotDEXVenue/PerpVenue's existing
    pattern) was the better-scoped choice; no new dependency or CDP account
    needed. AgentKit remains a viable option for a future, more complex
    protocol integration if one comes up.
    """

    def __init__(self, vault_key: str):
        if vault_key not in MORPHO_VAULTS:
            raise ValueError(f"Unknown vault: {vault_key!r}. Known: {list(MORPHO_VAULTS)}")
        self.vault_key = vault_key
        self.vault_config = MORPHO_VAULTS[vault_key]
        self.w3 = get_web3()
        self.vault = self.w3.eth.contract(
            address=Web3.to_checksum_address(self.vault_config["address"]),
            abi=ERC4626_VAULT_ABI,
        )

    def get_state(self, block: Optional[int] = None) -> Dict:
        call_kwargs = {"block_identifier": block} if block is not None else {}
        total_assets = self.vault.functions.totalAssets().call(**call_kwargs)
        total_supply = self.vault.functions.totalSupply().call(**call_kwargs)
        share_decimals = self.vault.functions.decimals().call(**call_kwargs)
        underlying_decimals = self.vault_config["underlying_decimals"]

        total_assets_human = total_assets / (10 ** underlying_decimals)
        total_supply_human = total_supply / (10 ** share_decimals)
        share_price = total_assets_human / total_supply_human if total_supply_human else None

        return {
            "venue": "morpho_vault",
            "vault": self.vault_key,
            "block": block if block is not None else self.w3.eth.block_number,
            "underlying": self.vault_config["underlying_symbol"],
            "total_assets": total_assets_human,
            "total_supply_shares": total_supply_human,
            "share_price_underlying": share_price,
            "caveat": (
                "No APY here -- ERC4626 doesn't expose a yield rate, and Morpho's "
                "fee/rate model isn't part of the standard interface. Would need "
                "either historical share-price snapshots over time or Morpho's own "
                "API for a real APY figure."
            ),
        }

    def simulate_trade(self, intent: Dict, block: Optional[int] = None) -> Dict:
        """Estimate shares minted/redeemed for a deposit or withdrawal, using
        the vault's own previewDeposit/previewRedeem (these already account
        for any deposit/withdrawal fee the vault charges, unlike
        SpotDEXVenue's hand-rolled fee subtraction).

        intent: {"action": "deposit"|"redeem", "amount": float}
                "deposit" amount is in underlying-asset units (e.g. USDC).
                "redeem" amount is in vault share units.
        """
        action = intent["action"]
        if action not in ("deposit", "redeem"):
            raise ValueError(f"action must be 'deposit' or 'redeem', got {action!r}")

        call_kwargs = {"block_identifier": block} if block is not None else {}
        underlying_decimals = self.vault_config["underlying_decimals"]

        if action == "deposit":
            amount_raw = int(intent["amount"] * (10 ** underlying_decimals))
            shares_raw = self.vault.functions.previewDeposit(amount_raw).call(**call_kwargs)
            return {
                "venue": "morpho_vault",
                "vault": self.vault_key,
                "block": block if block is not None else self.w3.eth.block_number,
                "action": "deposit",
                "amount_in": intent["amount"],
                "shares_out_estimate": shares_raw,
            }
        else:
            shares_raw = int(intent["amount"])
            assets_raw = self.vault.functions.previewRedeem(shares_raw).call(**call_kwargs)
            return {
                "venue": "morpho_vault",
                "vault": self.vault_key,
                "block": block if block is not None else self.w3.eth.block_number,
                "action": "redeem",
                "shares_in": shares_raw,
                "amount_out_estimate": assets_raw / (10 ** underlying_decimals),
            }

    def cost_model(self) -> Dict:
        return {
            "description": (
                "Morpho Vault costs: a performance fee on yield (rate is "
                "vault-curator-specific, not exposed by the standard ERC4626 "
                "interface -- previewDeposit/previewRedeem already net out any "
                "deposit/withdrawal fee, but the ongoing yield fee is not "
                "visible here). Gas only otherwise; no swap-style slippage."
            ),
        }
