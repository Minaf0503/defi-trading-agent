# Standard User Input Prompts for Onchain Analyst

## Quick Start Prompts

### Basic Prompt (Simple)
```
Analyze onchain data for [TOKEN_SYMBOL] and provide a trading recommendation.
```

### Standard Prompt (Recommended)
```
Please analyze the onchain data for [TOKEN_SYMBOL] (token address: [TOKEN_ADDRESS]) by examining liquidity pools, holder distribution, transaction patterns, and network activity. Provide a comprehensive onchain analysis and trading recommendation (BUY/HOLD/SELL) with confidence level and rationale based on onchain signals.
```

### Detailed Prompt (Comprehensive)
```
Analyze the onchain data for [TOKEN_SYMBOL] ([TOKEN_ADDRESS]) on [NETWORK] (e.g., ethereum, polygon). Please:
1. Gather onchain data from all available sources (liquidity pools, holders, transactions, supply)
2. Analyze holder behavior and distribution patterns
3. Examine liquidity pool dynamics and concentration
4. Review transaction patterns and network activity
5. Monitor mempool for large pending transactions
6. Identify accumulation/distribution signals and whale movements
7. Provide a trading recommendation (BUY/HOLD/SELL) with:
   - Confidence level (high/medium/low)
   - Detailed rationale based on onchain metrics
   - Key onchain factors driving the recommendation
   - Risk factors based on onchain data
8. Include a summary table with key onchain metrics and signals
```

---

## Template Prompts

### Template 1: Token Analysis
```
Analyze onchain data for [TOKEN_SYMBOL] ([TOKEN_ADDRESS]) and provide a trading recommendation based on:
- Liquidity pool metrics and DEX liquidity
- Token holder distribution and whale movements
- Transaction patterns and network activity
- Supply metrics and distribution
- Mempool activity and pending transactions

Please provide a comprehensive onchain analysis with BUY/HOLD/SELL recommendation.
```

### Template 2: Network-Specific Analysis
```
Analyze the onchain data for [TOKEN_SYMBOL] on [NETWORK] blockchain. Gather data on:
1. Liquidity pools across DEXs
2. Holder distribution and top holders
3. Transaction volume and patterns
4. Network activity and congestion
5. Mempool activity

Provide onchain analysis and trading recommendation with confidence level.
```

### Template 3: Focused Analysis
```
Analyze [TOKEN_SYMBOL] onchain data with focus on [FOCUS_AREA]:
- Holder behavior and whale movements
- Liquidity pool dynamics
- Transaction patterns
- Network activity

Provide trading recommendation based on onchain signals.
```

---

## Example Prompts for Common Tokens

### Ethereum (ETH)
```
Please analyze the onchain data for ETH (Ethereum mainnet) by examining liquidity pools, holder distribution, transaction patterns, and network activity. Provide a comprehensive onchain analysis and trading recommendation (BUY/HOLD/SELL) with confidence level and rationale based on onchain signals.
```

### Uniswap (UNI)
```
Analyze onchain data for UNI token (0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984 on Ethereum). Examine:
- Uniswap liquidity pools and DEX liquidity
- UNI holder distribution and whale movements
- Transaction patterns and network activity
- Supply metrics and token distribution

Provide trading recommendation with confidence level and onchain rationale.
```

### USDC (USD Coin)
```
Analyze onchain data for USDC (0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48 on Ethereum). Focus on:
- Liquidity pool depth and concentration
- Holder distribution and large holder activity
- Transaction volume and patterns
- Supply metrics and minting/burning activity

Provide onchain analysis and trading recommendation.
```

---

## Advanced Prompts

### Whale Movement Focus
```
Analyze onchain data for [TOKEN_SYMBOL] with focus on whale movements and large transactions. Identify:
- Large holder activity and transfers
- Accumulation/distribution patterns
- Whale wallet behavior
- Potential market impact of large transactions

Provide trading recommendation based on whale activity signals.
```

### Liquidity Focus
```
Analyze onchain data for [TOKEN_SYMBOL] with focus on liquidity pool dynamics. Examine:
- DEX liquidity depth and concentration
- Liquidity pool changes over time
- Liquidity provider behavior
- Slippage and liquidity risks

Provide trading recommendation based on liquidity analysis.
```

### Network Activity Focus
```
Analyze onchain data for [TOKEN_SYMBOL] with focus on network activity. Review:
- Transaction volume and frequency
- Active address counts
- Network congestion indicators
- Smart contract interactions

Provide trading recommendation based on network activity signals.
```

---

## Prompt Format for API/Programmatic Use

### JSON Format
```json
{
  "token_symbol": "UNI",
  "token_address": "0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984",
  "network": "ethereum",
  "analysis_type": "comprehensive",
  "focus_areas": ["liquidity", "holders", "transactions"],
  "output_format": "detailed",
  "include_recommendation": true
}
```

### Structured Prompt
```
Token: [TOKEN_SYMBOL]
Token Address: [TOKEN_ADDRESS]
Network: [NETWORK]
Focus Areas: Liquidity, Holders, Transactions, Network Activity
Output: Comprehensive onchain analysis with trading recommendation
```

---

## Best Practices for Prompts

1. **Be Specific**: Always include token symbol and address
2. **Specify Network**: Mention blockchain network (ethereum, polygon, etc.)
3. **Request Sources**: Explicitly mention which onchain data to analyze
4. **Ask for Recommendation**: Always request a trading recommendation
5. **Request Confidence**: Ask for confidence level in the recommendation
6. **Request Rationale**: Ask for detailed reasoning based on onchain data

---

## Example Conversation Flow

### User Input 1:
```
Analyze onchain data for UNI and provide a trading recommendation.
```

### User Input 2 (Follow-up):
```
Can you provide more details on the whale movements for UNI?
```

### User Input 3 (Follow-up):
```
What are the liquidity pool risks you identified from the onchain analysis?
```

---

## Quick Reference

**Minimum Required Information:**
- Token symbol (e.g., UNI, ETH, USDC)
- Token address (contract address on blockchain)

**Recommended Information:**
- Token symbol
- Token address
- Network (ethereum, polygon, base, solana)
- Focus areas (liquidity, holders, transactions, etc.)
- Request for trading recommendation

**Optional Enhancements:**
- Specific focus (whale movements, liquidity, network activity)
- Time range for analysis
- Output format preferences
- Confidence level request

