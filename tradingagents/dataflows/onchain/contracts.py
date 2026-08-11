"""
Known contract addresses and minimal ABIs for the on-chain data layer.

Addresses verified live against Ethereum mainnet on 2026-06-21 (see
writing/papers/PROGRESS_LOG.md). All on Ethereum mainnet for now -- Arbitrum
addresses (for GMX v2 PerpVenue, Week 6) will be added separately.
"""

CHAINLINK_AGGREGATOR_ABI = [
    {
        "inputs": [],
        "name": "latestRoundData",
        "outputs": [
            {"name": "roundId", "type": "uint80"},
            {"name": "answer", "type": "int256"},
            {"name": "startedAt", "type": "uint256"},
            {"name": "updatedAt", "type": "uint256"},
            {"name": "answeredInRound", "type": "uint80"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "stateMutability": "view",
        "type": "function",
    },
]

UNISWAP_V3_POOL_ABI = [
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
    {
        "inputs": [],
        "name": "token0",
        "outputs": [{"name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "token1",
        "outputs": [{"name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
]

# Chainlink price feeds, Ethereum mainnet.
CHAINLINK_FEEDS = {
    "ETH/USD": {
        "address": "0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419",
    },
}

# Uniswap v3 pools, Ethereum mainnet. decimals/symbols are for the token0/token1
# ordering Uniswap actually uses on-chain (lower address = token0), not display order.
#
# Original three pools (WETH/USDC, UNI/WETH, AAVE/WETH) were verified
# 2026-06-21. Seven additional pools added 2026-06-27 for the FC27 10-token
# panel (see experiments/config.py PANEL_TOKENS). All addresses verified via
# Uniswap v3 Factory.getPool() calls at block 25412313; token0/token1 ordering
# confirmed via each pool's token0() getter; deepest fee tier selected by
# on-chain liquidity() at that block. Pool addresses are stable (Uniswap v3
# pools are immutable), but liquidity may migrate across fee tiers over time --
# re-verify which tier is deepest at each backtest block for RQ2 accuracy.
UNISWAP_V3_POOLS = {
    # ── Original three pools ──────────────────────────────────────────────────
    "WETH/USDC": {
        "address": "0x88e6A0c2dDD26FEEb64F039a2c41296FcB3f5640",
        "fee_tier_bps": 5,   # 0.05%; fee=500
        "token0_symbol": "USDC",
        "token0_decimals": 6,
        "token1_symbol": "WETH",
        "token1_decimals": 18,
    },
    "UNI/WETH": {
        "address": "0x1d42064Fc4Beb5F8aAF85F4617AE8b3b5B8Bd801",
        "fee_tier_bps": 30,  # 0.3%; fee=3000
        "token0_symbol": "UNI",
        "token0_decimals": 18,
        "token1_symbol": "WETH",
        "token1_decimals": 18,
    },
    "AAVE/WETH": {
        "address": "0x5aB53EE1d50eeF2C1DD3d5402789cd27bB52c1bB",
        "fee_tier_bps": 30,  # 0.3%; fee=3000
        "token0_symbol": "AAVE",
        "token0_decimals": 18,
        "token1_symbol": "WETH",
        "token1_decimals": 18,
    },
    # ── FC27 panel additions (verified 2026-06-27, block 25412313) ────────────
    # WBTC: 0.3% pool cited in experiment design spec. A 0.05% pool also
    # exists (0x4585FE...) with ~10x more current liquidity -- re-check which
    # was deeper at each 2022-2024 backtest block; the 0.05% tier was less
    # dominant in early v3 history.
    "WBTC/WETH": {
        "address": "0xCBCdF9626bC03E24f779434178A73a0B4bad62eD",
        "fee_tier_bps": 30,  # 0.3%; fee=3000
        "token0_symbol": "WBTC",
        "token0_decimals": 8,
        "token1_symbol": "WETH",
        "token1_decimals": 18,
    },
    # LINK: deepest pool by liquidity() at verification block.
    "LINK/WETH": {
        "address": "0xa6Cc3C2531FdaA6Ae1A3CA84c2855806728693e8",
        "fee_tier_bps": 30,  # 0.3%; fee=3000
        "token0_symbol": "LINK",
        "token0_decimals": 18,
        "token1_symbol": "WETH",
        "token1_decimals": 18,
    },
    # MKR: deepest pool by liquidity() at verification block.
    "MKR/WETH": {
        "address": "0xe8c6c9227491C0a8156A0106A0204d881BB7E531",
        "fee_tier_bps": 30,  # 0.3%; fee=3000
        "token0_symbol": "MKR",
        "token0_decimals": 18,
        "token1_symbol": "WETH",
        "token1_decimals": 18,
    },
    # CRV: WETH address (0xC02a...) is numerically lower than CRV (0xD533...),
    # so WETH is token0. The 0.3% pool is by far the deepest (primary CRV
    # liquidity on Uniswap v3; most CRV liquidity is on Curve itself).
    "CRV/WETH": {
        "address": "0x919Fa96e88d67499339577Fa202345436bcDaf79",
        "fee_tier_bps": 30,  # 0.3%; fee=3000
        "token0_symbol": "WETH",
        "token0_decimals": 18,
        "token1_symbol": "CRV",
        "token1_decimals": 18,
    },
    # PEPE: spec suggested 1% fee tier, but the 0.3% pool has ~8x more
    # liquidity at the verification block. Using 0.3% for execution quality
    # measurements. PEPE only appears on panel dates >= 2023-09-15.
    "PEPE/WETH": {
        "address": "0x11950d141EcB863F01007AdD7D1A342041227b58",
        "fee_tier_bps": 30,  # 0.3%; fee=3000
        "token0_symbol": "PEPE",
        "token0_decimals": 18,
        "token1_symbol": "WETH",
        "token1_decimals": 18,
    },
    # ONDO: WETH address (0xC02a...) < ONDO address (0xfAbA...), so WETH is
    # token0. WETH pair (0.3%) has ~11x more liquidity than USDC pair.
    # ONDO only appears on panel dates >= 2024-06-15.
    "ONDO/WETH": {
        "address": "0x7b1E5D984A43eE732de195628d20d05CFaBc3cC7",
        "fee_tier_bps": 30,  # 0.3%; fee=3000
        "token0_symbol": "WETH",
        "token0_decimals": 18,
        "token1_symbol": "ONDO",
        "token1_decimals": 18,
    },
    # ENA: ENA address (0x57e1...) < WETH address (0xC02a...), so ENA is
    # token0. WETH pair (0.3%) is by far the deepest (~$20M spec estimate was
    # for USDC pair; WETH pair is orders of magnitude deeper at current block).
    # ENA only appears on panel dates >= 2024-06-15.
    "ENA/WETH": {
        "address": "0xc3Db44ADC1fCdFd5671f555236eae49f4A8EEa18",
        "fee_tier_bps": 30,  # 0.3%; fee=3000
        "token0_symbol": "ENA",
        "token0_decimals": 18,
        "token1_symbol": "WETH",
        "token1_decimals": 18,
    },
}

ERC20_ABI = [
    {
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "symbol",
        "outputs": [{"name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
]

# Standard ERC4626 ("Tokenized Vault") interface -- Morpho Vaults (and most
# other DeFi vaults) implement this directly, no protocol-specific SDK needed.
ERC4626_VAULT_ABI = [
    {
        "inputs": [],
        "name": "asset",
        "outputs": [{"name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "totalAssets",
        "outputs": [{"name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"name": "assets", "type": "uint256"}],
        "name": "convertToShares",
        "outputs": [{"name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"name": "shares", "type": "uint256"}],
        "name": "convertToAssets",
        "outputs": [{"name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"name": "assets", "type": "uint256"}],
        "name": "previewDeposit",
        "outputs": [{"name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"name": "shares", "type": "uint256"}],
        "name": "previewRedeem",
        "outputs": [{"name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"name": "assets", "type": "uint256"}, {"name": "receiver", "type": "address"}],
        "name": "deposit",
        "outputs": [{"name": "", "type": "uint256"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]

# Morpho Vaults, Ethereum mainnet -- ERC4626-compliant, no Morpho-specific ABI
# needed for reads. Addresses verified live 2026-06-21.
MORPHO_VAULTS = {
    "STEAKHOUSE_USDC": {
        "address": "0xBEEF01735c132Ada46AA9aA4c54623cAA92A64CB",
        "underlying_symbol": "USDC",
        "underlying_decimals": 6,
    },
}

# ERC20 addresses for experiment tokens that actually have an Ethereum mainnet
# presence -- mirrors experiments/config.py's EXPERIMENT_TOKENS["..."]["addresses"].
# SOL (Solana-native), ZEC, XMR have no EVM address at all; BTC's is WBTC, a
# wrapped representation, not native BTC. Tools using this should report
# "no on-chain venue data" for tokens absent here rather than guessing.
ERC20_TOKENS = {
    "BTC":  {"address": "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599", "decimals": 8,  "note": "WBTC, not native BTC"},
    "WBTC": {"address": "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599", "decimals": 8,  "note": "WBTC"},
    "ETH":  {"address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2", "decimals": 18, "note": "WETH"},
    "UNI":  {"address": "0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984", "decimals": 18},
    "AAVE": {"address": "0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9", "decimals": 18},
    "LINK": {"address": "0x514910771AF9Ca656af840dff83E8264EcF986CA", "decimals": 18},
    "MKR":  {"address": "0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2", "decimals": 18},
    "CRV":  {"address": "0xD533a949740bb3306d119CC777fa900bA034cd52", "decimals": 18},
    "PEPE": {"address": "0x6982508145454Ce325dDbE47a25d4ec3d2311933", "decimals": 18},
    "ONDO": {"address": "0xfAbA6f8e4a5E8Ab82F62fe7C39859FA577269BE3", "decimals": 18},
    "ENA":  {"address": "0x57e114B691Db790C35207b2e685D4A43181e6061", "decimals": 18},
}
