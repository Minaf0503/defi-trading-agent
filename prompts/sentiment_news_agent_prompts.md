# Standard User Input Prompts for Sentiment News Analyst

## Quick Start Prompts

### Basic Prompt (Simple)
```
Analyze sentiment for BTC and provide a trading recommendation.
```

### Standard Prompt (Recommended)
```
Please analyze the current market sentiment for [TOKEN_SYMBOL] (e.g., BTC, ETH, UNI) by gathering information from RSS feeds, internet search, Twitter, and Reddit. Provide a comprehensive sentiment analysis and trading recommendation (BUY/HOLD/SELL) with confidence level and rationale.
```

### Detailed Prompt (Comprehensive)
```
Analyze the market sentiment for [TOKEN_SYMBOL] ([TOKEN_NAME]) over the last 7 days. Please:
1. Gather information from all available sources (DL News RSS feed, internet search, Twitter/X, and Reddit)
2. Analyze sentiment from each source
3. Identify key themes, narratives, and trends
4. Detect any FUD or FOMO indicators
5. Provide a trading recommendation (BUY/HOLD/SELL) with:
   - Confidence level (high/medium/low)
   - Detailed rationale based on all sources
   - Key factors driving the recommendation
   - Risk factors and opportunities
6. Include a summary table with sources analyzed and sentiment metrics
```

---

## Template Prompts

### Template 1: Token Analysis
```
Analyze sentiment for [TOKEN_SYMBOL] ([TOKEN_NAME]) and provide a trading recommendation based on:
- News articles from credible sources
- Social media sentiment (Twitter and Reddit)
- Internet search results
- Overall market perception

Please provide a comprehensive analysis with BUY/HOLD/SELL recommendation.
```

### Template 2: Time-Specific Analysis
```
Analyze the market sentiment for [TOKEN_SYMBOL] over the last [N] days. Gather information from:
1. DL News RSS feed
2. Internet search results
3. Twitter/X discussions
4. Reddit community posts

Provide sentiment analysis and trading recommendation with confidence level.
```

### Template 3: Event-Driven Analysis
```
Analyze sentiment for [TOKEN_SYMBOL] in light of [EVENT/DESCRIPTION]. Search for:
- Recent news articles
- Social media discussions
- Community reactions
- Market impact

Provide trading recommendation based on sentiment analysis.
```

---

## Example Prompts for Common Tokens

### Bitcoin (BTC)
```
Analyze the current market sentiment for Bitcoin (BTC) by gathering information from RSS feeds, internet search, Twitter, and Reddit. Provide a comprehensive sentiment analysis and trading recommendation (BUY/HOLD/SELL) with confidence level and detailed rationale.
```

### Ethereum (ETH)
```
Please analyze sentiment for Ethereum (ETH) over the last 7 days. Gather information from all available sources including DL News RSS feed, internet search, Twitter/X, and Reddit. Provide a trading recommendation with confidence level and key factors driving the decision.
```

### Uniswap (UNI)
```
Analyze market sentiment for Uniswap (UNI) token. Search for recent news, social media discussions, and community sentiment. Provide a comprehensive analysis with BUY/HOLD/SELL recommendation, confidence level, and rationale based on all sources.
```

---

## Advanced Prompts

### Multi-Source Comparison
```
Analyze sentiment for [TOKEN_SYMBOL] and compare sentiment across different sources:
- News articles (RSS feeds and internet search)
- Twitter/X social media
- Reddit community discussions

Identify any sentiment divergences between sources and provide an overall trading recommendation.
```

### Risk-Focused Analysis
```
Analyze sentiment for [TOKEN_SYMBOL] with focus on risk factors. Search for:
- Negative news and FUD indicators
- Regulatory concerns
- Technical issues or vulnerabilities
- Market risks

Provide sentiment analysis emphasizing risk assessment and trading recommendation.
```

### Opportunity-Focused Analysis
```
Analyze sentiment for [TOKEN_SYMBOL] with focus on opportunities. Search for:
- Positive news and developments
- Partnership announcements
- Technical upgrades
- Market catalysts

Provide sentiment analysis emphasizing opportunities and trading recommendation.
```

---

## Prompt Format for API/Programmatic Use

### JSON Format
```json
{
  "token_symbol": "BTC",
  "token_name": "Bitcoin",
  "days_back": 7,
  "analysis_type": "comprehensive",
  "sources": ["rss", "internet", "twitter", "reddit"],
  "output_format": "detailed",
  "include_recommendation": true
}
```

### Structured Prompt
```
Token: [TOKEN_SYMBOL]
Token Name: [TOKEN_NAME]
Time Period: Last [N] days
Sources: RSS feeds, Internet search, Twitter, Reddit
Output: Comprehensive sentiment analysis with trading recommendation
```

---

## Best Practices for Prompts

1. **Be Specific**: Always include the token symbol (e.g., BTC, ETH, UNI)
2. **Specify Timeframe**: Mention the lookback period (e.g., "last 7 days")
3. **Request Sources**: Explicitly mention which sources to use
4. **Ask for Recommendation**: Always request a trading recommendation
5. **Request Confidence**: Ask for confidence level in the recommendation
6. **Request Rationale**: Ask for detailed reasoning

---

## Example Conversation Flow

### User Input 1:
```
Analyze sentiment for BTC and provide a trading recommendation.
```

### User Input 2 (Follow-up):
```
Can you provide more details on the Twitter sentiment for BTC?
```

### User Input 3 (Follow-up):
```
What are the main risk factors you identified from the news analysis?
```

---

## Quick Reference

**Minimum Required Information:**
- Token symbol (e.g., BTC, ETH, UNI)

**Recommended Information:**
- Token symbol
- Token name (optional but helpful)
- Time period (default: 7 days)
- Request for trading recommendation

**Optional Enhancements:**
- Specific focus (risk, opportunities, events)
- Source preferences
- Output format preferences
- Confidence level request

