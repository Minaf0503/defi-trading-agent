# DeFi Trading Agent Skills

This directory contains Agent Skills for the DeFi Trading Agents framework. These Skills extend Claude's functionality to provide specialized cryptocurrency trading analysis capabilities.

## Available Skills

### 1. Sentiment News Analyst (`sentiment-news-analyst`)

Analyzes cryptocurrency market sentiment by aggregating information from multiple sources:
- RSS feeds (DL News)
- Internet search
- Twitter/X social media
- Reddit discussions

**Use when:** Analyzing market sentiment, news analysis, social media sentiment, or trading recommendations for crypto assets.

**Key Features:**
- Multi-source information aggregation
- Sentiment analysis (bullish/bearish/neutral)
- FUD/FOMO detection
- Trading recommendations with confidence levels

### 2. Onchain Analyst (`onchain-analyst`)

Analyzes blockchain data to discover potential sudden/trend shifts:
- Network activity analysis
- Token holder behavior
- Liquidity pool dynamics
- Wallet distributions
- Mempool activity
- Blockchain state changes

**Use when:** Analyzing onchain data, blockchain analysis, holder analysis, liquidity analysis, whale movements, or trading recommendations based on onchain metrics.

**Key Features:**
- Comprehensive onchain data analysis
- Accumulation/distribution pattern detection
- Whale movement identification
- Trading recommendations with confidence levels

## Using These Skills

### In Claude Code

These Skills are automatically discovered when placed in `.claude/skills/`. Claude will use them automatically when relevant to your request.

### In Claude API

Upload these Skills via the Skills API (`/v1/skills` endpoints) to use them with the Claude API.

### In Claude.ai

Upload these Skills as zip files through Settings > Features to use them in Claude.ai.

## Skill Structure

Each Skill follows the standard Agent Skills structure:
- `SKILL.md`: Main instructions with YAML frontmatter
- Contains workflows, best practices, and guidance
- References agent configurations and documentation

## Documentation

For more information about each agent:
- **Sentiment News Analyst**: See `NEBULA_ONE_AGENT_CONFIG.md` and `NEBULA_ONE_SUMMARY.md`
- **Onchain Analyst**: See `NEBULA_ONE_ONCHAIN_ANALYST.md` and `NEBULA_ONE_ONCHAIN_SUMMARY.md`

For standard prompts:
- **Sentiment News Analyst**: See `prompts/sentiment_news_agent_prompts.md`
- **Onchain Analyst**: See `prompts/onchain_analyst_prompts.md`

## References

- [Agent Skills Documentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Agent Skills Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Agent Skills Quickstart](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart)

