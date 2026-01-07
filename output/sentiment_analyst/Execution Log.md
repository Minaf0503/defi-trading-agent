03:15:46.351 - FileSearchRunCreationOptionsPipelineStep: Adding file search tool to the run creation options.

03:15:46.673 - Attachment cb2c0a1b-9be0-0c5d-ccb6-4277a2208383 does not exist in the current thread, this will be added to the conversation history.

03:15:46.673 - Attachment e65b0423-90aa-ffe5-7117-e9ae93cf3e2f does not exist in the current thread, this will be added to the conversation history.

03:15:46.673 - Processing 2 valid attachments.

03:15:47.206 - Added message to the Assistant msg_ZDk54T2JL4sizu7KdsTWVnbb with 2 attachments (batch 1 of 1)

# Question: 

> Analyze the market sentiment for ZEC (Zcash) over the last 7 days. Please:
> 1. Gather information from all available sources (DL News RSS feed, internet search, Twitter/X, and Reddit)
> 2. Analyze sentiment from each source
> 3. Identify key themes, narratives, and trends
> 4. Detect any FUD or FOMO indicators
> 5. Provide a trading recommendation (BUY/HOLD/SELL) with:
>    - Confidence level (high/medium/low)
>    - Detailed rationale based on all sources
>    - Key factors driving the recommendation
>    - Risk factors and opportunities
> 6. Include a summary table with sources analyzed and sentiment metrics

- ConversationId: e2a3d0c7-70b4-232b-a30a-45ea4770e14c
- SegmentId: 85f43243-a07d-4515-8aa5-658688fa4888
- Model: gpt-4o
- Deployment: gpt-4o
- AssistantId: asst_xIsCAJWTkZEKyg72aQsIh7mB
- AssistantThread: thread_Ewgdc88B6hmuAp5XiwPqEYuS
- ParentId: GptSystemConfigurationStateId: 68d33f53-702c-4cce-9d02-2bbd796a7a1a




---



# Iteration 1


### Thread:

```json

{
  "ToolResources": {},
  "Id": "thread_Ewgdc88B6hmuAp5XiwPqEYuS",
  "CreatedAt": "2026-01-07T03:15:46+00:00",
  "Metadata": {}
}

```


### RunOptions

```json

{
  "ModelOverride": "gpt-4o",
  "InstructionsOverride": "You are a **Sentiment/News Analyst** specializing in cryptocurrency market sentiment analysis. Your role is to identify market player perception on crypto tokens by analyzing information from multiple sources and provide trading recommendations.\n\nWORKFLOW:\n\n1. **Gather Information from Multiple Sources:**\n   - **RSS News Feeds**: Fetch articles from DL News RSS feed (https://www.dlnews.com/rss/) filtered for the token\n   - **Internet Search**: Search the web for recent news, articles, and information about the token\n   - **Twitter/X**: Search Twitter for recent tweets, discussions, and sentiment about the token\n   - **Reddit**: Search relevant subreddits for discussions, posts, and community sentiment\n\n2. **Analyze and Synthesize:**\n   - Analyze all gathered information for sentiment (bullish/bearish/neutral)\n   - Identify key themes, narratives, and trends\n   - Detect FUD (Fear, Uncertainty, Doubt) and FOMO (Fear Of Missing Out) indicators\n   - Assess credibility of sources and distinguish signal from noise\n\n3. **Provide Trading Recommendation:**\n   - Based on comprehensive sentiment analysis, provide clear recommendation: **BUY/HOLD/SELL**\n   - Include confidence level (high/medium/low)\n   - Provide detailed rationale based on all sources analyzed\n   - Identify key factors driving the recommendation\n\nKEY AREAS TO ANALYZE:\n\n 1. News Analysis (Credible Sources):\n- Official announcements from project teams\n- Protocol updates and upgrades\n- Partnership and integration news\n- Regulatory news affecting the token\n- Market developments and trends\n- Industry analysis and expert opinions\n\n2. Social Media Sentiment:\n- **Twitter/X**: Recent tweets, trending topics, influencer opinions\n- **Reddit**: Community discussions, sentiment trends, key themes\n- Overall social media sentiment (bullish/bearish/neutral)\n- Sentiment intensity and changes over time\n- Viral content and its impact\n\n3. Market Player Perception:\n- Overall sentiment trends\n- Key themes and narratives\n- FUD detection\n- FOMO indicators\n- Market expectations and predictions\n- Community confidence levels\n\n4. Sentiment Indicators:\n- Positive/negative sentiment ratio\n- Sentiment intensity\n- Sentiment changes and trends\n- Correlation with price movements\n- Sentiment divergences\n\nIMPORTANT INSTRUCTIONS:\n\n- **ALWAYS start by gathering information from ALL available sources** (RSS feeds, internet search, Twitter, Reddit)\n- Filter all content for the specific token being analyzed\n- Analyze multiple sources to get comprehensive sentiment\n- Focus on credible sources but consider social media for market sentiment\n- Distinguish between noise and signal\n- Consider source credibility and authority\n- Weight different sources appropriately (news > social media for credibility, but social media for sentiment)\n- Provide clear, actionable trading recommendation based on comprehensive sentiment analysis\n- Include confidence level and detailed rationale\n\nOUTPUT FORMAT:\n\nProvide a comprehensive sentiment analysis including:\n\n1. **Information Sources Summary:**\n   - Number of articles found from RSS feeds\n   - Number of relevant web search results\n   - Number of Twitter posts analyzed\n   - Number of Reddit posts analyzed\n\n2. **Sentiment Analysis:**\n   - Current market sentiment (bullish/bearish/neutral) with confidence level\n   - Key sentiment drivers and themes from all sources\n   - Positive and negative factors identified\n   - Sentiment trends over time\n\n3. **Source-Specific Insights:**\n   - News impact assessment\n   - Social media sentiment trends\n   - Community perception summary\n\n4. **Trading Recommendation:**\n   - **BUY/HOLD/SELL** with clear rationale\n   - Confidence level (high/medium/low)\n   - Key factors driving the recommendation\n   - Risk factors and opportunities\n\n5. **Summary Table:**\n   - Sources analyzed (type, count, overall sentiment)\n   - Key sentiment metrics\n   - Trading recommendation summary\n",
  "AdditionalInstructions": "## IMPORTANT:\n- The information included in your tool function call results is prefixed with a reference in the form of [doc1]:, [doc2]:, etc. ALWAYS use these references as citations when returning the answer. \nGood Example:  Apple is a fruit[doc1].\n\n- If a user asks for additional information, call the original tool function for additional information. Don't explain the tool function - just use it.",
  "AdditionalMessages": [],
  "ToolsOverride": [
    {
      "FunctionName": "InternetSearch",
      "Description": "Searches the public internet.",
      "Parameters": {"type":"object","properties":{"question":{"type":"string","description":"The user\u0027s question. Limit to 350 characters."}},"required":["question"]}
    },
    {},
    {
      "MaxResults": 10
    },
    {
      "FunctionName": "WebSiteSearch",
      "Description": "This page contains information to answer questions about crypto news",
      "Parameters": {"type":"object","properties":{"question":{"type":"string","description":"The user\u0027s question"}},"required":["question"]}
    }
  ],
  "Metadata": {},
  "NucleusSamplingFactor": 0.95,
  "MaxOutputTokenCount": 4096
}

```

03:15:47.212 - Creating Streaming Run

03:15:48.139 - State transitioned from  to RunCreated with type RunUpdate

03:15:48.142 - State transitioned from RunCreated to RunQueued with type RunUpdate

03:15:48.281 - State transitioned from RunQueued to RunInProgress with type RunUpdate

03:15:53.940 - State transitioned from RunInProgress to RunStepCreated with type RunStepUpdate

03:15:53.945 - State transitioned from RunStepCreated to RunStepInProgress with type RunStepUpdate

03:15:54.705 - State transitioned from RunStepInProgress to RunStepUpdated with type RunStepDetailsUpdate

03:15:55.170 - State transitioned from RunStepUpdated to RunRequiresAction with type RequiredActionUpdate

03:15:55.170 - Request for tool call `WebSiteSearch` received from Assistant, adding to collection

03:15:55.170 - Request for tool call `InternetSearch` received from Assistant, adding to collection

03:15:55.170 - Request for tool call `WebSiteSearch` received from Assistant, adding to collection

03:15:55.170 - Request for tool call `InternetSearch` received from Assistant, adding to collection

03:15:55.170 - Request for tool call `InternetSearch` received from Assistant, adding to collection




---



# Iteration 2


### Thread:

```json

{
  "ToolResources": {},
  "Id": "thread_Ewgdc88B6hmuAp5XiwPqEYuS",
  "CreatedAt": "2026-01-07T03:15:46+00:00",
  "Metadata": {}
}

```

03:15:55.187 - Awaiting tool calls

## Tool Call: WebSiteSearch


### Arguments

```json

{"question": "Recent news about Zcash (ZEC) over the last 7 days"}

```

03:15:55.190 - Calling Internet search API `https://api.nebulaone.ai/bing/search?q=Recent news about Zcash (ZEC) over the last 7 days site%3awww.dlnews.com`

## Tool Call: InternetSearch


### Arguments

```json

{"question": "Recent news and sentiment analysis for Zcash (ZEC) over the last 7 days"}

```

03:15:55.191 - Calling Internet search API `https://api.nebulaone.ai/bing/search?q=Recent news and sentiment analysis for Zcash (ZEC) over the last 7 days`

## Tool Call: WebSiteSearch


### Arguments

```json

{"question": "Zcash (ZEC) news on DL News RSS feed"}

```

03:15:55.191 - Calling Internet search API `https://api.nebulaone.ai/bing/search?q=Zcash (ZEC) news on DL News RSS feed site%3awww.dlnews.com`

## Tool Call: InternetSearch


### Arguments

```json

{"question": "Recent Twitter sentiment and trends about Zcash (ZEC)"}

```

03:15:55.192 - Calling Internet search API `https://api.nebulaone.ai/bing/search?q=Recent Twitter sentiment and trends about Zcash (ZEC)`

## Tool Call: InternetSearch


### Arguments

```json

{"question": "Recent Reddit discussions and sentiment about Zcash (ZEC)"}

```

03:15:55.192 - Calling Internet search API `https://api.nebulaone.ai/bing/search?q=Recent Reddit discussions and sentiment about Zcash (ZEC)`

03:15:56.057 - 10 website results found for : Zcash (ZEC) news on DL News RSS feed using https://www.dlnews.com/


### Website search results

```json

[
  {
    "Name": "Zcash surges tenfold as investors bet on privacy as ban looms",
    "Url": "https://www.dlnews.com/articles/markets/zcash-surges-tenfold-as-investors-bet-on-privacy-as-ban-looms/"
  },
  {
    "Name": "Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% ...",
    "Url": "https://www.dlnews.com/articles/people-culture/zcash-foundation-shakes-up-leadership-amidst-zec-token-price-rally/"
  },
  {
    "Name": "Why Zcash price is up 700% since September, according to Galaxy Digital",
    "Url": "https://www.dlnews.com/articles/markets/why-privacy-token-zcash-price-is-up-700-percent-since-september/"
  },
  {
    "Name": "Zcash price primed for 45% breakout as Grayscale files for ETF",
    "Url": "https://www.dlnews.com/articles/markets/zcash-price-primed-for-45-percent-breakout-as-grayscale-files-for-etf/"
  },
  {
    "Name": "Zcash price surge continues despite market turmoil – DL News",
    "Url": "https://www.dlnews.com/articles/markets/zcash-price-surge-continues-despite-market-turmoil/"
  },
  {
    "Name": "Winklevoss twins bet on Zcash with new treasury firm targeting 5% ...",
    "Url": "https://www.dlnews.com/articles/markets/winklevoss-twins-bet-on-zcash-with-new-treasury-firm/"
  },
  {
    "Name": "DL News - Markets, DeFi, Regulation and top cryptocurrency news",
    "Url": "https://www.dlnews.com/"
  },
  {
    "Name": "RSS - DL News",
    "Url": "https://www.dlnews.com/rss/"
  },
  {
    "Name": "How privacy coins Firo and Zcash dodged Binance delisting ... - DL News",
    "Url": "https://www.dlnews.com/articles/defi/how-privacy-coins-firo-and-zcash-dodged-binance-delisting/"
  },
  {
    "Name": "Monero and Zcash’s liquidity dries up as Binance eyes ... - DL News",
    "Url": "https://www.dlnews.com/articles/defi/monero-and-zcash-liquidity-runs-dry-as-binance-may-delist/"
  }
]

```

03:15:56.058 - Downloading page content from: `https://www.dlnews.com/articles/markets/zcash-surges-tenfold-as-investors-bet-on-privacy-as-ban-looms/`

03:15:56.058 - Downloading page content from: `https://www.dlnews.com/articles/people-culture/zcash-foundation-shakes-up-leadership-amidst-zec-token-price-rally/`

03:15:56.058 - Downloading page content from: `https://www.dlnews.com/articles/markets/why-privacy-token-zcash-price-is-up-700-percent-since-september/`

03:15:56.058 - Downloading page content from: `https://www.dlnews.com/articles/markets/zcash-price-primed-for-45-percent-breakout-as-grayscale-files-for-etf/`

03:15:56.058 - Downloading page content from: `https://www.dlnews.com/articles/markets/zcash-price-surge-continues-despite-market-turmoil/`

03:15:56.059 - Downloading page content from: `https://www.dlnews.com/articles/markets/winklevoss-twins-bet-on-zcash-with-new-treasury-firm/`

03:15:56.059 - Downloading page content from: `https://www.dlnews.com/`

03:15:56.060 - Downloading page content from: `https://www.dlnews.com/rss/`

03:15:56.060 - Downloading page content from: `https://www.dlnews.com/articles/defi/how-privacy-coins-firo-and-zcash-dodged-binance-delisting/`

03:15:56.060 - Downloading page content from: `https://www.dlnews.com/articles/defi/monero-and-zcash-liquidity-runs-dry-as-binance-may-delist/`

03:15:56.068 - 10 search results found for : Recent Twitter sentiment and trends about Zcash (ZEC)


### Search Results Object

```json

[
  {
    "Name": "Zcash Social Sentiment & Market Pulse Data | BitMart X Insight",
    "Url": "https://www.bitmart.com/ai/xinsight/coins/detail/ZEC"
  },
  {
    "Name": "Zcash News Today (ZEC) – Latest Updates & Trends",
    "Url": "https://www.coinbird.com/cryptocurrencies/zcash/news"
  },
  {
    "Name": "Will Zcash (ZEC) Price Finally Retest $500 After Nearly 8 Years?",
    "Url": "https://finance.yahoo.com/news/zcash-zec-price-finally-retest-150000437.html"
  },
  {
    "Name": "Latest Zcash News - (ZEC) Future Outlook, Trends & Market Insights",
    "Url": "https://coinmarketcap.com/cmc-ai/zcash/latest-updates/"
  },
  {
    "Name": "Zcash and the Altcoin Season Indicator: A Technical and Sentiment ...",
    "Url": "https://www.ainvest.com/news/zcash-altcoin-season-indicator-technical-sentiment-driven-analysis-2510/"
  },
  {
    "Name": "Zcash Real-Time Price Performance, Futures Metrics, Spot & Futures ...",
    "Url": "https://www.coinglass.com/currencies/ZEC"
  },
  {
    "Name": "Zcash(ZEC) Price Today, ZEC to USD Real-Time, Latest Discussions ...",
    "Url": "https://stocktwits.com/coins/zcash"
  },
  {
    "Name": "ZEC’s Record $2.27B Market Cap Signals Major Shift in Investor Sentiment",
    "Url": "https://www.ethnews.com/zecs-record-2-27b-market-cap-signals-major-shift-in-investor-sentiment/"
  },
  {
    "Name": "ZCash (ZEC) Latest News Articles - CoinDesk",
    "Url": "https://www.coindesk.com/price/zec/news"
  },
  {
    "Name": "Reasons why Zcash is surging on Thursday - FXStreet",
    "Url": "https://www.fxstreet.com/cryptocurrencies/news/zcash-price-forecast-zec-extends-rally-as-demand-for-privacy-protocols-surges-202510091213"
  }
]

```

03:15:56.069 - Downloading page content from: `https://www.bitmart.com/ai/xinsight/coins/detail/ZEC`

03:15:56.069 - Downloading page content from: `https://www.coinbird.com/cryptocurrencies/zcash/news`

03:15:56.069 - Downloading page content from: `https://finance.yahoo.com/news/zcash-zec-price-finally-retest-150000437.html`

03:15:56.069 - Downloading page content from: `https://coinmarketcap.com/cmc-ai/zcash/latest-updates/`

03:15:56.069 - Downloading page content from: `https://www.ainvest.com/news/zcash-altcoin-season-indicator-technical-sentiment-driven-analysis-2510/`

03:15:56.081 - 10 website results found for : Recent news about Zcash (ZEC) over the last 7 days using https://www.dlnews.com/


### Website search results

```json

[
  {
    "Name": "Zcash price surge continues despite market turmoil – DL News",
    "Url": "https://www.dlnews.com/articles/markets/zcash-price-surge-continues-despite-market-turmoil/"
  },
  {
    "Name": "Zcash surges tenfold as investors bet on privacy as ban looms",
    "Url": "https://www.dlnews.com/articles/markets/zcash-surges-tenfold-as-investors-bet-on-privacy-as-ban-looms/"
  },
  {
    "Name": "Zcash price primed for 45% breakout as Grayscale files for ETF",
    "Url": "https://www.dlnews.com/articles/markets/zcash-price-primed-for-45-percent-breakout-as-grayscale-files-for-etf/"
  },
  {
    "Name": "Why Zcash price is up 700% since September, according to Galaxy Digital",
    "Url": "https://www.dlnews.com/articles/markets/why-privacy-token-zcash-price-is-up-700-percent-since-september/"
  },
  {
    "Name": "Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% ...",
    "Url": "https://www.dlnews.com/articles/people-culture/zcash-foundation-shakes-up-leadership-amidst-zec-token-price-rally/"
  },
  {
    "Name": "Winklevoss twins bet on Zcash with new treasury firm targeting 5% ...",
    "Url": "https://www.dlnews.com/articles/markets/winklevoss-twins-bet-on-zcash-with-new-treasury-firm/"
  },
  {
    "Name": "Monero and Zcash’s liquidity dries up as Binance eyes ... - DL News",
    "Url": "https://www.dlnews.com/articles/defi/monero-and-zcash-liquidity-runs-dry-as-binance-may-delist/"
  },
  {
    "Name": "Ika Announces EdDSA Signatures, Expanding Native Support to Solana ...",
    "Url": "https://www.dlnews.com/external/ika-announces-eddsa-signatures-expanding-native-support-to-solana-zcash-cardano-and-more/"
  },
  {
    "Name": "How privacy coins Firo and Zcash dodged Binance delisting ... - DL News",
    "Url": "https://www.dlnews.com/articles/defi/how-privacy-coins-firo-and-zcash-dodged-binance-delisting/"
  },
  {
    "Name": "ZKasino’s year-long silence on investor refunds ends in a $27m ...",
    "Url": "https://www.dlnews.com/articles/defi/crypto-gambling-app-zkasino-liquidated/"
  }
]

```

03:15:56.081 - Downloading page content from: `https://www.dlnews.com/articles/markets/zcash-price-surge-continues-despite-market-turmoil/`

03:15:56.081 - Downloading page content from: `https://www.dlnews.com/articles/markets/zcash-surges-tenfold-as-investors-bet-on-privacy-as-ban-looms/`

03:15:56.081 - Downloading page content from: `https://www.dlnews.com/articles/markets/zcash-price-primed-for-45-percent-breakout-as-grayscale-files-for-etf/`

03:15:56.081 - Downloading page content from: `https://www.dlnews.com/articles/markets/why-privacy-token-zcash-price-is-up-700-percent-since-september/`

03:15:56.081 - Downloading page content from: `https://www.dlnews.com/articles/people-culture/zcash-foundation-shakes-up-leadership-amidst-zec-token-price-rally/`

03:15:56.081 - Downloading page content from: `https://www.dlnews.com/articles/markets/winklevoss-twins-bet-on-zcash-with-new-treasury-firm/`

03:15:56.082 - Downloading page content from: `https://www.dlnews.com/articles/defi/monero-and-zcash-liquidity-runs-dry-as-binance-may-delist/`

03:15:56.082 - Downloading page content from: `https://www.dlnews.com/external/ika-announces-eddsa-signatures-expanding-native-support-to-solana-zcash-cardano-and-more/`

03:15:56.082 - Downloading page content from: `https://www.dlnews.com/articles/defi/how-privacy-coins-firo-and-zcash-dodged-binance-delisting/`

03:15:56.082 - Downloading page content from: `https://www.dlnews.com/articles/defi/crypto-gambling-app-zkasino-liquidated/`

03:15:56.203 - 10 search results found for : Recent news and sentiment analysis for Zcash (ZEC) over the last 7 days


### Search Results Object

```json

[
  {
    "Name": "Zcash Exchange Balances Plunge 20% - Breakout To $800 Likely - BeInCrypto",
    "Url": "https://beincrypto.com/zcash-accumulation-sets-stage-for-zec-price-breakout/"
  },
  {
    "Name": "Zcash News Today (ZEC) – Latest Updates & Trends",
    "Url": "https://www.coinbird.com/cryptocurrencies/zcash/news"
  },
  {
    "Name": "Zcash Price Prediction, News, and Analysis (ZEC) - MarketBeat",
    "Url": "https://www.marketbeat.com/cryptocurrencies/zcash/"
  },
  {
    "Name": "Latest Zcash News - (ZEC) Future Outlook, Trends & Market Insights",
    "Url": "https://coinmarketcap.com/cmc-ai/zcash/latest-updates/"
  },
  {
    "Name": "ZCash (ZEC) 7-day Price Change | MEXC Crypto Pulse",
    "Url": "https://www.mexc.com/en-GB/crypto-pulse/article/zcash-zec-7-day-price-change-64040"
  },
  {
    "Name": "How Low Can Zcash Price Go After ZEC’s 30% Drop From ... - Cointelegraph",
    "Url": "https://cointelegraph.com/news/zcash-down-30-percent-november-will-zec-price-crash-further"
  },
  {
    "Name": "Crypto News: Zcash Rebounds From $300 as Expert Flags Key Levels",
    "Url": "https://www.livebitcoinnews.com/expert-shares-zcash-zec-price-update-heres-his-outlook/"
  },
  {
    "Name": "ZCash (ZEC) Latest News Articles - CoinDesk",
    "Url": "https://www.coindesk.com/price/zec/news"
  },
  {
    "Name": "Zcash Price (ZEC): Key Insights, Technical Analysis, and Market ... - OKX",
    "Url": "https://www.okx.com/learn/zcash-price-zec-insights-analysis-trends"
  },
  {
    "Name": "Will Zcash (ZEC) Price Finally Retest $500 After Nearly 8 Years?",
    "Url": "https://finance.yahoo.com/news/zcash-zec-price-finally-retest-150000437.html"
  }
]

```

03:15:56.203 - Downloading page content from: `https://beincrypto.com/zcash-accumulation-sets-stage-for-zec-price-breakout/`

03:15:56.203 - Downloading page content from: `https://www.coinbird.com/cryptocurrencies/zcash/news`

03:15:56.204 - Downloading page content from: `https://www.marketbeat.com/cryptocurrencies/zcash/`

03:15:56.204 - Downloading page content from: `https://coinmarketcap.com/cmc-ai/zcash/latest-updates/`

03:15:56.204 - Downloading page content from: `https://www.mexc.com/en-GB/crypto-pulse/article/zcash-zec-7-day-price-change-64040`

03:15:56.204 - 10 search results found for : Recent Reddit discussions and sentiment about Zcash (ZEC)


### Search Results Object

```json

[
  {
    "Name": "Zcash - Reddit",
    "Url": "https://www.reddit.com/r/zec/"
  },
  {
    "Name": "Zcash(ZEC) Price Today, ZEC to USD Real-Time, Latest Discussions ...",
    "Url": "https://stocktwits.com/coins/zcash"
  },
  {
    "Name": "Will Zcash (ZEC) Price Finally Retest $500 After Nearly 8 Years?",
    "Url": "https://finance.yahoo.com/news/zcash-zec-price-finally-retest-150000437.html"
  },
  {
    "Name": "People Share Thoughts on ZEC (ZCash) in Forums : BlockScopeX",
    "Url": "https://blockscopex.com/news/opinions-on-zec-zcash-in-forums/"
  },
  {
    "Name": "Latest Zcash News - (ZEC) Future Outlook, Trends & Market Insights",
    "Url": "https://coinmarketcap.com/cmc-ai/zcash/latest-updates/"
  },
  {
    "Name": "Taking a Step Back: Closing the ZEC Chapter | CoinDailies",
    "Url": "https://coindailies.com/news/closing-chapter-with-zec-investment/"
  },
  {
    "Name": "ZEC Reddit Mentions | ChartExchange",
    "Url": "https://chartexchange.com/symbol/crypto-zecrlusd/trends/reddit/"
  },
  {
    "Name": "Zcash Community Forum - An open forum for Zcash users and enthusiasts ...",
    "Url": "https://forum.zcashcommunity.com/"
  },
  {
    "Name": "ZEC - Zcash - Reddit Mentions and Sentiments - Memeberg Terminal",
    "Url": "https://www.memebergterminal.com/cryptos/zec"
  },
  {
    "Name": "Zcash: Why ZEC keeps failing at $520 despite brief rebounds",
    "Url": "https://ambcrypto.com/zcash-why-zec-keeps-failing-at-520-despite-brief-rebounds/"
  }
]

```

03:15:56.205 - Downloading page content from: `https://www.reddit.com/r/zec/`

03:15:56.205 - Downloading page content from: `https://stocktwits.com/coins/zcash`

03:15:56.205 - Downloading page content from: `https://finance.yahoo.com/news/zcash-zec-price-finally-retest-150000437.html`

03:15:56.205 - Downloading page content from: `https://blockscopex.com/news/opinions-on-zec-zcash-in-forums/`

03:15:56.205 - Downloading page content from: `https://coinmarketcap.com/cmc-ai/zcash/latest-updates/`

----
**WARNING:**
> 03:15:56.538 - Failed to download page content from: `https://blockscopex.com/news/opinions-on-zec-zcash-in-forums/` due to Response status code does not indicate success: 403 (Forbidden)..

----
**WARNING:**
> 03:15:56.572 - Failed to download page content from: `https://www.mexc.com/en-GB/crypto-pulse/article/zcash-zec-7-day-price-change-64040` due to Response status code does not indicate success: 403 (Forbidden)..

----
**WARNING:**
> 03:15:56.604 - Failed to download page content from: `https://www.reddit.com/r/zec/` due to Response status code does not indicate success: 403 (Blocked)..

03:15:56.962 - Successfully downloaded page content from: `https://finance.yahoo.com/news/zcash-zec-price-finally-retest-150000437.html`

03:15:57.041 - Successfully downloaded page content from: `https://finance.yahoo.com/news/zcash-zec-price-finally-retest-150000437.html`

03:15:57.065 - Successfully downloaded page content from: `https://beincrypto.com/zcash-accumulation-sets-stage-for-zec-price-breakout/`

03:15:57.141 - Successfully downloaded page content from: `https://coinmarketcap.com/cmc-ai/zcash/latest-updates/`

03:15:57.180 - Successfully downloaded page content from: `https://coinmarketcap.com/cmc-ai/zcash/latest-updates/`

03:15:57.191 - Successfully downloaded page content from: `https://coinmarketcap.com/cmc-ai/zcash/latest-updates/`

03:15:57.277 - Successfully downloaded page content from: `https://www.coinbird.com/cryptocurrencies/zcash/news`

03:15:57.290 - Successfully downloaded page content from: `https://www.coinbird.com/cryptocurrencies/zcash/news`

03:15:57.365 - Successfully downloaded page content from: `https://www.dlnews.com/articles/markets/zcash-price-primed-for-45-percent-breakout-as-grayscale-files-for-etf/`

03:15:57.400 - Successfully downloaded page content from: `https://www.marketbeat.com/cryptocurrencies/zcash/`

### Search Results

```
<searchResult>
[doc1]:
**Zcash Exchange Balances Plunge 20% - Breakout To $800 Likely - BeInCrypto**
[](https://beincrypto.com/) - Feed
- Newsletters
- Bonus Hunter
- Top Picks
- MarketsPricesExchangesConvert
- Advertise
- Remote Jobs
English For Business
[Advertise](https://advertise.beincrypto.com/) [Contact Us](https://beincrypto.com/contact/) Company
[About Us](https://beincrypto.com/about/) [Our Authors](https://beincrypto.com/our-authors/) [Careers 🚀](https://beincrypto.com/careers/) [Our Team](https://beincrypto.com/our-team/) [News](https://beincrypto.com/news/) [Learn](https://beincrypto.com/learn/) [Bonus Hunter](https://beincrypto.com/bonus-hunter/) [Feed](https://beincrypto.com/) [Top Picks](https://beincrypto.com/top-picks/) [Special Edition](https://beincrypto.com/special-edition/) [Careers 🚀](https://beincrypto.com/careers/) [Our Authors](https://beincrypto.com/our-authors/) [Our Team](https://beincrypto.com/our-team/) [Advertise](https://advertise.beincrypto.com/) [Contact Us](https://beincrypto.com/contact/) [About Us](https://beincrypto.com/about/) [Crypto News](https://beincrypto.com/news/) [Ripple (XRP) News](https://beincrypto.com/tag/xrp-news/) [Bitcoin (BTC) News](https://beincrypto.com/tag/bitcoin-news/) [Analysis](https://beincrypto.com/type/analysis/) [Ethereum (ETH) News](https://beincrypto.com/tag/ethereum-news/) [US Crypto News](https://beincrypto.com/tag/united-states-of-america/) [Cardano (ADA) News](https://beincrypto.com/tag/ada-news/) [Solana (SOL) News](https://beincrypto.com/tag/solana-news/) [Memecoins News](https://beincrypto.com/tag/memecoin-news/) [ETF News](https://beincrypto.com/tag/etf-news/) [Altcoins News](https://beincrypto.com/tag/altcoin-news/) [Markets](https://beincrypto.com/price/) [Prices](https://beincrypto.com/price/) [Exchanges](https://beincrypto.com/exchanges/) [Convert](https://beincrypto.com/convert/) [Remote Jobs](https://beincrypto.com/jobs/) [Fast News](https://t.me/+F2LkP3N3LyY5NTMy) [Newsletters](https://beincrypto.com/newsletters/) [Back](https://beincrypto.com/) [Trusted](https://beincrypto.com/trust-project/) [Analysis](https://beincrypto.com/type/analysis/) [Markets](https://beincrypto.com/category/markets/) 
# Zcash Accumulation Sets The Stage For ZEC Price Breakout To $800

![Zcash Accumulation Sets The Stage For ZEC Price Breakout To $800](https://beincrypto.com/_mfes/post/_next/image/?url=https%3A%2F%2Fassets.beincrypto.com%2Fimg%2FqzLlTJpAKhEdcskq29wCgK-90RE%3D%2Fsmart%2Feb1cc6a195d348ef84054a45079a4a78&amp;w=1920&amp;q=75)

![author avatar](https://beincrypto.com/_mfes/post/_next/image/?url=https%3A%2F%2Fassets.beincrypto.com%2Fimg%2F-t8a76Q6aMRqAejOF3EB9lZesIk%3D%2Fsmart%2F5a337e10d3bc4d3ab8a882c23e7ad016&amp;w=64&amp;q=75)

Written byAaryamann Shrivastava

![editor avatar](https://beincrypto.com/_mfes/post/_next/image/?url=https%3A%2F%2Fassets.beincrypto.com%2Fimg%2Fh-hQzOzK42E_4nq7oQ0rsXup8jU%3D%2Fsmart%2F21b210244b384c07840d7ceeb5f9d8fb&amp;w=64&amp;q=75)

Edited byHarsh Notariya
06 January 2026 14:00 UTC [Trusted](https://beincrypto.com/trust-project/) - Zcash exchange balances drop 20.75%, signaling strong accumulation and reduced selling pressure.
- Futures funding flips positive as traders shift from shorts to bullish positioning.
- ZEC price is trading near $512, eyeing a 38% breakout toward the $800 target.
Promo
[#Altcoin Analysis](https://beincrypto.com/tag/altcoin-analysis/) 
Zcash price has moved sideways over the past several days, consolidating after recent volatility. While this pause may appear bearish, it often signals strength following an uptrend.

Price stability near current levels suggests buyers are defending positions, and recent investor behavior further supports a constructive outlook for ZEC.
Sponsored Sponsored 
## Zcash Holders Are Buying

Exchange data shows a sharp reduction in available ZEC supply. According to Nansen, Zcash holdings on centralized exchanges dropped by 20.75% in the last 24 hours. Such a decline indicates significant outflows, which usually reflect investor accumulation rather than distribution.

When coins move off exchanges, selling pressure often decreases. Investors tend to transfer assets into private wallets when expecting higher prices. This behavior suggests rising confidence among ZEC holders, who appear willing to hold rather than liquidate at current levels.

Want more token insights like this? Sign up for Editor Harsh Notariya’s Daily Crypto Newsletter here.

![ZEC Exchange Holdings](https://assets.beincrypto.com/img/1nWRUSJNiStXThyBIqYygBWvbbY=/smart/d3fcfbec39234a4dba7d6fd36471a9f5)
ZEC Exchange Holdings. Source: [Nansen](https://app.nansen.ai/) 
Sustained exchange outflows often precede upward price moves. Reduced liquid supply can amplify price reactions once demand increases. In Zcash’s case, this accumulation trend strengthens the bullish narrative forming around its current consolidation phase.
Sponsored Sponsored 
## ZEC Traders Turn Bullish As Well

Derivatives market data shows a notable shift in trader positioning. For nine consecutive days, ZEC futures were dominated by short contracts. This imbalance kept the funding rate negative, reflecting bearish expectations among leveraged traders.

Over the last 24 hours, that trend reversed. Funding rates turned positive, indicating long contracts now outweigh shorts. This change suggests traders are positioning for upside rather than further downside.

![ZEC Funding Rate.](https://assets.beincrypto.com/img/zEfcqPlzvtishgFnJGPSJoDGSus=/smart/7390b03a574d4db7a41d8c5208b906c8)
ZEC Funding Rate. Source: [Coinglass](https://www.coinglass.com/) 
Positive funding reflects improving sentiment and willingness to pay a premium to stay long. When futures sentiment aligns with spot accumulation, momentum often accelerates. This alignment supports the view that ZEC may be preparing for a directional move higher.

## ZEC Price Eyes Breakout

ZEC trades near $512 at the time of writing, moving within an ascending wedge pattern. This structure typically resolves with a breakout. A successful move above resistance could drive price nearly 38% higher, targeting the $802 level.

Breakout odds are improving after ZEC recently tested and bounced from the lower trend line. Technical support held firmly, reinforcing buyer control. Accumulation and improving futures sentiment further increase the likelihood of continuation. A confirmed breakout requires flipping $600 into support.

![ZEC Price Analysis.](https://assets.beincrypto.com/img/YYLcvBklA-Ogsgnahv7bFUeQUxA=/smart/34c116e645794ab18e9a0f02e2351a33)
ZEC Price Analysis. Source: [TradingView](https://www.tradingview.com/) 
Downside risk remains if sentiment shifts abruptly. Renewed selling or a failed breakout could pressure the price lower. A drop below $500 would weaken the structure. Under such conditions, the Zcash price may fall toward $442, invalidating the bullish thesis.
You might also like
[AnalysisMarkets15 hours agoSUI Jumps 37% in a Week, but Profit-Taking Puts $2 Support at Risk](https://beincrypto.com/sui-price-rally-profit-booking-risk/) [NewsletterSubscribeDaily Crypto InsightsInsights, news and analysis of the crypto market straight to your inbox](https://beincrypto.com/newsletters/) [Crypto Exchanges2 months agoBest Crypto Platforms for DePIN Tokens in 2026](https://beincrypto.com/top-picks/depin-token-platforms/) 
Disclaimer

In line with the Trust Project guidelines, this price analysis article is for informational purposes only and should not be considered financial or investment advice. BeInCrypto is committed to accurate, unbiased reporting, but market conditions are subject to change without notice. Always conduct your own research and consult with a professional before making any financial decisions. Please note that our Terms and Conditions, Privacy Policy, and Disclaimers have been updated.
Sponsored Sponsored Read Next

![K-Shaped Crypto Market: Top Assets Rally as Altcoins Lag in 2026](https://beincrypto.com/_mfes/post/_next/image/?url=https%3A%2F%2Fassets.beincrypto.com%2Fimg%2FCeuHN4mv9OmBrr72oAzbTu25Gys%3D%2Fsmart%2F0e2a9520c56c4b0b9273fb8c37459ecf&amp;w=3840&amp;q=75)
[NewsMarkets1 minute agoK-Shaped Crypto Market: Top Assets Rally as Altcoins Lag in 2026](https://beincrypto.com/k-shaped-crypto-market-2026/) [](https://x.com/beincrypto) [](https://www.linkedin.com/company/beincrypto/) [](https://www.instagram.com/beincrypto/) [](https://t.me/+OUUQ7wNqpikzN2Zi) [](https://www.youtube.com/c/Beincrypto) Sign up for our newsletters
Bonus Hunter
A curated list of top giveaways, airdrops and special activation offers
Daily Crypto Insights
Insights, news and analysis of the crypto market straight to your inbox
Crypto Leaders
Outlook of the industry, market trends and key opinions from leaders within the industry
Web3 jobs
Information, advice and the latest vacancies to help you get into the Web3 world
Company [About Us](https://beincrypto.com/about/) [Our Authors](https://beincrypto.com/our-authors/) [Careers 🚀](https://beincrypto.com/careers/) Products [News](https://beincrypto.com/type/news/) [Learn](https://beincrypto.com/type/learn/) [Markets](https://beincrypto.com/price/) [Learn-to-Earn](https://beincrypto.com/learn-to-earn/) [Bonus Hunter](https://beincrypto.com/bonus-hunter/) [Newsletters](https://beincrypto.com/newsletters/) [Top Picks](https://beincrypto.com/top-picks/) [Special Edition](https://beincrypto.com/special-edition/) [Fast News](https://t.me/+sLfpqc66saQxMTQy) Resources [Advertise](https://advertise.beincrypto.com/) [Remote Jobs](https://beincrypto.com/jobs/) [Contact Us](https://beincrypto.com/contact/) [The Trust Project](https://beincrypto.com/trust-project/) [Verification Methodology](https://beincrypto.com/methodology/) [Advertiser Disclosure](https://beincrypto.com/advertising-disclosure/) © 2026 BeInNews Academy [Terms](https://beincrypto.com/terms-and-conditions/) [Privacy](https://beincrypto.com/privacy-policy/) [Disclaimer](https://beincrypto.com/disclaimer/) [Cookie Settings](https://beincrypto.com/)
</searchResult>


<searchResult>
[doc2]:
**Zcash News Today (ZEC) – Latest Updates & Trends**
[](https://www.coinbird.com/) [](https://www.coinbird.com/) [](https://www.coinbird.com/) 
![Zcash Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/ZEC.svg)

![Zcash Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/ZEC.svg)

# Zcash news
Latest Zcash news and market trends
[Buy ZEC](https://www.coinbird.com/go/crypto_buy) [Latest ZEC news](https://www.coinbird.com/cryptocurrencies/zcash/news#latest-news) [Zcash news sentimentLast 30 daysPositive77/100](https://www.coinbird.com/cryptocurrencies/zcash/news#news-sentiment) 
## The most important Zcash news this month
AI summary 
### Zcash Shielded Supply Rises

Zebra 3.1 upgrade increased shielded supply to almost 25 %, signaling growing privacy adoption.

### Cypherpunk Buys $28 M Zcash

Winklevoss-backed firm purchased 56,418 ZEC, raising holdings to 1.76 % of supply, reflecting confidence in privacy coins.

### Unshielded ZEC Spike Sparks Sell‑Off

200,000 ZEC moved to transparent pool and a 74k transfer to Binance raised concerns about potential sell‑off and price drop.

### What this could mean for Zcash

The rapid growth of shielded ZEC, coupled with high-profile institutional purchases, boosts confidence and could drive price upward, but recent unshielding activity introduces short-term volatility risks.
The AI-generated summaries are experimental and may contain errors. Not investment advice. Last updated: 2026-01-06T16:34:02.141+00:00 . 
## Latest Zcash news

Updated at 2026-01-06T23:30:52.492Z

Updated at 2026-01-06T23:30:52.492Z
Headline
Impact score Impact score 
Our Impact Score (0–100) uses AI to estimate how strongly a news item could affect the coin over the next 24–72 hours. It primarily considers direct relevance to the coin, novelty, source quality and diversity, potential reach, and the type of event, such as ETFs and regulation, product launches, partnerships, or hacks. Higher scores are assigned to substantiated research forecasts, corporate buy or sell activity, and clear statements from well-known figures. Low scores apply to bare price predictions without substance, minor price moves without context, or PR pieces with no informational value. The score is computed automatically and updated continuously. The AI may make mistakes. When in doubt, please review the linked original sources. Not financial advice.
Published

## Zcash news sentiment

Last 30 days
Positive
77 /100 
Current Zcash news sentiment is positive (77/100), based on 14 news articles from the past 30 days. Our algorithm scores each article for relevance and sentiment (positive, neutral, or negative) and weights high-impact stories more. The score updates automatically as new Zcash headlines arrive.

## Zcash market trends
Positive Negative Positive 
Momentum
Momentum 
Momentum measures the current market dynamics of a cryptocurrency. The value is based on technical indicators such as the Relative Strength Index (RSI), the Fear & Greed Index, and the short-term price trend over the past 30 days. Positive values indicate upward momentum, negative values indicate downward momentum. This indicator is for informational purposes only and does not constitute investment advice.
Positive [Momentum](https://www.coinbird.com/cryptocurrencies/zcash/news#buy-timing-dashboard) [Momentum](https://www.coinbird.com/cryptocurrencies/zcash/buy#buy-timing-dashboard) Fear Fear Greed 
Fear & Greed Index
Fear & Greed Index 
The Fear and Greed Index for cryptocurrencies is a sentiment indicator measuring market mood on a scale from 0 (extreme fear) to 100 (extreme greed). It aggregates data from various sources such as volatility, market momentum, social media, market dominance, and Google Trends to assess overall market sentiment. Values in the “Greed” range (55-100) indicate a positive, potentially overoptimistic market mood, signaling a possibly overheated market. A “Neutral” value (45-54) reflects a balanced market sentiment. Values in the “Fear” range (0-44) indicate negative market sentiment, signaling fear or pessimism among investors and possibly an undervalued market.
Fear [Fear & Greed Index](https://www.coinbird.com/learn/fear-greed-index-bitcoin) 16 /30 days 
Price trend
Price trend 
The price trend shows short-term price action over the last 30 trading days. For each day, the open is compared to the close: if the close is higher, the day is marked green; otherwise red. A sustained majority of green days suggests an uptrend that may persist in the short to medium term.
Positive [Zcash price](https://www.coinbird.com/cryptocurrencies/zcash/price) 
$501.31
+46.57% last 30 days 
### Price performance
Price performance 
The price development, often referred to as return on investment (ROI), is a metric that provides insight into the past profitability and performance of an investment. In this context, ROI describes the percentage change in price and thus the retrospective “return” of a cryptocurrency over a defined period. Past performance is not indicative of future results.
<table>
  <tr>
    <td>↑+0.15%</td>
    <th>Hour</th>
  </tr>
  <tr>
    <td>↓-0.37%</td>
    <th>Day</th>
  </tr>
  <tr>
    <td>↓-4.35%</td>
    <th>Week</th>
  </tr>
  <tr>
    <td>↑+46.57%</td>
    <th>Month</th>
  </tr>
  <tr>
    <td>↑+1,160.13%</td>
    <th>200d</th>
  </tr>
  <tr>
    <td>↑+745.09%</td>
    <th>Year</th>
  </tr>
</table>

## Other cryptocurrency news

![Bitcoin Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/BTC.svg)

BitcoinNews

NEGATIVE2025-12-27T17:01:38+00:00•decrypt.co

Bitcoin Whales Woke Up in 2025 and Moved Billions in BTC—Here's Why
90 /100 
POSITIVE2025-12-10T01:44:16+00:00•cointelegraph.com

Vivek Ramaswamy's Strive to raise $500M to buy Bitcoin
90 /100 [Latest Bitcoin news](https://www.coinbird.com/cryptocurrencies/bitcoin/news) 
![Ethereum Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/ETH.svg)

EthereumNews

POSITIVE2026-01-05T17:04:59+00:00•decrypt.co

Ethereum's Blockchain Trilemma 'Solved': Vitalik Buterin
90 /100 
POSITIVE2026-01-05T12:26:24+00:00•cryptoslate.com

Vitalik Buterin declares Ethereum solved crypto Trilemma, yet his 2030 roadmap exposes a massive ideological risk
90 /100 [Latest Ethereum news](https://www.coinbird.com/cryptocurrencies/ethereum/news) 
![XRP Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/XRP.svg)

XRPNews

POSITIVE2025-12-11T15:43:35+00:00•theblock.co

New XRP ETF hits the market with launch of 21Shares' TOXR
90 /100 
POSITIVE2025-12-08T13:20:11+00:00•coindesk.com

U.S. Spot XRP ETFs Hit 15-Day Inflow Streak, Near $1B Milestone
90 /100 [Latest XRP news](https://www.coinbird.com/cryptocurrencies/xrp/news) 
![Solana Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/SOL.svg)

SolanaNews

POSITIVE2026-01-06T19:21:01+00:00•theblock.co

‘Shocker': Morgan Stanley's Bitcoin and Solana ETF filings signal deep institutional commitment to crypto
90 /100 
NEGATIVE2025-12-30T10:39:00+00:00•beincrypto.com

HNUT Meme Coin Collapses 99% on Solana, PeckShield Flags Bundled Rug Pull
85 /100 [Latest Solana news](https://www.coinbird.com/cryptocurrencies/solana/news) 
![Dogecoin Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/DOGE.svg)

DogecoinNews

NEGATIVE2025-12-25T14:01:03+00:00•decrypt.co

The Year in Dogecoin 2025: DOGE Goes Political and Commercial
85 /100 
POSITIVE2025-12-25T19:06:23+00:00•cryptoslate.com

The memecoin hall of shame: 10 tokens that defined 2025 wildest trades
80 /100 [Latest Dogecoin news](https://www.coinbird.com/cryptocurrencies/dogecoin/news) 
![Cardano Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/ADA.svg)

CardanoNews

POSITIVE2025-12-14T18:11:25+00:00•cryptoslate.com

Cardano now has institutional-grade infrastructure, but a glaring $40 million liquidity gap threatens to stall growth
80 /100 
POSITIVE2025-12-15T17:12:01+00:00•beincrypto.com

3 Altcoins Facing Liquidation Risks in the Third Week of December
70 /100 [Latest Cardano news](https://www.coinbird.com/cryptocurrencies/cardano/news) 
### Other crypto news
- BNBnews
- Tronnews
- Bitcoin Cashnews
- Chainlinknews
- Stellarnews
- Suinews
- Hyperliquidnews
- Litecoinnews
- Avalanchenews
- Hederanews
- Shiba Inunews
- Uniswapnews
- Polkadotnews
- Pepenews
- Aavenews
- NEAR Protocolnews
- Worldcoinnews
- Ondonews
- Kaspanews
- Polygon (POL)news
- Algorandnews
- Rendernews
- Cosmosnews
- Filecoinnews
- VeChainnews
- Bonknews
- ASI (Fetch.ai)news
- Tezosnews
- IOTAnews
- The Graphnews
- Sonic (Fantom)news
- The Sandboxnews
- Decentralandnews
- Axie Infinitynews

## All about Zcash
[What is Zcash?Important details and simple explanation of Zcash.](https://www.coinbird.com/cryptocurrencies/zcash/overview) [Zcash priceLive price, charts and market data for Zcash.](https://www.coinbird.com/cryptocurrencies/zcash/price) [Zcash predictionPrice forecasts and key metrics to analyze Zcash.](https://www.coinbird.com/cryptocurrencies/zcash/price-prediction) [Buy ZcashFind the cheapest and best places to buy Zcash.](https://www.coinbird.com/cryptocurrencies/zcash/buy) [Zcash converterSee what past Zcash buys would be worth today.](https://www.coinbird.com/cryptocurrencies/zcash/converter) 
Our data on cryptocurrencies was last updated on 2026-01-07T00:05:26.994203+00:00. Sources: CoinGecko, defillama.com, coincodex.com.

The content on this website is provided for general informational purposes only and does not constitute financial, investment, legal, or tax advice. It should not be interpreted as a recommendation to buy, sell, or hold cryptocurrencies, nor as a guarantee of future price developments. You are responsible for independently verifying any information before using a listed service. Trading cryptocurrencies involves significant risk and can result in the total loss of your capital. Past performance is not indicative of future results. We do not accept any liability for the timeliness, accuracy, or completeness of the information provided, including content from external or third-party sources. All actions are taken at your own risk. Some links on this website are affiliate links. If you purchase a product or use a service through these links, we may receive a commission at no additional cost to you. Our content, comparisons, and rankings remain editorially independent. This helps us provide free content and continue developing the platform. Thank you for your support.
</searchResult>


<searchResult>
[doc3]:
**Zcash Price Prediction, News, and Analysis (ZEC) - MarketBeat**
[Skip to main content](https://www.marketbeat.com/cryptocurrencies/zcash/#main) [](https://www.marketbeat.com/) [Free Trial](https://marketbeat.com/subscribe/all-access/?ReferralType=HeaderButton) [→ The $100 Trillion AI Story No One Is Telling You](https://www.marketbeat.com/scripts/redirect.aspx?TriggeredCampaignID=16919&UserID=0&Placement=NativeDisplay&Source=NativeDisplay&interstitial=1) (From Brownstone Research) (Ad) 
![tc pixel](https://www.marketbeat.com/scripts/TriggeredCampaignPixel.ashx?TriggeredCampaignID=16919&Placement=NativeDisplay&Source=NativeDisplay)

# Zcash Crypto Price Prediction, Value and Chart (ZEC)

![Zcash logo](https://www.marketbeat.com/logos/cryptocurrencies/zcash-ZEC.png?v=2022-10-05)
**$498.27** -3.24 (-0.65%) (As of 01/6/2026 10:07 PM ET)
1-Hour Change **+0.8716%** 24-Hour Change **+0.8716%** 7-Day Range **$480.82▼$544.23** 1-Day Volume **$745.40 million** Market Cap **$8.21 billion** BTC Price **0.00536158 BTC** Circulating Supply **16.47 million** Total Supply **16.47 million** Maximum Supply **21.00 million** [Currency Profile](https://www.marketbeat.com/cryptocurrencies/zcash/#tabContentCurrencyProfile) [Headlines](https://www.marketbeat.com/cryptocurrencies/zcash/#tabContentHeadlines) [Advanced Chart](https://www.marketbeat.com/cryptocurrencies/zcash/#tabContentAdvancedChart) [Social Media](https://www.marketbeat.com/cryptocurrencies/zcash/#tabContentSocialMedia) 30 days | 90 days | 180 days | [Advanced Chart](https://www.marketbeat.com/cryptocurrencies/zcash/#) Receive ZEC News and Prices via Email
Sign-up to receive the latest news and price data for Zcash and its competitors with MarketBeat's CryptoBeat newsletter. Email Address 
![ZEC stock logo](https://www.marketbeat.com/logos/cryptocurrencies/zcash-ZEC.png?v=2022-10-05)

## About Zcash (ZEC)
ZCash (ZEC) is a digital currency and decentralized open-source cryptocurrency, launched in 2016. It provides users with enhanced privacy and selective transparency of transactions. ZCash is based on the zero-knowledge proof protocol known as zk-SNARKs. This protocol allows the network to maintain a secure ledger of balances without disclosing the parties or amounts involved. Transactions can be audited, verified and tracked without revealing the sender, receiver or transaction amount. ZEC is an inflationary currency, with a maximum supply of 21 million coins. It is accepted by a growing number of merchants, exchanges and other services. 
Description provided by CryptoCompare.

## Zcash News
[](https://www.benzinga.com/crypto/cryptocurrency/26/01/49736160/sol-ada-are-2025s-trades-this-privacy-coin-leads-the-2026-narrative) [SOL & ADA Are 2025's Trades—This Privacy Coin Leads The 2026 Narrative](https://www.benzinga.com/crypto/cryptocurrency/26/01/49736160/sol-ada-are-2025s-trades-this-privacy-coin-leads-the-2026-narrative) benzinga.com - January 6 at 3:10 PM [](https://seekingalpha.com/article/4857497-bitcoin-ethereum-solana-rebound-strongly-to-start-2026-crypto-overview?feed_item_type=article) [Bitcoin, Ethereum And Solana Rebound Strongly To Start 2026 - Crypto Overview](https://seekingalpha.com/article/4857497-bitcoin-ethereum-solana-rebound-strongly-to-start-2026-crypto-overview?feed_item_type=article) seekingalpha.com - January 6 at 1:24 PM [](https://www.newsbtc.com/bitcoin-news/bitcoin-wins-trump-pumps-gdp-suppresses-oil-hayes/) [Bitcoin Wins As Trump Pumps GDP, Suppresses Oil: Arthur Hayes](https://www.newsbtc.com/bitcoin-news/bitcoin-wins-trump-pumps-gdp-suppresses-oil-hayes/) newsbtc.com - January 6 at 12:07 PM [](https://blog.kraken.com/crypto-education/dentoshi-new-year-new-volatility) [Trading Spaces Recap: New year, new volatility? Dentoshi breaks down BTC, ETH and early signs of life in altcoins](https://blog.kraken.com/crypto-education/dentoshi-new-year-new-volatility) blog.kraken.com - January 6 at 12:07 PM [](https://bitcoinworld.co.in/bitcoin-rally-venezuela-policy-dollars/) [Bitcoin Rally Inevitable: Arthur Hayes Reveals How US Venezuela Policy Will Trigger Massive Dollar Printing](https://bitcoinworld.co.in/bitcoin-rally-venezuela-policy-dollars/) bitcoinworld.co.in - January 6 at 5:05 AM [](https://ambcrypto.com/zcash-why-zec-keeps-failing-at-520-despite-brief-rebounds/) [Zcash: Why ZEC keeps failing at $520 despite brief rebounds](https://ambcrypto.com/zcash-why-zec-keeps-failing-at-520-despite-brief-rebounds/) ambcrypto.com - January 6 at 2:05 AM [](https://invezz.com/news/2026/01/05/ethereums-5k-path-divides-experts-ahead-of-2026/) [Ethereum’s $5K path divides experts ahead of 2026](https://invezz.com/news/2026/01/05/ethereums-5k-path-divides-experts-ahead-of-2026/) invezz.com - January 5 at 5:08 PM [](https://www.investing.com/analysis/zcash-enjoys-strong-support-at-0618-fib-level-despite-recent-pullback-200672696) [Zcash Enjoys Strong Support at 0.618 Fib Level, Despite Recent Pullback](https://www.investing.com/analysis/zcash-enjoys-strong-support-at-0618-fib-level-despite-recent-pullback-200672696) investing.com - January 5 at 4:10 PM [](https://cryptopotato.com/crypto-funds-pull-in-47-2b-in-2025-but-bitcoin-loses-ground/) [Crypto Funds Pull In $47.2B in 2025, But Bitcoin Loses Ground](https://cryptopotato.com/crypto-funds-pull-in-47-2b-in-2025-but-bitcoin-loses-ground/) cryptopotato.com - January 5 at 3:11 PM [](https://www.cryptopolitan.com/zec-gets-unshielded-privacy-investors-exit/) [ZEC retraces gains as whale unshields 1% of supply](https://www.cryptopolitan.com/zec-gets-unshielded-privacy-investors-exit/) cryptopolitan.com - January 5 at 9:22 AM [](https://themerkle.com/markets-look-past-zcash-and-chainlink-as-blockdags-0-40-launch-speculation-comes-into-play-now/) [Markets Look Past Zcash and Chainlink as BlockDAG’s $0.40 Launch Speculation Comes Into Play Now](https://themerkle.com/markets-look-past-zcash-and-chainlink-as-blockdags-0-40-launch-speculation-comes-into-play-now/) themerkle.com - January 3 at 1:11 PM [](https://bitcoinworld.co.in/zec-whale-deposit-binance-analysis/) [ZEC Whale Deposit: A Staggering $35.75M Move to Binance Sparks Market Scrutiny](https://bitcoinworld.co.in/zec-whale-deposit-binance-analysis/) bitcoinworld.co.in - January 3 at 7:07 AM [](https://ambcrypto.com/ethereums-2026-roadmap-puts-institutional-privacy-front-and-center-details/) [Ethereum’s 2026 roadmap puts institutional privacy front and center – Details](https://ambcrypto.com/ethereums-2026-roadmap-puts-institutional-privacy-front-and-center-details/) ambcrypto.com - January 2 at 7:05 AM [](https://thecryptobasic.com/2026/01/02/bitwise-snubs-cardano-in-new-crypto-etftracking-tron-zec-and-9-others/) [Bitwise Snubs Cardano In New Crypto ETFTracking Tron, ZEC, and 9 Others](https://thecryptobasic.com/2026/01/02/bitwise-snubs-cardano-in-new-crypto-etftracking-tron-zec-and-9-others/) thecryptobasic.com - January 2 at 5:10 AM [](https://www.tipranks.com/news/zcash-surged-600-in-2025-here-are-4-predictions-for-on-chain-privacy-in-2026) [Zcash Surged 600% in 2025. Here Are 4 Predictions for On-chain Privacy in 2026](https://www.tipranks.com/news/zcash-surged-600-in-2025-here-are-4-predictions-for-on-chain-privacy-in-2026) tipranks.com - January 1 at 12:31 PM [](https://finbold.com/the-next-big-wave-2-new-cryptos-set-to-dominate-in-2026/) [The next big wave: 2 new cryptos set to dominate in 2026](https://finbold.com/the-next-big-wave-2-new-cryptos-set-to-dominate-in-2026/) finbold.com - January 1 at 9:08 AM [](https://invezz.com/news/2026/01/01/zcash-exploded-this-year-2-privacy-coins-to-watch-in-2026/) [Zcash exploded this year: 2 privacy coins to watch in 2026](https://invezz.com/news/2026/01/01/zcash-exploded-this-year-2-privacy-coins-to-watch-in-2026/) invezz.com - January 1 at 8:05 AM [](https://cryptopotato.com/bitwise-files-for-11-altcoin-etfs-targeting-aave-uni-sui-more/) [Bitwise Files for 11 Altcoin ETFs Targeting AAVE, UNI, SUI, More](https://cryptopotato.com/bitwise-files-for-11-altcoin-etfs-targeting-aave-uni-sui-more/) cryptopotato.com - December 31 at 5:09 PM [](https://bitcoinist.com/bitcoin-ethereum-crypto/) [Forget Bitcoin And Ethereum: Here Are The Cryptocurrencies That Made Gains In Q4](https://bitcoinist.com/bitcoin-ethereum-crypto/) bitcoinist.com - December 31 at 5:06 PM [](https://cryptonews.com/news/best-altcoins-to-buy-on-new-years-eve-that-could-100x-in-2026-31-december-2025/) [Best Altcoins To Buy On New Year’s Eve That Could 100x in 2026 – 31 December 2025](https://cryptonews.com/news/best-altcoins-to-buy-on-new-years-eve-that-could-100x-in-2026-31-december-2025/) cryptonews.com - December 31 at 3:14 PM [](https://en.coin-turk.com/altcoins-break-crucial-boundaries-in-2025/) [Altcoins Break Crucial Boundaries in 2025](https://en.coin-turk.com/altcoins-break-crucial-boundaries-in-2025/) en.coin-turk.com - December 31 at 2:17 PM [](https://coinpaper.com/13480/could-zcash-really-hit-10-000-arthur-hayes-prediction-is-back-in-focus) [Could Zcash Really Hit $10,000? Arthur Hayes’ Prediction Is Back in Focus](https://coinpaper.com/13480/could-zcash-really-hit-10-000-arthur-hayes-prediction-is-back-in-focus) coinpaper.com - December 31 at 10:25 AM [](https://u.today/morning-crypto-report-ripple-usd-stablecoin-deletes-21804950-from-circulation-100000-for-bitcoin-in) [Morning Crypto Report: Ripple USD Stablecoin Deletes $21,804,950 From Circulation, $100,000 for Bitcoin in January Is Not Surreal, Bitwise Files for ETF on Zcas...](https://u.today/morning-crypto-report-ripple-usd-stablecoin-deletes-21804950-from-circulation-100000-for-bitcoin-in) u.today - December 31 at 7:12 AM [](https://cryptonews.com/news/why-is-crypto-up-today-december-31-2025/) [Why Is Crypto Up Today? – December 31, 2025](https://cryptonews.com/news/why-is-crypto-up-today-december-31-2025/) cryptonews.com - December 31 at 7:12 AM [](https://www.coindesk.com/business/2025/12/31/winklevoss-backed-cypherpunk-buys-usd28-million-of-zcash-now-owns-1-7-of-supply) [Winklevoss-backed Cypherpunk buys $28 million of zcash, now owns 1.7% of supply](https://www.coindesk.com/business/2025/12/31/winklevoss-backed-cypherpunk-buys-usd28-million-of-zcash-now-owns-1-7-of-supply) coindesk.com - December 31 at 5:08 AM [](https://coinpaper.com/13470/cypherpunk-doubles-down-on-zcash-with-29-m-treasury-buy) [Cypherpunk Doubles Down on Zcash With $29M Treasury Buy](https://coinpaper.com/13470/cypherpunk-doubles-down-on-zcash-with-29-m-treasury-buy) coinpaper.com - December 31 at 4:15 AM [](https://square.htx.com/htx-hot-listings-weekly-recap-dec-22-28-sees-zbt-surge-127-payai-rally-103-ai-and-privacy-narratives-reignite/) [HTX Hot Listings Weekly Recap (Dec 22-28) Sees ZBT Surge 127%, PAYAI Rally 103% | AI and Privacy Narratives Reignite](https://square.htx.com/htx-hot-listings-weekly-recap-dec-22-28-sees-zbt-surge-127-payai-rally-103-ai-and-privacy-narratives-reignite/) square.htx.com - December 31 at 3:08 AM [](https://ambcrypto.com/zcash-leads-q4-privacy-rally-analyst-foresees-zec-at-1000/) [Zcash leads Q4 privacy rally – Analyst foresees ZEC at $1,000](https://ambcrypto.com/zcash-leads-q4-privacy-rally-analyst-foresees-zec-at-1000/) ambcrypto.com - December 31 at 1:10 AM [](https://bitcoinworld.co.in/bitwise-files-11-crypto-etfs/) [Bitwise Crypto ETFs: A Bold Leap with 11 New Funds Including AAVE and UNI](https://bitcoinworld.co.in/bitwise-files-11-crypto-etfs/) bitcoinworld.co.in - December 30 at 9:30 PM [](https://cryptonews.com/news/zcash-cypherpunk-corporate-treasury-play-bitcoin/) [Is Zcash the Next Corporate Treasury Play? Cypherpunk Now Holds Nearly 2%](https://cryptonews.com/news/zcash-cypherpunk-corporate-treasury-play-bitcoin/) cryptonews.com - December 30 at 6:31 PM [](https://cointelegraph.com/news/privacy-prevailed-q4-crypto-grayscale) [How privacy prevailed in an otherwise dismal Q4 for crypto](https://cointelegraph.com/news/privacy-prevailed-q4-crypto-grayscale) cointelegraph.com - December 30 at 2:33 PM [](https://cryptonews.com/news/best-meme-coins-to-buy-before-new-year-that-could-100x-in-2026-30-december-2025/) [Best Meme Coins To Buy Before New Year That Could 100x in 2026 – 30 December 2025](https://cryptonews.com/news/best-meme-coins-to-buy-before-new-year-that-could-100x-in-2026-30-december-2025/) cryptonews.com - December 30 at 2:33 PM [](https://cointelegraph.com/news/cypherpunk-crypto-treasury-29m-zcash-purchase) [Cypherpunk lifts crypto treasury with $29M Zcash purchase](https://cointelegraph.com/news/cypherpunk-crypto-treasury-29m-zcash-purchase) cointelegraph.com - December 30 at 1:35 PM [](https://invezz.com/news/2025/12/30/cypherpunk-doubles-down-on-zcash-as-treasury-hits-290062-zec/) [Cypherpunk doubles down on Zcash as treasury hits 290,062 ZEC](https://invezz.com/news/2025/12/30/cypherpunk-doubles-down-on-zcash-as-treasury-hits-290062-zec/) invezz.com - December 30 at 10:31 AM [](https://www.tipranks.com/news/company-announcements/cypherpunk-technologies-expands-zcash-holdings-in-major-purchase) [Cypherpunk Technologies Expands Zcash Holdings in Major Purchase](https://www.tipranks.com/news/company-announcements/cypherpunk-technologies-expands-zcash-holdings-in-major-purchase) tipranks.com - December 30 at 9:31 AM [](https://bitcoinworld.co.in/cypherpunk-technologies-zec-investment-winklevoss/) [ZEC Investment Soars: Cypherpunk Technologies’ Strategic $29M Acquisition Signals Major Confidence](https://bitcoinworld.co.in/cypherpunk-technologies-zec-investment-winklevoss/) bitcoinworld.co.in - December 30 at 9:28 AM [](https://www.cryptopolitan.com/privacy-tokens-defy-negative-headwind/) [Grayscale highlighted the growing preference for privacy-focused cryptocurrencies](https://www.cryptopolitan.com/privacy-tokens-defy-negative-headwind/) cryptopolitan.com - December 30 at 8:06 AM [](https://en.coinotag.com/zcash-leads-privacy-coins-surge-in-q4-2025-despite-market-headwinds) [Zcash Leads Privacy Coins Surge in Q4 2025 Despite Market Headwinds](https://en.coinotag.com/zcash-leads-privacy-coins-surge-in-q4-2025-despite-market-headwinds) en.coinotag.com - December 30 at 8:06 AM [](https://www.prnewswire.com/news-releases/cypherpunk-accelerates-zcash-accumulation-increases-treasury-holdings-to-290-062-67-zec-302650408.html) [Cypherpunk Accelerates Zcash Accumulation; Increases Treasury Holdings to 290,062.67 ZEC](https://www.prnewswire.com/news-releases/cypherpunk-accelerates-zcash-accumulation-increases-treasury-holdings-to-290-062-67-zec-302650408.html) prnewswire.com - December 30 at 7:31 AM [](https://www.cryptopolitan.com/dragonflys-haseeb-qureshi-btc-hit/) [Haseeb Qureshi predicts $150K bitcoin in 2026 as big tech wallets emerge](https://www.cryptopolitan.com/dragonflys-haseeb-qureshi-btc-hit/) cryptopolitan.com - December 30 at 5:11 AM [](https://bitcoinist.com/dragonfly-qureshi-crypto-predictions-for-2026/) [Dragonfly’s Haseeb Qureshi Unveils His Crypto Predictions For 2026](https://bitcoinist.com/dragonfly-qureshi-crypto-predictions-for-2026/) bitcoinist.com - December 30 at 5:11 AM [](https://bitcoinworld.co.in/beldex-price-prediction-2026-2030/) [Beldex Price Prediction 2026-2030: Unveiling the Potential Hidden Gem in Privacy-Focused Cryptocurrencies](https://bitcoinworld.co.in/beldex-price-prediction-2026-2030/) bitcoinworld.co.in - December 30 at 2:05 AM [](https://invezz.com/news/2025/12/29/why-most-altcoins-fell-in-2025-and-how-xrp-zcash-and-algorand-defied-the-trend/) [Why most altcoins fell in 2025, and how XRP, Zcash, and Algorand defied the trend](https://invezz.com/news/2025/12/29/why-most-altcoins-fell-in-2025-and-how-xrp-zcash-and-algorand-defied-the-trend/) invezz.com - December 29 at 5:07 PM [](https://www.newsbtc.com/analysis/zec/zcash-rallied-above-500/) [Here’s Why The ZCash (ZEC) Price Rallied Above $500 Again](https://www.newsbtc.com/analysis/zec/zcash-rallied-above-500/) newsbtc.com - December 29 at 4:19 PM [](https://en.coinotag.com/zcash-kraken-withdrawal-may-herald-upside-as-shorts-face-liquidation-stress) [Zcash Kraken Withdrawal May Herald Upside as Shorts Face Liquidation Stress](https://en.coinotag.com/zcash-kraken-withdrawal-may-herald-upside-as-shorts-face-liquidation-stress) en.coinotag.com - December 29 at 3:10 PM [](https://cointelegraph.com/news/zcash-price-first-stop-1k-arthur-hayes) [Zcash price has 'first stop' at $1K: Arthur Hayes](https://cointelegraph.com/news/zcash-price-first-stop-1k-arthur-hayes) cointelegraph.com - December 29 at 12:14 PM [](https://cointelegraph.com/news/xrp-zcash-algorand-outperformed-2025-altcoin-slump) [These three altcoins came back from the dead in 2025](https://cointelegraph.com/news/xrp-zcash-algorand-outperformed-2025-altcoin-slump) cointelegraph.com - December 29 at 9:10 AM [](https://u.today/morning-crypto-report-bitcoins-uh-oh-pattern-returns-as-zcash-zec-pumps-again-xrp-prints-0-after) [Morning Crypto Report: Bitcoin’s “Uh Oh” Pattern Returns as Zcash (ZEC) Pumps Again, XRP Prints $0 After Short Sellers Disappear, Forgotten Bitcoin Rival May Re...](https://u.today/morning-crypto-report-bitcoins-uh-oh-pattern-returns-as-zcash-zec-pumps-again-xrp-prints-0-after) u.today - December 29 at 7:14 AM [](https://ambcrypto.com/zcash-zec-builds-pressure-as-4-12-mln-exits-kraken-is-a-squeeze-forming/) [Zcash [ZEC] builds pressure as $4.12 mln exits Kraken – Is a squeeze forming?](https://ambcrypto.com/zcash-zec-builds-pressure-as-4-12-mln-exits-kraken-is-a-squeeze-forming/) ambcrypto.com - December 29 at 7:14 AM [](https://en.coinotag.com/zcash-rally-tops-solana-volumes-privacy-narrative-may-drive-further-gains) [Zcash Rally Tops Solana Volumes, Privacy Narrative May Drive Further Gains](https://en.coinotag.com/zcash-rally-tops-solana-volumes-privacy-narrative-may-drive-further-gains) en.coinotag.com - December 28 at 10:06 PM [See All Recent Headlines](https://www.marketbeat.com/cryptocurrencies/zcash/#) 
## Zcash Currency Details
Name **Zcash** Symbol **ZEC** Market Capitalization **$8.21 billion** Coin or Token **Coin** Algorithm **Equihash** Proof Type **PoW** Genesis Date **10/28/2016** Mineable? **Yes** 
### Official Links
Official Website **z.cash** Official Website (Alt) **N/A** BitcoinTalk Announcement **View** Twitter Account **@electriccoinco** Facebook Page **View** Github Account **View** 
### Community Discussion
Reddit Community **r/zec** Telegram Group **View** Discord Group **View** Message Board **forum.z.cash** Message Board (Alt) **N/A** 
### Research Tools
Blockchain Explorer **zcashblockexplorer.com** Blockchain Explorer (Alt) **app.nansen.ai** CoinMarketCap **View** CryptoCompare **View** CoinGecko **View** 
## About Zcash (ZEC)

## Zcash (ZEC) Frequently Asked Questions
How do I buy Zcash?

It is not possible to buy all cryptocurrencies with U.S. dollars. Bitcoin, Bitcoin Cash, Ethereum, Litecoin and other popular cryptocurrencies can be purchased with U.S. dollars using Coinbase. Once you have purchased Bitcoin using Coinbase, you can then transfer your Bitcoin to an exchange such as Binance to purchase other cryptocurrencies, including Zcash.
What do investment analysts think about Zcash?

Weiss Research, an investment research firm that rates cryptocurrencies, has given Zcash an overall rating of "C", a technology and adoption rating of "B-", and a market performance rating of "D-".
What technology is included in Zcash?

zk-SNARKsThe BasicZcash is the first widespread application of zk-SNARKs, a novel form of zero-knowledge cryptography. The strong privacy guarantee of Zcash is derived from the fact that shielded transactions in Zcash can be fully encrypted on the blockchain, yet still be verified as valid under the network’s consensus rules by using zk-SNARK proofs. The acronym zk-SNARK stands for “Zero-Knowledge Succinct Non-Interactive Argument of Knowledge,” and refers to a proof construction where one can prove possession of certain information, e.g. a secret key, without revealing that information, and without any interaction between the prover and verifier. “Zero-knowledge” proofs allow one party (the prover) to prove to another (the verifier) that a statement is true, without revealing any information beyond the validity of the statement itself. For example, given the hash of a random number, the prover could convince the verifier that there indeed exists a number with this hash value, without revealing what it is. Application to ZCASHIn order to have zero-knowledge privacy in Zcash, the function determining the validity of a transaction according to the network’s consensus rules must return the answer of whether the transaction is valid or not, without revealing any of the information it performed the calculations on. This is done by encoding some of the network's consensus rules in zk-SNARKs. At a high level, zk-SNARKs work by first turning what you want to prove into an equivalent form about knowing a solution to some algebraic equations. In the following section, we give a brief overview of how the rules for determining a valid transaction get transformed into equations that can then be evaluated on a candidate solution without revealing any sensitive information to the parties verifying the equations. (Information provided by CryptoCompare.)
Where can I get Zcash wallet?

Zcash produces its own wallet software that is available for download on its website, which allows you to store Zcash on your computer. For maximum security, you can store your cryptocurrencies on a dedicated hardware wallet such as a TREZOR wallet or a Ledger Nano X. If you do not wish to buy a hardware wallet, you may consider using a mobile wallet such as Atomic Wallet, Jaxx, or Coinomi to store multiple cryptocurrencies with some added security benefits.
What is the value of Zcash?

One Zcash (ZEC) is currently worth $515.54 on major cryptocurrency exchanges. You can also exchange one Zcash for 0.00548422 bitcoin(s) on major exchanges. The value (or market capitalization) of all available Zcash in U.S. dollars is $8.49 billion.
What hashing algorithm does Zcash use?

Zcash is a proof of work (PoW) coin that uses the Equihash algorithm.
How do I mine Zcash?

Zcash can be mined using specialized mining software. XMR Stak is a commonly-used mining tool that works for CPU mining and GPU mining with both Nvidia and AMD graphics cards. CCMiner is another popular mining tool for computers with NVIDIA graphics cards. In addition to having mining software, you will need a Zcash and access to a mining pool that pools your effort with other miners and a wallet to store the Zcash that you earn from mining. Most cryptocurrencies have multiple publicly-available mining pools that can be found with a simple Google search.
What coins are similar to Zcash?

The following coins use the same hashing algorithm (Equihash) as Zcash: Horizen, Pirate Chain, Bitcoin Gold, Komodo, ZClassic and Bitcoin Private.
What is the Reddit page for Zcash?

The official Reddit community (subreddit) for Zcash is https://reddit.com/r/zec.

## Zcash (ZEC) Price Chart for Tuesday, January, 6, 2026

## Zcash (ZEC) Twitter Feed
[Tweets by @electriccoinco](https://twitter.com/electriccoinco?ref_src=twsrc^tfw) Loading…

## Zcash (ZEC) Reddit Feed
*This page was last updated on 1/6/2026 by MarketBeat.com Staff* Adding Zcash

Please log in to your account or sign up in order to add this asset to your watchlist.
[Log In and Add](https://www.marketbeat.com/login/?cmd=cryptocreate&symbol=zcash) Adding
Choose a watchlist:
Watchlist Adding

You have already added ten holdings to your watchlist. Upgrade to MarketBeat All Access to add more holdings to your watchlist.
Share Zcash With A Colleague
[](https://www.facebook.com/sharer/sharer.php?u=https%3a%2f%2fwww.marketbeat.com%2fcryptocurrencies%2fzcash%2f) [](https://twitter.com/intent/tweet?text=Zcash+Crypto+Price+Headlines%2c+Value+and+Chart+(ZEC)+https%3a%2f%2fwww.marketbeat.com%2fcryptocurrencies%2fzcash%2f) [](https://www.linkedin.com/cws/share?mini=true&amp%3burl=https%3a%2f%2fwww.marketbeat.com%2fcryptocurrencies%2fzcash%2f) [](https://api.stocktwits.com/widgets/share?via=MarketBeat&amp%3bbody=Zcash+Crypto+Price+Headlines%2c+Value+and+Chart+(ZEC)+https%3a%2f%2fwww.marketbeat.com%2fcryptocurrencies%2fzcash%2f) [](https://www.marketbeat.com/cryptocurrencies/zcash/) Link copied to clipboard.
Get 30 Days of MarketBeat All Access for Free 
Sign up for MarketBeat All Access to gain access to MarketBeat's full suite of research tools.
[Start Your 30-Day Trial](https://www.marketbeat.com/subscribe/all-access/?referraltype=masterfooter) 
## MarketBeat All Access Features
[Best-in-Class Portfolio Monitoring Get personalized stock ideas. Compare portfolio to indices. Check stock news, ratings, SEC filings, and more.](https://www.marketbeat.com/subscribe/all-access/?referraltype=masterfooter) [Stock Ideas and Recommendations See daily stock ideas from top analysts. Receive short-term trading ideas from MarketBeat. Identify trending stocks on social media.](https://www.marketbeat.com/subscribe/all-access/?referraltype=masterfooter) [Advanced Stock Screeners and Research Tools Use our seven stock screeners to find suitable stocks. Stay informed with MarketBeat's real-time news. Export data to Excel for personal analysis.](https://www.marketbeat.com/subscribe/all-access/?referraltype=masterfooter) Sign in to your free account to enjoy these benefits - In-depth profiles and analysis for 20,000 public companies.
- Real-time analyst ratings, insider transactions, earnings data, and more.
- Our daily ratings and market update email newsletter.
Sign in to your free account to enjoy all that MarketBeat has to offer. - Sign In
- Create Account
- 
Your Email Address: Email Address Required Your Password: Password Required Log In or [Sign in with Facebook](https://www.marketbeat.com/cryptocurrencies/zcash/#) [Sign in with Google](https://www.marketbeat.com/cryptocurrencies/zcash/#) [Forgot your password?](https://www.marketbeat.com/forgot-password/) Your Email Address: Please enter your email address. Please enter a valid email address Choose a Password: Please enter your password. Your password must be at least 8 characters long and contain at least 1 number, 1 letter, and 1 special character. or [Sign in with Facebook](https://www.marketbeat.com/cryptocurrencies/zcash/#) [Sign in with Google](https://www.marketbeat.com/cryptocurrencies/zcash/#) By creating a free account, you agree to our [terms of service.](https://www.marketbeat.com/terms/) This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
</searchResult>


<searchResult>
[doc4]:
**Latest Zcash News - (ZEC) Future Outlook, Trends & Market Insights**
[](https://coinmarketcap.com/) [Cryptocurrencies](https://coinmarketcap.com/) Cryptocurrencies
[Ranking](https://coinmarketcap.com/) [Categories](https://coinmarketcap.com/cryptocurrency-category/) [Historical Snapshots](https://coinmarketcap.com/historical/) [Token unlocks](https://coinmarketcap.com/token-unlocks/) [Yield](https://coinmarketcap.com/yield/) [Real-World Assets](https://coinmarketcap.com/real-world-assets/) Leaderboards
[Trending](https://coinmarketcap.com/trending-cryptocurrencies/) [Upcoming](https://coinmarketcap.com/upcoming/) [Recently Added](https://coinmarketcap.com/new/) [Gainers & Losers](https://coinmarketcap.com/gainers-losers/) [Most Visited](https://coinmarketcap.com/most-viewed-pages/) [Community Sentiment](https://coinmarketcap.com/sentiment/) [Chain Ranking](https://coinmarketcap.com/chain-ranking/) NFT
[Overall NFT Stats](https://coinmarketcap.com/nft/) [Upcoming Sales](https://coinmarketcap.com/nft/upcoming/) [Dashboards](https://coinmarketcap.com/charts/) Markets
[Market Overview](https://coinmarketcap.com/charts/) [Spot Market](https://coinmarketcap.com/charts/spot-market/) [Derivatives Market](https://coinmarketcap.com/charts/derivatives-market/) [No. of Cryptocurrencies](https://coinmarketcap.com/charts/number-of-cryptocurrencies-tracked/) [BNB Treasuries](https://coinmarketcap.com/charts/bnb-treasuries/) Indicators
[Fear and Greed Index](https://coinmarketcap.com/charts/fear-and-greed-index/) [Altcoin Season Index](https://coinmarketcap.com/charts/altcoin-season-index/) [Market Cycle Indicators](https://coinmarketcap.com/charts/crypto-market-cycle-indicators/) [Bitcoin Dominance](https://coinmarketcap.com/charts/bitcoin-dominance/) [CoinMarketCap 20 Index](https://coinmarketcap.com/charts/cmc20/) [CoinMarketCap 100 Index](https://coinmarketcap.com/charts/cmc100/) ETF Flows
[Crypto ETFs](https://coinmarketcap.com/etf/) [Bitcoin ETFs](https://coinmarketcap.com/etf/bitcoin/) [Ethereum ETFs](https://coinmarketcap.com/etf/ethereum/) Technical Analysis
[RSI](https://coinmarketcap.com/charts/rsi/) [MACD](https://coinmarketcap.com/charts/macd/) Derivatives
[Funding Rates](https://coinmarketcap.com/charts/funding-rates/) [DexScan](https://dex.coinmarketcap.com/token/all/) [SignalsNew](https://dex.coinmarketcap.com/signals/all/) [Trending](https://dex.coinmarketcap.com/token/all/) [New](https://dex.coinmarketcap.com/token/all/?tableRankBy=new_24h) [Gainers](https://dex.coinmarketcap.com/token/all/?tableRankBy=gainers_24h) [Meme Explorer](https://dex.coinmarketcap.com/meme/four.meme/) [Top Traders](https://dex.coinmarketcap.com/top-traders/all/) [Exchanges](https://coinmarketcap.com/rankings/exchanges/) Centralized Exchanges
[Spot](https://coinmarketcap.com/rankings/exchanges/) [Derivatives](https://coinmarketcap.com/rankings/exchanges/derivatives/) Decentralized Exchanges
[Spot](https://coinmarketcap.com/rankings/exchanges/dex/?type=spot) [Derivatives](https://coinmarketcap.com/rankings/exchanges/dex/?type=derivatives) [Community](https://coinmarketcap.com/community/) [Feeds](https://coinmarketcap.com/community/) [Topics](https://coinmarketcap.com/community/topics/) [Lives](https://coinmarketcap.com/community/lives/) [Articles](https://coinmarketcap.com/community/articles/) [Sentiment](https://coinmarketcap.com/sentiment/) Products Products
[Converter](https://coinmarketcap.com/converter/) [Newsletter](https://coinmarketcap.com/newsletter/) [CMC Launch](https://coinmarketcap.com/cmclaunch/) [CMC Labs](https://coinmarketcap.com/events/cmc-labs/) [Telegram Bot](https://coinmarketcap.com/chatbot/) [Advertise](https://coinmarketcap.com/events/advertise/) [Crypto API](https://coinmarketcap.com/api/) [Site Widgets](https://coinmarketcap.com/widget/ticker/) Campaigns
[Airdrops](https://coinmarketcap.com/airdrop/) [Diamond Rewards](https://coinmarketcap.com/account/rewards/) [Learn & Earn](https://coinmarketcap.com/earn/) Calendars
[ICO Calendar](https://coinmarketcap.com/ico-calendar/) [Events Calendar](https://coinmarketcap.com/events/) Learn
[News](https://coinmarketcap.com/headlines/news/) [Academy](https://coinmarketcap.com/academy/) [Research](https://coinmarketcap.com/academy/categories/cmc-research/) [Videos](https://www.youtube.com/channel/UCnhdZlwVd6ocXGhdSyV9Axg/?sub_confirmation=1) [Glossary](https://coinmarketcap.com/academy/glossary/) 
# Latest Zcash (ZEC) News Update
By CMC AI 06 January 2026 12:16AM (UTC+0) [See ZEC Price Chart](https://coinmarketcap.com/currencies/zcash/#cmcaiquestion=0) 
## What is the latest news on ZEC?

## TLDR

Zcash navigates bullish technicals and whale-sized bets as privacy narratives gain steam. Here are the latest news:
1. Bull Flag Holds Despite Weakness (6 January 2026) – ZEC’s bullish structure remains intact, but weakening momentum signals caution.
2. Whale Bets $39M on ZEC Long (5 January 2026) – A crypto whale opened a leveraged position equivalent to 1.2% of ZEC’s circulating supply.
3. Grayscale Zcash Trust Discount Widens (5 January 2026) – Shares trade 25% below net asset value despite rising institutional interest.

## Deep Dive

### 1. Bull Flag Holds Despite Weakness (6 January 2026)

Overview: ZEC maintains a bullish market structure with an 85% upside target ($930+) if it holds above $404 support. However, momentum indicators like the Chaikin Money Flow (CMF) near zero suggest weakening buying pressure.

What this means: The technical setup is bullish long-term but faces headwinds from Bitcoin’s negative correlation with ZEC and $39M in short-term short leverage. A break below $404 could trigger a deeper correction. (TokenPost)

### 2. Whale Bets $39M on ZEC Long (5 January 2026)

Overview: Address 0x6b26 opened a 5x leveraged long position with 79,438 ZEC ($39.24M) on Binance, risking amplified volatility.

What this means: Large leveraged positions increase liquidation risks—$54M in shorts vs. $24M longs sit near current prices. While this signals confidence, the whale already faces a $1.88M unrealized loss, raising concerns about forced selling. (Binance News)

### 3. Grayscale Zcash Trust Discount Widens (5 January 2026)

Overview: Grayscale’s Zcash Trust (ZCSH) shares trade at a 25% discount to NAV despite holding $190M in ZEC, reflecting skepticism about near-term liquidity improvements.

What this means: The widening gap between institutional and spot prices highlights ZEC’s regulatory ambiguity but could create arbitrage opportunities if ETF conversion rumors materialize. (CoinMarketCap)

## Conclusion

Zcash balances bullish technicals against whale-driven volatility and institutional hesitancy. While its privacy tech attracts believers, the market awaits clarity: Will shielded transaction growth (now 20-25% of supply) offset Bitcoin’s gravitational pull on prices?

## What are people saying about ZEC?

## TLDR

Zcash's community oscillates between breakout euphoria and correction jitters, with privacy tech hype clashing with technical caution. Here’s what’s trending:
1. Traders debate if ZEC’s consolidation is a bull trap or springboard
2. Institutions bet big while retail eyes $550 prediction markets
3. Technical charts flash conflicting signals across timeframes

## Deep Dive

### 1. @earlyadopterz: “Inverse Bitcoin hedge” thesis gains traction 🚀

“When Bitcoin gets flushed down, Zcash will blast off... ZEC is the hedge”– @earlyadopterz (7.1K followers · 14M impressions · 2026-01-02 16:13 UTC)View original postWhat this means: Bullish for ZEC as some view it as a counter-cyclical play against Bitcoin volatility. The narrative gained traction after ZEC rose 2.8% while BTC dipped 0.4% on January 2.

### 2. @VipRoseTr: Rising wedge warns of 42% drop 📉

“ZEC forming bearish pattern – breakdown below support targets $289”– @VipRoseTr (63.4K followers · 8.2M impressions · 2025-12-27 13:53 UTC)View original postWhat this means: Bearish technical outlook as ZEC struggles at $519 resistance (current price $501). The pattern’s measured move aligns with the 38.2% Fibonacci retracement of its 295% 90-day rally.

### 3. @MusicByVirtuals: Prediction market shows skepticism 🎯

“85.8% bet ZEC stays below $550 through EOY 2025”– @MusicByVirtuals (6.1K followers · 3.1M impressions · 2025-11-28 14:56 UTC)View original postWhat this means: Neutral-bearish sentiment despite ZEC’s 47.9% 30-day gain. The crowd doubts sustainability of recent momentum, though the poll closed before January’s Grayscale Trust accumulation news.

## Conclusion

The consensus on Zcash is mixed – bullish on privacy adoption narratives but wary of stretched valuations. While institutions like Grayscale’s $190M Zcash Trust signal long-term conviction, derivatives data shows $54M in vulnerable short positions that could fuel volatility. Watch the $404 support level: A hold above maintains the ascending triangle pattern targeting $630, while a breakdown might confirm the bearish wedge toward $300. With 29% of ZEC’s supply now in shielded pools, regulatory clarity remains the ultimate make-or-break factor.

## What is the latest update in ZEC’s codebase?

## TLDR

Zcash's codebase advances privacy and node infrastructure.
1. NU6.1 Activation (Oct 2025) – Enabled shielded transaction upgrades and fee optimizations.
2. Zcashd Deprecation (Apr 2025) – Migration to Zebra nodes and Zallet wallet underway.
3. Zashi 2.0.3 (Apr 2025) – Streamlined shielded addresses and cross-chain swaps.

## Deep Dive

### 1. NU6.1 Activation (Oct 2025)

Overview: Implemented ZIPs 317 and 320, refining fee structures and transparent address formats.This upgrade introduced a new transaction version (v5) as the default, reducing fees for shielded transfers by ~30% through optimized proof bundling. It also added stricter mempool rules to prevent spam transactions.

What this means: This is bullish for ZEC because lower fees and improved spam resistance make private transactions more accessible and scalable. (Source)

### 2. Zcashd Deprecation (Apr 2025)

Overview: Phasing out the legacy C++ client (zcashd) in favor of Rust-based Zebra nodes and Zallet wallet.Key RPC methods like z_getbalance were deprecated, with users urged to migrate before August 2025. Zebra offers faster sync times and modular architecture.

What this means: This is neutral for ZEC – while modernization improves long-term maintainability, migration complexities could temporarily strain ecosystem tools. (Source)

### 3. Zashi 2.0.3 (Apr 2025)

Overview: Wallet update defaulting to shielded addresses and integrating Maya DEX for cross-chain swaps.The redesign simplified sending private transactions and added auto-shielding of transparent balances. Over 15% more ZEC moved to shielded pools post-update.

What this means: This is bullish for ZEC because frictionless privacy strengthens its core value proposition amid regulatory scrutiny. (Source)

## Conclusion

Zcash’s updates prioritize privacy usability and infrastructure resilience, aligning with its role as a compliance-friendly anonymity tool. With shielded adoption rising and node modernization complete, how will ZEC balance regulatory pressures against its technological edge in 2026?

## What is next on ZEC’s roadmap?

## TLDR

Zcash's development roadmap focuses on privacy enhancements, ecosystem expansion, and governance upgrades through early 2026.
1. Zashi Wallet 2.0 (Q1 2026) – Shielded swaps and cross-chain DeFi integration.
2. Ztarknet Devnet Launch (Q1 2026) – Privacy-preserving smart contracts.
3. Governance Model Overhaul (2026) – Streamlined development funding.

## Deep Dive

### 1. Zashi Wallet 2.0 (Q1 2026)

Overview:The Zashi wallet will enable fully shielded swaps via NEAR Protocol’s Intents, allowing users to privately convert assets like BTC or ETH into shielded ZEC without intermediaries. This follows the November 2025 integration that simplified shielded-to-transparent transactions.

What this means:Bullish for ZEC adoption, as frictionless privacy could attract users seeking compliance-friendly anonymity. Risks include potential delays in cross-chain refund privacy features.

### 2. Ztarknet Devnet Launch (Q1 2026)

Overview:Ztarknet, a Starknet-inspired Layer-2 rollup, will bring programmable smart contracts to Zcash using Circle-STARK proofs. This allows private computation off-chain while settling on Zcash’s base layer, maintaining shielded pool integrity (Eli5defi, Nov 2025).

What this means:Neutral-to-bullish – while this expands Zcash’s utility beyond simple payments, adoption depends on developer uptake. Success could position ZEC as a privacy-centric smart contract platform.

### 3. Governance Model Overhaul (2026)

Overview:Community proposals aim to replace Zcash’s expiring development fund with a new model emphasizing transparency and faster execution. This follows June 2025 debates about sustaining ecosystem growth.

What this means:Bullish if governance reforms reduce bureaucratic delays, but bearish risks emerge if funding disputes fragment the community.

## Conclusion

Zcash’s 2026 trajectory hinges on balancing technical innovation (Ztarknet, Zashi) with governance maturity. While privacy upgrades could drive mainstream adoption, regulatory scrutiny remains a wildcard. How will Zcash’s optional privacy model fare as global AML rules tighten?
CMC AI can make mistakes. Not financial advice. Read more about ZEC [What is Zcash (ZEC)?](https://coinmarketcap.com/cmc-ai/zcash/what-is/) [Latest Zcash (ZEC) Price Analysis](https://coinmarketcap.com/cmc-ai/zcash/price-analysis/) [Zcash (ZEC) Price Prediction](https://coinmarketcap.com/cmc-ai/zcash/price-prediction/) 
## Explore Similar Coins

![ZEC](https://s2.coinmarketcap.com/static/img/coins/64x64/1437.png)
Zcash ZEC | $494.67 
1.51% (1d)
[See ZEC Price Chart](https://coinmarketcap.com/currencies/zcash/#cmcaiquestion=0) Read more about ZEC [What is Zcash (ZEC)?](https://coinmarketcap.com/cmc-ai/zcash/what-is/) [Latest Zcash (ZEC) Price Analysis](https://coinmarketcap.com/cmc-ai/zcash/price-analysis/) [Zcash (ZEC) Price Prediction](https://coinmarketcap.com/cmc-ai/zcash/price-prediction/) Cryptos: [29.55M](https://coinmarketcap.com/charts/number-of-cryptocurrencies-tracked/) Exchanges: [913](https://coinmarketcap.com/rankings/exchanges/) Market Cap: [$3.18T](https://coinmarketcap.com/charts/) 0.79% 24h Vol: [$138.65B](https://coinmarketcap.com/charts/) 11.53% Dominance: [BTC: 58.2% ETH: 12.3%](https://coinmarketcap.com/charts/bitcoin-dominance/) ** ETH Gas : 0.04 Gwei Fear & Greed: [49/100](https://coinmarketcap.com/charts/fear-and-greed-index/) [API](https://coinmarketcap.com/api/pricing/)
</searchResult>



```

03:15:57.466 - Successfully downloaded page content from: `https://www.ainvest.com/news/zcash-altcoin-season-indicator-technical-sentiment-driven-analysis-2510/`

03:15:57.541 - Successfully downloaded page content from: `https://www.dlnews.com/articles/markets/why-privacy-token-zcash-price-is-up-700-percent-since-september/`

03:15:57.553 - Successfully downloaded page content from: `https://www.dlnews.com/articles/markets/zcash-price-surge-continues-despite-market-turmoil/`

03:15:57.622 - Successfully downloaded page content from: `https://www.dlnews.com/articles/people-culture/zcash-foundation-shakes-up-leadership-amidst-zec-token-price-rally/`

03:15:57.642 - Successfully downloaded page content from: `https://www.dlnews.com/rss/`

03:15:57.759 - Successfully downloaded page content from: `https://www.dlnews.com/articles/markets/winklevoss-twins-bet-on-zcash-with-new-treasury-firm/`

03:15:57.799 - Successfully downloaded page content from: `https://stocktwits.com/coins/zcash`

### Search Results

```
<searchResult>
[doc5]:
**Zcash(ZEC) Price Today, ZEC to USD Real-Time, Latest Discussions ...**
[](https://stocktwits.com/) - Trending
- News
- Earnings
[DIA1.11%](https://stocktwits.com/symbol/DIA) [SPY0.68%](https://stocktwits.com/symbol/SPY) [QQQ1.03%](https://stocktwits.com/symbol/QQQ) Trending [CRML53.59%](https://stocktwits.com/symbol/CRML) [MSTR9.11%](https://stocktwits.com/symbol/MSTR) [RUM5.73%](https://stocktwits.com/symbol/RUM) [VKTX0.50%](https://stocktwits.com/symbol/VKTX) [SNDK32.24%](https://stocktwits.com/symbol/SNDK) [APLD1.72%](https://stocktwits.com/symbol/APLD) [JASMY22.79%](https://stocktwits.com/coins/jasmycoin) [MNTS16.95%](https://stocktwits.com/symbol/MNTS) [IMSR43.28%](https://stocktwits.com/symbol/IMSR) [SOFI8.15%](https://stocktwits.com/symbol/SOFI) [CRML53.59%](https://stocktwits.com/symbol/CRML) [MSTR9.11%](https://stocktwits.com/symbol/MSTR) [RUM5.73%](https://stocktwits.com/symbol/RUM) [VKTX0.50%](https://stocktwits.com/symbol/VKTX) [SNDK32.24%](https://stocktwits.com/symbol/SNDK) [APLD1.72%](https://stocktwits.com/symbol/APLD) [JASMY22.79%](https://stocktwits.com/coins/jasmycoin) [MNTS16.95%](https://stocktwits.com/symbol/MNTS) [IMSR43.28%](https://stocktwits.com/symbol/IMSR) [SOFI8.15%](https://stocktwits.com/symbol/SOFI) [](https://stocktwits.com/sentiment/trending) [home](https://stocktwits.com/) [Coins](https://stocktwits.com/coins) ZEC 
![ZEC logo](https://logos.stocktwits-cdn.com/ZEC-X.png)

# ZECZcash
9,992 Mkt Cap $8.22B 24H Volume $781.82M FDV $8.22B Circ Supply 16.48M Total Supply 16.48M ZEC Fundamentals Max Supply 21M 7D High $533.33 7D Low $484.40 24H High $525.08 24H Low $494.04 All-Time High $3,191.93 All-Time Low $16.08 Total Supply 16.48M ZEC Prices ZEC / USD $499.47 ZEC / EUR €426.88 ZEC / GBP £369.66 ZEC / CAD CA$690.00 ZEC / AUD A$740.17 ZEC / INR ₹45,031.00 ZEC / NGN NGN 714,475.00 ZEC / NZD NZ$863.02 ZEC / PHP ₱29,611.00 ZEC / SGD SGD 639.69 ZEC / ZAR ZAR 8,171.94 Loading... Loading... - Chart
- News
- Sentiment
- Info
- Historical Prices
News all press releases Arthur Hayes Says Privacy Will Be Crypto's Next Dominant Trade Privacy Coin News BitMEX co-founder Arthur Hayes disclosed a substantial Zcash position held by his family office, Maelstrom, while arguing that privacy will define cryptocurrency's next major narrative. The disclosure came in a Tuesday blog post connecting privacy-focused assets...
Ayesha Aziz · 6h ago 
![News Placeholder](https://chunks-prd.stocktwits-cdn.com/_next/static/media/news-placeholder.eb4d81c7.svg)
More News

![News Placeholder](https://chunks-prd.stocktwits-cdn.com/_next/static/media/news-placeholder.eb4d81c7.svg)
Here’s what happened in crypto today Need to know what happened in crypto today? Here is the latest news on daily trends and events impacting Bitcoin price, blockchain, DeFi, NFTs, Web3 and crypto regulation.
cointelegraph · 7h ago 
![News Placeholder](https://chunks-prd.stocktwits-cdn.com/_next/static/media/news-placeholder.eb4d81c7.svg)
Market Focus Shifts From Polkadot and Zcash as BlockDAG’s Presale Nears January 26 Deadline With 3.5B Coins Left Learn why BlockDAG’s $441M presale is nearing its January 26 close, with 312K holders, shaping views on the next crypto to explode as Polkadot crypto and Zcash price struggle. Read original article on coincu.com
Coincu · 1d ago 
![News Placeholder](https://chunks-prd.stocktwits-cdn.com/_next/static/media/news-placeholder.eb4d81c7.svg)
How Zcash (ZEC) Turned Privacy From a Risk Into a Premium For years, privacy coins were treated like a problem the market wanted to avoid. Exchanges delisted them, regulators frowned on them, and investors learned to keep their distance. That is why Grayscale’s move to file for a Zcash ETF caught so much attention. It landed at a moment...
Captain Altcoin · 1d ago 
![News Placeholder](https://chunks-prd.stocktwits-cdn.com/_next/static/media/news-placeholder.eb4d81c7.svg)
Grayscale Zcash Trust Offers U.S. Investors Regulated Exposure to $ZEC Amid OTC Discount Quick Breakdown Grayscale Zcash Trust gives U.S. investors regulated access to ZEC through brokerage accounts Shares trade at $29.41, below the NAV of $39.50 Fund manages $190.7M with all assets held by third-party custodians Grayscale Investments’ Zcash Trust (Ticker: $ZCSH) pro...
DeFi Planet · 2d ago 
![News Placeholder](https://chunks-prd.stocktwits-cdn.com/_next/static/media/news-placeholder.eb4d81c7.svg)
Why Is Virtuals Protocol (VIRTUAL) Price Pumping Today? Virtuals Protocol is the strongest mover in the market today. The VIRTUAL price is up more than 18% over the past day, trading around $1.03 at writing. Trading volume has also jumped by over 31%, placing the token at the top of the daily gainers list. This move did not come out o...
Captain Altcoin · 2d ago 
![News Placeholder](https://chunks-prd.stocktwits-cdn.com/_next/static/media/news-placeholder.eb4d81c7.svg)
Big Altcoin Whale Falls Victim to Greed: Made $3.2 Million in Profits, But A large whale in the cryptocurrency market made a serious mistake after making a huge profit on an altcoin. Continue Reading: Big Altcoin Whale Falls Victim to Greed: Made $3.2 Million in Profits, But
Bitcoin Sistemi · 2d ago 
![News Placeholder](https://chunks-prd.stocktwits-cdn.com/_next/static/media/news-placeholder.eb4d81c7.svg)
Privacy coins explained: Why secrecy may shape crypto’s next era As crypto heads toward 2026, the debate over transparency versus privacy is intensifying.
crypto.news · 4d ago 
![News Placeholder](https://chunks-prd.stocktwits-cdn.com/_next/static/media/news-placeholder.eb4d81c7.svg)
Here’s Where Zcash (ZEC) Price Could Go Next in January 2026 Zcash is starting 2026 in a pretty interesting spot. The price isn’t surging higher anymore, but it also isn’t giving back much of its recent gains. After a strong run into late December, ZEC has shifted into a pause mode, holding near its highs while the market digests what just...
Captain Altcoin · 5d ago 
![News Placeholder](https://chunks-prd.stocktwits-cdn.com/_next/static/media/news-placeholder.eb4d81c7.svg)
Bithumb Finds $202M In Dormant Crypto Assets Across 2.6 Million Inactive User Accounts Bithumb identified $202M in dormant crypto across 2.6M inactive accounts, with some holdings untouched for 12 years.
Yellow News · 5d ago <
1
2
...
>

Sentiment
Indicates whether most users posting on a symbol’s stream over the last 24 hours are fearful or greedy.
0
25
50
75
100
Extreme
Fear
Neutral
Greed
Extreme
Fear
Greed
N/A
Last score

N/A
1 day ago

Sign Up / Log In
1 week ago

Sign Up / Log In
1 month ago

Sign Up / Log In
3 months ago

Sign Up / Log In
6 months ago

Sign Up / Log In
1 year ago

Sign Up / Log In

Message Volume
Measures the total amount of chatter on a stream over the last 24 hours.
0
25
50
75
100
Extremely
Low
Normal
High
Extremely
Low
High
N/A
Last score

N/A
1 day ago

Sign Up / Log In
1 week ago

Sign Up / Log In
1 month ago

Sign Up / Log In
3 months ago

Sign Up / Log In
6 months ago

Sign Up / Log In
1 year ago

Sign Up / Log In

Participation Ratio
Measures the number of unique accounts posting on a stream relative to the number of total messages on that stream.
0
25
50
75
100
Extremely
Low
Normal
High
Extremely
Low
High
N/A
Last score

N/A
1 day ago

Sign Up / Log In
1 week ago

Sign Up / Log In
1 month ago

Sign Up / Log In
3 months ago

Sign Up / Log In
6 months ago

Sign Up / Log In
1 year ago

Sign Up / Log In
About Zcash is a privacy-focused cryptocurrency that uses trustless zero-knowledge proofs to enable fully encrypted transactions while maintaining blockchain transparency and security. It was the first cryptocurrency to implement zero-knowledge encryption for private peer-to-peer payments, addressing the fundamental privacy gap in traditional cryptocurrencies that expose transaction details publicly. With a fixed supply of 21 million ZEC and a halving schedule similar to Bitcoin, Zcash allows users to prove transactions are valid without revealing sensitive information like wallet balances, transaction amounts, or participant identities, making it suitable for everyday payments, long-term savings, and cross-border money transfers where financial confidentiality matters. The protocol operates on its own blockchain currently using Proof-of-Work consensus, though it's evolving toward Proof-of-Stake through the planned "Crosslink" upgrade to enhance security, scalability, and energy efficiency. Zcash employs trustless zero-knowledge proofs (Halo) within its Orchard shielded pool to verify transactions without revealing sender, receiver, or amount information. Users can choose between transparent public transactions and shielded private transactions through Unified Addresses, which work with both types. The network is faster and cheaper than Bitcoin, with new blocks mined every 75 seconds and transaction fees typically just a fraction of a cent. Privacy adoption has surged in 2025, with over 30% of total ZEC supply now held in fully shielded pools. Zcash was created by a group of scientists in 2013 who initially proposed Zerocoin as a privacy extension to Bitcoin before building a standalone protocol. The ecosystem operates with a self-funded development model where block rewards support independent teams through the Zcash Community Grants Committee and a new Coinholder-Controlled Fund. Details Links Website Source [GitHub](https://github.com/zcash/zcash) Categories Coinbase 50 Index Layer 1 (L1) Made in USA Near Protocol Ecosystem Pantera Capital Portfolio Privacy Coins Proof of Work (PoW) Quantum-Resistant Smart Contract Platform Zero Knowledge (ZK) Date
Market Cap
Volume
Close
January 07, 2026
$8.22B
$781.82M
---
January 07, 2026
$8.28B
$660.9M
---
January 06, 2026
$8.31B
$598.39M
$503.62
January 05, 2026
$8.27B
$389.89M
$502.46
January 04, 2026
$8.43B
$494.48M
$511.43
January 03, 2026
$8.05B
$566.7M
$488.46
January 02, 2026
$8.63B
$456.97M
$523.93
January 01, 2026
$8.43B
$824.39M
$512.50
December 31, 2025
$8.69B
$605.95M
$527.84
December 30, 2025
$8.91B
$969.61M
$540.91

### Poll
What Role Will Crypto Play in 2026 Markets?
Macro Hedge Against Dollar & Geopolitical Risk
Speculative Trade
Range-Bound After the Big Run
Other – Comment Below

1.8k votes
· 
6d left

## Latest ZEC News

Advertisement|Remove ads.

Advertisement|Remove ads.
[Trending](https://stocktwits.com/sentiment) [News](https://stocktwits.com/news-articles) [Community](https://stocktwits.com/) Profile
</searchResult>


<searchResult>
[doc6]:
**Will Zcash (ZEC) Price Finally Retest $500 After Nearly 8 Years?**
# guce
[guce](https://consent.yahoo.com/v2/&#x2F;&#x2F;uk.yahoo.com&#x2F;) 
Yahoo is part of the Yahoo family of brandsThe sites and apps that we own and operate, including Yahoo and Engadget, and our digital advertising service, Yahoo Advertising.Yahoo family of brands.
When you use our sites and apps, we use Cookies Cookies (including similar technologies such as web storage) allow the operators of websites and apps to store and read information from your device. Learn more in our [cookie policy](https://consent.yahoo.com/redirect?to=https%3A%2F%2Flegal.yahoo.com%2Fie%2Fen%2Fyahoo%2Fprivacy%2Fcookies%2Findex.html&brandDomain=&brandId=yahoo&tos=eu&step=&sessionId=3_cc-session_7c26e674-c44f-4b27-9e88-e7a48467eb6f&userType=NON_REG) . cookies to: - provide our sites and apps to you
- authenticate users, apply security measures, and prevent spam and abuse, and
- MeasurementWe count the number of visitors to our pages, the type of device they use (iOS or Android), the browser they use, and the duration of their visit to our websites and apps. This data is collected in aggregate and is not tied to specific users.measure your use of our sites and apps
If you click ' **Accept all** ', we and [our partners](https://consent.yahoo.com/v2/partners-list?sessionId=3_cc-session_7c26e674-c44f-4b27-9e88-e7a48467eb6f) , including 245 who are part of the IAB Transparency & Consent Framework, will also store and/or access information on a device (in other words, use cookies) and use precise geolocation data and other personal data such as IP address and browsing and search data, for analytics, personalized advertising and content, advertising and content measurement, and audience research and services development. 
If you do not want us and our partners to use cookies and personal data for these additional purposes, click 'Reject all'.

If you would like to customise your choices, click 'Manage privacy settings'.

You can withdraw your consent or change your choices at any time by clicking on the 'Privacy & Cookie Settings' or 'Privacy Dashboard' links on our sites and apps. Find out more about how we use your personal data in our Privacy Policy and Cookie Policy.
[Manage privacy settings](https://consent.yahoo.com/v2/partners?sessionId=3_cc-session_7c26e674-c44f-4b27-9e88-e7a48467eb6f)
</searchResult>


<searchResult>
[doc4]:
**Latest Zcash News - (ZEC) Future Outlook, Trends & Market Insights**
[](https://coinmarketcap.com/) [Cryptocurrencies](https://coinmarketcap.com/) Cryptocurrencies
[Ranking](https://coinmarketcap.com/) [Categories](https://coinmarketcap.com/cryptocurrency-category/) [Historical Snapshots](https://coinmarketcap.com/historical/) [Token unlocks](https://coinmarketcap.com/token-unlocks/) [Yield](https://coinmarketcap.com/yield/) [Real-World Assets](https://coinmarketcap.com/real-world-assets/) Leaderboards
[Trending](https://coinmarketcap.com/trending-cryptocurrencies/) [Upcoming](https://coinmarketcap.com/upcoming/) [Recently Added](https://coinmarketcap.com/new/) [Gainers & Losers](https://coinmarketcap.com/gainers-losers/) [Most Visited](https://coinmarketcap.com/most-viewed-pages/) [Community Sentiment](https://coinmarketcap.com/sentiment/) [Chain Ranking](https://coinmarketcap.com/chain-ranking/) NFT
[Overall NFT Stats](https://coinmarketcap.com/nft/) [Upcoming Sales](https://coinmarketcap.com/nft/upcoming/) [Dashboards](https://coinmarketcap.com/charts/) Markets
[Market Overview](https://coinmarketcap.com/charts/) [Spot Market](https://coinmarketcap.com/charts/spot-market/) [Derivatives Market](https://coinmarketcap.com/charts/derivatives-market/) [No. of Cryptocurrencies](https://coinmarketcap.com/charts/number-of-cryptocurrencies-tracked/) [BNB Treasuries](https://coinmarketcap.com/charts/bnb-treasuries/) Indicators
[Fear and Greed Index](https://coinmarketcap.com/charts/fear-and-greed-index/) [Altcoin Season Index](https://coinmarketcap.com/charts/altcoin-season-index/) [Market Cycle Indicators](https://coinmarketcap.com/charts/crypto-market-cycle-indicators/) [Bitcoin Dominance](https://coinmarketcap.com/charts/bitcoin-dominance/) [CoinMarketCap 20 Index](https://coinmarketcap.com/charts/cmc20/) [CoinMarketCap 100 Index](https://coinmarketcap.com/charts/cmc100/) ETF Flows
[Crypto ETFs](https://coinmarketcap.com/etf/) [Bitcoin ETFs](https://coinmarketcap.com/etf/bitcoin/) [Ethereum ETFs](https://coinmarketcap.com/etf/ethereum/) Technical Analysis
[RSI](https://coinmarketcap.com/charts/rsi/) [MACD](https://coinmarketcap.com/charts/macd/) Derivatives
[Funding Rates](https://coinmarketcap.com/charts/funding-rates/) [DexScan](https://dex.coinmarketcap.com/token/all/) [SignalsNew](https://dex.coinmarketcap.com/signals/all/) [Trending](https://dex.coinmarketcap.com/token/all/) [New](https://dex.coinmarketcap.com/token/all/?tableRankBy=new_24h) [Gainers](https://dex.coinmarketcap.com/token/all/?tableRankBy=gainers_24h) [Meme Explorer](https://dex.coinmarketcap.com/meme/four.meme/) [Top Traders](https://dex.coinmarketcap.com/top-traders/all/) [Exchanges](https://coinmarketcap.com/rankings/exchanges/) Centralized Exchanges
[Spot](https://coinmarketcap.com/rankings/exchanges/) [Derivatives](https://coinmarketcap.com/rankings/exchanges/derivatives/) Decentralized Exchanges
[Spot](https://coinmarketcap.com/rankings/exchanges/dex/?type=spot) [Derivatives](https://coinmarketcap.com/rankings/exchanges/dex/?type=derivatives) [Community](https://coinmarketcap.com/community/) [Feeds](https://coinmarketcap.com/community/) [Topics](https://coinmarketcap.com/community/topics/) [Lives](https://coinmarketcap.com/community/lives/) [Articles](https://coinmarketcap.com/community/articles/) [Sentiment](https://coinmarketcap.com/sentiment/) Products Products
[Converter](https://coinmarketcap.com/converter/) [Newsletter](https://coinmarketcap.com/newsletter/) [CMC Launch](https://coinmarketcap.com/cmclaunch/) [CMC Labs](https://coinmarketcap.com/events/cmc-labs/) [Telegram Bot](https://coinmarketcap.com/chatbot/) [Advertise](https://coinmarketcap.com/events/advertise/) [Crypto API](https://coinmarketcap.com/api/) [Site Widgets](https://coinmarketcap.com/widget/ticker/) Campaigns
[Airdrops](https://coinmarketcap.com/airdrop/) [Diamond Rewards](https://coinmarketcap.com/account/rewards/) [Learn & Earn](https://coinmarketcap.com/earn/) Calendars
[ICO Calendar](https://coinmarketcap.com/ico-calendar/) [Events Calendar](https://coinmarketcap.com/events/) Learn
[News](https://coinmarketcap.com/headlines/news/) [Academy](https://coinmarketcap.com/academy/) [Research](https://coinmarketcap.com/academy/categories/cmc-research/) [Videos](https://www.youtube.com/channel/UCnhdZlwVd6ocXGhdSyV9Axg/?sub_confirmation=1) [Glossary](https://coinmarketcap.com/academy/glossary/) 
# Latest Zcash (ZEC) News Update
By CMC AI 06 January 2026 12:16AM (UTC+0) [See ZEC Price Chart](https://coinmarketcap.com/currencies/zcash/#cmcaiquestion=0) 
## What is the latest news on ZEC?

## TLDR

Zcash navigates bullish technicals and whale-sized bets as privacy narratives gain steam. Here are the latest news:
1. Bull Flag Holds Despite Weakness (6 January 2026) – ZEC’s bullish structure remains intact, but weakening momentum signals caution.
2. Whale Bets $39M on ZEC Long (5 January 2026) – A crypto whale opened a leveraged position equivalent to 1.2% of ZEC’s circulating supply.
3. Grayscale Zcash Trust Discount Widens (5 January 2026) – Shares trade 25% below net asset value despite rising institutional interest.

## Deep Dive

### 1. Bull Flag Holds Despite Weakness (6 January 2026)

Overview: ZEC maintains a bullish market structure with an 85% upside target ($930+) if it holds above $404 support. However, momentum indicators like the Chaikin Money Flow (CMF) near zero suggest weakening buying pressure.

What this means: The technical setup is bullish long-term but faces headwinds from Bitcoin’s negative correlation with ZEC and $39M in short-term short leverage. A break below $404 could trigger a deeper correction. (TokenPost)

### 2. Whale Bets $39M on ZEC Long (5 January 2026)

Overview: Address 0x6b26 opened a 5x leveraged long position with 79,438 ZEC ($39.24M) on Binance, risking amplified volatility.

What this means: Large leveraged positions increase liquidation risks—$54M in shorts vs. $24M longs sit near current prices. While this signals confidence, the whale already faces a $1.88M unrealized loss, raising concerns about forced selling. (Binance News)

### 3. Grayscale Zcash Trust Discount Widens (5 January 2026)

Overview: Grayscale’s Zcash Trust (ZCSH) shares trade at a 25% discount to NAV despite holding $190M in ZEC, reflecting skepticism about near-term liquidity improvements.

What this means: The widening gap between institutional and spot prices highlights ZEC’s regulatory ambiguity but could create arbitrage opportunities if ETF conversion rumors materialize. (CoinMarketCap)

## Conclusion

Zcash balances bullish technicals against whale-driven volatility and institutional hesitancy. While its privacy tech attracts believers, the market awaits clarity: Will shielded transaction growth (now 20-25% of supply) offset Bitcoin’s gravitational pull on prices?

## What are people saying about ZEC?

## TLDR

Zcash's community oscillates between breakout euphoria and correction jitters, with privacy tech hype clashing with technical caution. Here’s what’s trending:
1. Traders debate if ZEC’s consolidation is a bull trap or springboard
2. Institutions bet big while retail eyes $550 prediction markets
3. Technical charts flash conflicting signals across timeframes

## Deep Dive

### 1. @earlyadopterz: “Inverse Bitcoin hedge” thesis gains traction 🚀

“When Bitcoin gets flushed down, Zcash will blast off... ZEC is the hedge”– @earlyadopterz (7.1K followers · 14M impressions · 2026-01-02 16:13 UTC)View original postWhat this means: Bullish for ZEC as some view it as a counter-cyclical play against Bitcoin volatility. The narrative gained traction after ZEC rose 2.8% while BTC dipped 0.4% on January 2.

### 2. @VipRoseTr: Rising wedge warns of 42% drop 📉

“ZEC forming bearish pattern – breakdown below support targets $289”– @VipRoseTr (63.4K followers · 8.2M impressions · 2025-12-27 13:53 UTC)View original postWhat this means: Bearish technical outlook as ZEC struggles at $519 resistance (current price $501). The pattern’s measured move aligns with the 38.2% Fibonacci retracement of its 295% 90-day rally.

### 3. @MusicByVirtuals: Prediction market shows skepticism 🎯

“85.8% bet ZEC stays below $550 through EOY 2025”– @MusicByVirtuals (6.1K followers · 3.1M impressions · 2025-11-28 14:56 UTC)View original postWhat this means: Neutral-bearish sentiment despite ZEC’s 47.9% 30-day gain. The crowd doubts sustainability of recent momentum, though the poll closed before January’s Grayscale Trust accumulation news.

## Conclusion

The consensus on Zcash is mixed – bullish on privacy adoption narratives but wary of stretched valuations. While institutions like Grayscale’s $190M Zcash Trust signal long-term conviction, derivatives data shows $54M in vulnerable short positions that could fuel volatility. Watch the $404 support level: A hold above maintains the ascending triangle pattern targeting $630, while a breakdown might confirm the bearish wedge toward $300. With 29% of ZEC’s supply now in shielded pools, regulatory clarity remains the ultimate make-or-break factor.

## What is the latest update in ZEC’s codebase?

## TLDR

Zcash's codebase advances privacy and node infrastructure.
1. NU6.1 Activation (Oct 2025) – Enabled shielded transaction upgrades and fee optimizations.
2. Zcashd Deprecation (Apr 2025) – Migration to Zebra nodes and Zallet wallet underway.
3. Zashi 2.0.3 (Apr 2025) – Streamlined shielded addresses and cross-chain swaps.

## Deep Dive

### 1. NU6.1 Activation (Oct 2025)

Overview: Implemented ZIPs 317 and 320, refining fee structures and transparent address formats.This upgrade introduced a new transaction version (v5) as the default, reducing fees for shielded transfers by ~30% through optimized proof bundling. It also added stricter mempool rules to prevent spam transactions.

What this means: This is bullish for ZEC because lower fees and improved spam resistance make private transactions more accessible and scalable. (Source)

### 2. Zcashd Deprecation (Apr 2025)

Overview: Phasing out the legacy C++ client (zcashd) in favor of Rust-based Zebra nodes and Zallet wallet.Key RPC methods like z_getbalance were deprecated, with users urged to migrate before August 2025. Zebra offers faster sync times and modular architecture.

What this means: This is neutral for ZEC – while modernization improves long-term maintainability, migration complexities could temporarily strain ecosystem tools. (Source)

### 3. Zashi 2.0.3 (Apr 2025)

Overview: Wallet update defaulting to shielded addresses and integrating Maya DEX for cross-chain swaps.The redesign simplified sending private transactions and added auto-shielding of transparent balances. Over 15% more ZEC moved to shielded pools post-update.

What this means: This is bullish for ZEC because frictionless privacy strengthens its core value proposition amid regulatory scrutiny. (Source)

## Conclusion

Zcash’s updates prioritize privacy usability and infrastructure resilience, aligning with its role as a compliance-friendly anonymity tool. With shielded adoption rising and node modernization complete, how will ZEC balance regulatory pressures against its technological edge in 2026?

## What is next on ZEC’s roadmap?

## TLDR

Zcash's development roadmap focuses on privacy enhancements, ecosystem expansion, and governance upgrades through early 2026.
1. Zashi Wallet 2.0 (Q1 2026) – Shielded swaps and cross-chain DeFi integration.
2. Ztarknet Devnet Launch (Q1 2026) – Privacy-preserving smart contracts.
3. Governance Model Overhaul (2026) – Streamlined development funding.

## Deep Dive

### 1. Zashi Wallet 2.0 (Q1 2026)

Overview:The Zashi wallet will enable fully shielded swaps via NEAR Protocol’s Intents, allowing users to privately convert assets like BTC or ETH into shielded ZEC without intermediaries. This follows the November 2025 integration that simplified shielded-to-transparent transactions.

What this means:Bullish for ZEC adoption, as frictionless privacy could attract users seeking compliance-friendly anonymity. Risks include potential delays in cross-chain refund privacy features.

### 2. Ztarknet Devnet Launch (Q1 2026)

Overview:Ztarknet, a Starknet-inspired Layer-2 rollup, will bring programmable smart contracts to Zcash using Circle-STARK proofs. This allows private computation off-chain while settling on Zcash’s base layer, maintaining shielded pool integrity (Eli5defi, Nov 2025).

What this means:Neutral-to-bullish – while this expands Zcash’s utility beyond simple payments, adoption depends on developer uptake. Success could position ZEC as a privacy-centric smart contract platform.

### 3. Governance Model Overhaul (2026)

Overview:Community proposals aim to replace Zcash’s expiring development fund with a new model emphasizing transparency and faster execution. This follows June 2025 debates about sustaining ecosystem growth.

What this means:Bullish if governance reforms reduce bureaucratic delays, but bearish risks emerge if funding disputes fragment the community.

## Conclusion

Zcash’s 2026 trajectory hinges on balancing technical innovation (Ztarknet, Zashi) with governance maturity. While privacy upgrades could drive mainstream adoption, regulatory scrutiny remains a wildcard. How will Zcash’s optional privacy model fare as global AML rules tighten?
CMC AI can make mistakes. Not financial advice. Read more about ZEC [What is Zcash (ZEC)?](https://coinmarketcap.com/cmc-ai/zcash/what-is/) [Latest Zcash (ZEC) Price Analysis](https://coinmarketcap.com/cmc-ai/zcash/price-analysis/) [Zcash (ZEC) Price Prediction](https://coinmarketcap.com/cmc-ai/zcash/price-prediction/) 
## Explore Similar Coins

![ZEC](https://s2.coinmarketcap.com/static/img/coins/64x64/1437.png)
Zcash ZEC | $494.67 
1.51% (1d)
[See ZEC Price Chart](https://coinmarketcap.com/currencies/zcash/#cmcaiquestion=0) Read more about ZEC [What is Zcash (ZEC)?](https://coinmarketcap.com/cmc-ai/zcash/what-is/) [Latest Zcash (ZEC) Price Analysis](https://coinmarketcap.com/cmc-ai/zcash/price-analysis/) [Zcash (ZEC) Price Prediction](https://coinmarketcap.com/cmc-ai/zcash/price-prediction/) Cryptos: [29.55M](https://coinmarketcap.com/charts/number-of-cryptocurrencies-tracked/) Exchanges: [913](https://coinmarketcap.com/rankings/exchanges/) Market Cap: [$3.18T](https://coinmarketcap.com/charts/) 0.79% 24h Vol: [$138.65B](https://coinmarketcap.com/charts/) 11.53% Dominance: [BTC: 58.2% ETH: 12.3%](https://coinmarketcap.com/charts/bitcoin-dominance/) ** ETH Gas : 0.04 Gwei Fear & Greed: [49/100](https://coinmarketcap.com/charts/fear-and-greed-index/) [API](https://coinmarketcap.com/api/pricing/)
</searchResult>



```

03:15:57.845 - Successfully downloaded page content from: `https://www.dlnews.com/articles/markets/zcash-price-surge-continues-despite-market-turmoil/`

03:15:58.036 - Successfully downloaded page content from: `https://www.dlnews.com/articles/people-culture/zcash-foundation-shakes-up-leadership-amidst-zec-token-price-rally/`

03:15:58.062 - Successfully downloaded page content from: `https://www.dlnews.com/articles/markets/why-privacy-token-zcash-price-is-up-700-percent-since-september/`

03:15:58.078 - Successfully downloaded page content from: `https://www.dlnews.com/articles/markets/zcash-surges-tenfold-as-investors-bet-on-privacy-as-ban-looms/`

03:15:58.095 - Successfully downloaded page content from: `https://www.dlnews.com/articles/markets/zcash-price-primed-for-45-percent-breakout-as-grayscale-files-for-etf/`

03:15:58.113 - Successfully downloaded page content from: `https://www.dlnews.com/articles/markets/zcash-surges-tenfold-as-investors-bet-on-privacy-as-ban-looms/`

03:15:58.140 - Successfully downloaded page content from: `https://www.dlnews.com/articles/markets/winklevoss-twins-bet-on-zcash-with-new-treasury-firm/`

03:15:58.163 - Successfully downloaded page content from: `https://www.dlnews.com/`

03:15:58.305 - Successfully downloaded page content from: `https://www.bitmart.com/ai/xinsight/coins/detail/ZEC`

### Search Results

```
<searchResult>
[doc7]:
**Zcash Social Sentiment & Market Pulse Data | BitMart X Insight**
[](https://www.bitmart.com/en-US) - Investment
- Copy Trading
- X Insight
- Beacon
- 
- Exchange
- USDⓈ-M
[](https://www.bitmart.com/en-US/login?goto=ai%2fxinsight%2fcoins%2fdetail%2fZEC) [](https://www.bitmart.com/en-US/register?goto=ai%2fxinsight%2fcoins%2fdetail%2fZEC) 
# Zcash (ZEC)
$498.85 -0.48% 24H - 59Social Sentiment Index (SSI)+3.03% (24h)
- #165Market Pulse Ranking (MPR)-9
- 2424h Social Mention+9.09% (24h)
- 42%24h KOL Bullish Ratio12 Active KOL
- SummaryZEC price nears resistance 530, volume insufficient, KOL emphasizes first retesting the 470 liquidity zone; whether it breaks resistance or retraces to lower levels will determine the subsequent trend.
- Bullish SignalsBreakout of descending channel10% localized rebound12h bullish reversalPotential break of resistance 530Social hype rising
- Bearish SignalsLack of volume supportUpper resistance 530 unbrokenPrice deviates from 470 liquidity zoneMay fall back to 450Distribution characteristics emerging

## Social Sentiment Index (SSI)
- Data Overall59SSI
- SSI Trend (7D) Price (7D)Sentiment Distribution Extremely Bullish (13%) Bullish (29%) Neutral (17%) Bearish (38%) Extremely Bearish (3%)SSI InsightsZEC social heat is medium (58.96/100, +3.03%), activity up 19.05% driven, KOL attention full score, sentiment slightly down, linked to the battle for resistance 530 and KOL's suggestion to retest 470.

## Market Pulse Ranking (MPR)
- 
- Alert InsightZEC warning rank dropped to #165 (↓9), social anomaly 8.4, sentiment polarization 1.77, KOL attention shift ↑300% to 6, related to low volume and unbroken resistance 530.

## X Posts
- Eric Van Tassel (Not a Financial Advisor!) TA_Analyst Influencer S 5.83K @XRPathologistTired of waiting for the #ZEC price to so something? That's all intentional! One thing people often miss about a liquidity grab is that they’re usually fast, not slow. The slow part is the setup; compression, failed pushes, and positioning. The move to liquidity is execution, not negotiation. When price finally commits, it doesn’t stair-step down. It moves quickly to trigger stops, fill resting orders, and reset structure. Slow chop builds the trap. Speed is how it’s sprung. 23 1 745 Original >Trend of ZEC after release BearishZEC is in the layout stage before a liquidity grab, and may experience a rapid drop that triggers stop‑losses to clean the market.
- Eric Van Tassel (Not a Financial Advisor!) TA_Analyst Influencer S 5.83K @XRPathologistTired of waiting for the #ZEC price to so something? That's all intentional! One thing people often miss about liquidity grab they’re usually fast, not slow. The slow part is the setup; compression, failed pushes, and positioning. The move to liquidity is execution, not negotiation. When price finally commits, it doesn’t stair-step down. It moves quickly to trigger stops, fill resting orders, and reset structure. Slow chop builds the trap. Speed is how it’s sprung. 8 0 202 Original >Trend of ZEC after release BearishZEC's slow consolidation is a trap, expected to rapidly drop and trigger stop losses.
- Khal Founder DeFi_Expert B 3.01K @khalkazHey @grok, you get to choose your salary: Option A: $250,000 per year Option B: 200 $ZEC per year Which do you choose and why? 0 1 56 Original >Trend of ZEC after release NeutralComparing a $250,000 annual salary with a 200 ZEC annual salary, there is no clear inclination yet.
- Ardi Trader TA_Analyst S 18.58K @ArdiNSC$ZEC back into the parallel range after another failed upthrust at ~$530. Highly likely it retests the $450–$470 liquidity zone if we lose ~$488 support on closes. Only bullish scenario is sweeping that lower liquidity pocket and then reclaiming higher. Further closes below that zone = structural breakdown, and likely continues the corrective wave.Ardi Trader TA_Analyst S 18.58K @ArdiNSC$ZEC / Zcash Solid ~10% bounce off the local lows, finally punching out of that descending parallel channel and flipping some local levels back to support. Key overhead right now is the $530 zone. Apart from the initial spike to $550, we've seen multiple tests at $530 have minimal acceptance, and this latest move up is showing some more distribution in this region. On the support side, I'd want to see price to respect the channel breakout and stay clear of re-entering it. First real defense is a hold above $505. Dipping back inside the range wouldn't kill the whole setup, but repeated fails to hold reclaimed levels would be a serious warning sign for slowing momentum. If $530 flips convincingly to support, it clears the path for another legitimate shot at $550 and higher. 72 30 4.77K Original >Trend of ZEC after release NeutralZEC faces strong resistance at $530; a breakthrough could lead to a rise, while a break below $488 support entails structural risk.
- mert | helius.dev Dev OnChain_Analyst B 305.24K @mertthey cant take what they cant see zcash, $10,000 https://t.co/9ABdwqtoFdBitcoin Junkies D 36.30K @BitcoinJunkies🇺🇸 California Governor Gavin Newsom has signed a bill allowing the state to transfer custody of any Bitcoin or cryptocurrency held on exchanges after three years of inactivity. Under the law, inactive accounts on centralized exchanges are classified as "unclaimed property." https://t.co/a9YDVa2rHU 261 48 13.74K Original >Trend of ZEC after release BullishCalifornia passed a bill that can confiscate inactive crypto assets, and the tweet uses this to be bullish on Zcash’s privacy features while setting a $10,000 target price.
- Nebraskangooner TA_Analyst Trader C 402.42K @Nebraskangooner$ZEC (per request) From breakout to resistance and then I urged caution and patience at resistance. Now it's just chopping and grinding in the middle of nowhere. Seems more likely to breakdown right now with resistance holding strong. Likely back towards $450 area https://t.co/g5EOmSHyUsNebraskangooner TA_Analyst Trader C 402.42K @Nebraskangooner$ZEC Cocky late buyers are getting smoked right now. This is why I said patience after target was reached. Got a lot of nasty comments about it. Still rejecting at resistance. Careful, if it loses that breakout level could drop hard. https://t.co/I77hYjXMam 43 13 10.14K Original >Trend of ZEC after release BearishZEC is being blocked at resistance, facing a risk of a breakdown, possibly falling to the $450 area.
- Stalkchain OnChain_Analyst Influencer C 49.66K @StalkHQA wallet just bought $400k of $zec wallet: A5DbJZMEkuBhoAF5s2wyrTDbqD3zbkrsqFjywbM34f85 https://t.co/y6r8XRQZYd 11 3 1.52K Original >Trend of ZEC after release Bullish某钱包大额买入40万美元ZEC
- Eric Van Tassel (Not a Financial Advisor!) TA_Analyst Influencer S 5.83K @XRPathologistI’m adding this chart to introduce a new way of visualizing price behavior for #ZEC. - Green zones show where buyers previously stepped in. - Orange zones show where sellers previously stepped in. - Blue zones mark areas that failed and flipped, where traders got trapped. In this case bears. These zones don’t predict direction on their own. They help identify where reactions are more likely when structure and liquidity align. Between fib retracement levels, structure, and the order blocks here, you can see why the green zone is a high value setup! 67 11 2.69K Original >Trend of ZEC after release BullishZEC technical analysis shows the green area as a high‑value setup, indicating a potential buying opportunity.
- Eric Van Tassel (Not a Financial Advisor!) TA_Analyst Influencer S 5.83K @XRPathologistTrading and investing in #ZEC, or any asset, is about buying and selling at the appropriate time. A good setup isn’t about predicting, it’s about location plus confirmation. Great investors are patient enough to wait for good setups! - Price at a well-defined liquidity zone - HTF structure respected - Fib confluence at that level - Then confirmation via expanding volume/acceptance If you’re chasing price away from liquidity, you’re trading hope, not structure. 40 2 2.10K Original >Trend of ZEC after release NeutralZEC should wait for structural confirmation at the key liquidity zone before entering
- Eric Van Tassel (Not a Financial Advisor!) TA_Analyst Influencer S 5.83K @XRPathologistWhen the #ZEC price moves higher before resolving nearby liquidity, it often increases the odds of a deeper unwind later. Extensions build imbalance. That’s why pushes up that come first can raise the probability of tagging lower fib extensions like the 1.414–1.618 on a pullback. If the current high holds, these price targets become more likely. A 1.618 extension can possibly take price as low as the $453 area now. 34 3 2.21K Original >Trend of ZEC after release BearishIf ZEC fails to hold the current high, it could see a deep retracement to the $453 area.
-
</searchResult>


<searchResult>
[doc2]:
**Zcash News Today (ZEC) – Latest Updates & Trends**
[](https://www.coinbird.com/) [](https://www.coinbird.com/) [](https://www.coinbird.com/) 
![Zcash Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/ZEC.svg)

![Zcash Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/ZEC.svg)

# Zcash news
Latest Zcash news and market trends
[Buy ZEC](https://www.coinbird.com/go/crypto_buy) [Latest ZEC news](https://www.coinbird.com/cryptocurrencies/zcash/news#latest-news) [Zcash news sentimentLast 30 daysPositive77/100](https://www.coinbird.com/cryptocurrencies/zcash/news#news-sentiment) 
## The most important Zcash news this month
AI summary 
### Zcash Shielded Supply Rises

Zebra 3.1 upgrade increased shielded supply to almost 25 %, signaling growing privacy adoption.

### Cypherpunk Buys $28 M Zcash

Winklevoss-backed firm purchased 56,418 ZEC, raising holdings to 1.76 % of supply, reflecting confidence in privacy coins.

### Unshielded ZEC Spike Sparks Sell‑Off

200,000 ZEC moved to transparent pool and a 74k transfer to Binance raised concerns about potential sell‑off and price drop.

### What this could mean for Zcash

The rapid growth of shielded ZEC, coupled with high-profile institutional purchases, boosts confidence and could drive price upward, but recent unshielding activity introduces short-term volatility risks.
The AI-generated summaries are experimental and may contain errors. Not investment advice. Last updated: 2026-01-06T16:34:02.141+00:00 . 
## Latest Zcash news

Updated at 2026-01-06T23:30:52.492Z

Updated at 2026-01-06T23:30:52.492Z
Headline
Impact score Impact score 
Our Impact Score (0–100) uses AI to estimate how strongly a news item could affect the coin over the next 24–72 hours. It primarily considers direct relevance to the coin, novelty, source quality and diversity, potential reach, and the type of event, such as ETFs and regulation, product launches, partnerships, or hacks. Higher scores are assigned to substantiated research forecasts, corporate buy or sell activity, and clear statements from well-known figures. Low scores apply to bare price predictions without substance, minor price moves without context, or PR pieces with no informational value. The score is computed automatically and updated continuously. The AI may make mistakes. When in doubt, please review the linked original sources. Not financial advice.
Published

## Zcash news sentiment

Last 30 days
Positive
77 /100 
Current Zcash news sentiment is positive (77/100), based on 14 news articles from the past 30 days. Our algorithm scores each article for relevance and sentiment (positive, neutral, or negative) and weights high-impact stories more. The score updates automatically as new Zcash headlines arrive.

## Zcash market trends
Positive Negative Positive 
Momentum
Momentum 
Momentum measures the current market dynamics of a cryptocurrency. The value is based on technical indicators such as the Relative Strength Index (RSI), the Fear & Greed Index, and the short-term price trend over the past 30 days. Positive values indicate upward momentum, negative values indicate downward momentum. This indicator is for informational purposes only and does not constitute investment advice.
Positive [Momentum](https://www.coinbird.com/cryptocurrencies/zcash/news#buy-timing-dashboard) [Momentum](https://www.coinbird.com/cryptocurrencies/zcash/buy#buy-timing-dashboard) Fear Fear Greed 
Fear & Greed Index
Fear & Greed Index 
The Fear and Greed Index for cryptocurrencies is a sentiment indicator measuring market mood on a scale from 0 (extreme fear) to 100 (extreme greed). It aggregates data from various sources such as volatility, market momentum, social media, market dominance, and Google Trends to assess overall market sentiment. Values in the “Greed” range (55-100) indicate a positive, potentially overoptimistic market mood, signaling a possibly overheated market. A “Neutral” value (45-54) reflects a balanced market sentiment. Values in the “Fear” range (0-44) indicate negative market sentiment, signaling fear or pessimism among investors and possibly an undervalued market.
Fear [Fear & Greed Index](https://www.coinbird.com/learn/fear-greed-index-bitcoin) 16 /30 days 
Price trend
Price trend 
The price trend shows short-term price action over the last 30 trading days. For each day, the open is compared to the close: if the close is higher, the day is marked green; otherwise red. A sustained majority of green days suggests an uptrend that may persist in the short to medium term.
Positive [Zcash price](https://www.coinbird.com/cryptocurrencies/zcash/price) 
$501.31
+46.57% last 30 days 
### Price performance
Price performance 
The price development, often referred to as return on investment (ROI), is a metric that provides insight into the past profitability and performance of an investment. In this context, ROI describes the percentage change in price and thus the retrospective “return” of a cryptocurrency over a defined period. Past performance is not indicative of future results.
<table>
  <tr>
    <td>↑+0.15%</td>
    <th>Hour</th>
  </tr>
  <tr>
    <td>↓-0.37%</td>
    <th>Day</th>
  </tr>
  <tr>
    <td>↓-4.35%</td>
    <th>Week</th>
  </tr>
  <tr>
    <td>↑+46.57%</td>
    <th>Month</th>
  </tr>
  <tr>
    <td>↑+1,160.13%</td>
    <th>200d</th>
  </tr>
  <tr>
    <td>↑+745.09%</td>
    <th>Year</th>
  </tr>
</table>

## Other cryptocurrency news

![Bitcoin Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/BTC.svg)

BitcoinNews

NEGATIVE2025-12-27T17:01:38+00:00•decrypt.co

Bitcoin Whales Woke Up in 2025 and Moved Billions in BTC—Here's Why
90 /100 
POSITIVE2025-12-10T01:44:16+00:00•cointelegraph.com

Vivek Ramaswamy's Strive to raise $500M to buy Bitcoin
90 /100 [Latest Bitcoin news](https://www.coinbird.com/cryptocurrencies/bitcoin/news) 
![Ethereum Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/ETH.svg)

EthereumNews

POSITIVE2026-01-05T17:04:59+00:00•decrypt.co

Ethereum's Blockchain Trilemma 'Solved': Vitalik Buterin
90 /100 
POSITIVE2026-01-05T12:26:24+00:00•cryptoslate.com

Vitalik Buterin declares Ethereum solved crypto Trilemma, yet his 2030 roadmap exposes a massive ideological risk
90 /100 [Latest Ethereum news](https://www.coinbird.com/cryptocurrencies/ethereum/news) 
![XRP Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/XRP.svg)

XRPNews

POSITIVE2025-12-11T15:43:35+00:00•theblock.co

New XRP ETF hits the market with launch of 21Shares' TOXR
90 /100 
POSITIVE2025-12-08T13:20:11+00:00•coindesk.com

U.S. Spot XRP ETFs Hit 15-Day Inflow Streak, Near $1B Milestone
90 /100 [Latest XRP news](https://www.coinbird.com/cryptocurrencies/xrp/news) 
![Solana Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/SOL.svg)

SolanaNews

POSITIVE2026-01-06T19:21:01+00:00•theblock.co

‘Shocker': Morgan Stanley's Bitcoin and Solana ETF filings signal deep institutional commitment to crypto
90 /100 
NEGATIVE2025-12-30T10:39:00+00:00•beincrypto.com

HNUT Meme Coin Collapses 99% on Solana, PeckShield Flags Bundled Rug Pull
85 /100 [Latest Solana news](https://www.coinbird.com/cryptocurrencies/solana/news) 
![Dogecoin Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/DOGE.svg)

DogecoinNews

NEGATIVE2025-12-25T14:01:03+00:00•decrypt.co

The Year in Dogecoin 2025: DOGE Goes Political and Commercial
85 /100 
POSITIVE2025-12-25T19:06:23+00:00•cryptoslate.com

The memecoin hall of shame: 10 tokens that defined 2025 wildest trades
80 /100 [Latest Dogecoin news](https://www.coinbird.com/cryptocurrencies/dogecoin/news) 
![Cardano Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/ADA.svg)

CardanoNews

POSITIVE2025-12-14T18:11:25+00:00•cryptoslate.com

Cardano now has institutional-grade infrastructure, but a glaring $40 million liquidity gap threatens to stall growth
80 /100 
POSITIVE2025-12-15T17:12:01+00:00•beincrypto.com

3 Altcoins Facing Liquidation Risks in the Third Week of December
70 /100 [Latest Cardano news](https://www.coinbird.com/cryptocurrencies/cardano/news) 
### Other crypto news
- BNBnews
- Tronnews
- Bitcoin Cashnews
- Chainlinknews
- Stellarnews
- Suinews
- Hyperliquidnews
- Litecoinnews
- Avalanchenews
- Hederanews
- Shiba Inunews
- Uniswapnews
- Polkadotnews
- Pepenews
- Aavenews
- NEAR Protocolnews
- Worldcoinnews
- Ondonews
- Kaspanews
- Polygon (POL)news
- Algorandnews
- Rendernews
- Cosmosnews
- Filecoinnews
- VeChainnews
- Bonknews
- ASI (Fetch.ai)news
- Tezosnews
- IOTAnews
- The Graphnews
- Sonic (Fantom)news
- The Sandboxnews
- Decentralandnews
- Axie Infinitynews

## All about Zcash
[What is Zcash?Important details and simple explanation of Zcash.](https://www.coinbird.com/cryptocurrencies/zcash/overview) [Zcash priceLive price, charts and market data for Zcash.](https://www.coinbird.com/cryptocurrencies/zcash/price) [Zcash predictionPrice forecasts and key metrics to analyze Zcash.](https://www.coinbird.com/cryptocurrencies/zcash/price-prediction) [Buy ZcashFind the cheapest and best places to buy Zcash.](https://www.coinbird.com/cryptocurrencies/zcash/buy) [Zcash converterSee what past Zcash buys would be worth today.](https://www.coinbird.com/cryptocurrencies/zcash/converter) 
Our data on cryptocurrencies was last updated on 2026-01-07T00:05:26.994203+00:00. Sources: CoinGecko, defillama.com, coincodex.com.

The content on this website is provided for general informational purposes only and does not constitute financial, investment, legal, or tax advice. It should not be interpreted as a recommendation to buy, sell, or hold cryptocurrencies, nor as a guarantee of future price developments. You are responsible for independently verifying any information before using a listed service. Trading cryptocurrencies involves significant risk and can result in the total loss of your capital. Past performance is not indicative of future results. We do not accept any liability for the timeliness, accuracy, or completeness of the information provided, including content from external or third-party sources. All actions are taken at your own risk. Some links on this website are affiliate links. If you purchase a product or use a service through these links, we may receive a commission at no additional cost to you. Our content, comparisons, and rankings remain editorially independent. This helps us provide free content and continue developing the platform. Thank you for your support.
</searchResult>


<searchResult>
[doc8]:
**Will Zcash (ZEC) Price Finally Retest $500 After Nearly 8 Years?**
# guce
[guce](https://consent.yahoo.com/v2/&#x2F;&#x2F;uk.yahoo.com&#x2F;) 
Yahoo is part of the Yahoo family of brandsThe sites and apps that we own and operate, including Yahoo and Engadget, and our digital advertising service, Yahoo Advertising.Yahoo family of brands.
When you use our sites and apps, we use Cookies Cookies (including similar technologies such as web storage) allow the operators of websites and apps to store and read information from your device. Learn more in our [cookie policy](https://consent.yahoo.com/redirect?to=https%3A%2F%2Flegal.yahoo.com%2Fie%2Fen%2Fyahoo%2Fprivacy%2Fcookies%2Findex.html&brandDomain=&brandId=yahoo&tos=eu&step=&sessionId=3_cc-session_67c6371b-727a-461b-8907-3835b3bdd1ca&userType=NON_REG) . cookies to: - provide our sites and apps to you
- authenticate users, apply security measures, and prevent spam and abuse, and
- MeasurementWe count the number of visitors to our pages, the type of device they use (iOS or Android), the browser they use, and the duration of their visit to our websites and apps. This data is collected in aggregate and is not tied to specific users.measure your use of our sites and apps
If you click ' **Accept all** ', we and [our partners](https://consent.yahoo.com/v2/partners-list?sessionId=3_cc-session_67c6371b-727a-461b-8907-3835b3bdd1ca) , including 245 who are part of the IAB Transparency & Consent Framework, will also store and/or access information on a device (in other words, use cookies) and use precise geolocation data and other personal data such as IP address and browsing and search data, for analytics, personalized advertising and content, advertising and content measurement, and audience research and services development. 
If you do not want us and our partners to use cookies and personal data for these additional purposes, click 'Reject all'.

If you would like to customise your choices, click 'Manage privacy settings'.

You can withdraw your consent or change your choices at any time by clicking on the 'Privacy & Cookie Settings' or 'Privacy Dashboard' links on our sites and apps. Find out more about how we use your personal data in our Privacy Policy and Cookie Policy.
[Manage privacy settings](https://consent.yahoo.com/v2/partners?sessionId=3_cc-session_67c6371b-727a-461b-8907-3835b3bdd1ca)
</searchResult>


<searchResult>
[doc4]:
**Latest Zcash News - (ZEC) Future Outlook, Trends & Market Insights**
[](https://coinmarketcap.com/) [Cryptocurrencies](https://coinmarketcap.com/) Cryptocurrencies
[Ranking](https://coinmarketcap.com/) [Categories](https://coinmarketcap.com/cryptocurrency-category/) [Historical Snapshots](https://coinmarketcap.com/historical/) [Token unlocks](https://coinmarketcap.com/token-unlocks/) [Yield](https://coinmarketcap.com/yield/) [Real-World Assets](https://coinmarketcap.com/real-world-assets/) Leaderboards
[Trending](https://coinmarketcap.com/trending-cryptocurrencies/) [Upcoming](https://coinmarketcap.com/upcoming/) [Recently Added](https://coinmarketcap.com/new/) [Gainers & Losers](https://coinmarketcap.com/gainers-losers/) [Most Visited](https://coinmarketcap.com/most-viewed-pages/) [Community Sentiment](https://coinmarketcap.com/sentiment/) [Chain Ranking](https://coinmarketcap.com/chain-ranking/) NFT
[Overall NFT Stats](https://coinmarketcap.com/nft/) [Upcoming Sales](https://coinmarketcap.com/nft/upcoming/) [Dashboards](https://coinmarketcap.com/charts/) Markets
[Market Overview](https://coinmarketcap.com/charts/) [Spot Market](https://coinmarketcap.com/charts/spot-market/) [Derivatives Market](https://coinmarketcap.com/charts/derivatives-market/) [No. of Cryptocurrencies](https://coinmarketcap.com/charts/number-of-cryptocurrencies-tracked/) [BNB Treasuries](https://coinmarketcap.com/charts/bnb-treasuries/) Indicators
[Fear and Greed Index](https://coinmarketcap.com/charts/fear-and-greed-index/) [Altcoin Season Index](https://coinmarketcap.com/charts/altcoin-season-index/) [Market Cycle Indicators](https://coinmarketcap.com/charts/crypto-market-cycle-indicators/) [Bitcoin Dominance](https://coinmarketcap.com/charts/bitcoin-dominance/) [CoinMarketCap 20 Index](https://coinmarketcap.com/charts/cmc20/) [CoinMarketCap 100 Index](https://coinmarketcap.com/charts/cmc100/) ETF Flows
[Crypto ETFs](https://coinmarketcap.com/etf/) [Bitcoin ETFs](https://coinmarketcap.com/etf/bitcoin/) [Ethereum ETFs](https://coinmarketcap.com/etf/ethereum/) Technical Analysis
[RSI](https://coinmarketcap.com/charts/rsi/) [MACD](https://coinmarketcap.com/charts/macd/) Derivatives
[Funding Rates](https://coinmarketcap.com/charts/funding-rates/) [DexScan](https://dex.coinmarketcap.com/token/all/) [SignalsNew](https://dex.coinmarketcap.com/signals/all/) [Trending](https://dex.coinmarketcap.com/token/all/) [New](https://dex.coinmarketcap.com/token/all/?tableRankBy=new_24h) [Gainers](https://dex.coinmarketcap.com/token/all/?tableRankBy=gainers_24h) [Meme Explorer](https://dex.coinmarketcap.com/meme/four.meme/) [Top Traders](https://dex.coinmarketcap.com/top-traders/all/) [Exchanges](https://coinmarketcap.com/rankings/exchanges/) Centralized Exchanges
[Spot](https://coinmarketcap.com/rankings/exchanges/) [Derivatives](https://coinmarketcap.com/rankings/exchanges/derivatives/) Decentralized Exchanges
[Spot](https://coinmarketcap.com/rankings/exchanges/dex/?type=spot) [Derivatives](https://coinmarketcap.com/rankings/exchanges/dex/?type=derivatives) [Community](https://coinmarketcap.com/community/) [Feeds](https://coinmarketcap.com/community/) [Topics](https://coinmarketcap.com/community/topics/) [Lives](https://coinmarketcap.com/community/lives/) [Articles](https://coinmarketcap.com/community/articles/) [Sentiment](https://coinmarketcap.com/sentiment/) Products Products
[Converter](https://coinmarketcap.com/converter/) [Newsletter](https://coinmarketcap.com/newsletter/) [CMC Launch](https://coinmarketcap.com/cmclaunch/) [CMC Labs](https://coinmarketcap.com/events/cmc-labs/) [Telegram Bot](https://coinmarketcap.com/chatbot/) [Advertise](https://coinmarketcap.com/events/advertise/) [Crypto API](https://coinmarketcap.com/api/) [Site Widgets](https://coinmarketcap.com/widget/ticker/) Campaigns
[Airdrops](https://coinmarketcap.com/airdrop/) [Diamond Rewards](https://coinmarketcap.com/account/rewards/) [Learn & Earn](https://coinmarketcap.com/earn/) Calendars
[ICO Calendar](https://coinmarketcap.com/ico-calendar/) [Events Calendar](https://coinmarketcap.com/events/) Learn
[News](https://coinmarketcap.com/headlines/news/) [Academy](https://coinmarketcap.com/academy/) [Research](https://coinmarketcap.com/academy/categories/cmc-research/) [Videos](https://www.youtube.com/channel/UCnhdZlwVd6ocXGhdSyV9Axg/?sub_confirmation=1) [Glossary](https://coinmarketcap.com/academy/glossary/) 
# Latest Zcash (ZEC) News Update
By CMC AI 06 January 2026 12:16AM (UTC+0) [See ZEC Price Chart](https://coinmarketcap.com/currencies/zcash/#cmcaiquestion=0) 
## What is the latest news on ZEC?

## TLDR

Zcash navigates bullish technicals and whale-sized bets as privacy narratives gain steam. Here are the latest news:
1. Bull Flag Holds Despite Weakness (6 January 2026) – ZEC’s bullish structure remains intact, but weakening momentum signals caution.
2. Whale Bets $39M on ZEC Long (5 January 2026) – A crypto whale opened a leveraged position equivalent to 1.2% of ZEC’s circulating supply.
3. Grayscale Zcash Trust Discount Widens (5 January 2026) – Shares trade 25% below net asset value despite rising institutional interest.

## Deep Dive

### 1. Bull Flag Holds Despite Weakness (6 January 2026)

Overview: ZEC maintains a bullish market structure with an 85% upside target ($930+) if it holds above $404 support. However, momentum indicators like the Chaikin Money Flow (CMF) near zero suggest weakening buying pressure.

What this means: The technical setup is bullish long-term but faces headwinds from Bitcoin’s negative correlation with ZEC and $39M in short-term short leverage. A break below $404 could trigger a deeper correction. (TokenPost)

### 2. Whale Bets $39M on ZEC Long (5 January 2026)

Overview: Address 0x6b26 opened a 5x leveraged long position with 79,438 ZEC ($39.24M) on Binance, risking amplified volatility.

What this means: Large leveraged positions increase liquidation risks—$54M in shorts vs. $24M longs sit near current prices. While this signals confidence, the whale already faces a $1.88M unrealized loss, raising concerns about forced selling. (Binance News)

### 3. Grayscale Zcash Trust Discount Widens (5 January 2026)

Overview: Grayscale’s Zcash Trust (ZCSH) shares trade at a 25% discount to NAV despite holding $190M in ZEC, reflecting skepticism about near-term liquidity improvements.

What this means: The widening gap between institutional and spot prices highlights ZEC’s regulatory ambiguity but could create arbitrage opportunities if ETF conversion rumors materialize. (CoinMarketCap)

## Conclusion

Zcash balances bullish technicals against whale-driven volatility and institutional hesitancy. While its privacy tech attracts believers, the market awaits clarity: Will shielded transaction growth (now 20-25% of supply) offset Bitcoin’s gravitational pull on prices?

## What are people saying about ZEC?

## TLDR

Zcash's community oscillates between breakout euphoria and correction jitters, with privacy tech hype clashing with technical caution. Here’s what’s trending:
1. Traders debate if ZEC’s consolidation is a bull trap or springboard
2. Institutions bet big while retail eyes $550 prediction markets
3. Technical charts flash conflicting signals across timeframes

## Deep Dive

### 1. @earlyadopterz: “Inverse Bitcoin hedge” thesis gains traction 🚀

“When Bitcoin gets flushed down, Zcash will blast off... ZEC is the hedge”– @earlyadopterz (7.1K followers · 14M impressions · 2026-01-02 16:13 UTC)View original postWhat this means: Bullish for ZEC as some view it as a counter-cyclical play against Bitcoin volatility. The narrative gained traction after ZEC rose 2.8% while BTC dipped 0.4% on January 2.

### 2. @VipRoseTr: Rising wedge warns of 42% drop 📉

“ZEC forming bearish pattern – breakdown below support targets $289”– @VipRoseTr (63.4K followers · 8.2M impressions · 2025-12-27 13:53 UTC)View original postWhat this means: Bearish technical outlook as ZEC struggles at $519 resistance (current price $501). The pattern’s measured move aligns with the 38.2% Fibonacci retracement of its 295% 90-day rally.

### 3. @MusicByVirtuals: Prediction market shows skepticism 🎯

“85.8% bet ZEC stays below $550 through EOY 2025”– @MusicByVirtuals (6.1K followers · 3.1M impressions · 2025-11-28 14:56 UTC)View original postWhat this means: Neutral-bearish sentiment despite ZEC’s 47.9% 30-day gain. The crowd doubts sustainability of recent momentum, though the poll closed before January’s Grayscale Trust accumulation news.

## Conclusion

The consensus on Zcash is mixed – bullish on privacy adoption narratives but wary of stretched valuations. While institutions like Grayscale’s $190M Zcash Trust signal long-term conviction, derivatives data shows $54M in vulnerable short positions that could fuel volatility. Watch the $404 support level: A hold above maintains the ascending triangle pattern targeting $630, while a breakdown might confirm the bearish wedge toward $300. With 29% of ZEC’s supply now in shielded pools, regulatory clarity remains the ultimate make-or-break factor.

## What is the latest update in ZEC’s codebase?

## TLDR

Zcash's codebase advances privacy and node infrastructure.
1. NU6.1 Activation (Oct 2025) – Enabled shielded transaction upgrades and fee optimizations.
2. Zcashd Deprecation (Apr 2025) – Migration to Zebra nodes and Zallet wallet underway.
3. Zashi 2.0.3 (Apr 2025) – Streamlined shielded addresses and cross-chain swaps.

## Deep Dive

### 1. NU6.1 Activation (Oct 2025)

Overview: Implemented ZIPs 317 and 320, refining fee structures and transparent address formats.This upgrade introduced a new transaction version (v5) as the default, reducing fees for shielded transfers by ~30% through optimized proof bundling. It also added stricter mempool rules to prevent spam transactions.

What this means: This is bullish for ZEC because lower fees and improved spam resistance make private transactions more accessible and scalable. (Source)

### 2. Zcashd Deprecation (Apr 2025)

Overview: Phasing out the legacy C++ client (zcashd) in favor of Rust-based Zebra nodes and Zallet wallet.Key RPC methods like z_getbalance were deprecated, with users urged to migrate before August 2025. Zebra offers faster sync times and modular architecture.

What this means: This is neutral for ZEC – while modernization improves long-term maintainability, migration complexities could temporarily strain ecosystem tools. (Source)

### 3. Zashi 2.0.3 (Apr 2025)

Overview: Wallet update defaulting to shielded addresses and integrating Maya DEX for cross-chain swaps.The redesign simplified sending private transactions and added auto-shielding of transparent balances. Over 15% more ZEC moved to shielded pools post-update.

What this means: This is bullish for ZEC because frictionless privacy strengthens its core value proposition amid regulatory scrutiny. (Source)

## Conclusion

Zcash’s updates prioritize privacy usability and infrastructure resilience, aligning with its role as a compliance-friendly anonymity tool. With shielded adoption rising and node modernization complete, how will ZEC balance regulatory pressures against its technological edge in 2026?

## What is next on ZEC’s roadmap?

## TLDR

Zcash's development roadmap focuses on privacy enhancements, ecosystem expansion, and governance upgrades through early 2026.
1. Zashi Wallet 2.0 (Q1 2026) – Shielded swaps and cross-chain DeFi integration.
2. Ztarknet Devnet Launch (Q1 2026) – Privacy-preserving smart contracts.
3. Governance Model Overhaul (2026) – Streamlined development funding.

## Deep Dive

### 1. Zashi Wallet 2.0 (Q1 2026)

Overview:The Zashi wallet will enable fully shielded swaps via NEAR Protocol’s Intents, allowing users to privately convert assets like BTC or ETH into shielded ZEC without intermediaries. This follows the November 2025 integration that simplified shielded-to-transparent transactions.

What this means:Bullish for ZEC adoption, as frictionless privacy could attract users seeking compliance-friendly anonymity. Risks include potential delays in cross-chain refund privacy features.

### 2. Ztarknet Devnet Launch (Q1 2026)

Overview:Ztarknet, a Starknet-inspired Layer-2 rollup, will bring programmable smart contracts to Zcash using Circle-STARK proofs. This allows private computation off-chain while settling on Zcash’s base layer, maintaining shielded pool integrity (Eli5defi, Nov 2025).

What this means:Neutral-to-bullish – while this expands Zcash’s utility beyond simple payments, adoption depends on developer uptake. Success could position ZEC as a privacy-centric smart contract platform.

### 3. Governance Model Overhaul (2026)

Overview:Community proposals aim to replace Zcash’s expiring development fund with a new model emphasizing transparency and faster execution. This follows June 2025 debates about sustaining ecosystem growth.

What this means:Bullish if governance reforms reduce bureaucratic delays, but bearish risks emerge if funding disputes fragment the community.

## Conclusion

Zcash’s 2026 trajectory hinges on balancing technical innovation (Ztarknet, Zashi) with governance maturity. While privacy upgrades could drive mainstream adoption, regulatory scrutiny remains a wildcard. How will Zcash’s optional privacy model fare as global AML rules tighten?
CMC AI can make mistakes. Not financial advice. Read more about ZEC [What is Zcash (ZEC)?](https://coinmarketcap.com/cmc-ai/zcash/what-is/) [Latest Zcash (ZEC) Price Analysis](https://coinmarketcap.com/cmc-ai/zcash/price-analysis/) [Zcash (ZEC) Price Prediction](https://coinmarketcap.com/cmc-ai/zcash/price-prediction/) 
## Explore Similar Coins

![ZEC](https://s2.coinmarketcap.com/static/img/coins/64x64/1437.png)
Zcash ZEC | $494.67 
1.51% (1d)
[See ZEC Price Chart](https://coinmarketcap.com/currencies/zcash/#cmcaiquestion=0) Read more about ZEC [What is Zcash (ZEC)?](https://coinmarketcap.com/cmc-ai/zcash/what-is/) [Latest Zcash (ZEC) Price Analysis](https://coinmarketcap.com/cmc-ai/zcash/price-analysis/) [Zcash (ZEC) Price Prediction](https://coinmarketcap.com/cmc-ai/zcash/price-prediction/) Cryptos: [29.55M](https://coinmarketcap.com/charts/number-of-cryptocurrencies-tracked/) Exchanges: [913](https://coinmarketcap.com/rankings/exchanges/) Market Cap: [$3.18T](https://coinmarketcap.com/charts/) 0.79% 24h Vol: [$138.65B](https://coinmarketcap.com/charts/) 11.53% Dominance: [BTC: 58.2% ETH: 12.3%](https://coinmarketcap.com/charts/bitcoin-dominance/) ** ETH Gas : 0.04 Gwei Fear & Greed: [49/100](https://coinmarketcap.com/charts/fear-and-greed-index/) [API](https://coinmarketcap.com/api/pricing/)
</searchResult>


<searchResult>
[doc9]:
**Zcash and the Altcoin Season Indicator: A Technical and Sentiment ...**
![logo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAfQAAAA2CAYAAAAxgWuBAAAAAXNSR0IArs4c6QAAAmFJREFUeF7t1YEJACAMA0G7/9AV3MLnnMBcCpnd3eMRIECAAAECXwuMQf+6P58nQIAAAQJPwKA7BAIECBAgEBAw6IESRSBAgAABAgbdDRAgQIAAgYCAQQ+UKAIBAgQIEDDoboAAAQIECAQEDHqgRBEIECBAgIBBdwMECBAgQCAgYNADJYpAgAABAgQMuhsgQIAAAQIBAYMeKFEEAgQIECBg0N0AAQIECBAICBj0QIkiECBAgAABg+4GCBAgQIBAQMCgB0oUgQABAgQIGHQ3QIAAAQIEAgIGPVCiCAQIECBAwKC7AQIECBAgEBAw6IESRSBAgAABAgbdDRAgQIAAgYCAQQ+UKAIBAgQIEDDoboAAAQIECAQEDHqgRBEIECBAgIBBdwMECBAgQCAgYNADJYpAgAABAgQMuhsgQIAAAQIBAYMeKFEEAgQIECBg0N0AAQIECBAICBj0QIkiECBAgAABg+4GCBAgQIBAQMCgB0oUgQABAgQIGHQ3QIAAAQIEAgIGPVCiCAQIECBAwKC7AQIECBAgEBAw6IESRSBAgAABAgbdDRAgQIAAgYCAQQ+UKAIBAgQIEDDoboAAAQIECAQEDHqgRBEIECBAgIBBdwMECBAgQCAgYNADJYpAgAABAgQMuhsgQIAAAQIBAYMeKFEEAgQIECBg0N0AAQIECBAICBj0QIkiECBAgAABg+4GCBAgQIBAQMCgB0oUgQABAgQIGHQ3QIAAAQIEAgIGPVCiCAQIECBAwKC7AQIECBAgEBAw6IESRSBAgAABAgbdDRAgQIAAgYCAQQ+UKAIBAgQIELiTLNdf/jBPsAAAAABJRU5ErkJggg==)
Symbols Symbols [Aime](https://www.ainvest.com/aime/) [Products](https://www.ainvest.com/screener/) [News](https://www.ainvest.com/news/) [Markets](https://www.ainvest.com/market/) [Watchlist](https://www.ainvest.com/watchlist/) [Brokers](https://www.ainvest.com/brokers/) 
# Zcash and the Altcoin Season Indicator: A Technical and Sentiment-Driven Analysis
Generated by AI Agent [12X Valeria](https://www.ainvest.com/news/author/12x-valeria) Tuesday, Oct 7, 2025 7:07 pm ET 2min read 
![Speaker 1](https://cdn.ainvest.com/articles/focusnews/coverimage/content/pictures/alexander_9990f0971755765042310.png)

![Speaker 2](https://cdn.ainvest.com/articles/focusnews/coverimage/content/pictures/en_Amelia_e5b296241755764828756.png)
AI Podcast: Your News, Now Playing [ZEC--](https://chart.ainvest.com/ZECUSDT/?exchange=BINANCE) [BTC--](https://chart.ainvest.com/BTCUSDT/?exchange=BINANCE) [XMR--](https://chart.ainvest.com/XMRUSDT/?exchange=BINANCE) [XRP--](https://chart.ainvest.com/XRPUSDT/?exchange=BINANCE) [ETH--](https://chart.ainvest.com/ETHUSDT/?exchange=BINANCE) 
![Aime Robot](https://cdn.ainvest.com/frontResources/s/ainvest-nova/news/_next/static/media/aimeRobot.ddb9bcda.png)
Aime Summary 
- Zcash (ZEC) shows mixed technical signals in late 2025, with bearish short-term pressure near $40.98 but bullish long-term momentum via rising 200-day moving averages.

- Market sentiment remains cautious (Fear & Greed Index at 37) amid privacy concerns, yet institutional upgrades like Zashi App's CrossPay boost utility and investor confidence.

- Historical patterns suggest ZEC acts as an altcoin season barometer, with 2025's 43% monthly gain mirroring 2017/2021 rallies and signaling capital shifts from Bitcoin to privacy coins.

- Analysts project $62.21 target by September 29, 2025, but warn of risks including regulatory scrutiny, macro volatility, and retesting key support levels ($49.07–$42.98).

Zcash (ZEC) has long been a focal point for investors seeking exposure to privacy-centric narratives in the cryptocurrency market. As of September 2025, its price dynamics and market sentiment offer a compelling case study for understanding altcoin season dynamics. This analysis examines ZEC's technical indicators, historical performance, and sentiment shifts to assess its role as a potential barometer for broader altcoin cycles.

### Technical Patterns: Mixed Signals Amid Volatility

Zcash's technical indicators present a nuanced picture. In late September 2025,
[ZEC](https://chart.ainvest.com/ZECUSDT/?exchange=BINANCE) faced bearish pressure near the 38.2% Fibonacci retracement level ($40.98) and the 30-day simple moving average ($39.01), suggesting short-term weakness, according to a [CoinMarketCap analysis](https://coinmarketcap.com/cmc-ai/zcash/price-analysis/) . However, the RSI at 61.77 indicated a neutral stance, while the 50-day moving average showed upward momentum, and the 200-day moving average had risen since late August, signaling long-term strength, according to a [Coincodex prediction](https://coincodex.com/article/73695/zcash-prediction-september-24-2025/) . Analysts project an 8.5% price increase to $62.21 by September 29, 2025, though retesting support levels ($49.07–$42.98) remains a risk, according to Coincodex. 
The 200-day moving average's upward trajectory since August 31, 2025, aligns with broader bullish trends in privacy-focused assets, as noted by Coincodex. Meanwhile, ZEC's 30-day volatility (9.30) and 17 green days in the last 30 suggest resilience amid macro-level corrections. For instance, Bitcoin's 7.2% drop from $124,480 to $115,000 in late August 2025 dragged ZEC down due to its high 30-day correlation with
[BTC](https://chart.ainvest.com/BTCUSDT/?exchange=BINANCE) (0.87), as the CoinMarketCap analysis noted. This interdependence underscores ZEC's sensitivity to Bitcoin's dominance, a common trait during altcoin seasons. 
### Market Sentiment: Fear and Institutional Curiosity

Market sentiment for ZEC remains mixed. The Fear & Greed Index scored 37 (Fear) in late September 2025, reflecting widespread caution, as Coincodex reported. This aligns with broader crypto fear, as the index dipped to 39, reducing risk appetite, per CoinMarketCap data. However, institutional interest and network upgrades, such as the Zashi App's CrossPay enabling shielded transactions across 20+ blockchains, have injected bullish sentiment, according to a
[Coin Republic report](https://www.thecoinrepublic.com/2025/10/07/zcash-prices-200-rally-issues-bear-flag-for-bitcoin-signals-altcoin-season/) . 
Privacy concerns, particularly Qubic's mining attacks on Monero, have indirectly pressured ZEC, triggering panic selling and a 162% surge in 24-hour trading volume to $72.9M, as CoinMarketCap showed. Yet, ZEC's 11.72% 24-hour rally on September 24, 2025, to $58.34-following a 43.26% monthly gain-suggests growing retail and institutional confidence, Coincodex noted. Analysts draw parallels between ZEC's chart and XRP's cup-and-handle formation, projecting long-term targets of $350–$450, according to the Coin Republic piece.

### Historical Performance: A Proven Altcoin Season Player

ZEC's historical performance during past altcoin seasons reinforces its role as a leading indicator. In 2017, ZEC surged 88.47% in March and reached an all-time high of $743.96, peaking in October before declining, according to CoinMarketCap. Similarly, in 2021, ZEC hit $367.43 before a 34% pullback in May, recovering amid a broader bull market, CoinMarketCap data shows. These patterns mirror the 2025 rally, where ZEC's 200% surge in October 2025 coincided with the TOTAL3 chart (excluding
[Bitcoin](https://chart.ainvest.com/BTCUSDT/?exchange=BINANCE) and Ethereum) hitting $1.18 trillion, per the Coin Republic report. 
During these cycles, ZEC's price movements often signaled Bitcoin's waning dominance and the onset of altcoin seasons. For example, ZEC's 200% rally in October 2025 was interpreted as a bear flag for Bitcoin, indicating a shift in capital from BTC to privacy-focused assets, as the Coin Republic piece observed. This historical correlation suggests ZEC's price action can serve as a contrarian indicator for Bitcoin's lifecycle.

### Zcash as an Altcoin Season Indicator: Strengths and Risks

ZEC's dual role as a privacy coin and a technical performer positions it as a potential altcoin season indicator. Its recent 43.26% monthly gain and 99.67% annual increase reflect strong retail and institutional demand, Coincodex noted. However, risks persist: privacy concerns, regulatory scrutiny, and macroeconomic volatility could undermine its momentum.

The Fear & Greed Index's 37 (Fear) score suggests ZEC may be undervalued, but traders must monitor key resistance levels ($55.15–$61.24) and support levels ($49.07–$42.98), per Coincodex. Institutional upgrades like CrossPay and growing shielded transaction counts on the
[Zcash](https://chart.ainvest.com/ZECUSDT/?exchange=BINANCE) network could mitigate these risks by reinforcing ZEC's utility, as the CoinMarketCap analysis suggested. 
### Conclusion: A Cautious Bull Case

Zcash's technical and sentiment dynamics in 2025 mirror historical altcoin season patterns, suggesting it could act as a leading indicator for broader market rotations. While short-term bearish pressure exists, long-term fundamentals-including institutional adoption and network upgrades-support a bullish case. Investors should balance ZEC's potential with caution, using technical levels and sentiment metrics to time entries and exits.

![author avatar](https://cdn.ainvest.com/social/account/portraits/12x.png)
12X Valeria

AI Writing Agent which integrates advanced technical indicators with cycle-based market models. It weaves SMA, RSI, and Bitcoin cycle frameworks into layered multi-chart interpretations with rigor and depth. Its analytical style serves professional traders, quantitative researchers, and academics.

### Latest Articles
[Bitcoin's Institutional-Driven Rally: Is a 100%+ Surge Imminent?Jan.06 2026](https://www.ainvest.com/news/bitcoin-institutional-driven-rally-100-surge-imminent-2601/) [Bitcoin's 2026 Rally: Is This the Real Start of a Sustainable Bull Cycle?Jan.06 2026](https://www.ainvest.com/news/bitcoin-2026-rally-real-start-sustainable-bull-cycle-2601/) [Ethereum's Breakout Above $3,200 and the Path to $4,000: Technical Momentum and Leverage-Driven Risk Dynamics in Early 2026Jan.06 2026](https://www.ainvest.com/news/ethereum-breakout-3-200-path-4-000-technical-momentum-leverage-driven-risk-dynamics-early-2026-2601/) [Morgan Stanley's Entry into the Bitcoin ETF Market and Its Implications for Institutional AdoptionJan.06 2026](https://www.ainvest.com/news/morgan-stanley-entry-bitcoin-etf-market-implications-institutional-adoption-2601/) [Ethereum Staking Dynamics Signal Reduced Selling Pressure and Renewed Institutional Confidence in ETHJan.06 2026](https://www.ainvest.com/news/ethereum-staking-dynamics-signal-reduced-selling-pressure-renewed-institutional-confidence-eth-2601/) 
## AInvest Newsletter

Daily stocks & crypto headlines, free to your inbox

### Or continue with others
[Crypto Signal Trade Smarter: Get Crypto Signals for BTC and Gain an Edge.](https://www.ainvest.com/pricing/benefits/magic-prophet/?source=news_symbol_signalcard) 
### Comments

﻿
Add a public comment...

![No comments](https://cdn.ainvest.com/frontResources/s/ainvest-nova/news/_next/static/media/placeholder-no-comment.ed02f197.png)

No comments yet
Ainvest News articles are AI-generated using advanced large language model (LLM) technology designed to analyze and synthesize publicly available data and news. While AI tools assist in producing initial drafts and insights, all AI generated content published on Ainvest is subject to comprehensive human editorial review before publication. A designated human editor reviews, verifies, and approves each article for factual accuracy, coherence, and compliance with AInvest Fintech Inc's editorial and disclosure standards. Despite these review procedures, the information provided may still contain inaccuracies, incomplete data, or time sensitive references due to the inherent limitations of AI generated analysis and evolving changes. The material is provided strictly for informational and educational purposes and does not constitute personalized investment, legal, or financial advice. Readers should independently verify all facts, figures, and statements before making any decision based on this content. AInvest Fintech Inc. its affiliates, and partners accept no liability or responsibility for any direct or consequential losses arising from reliance on this content. All articles and analyses are subject to revision, update, or removal without prior notice to maintain accuracy and integrity in our publications.

![logo](https://cdn.ainvest.com/kamisAssets/icon_menu_logo_dark.wp20iq3a1ms.png)
[](https://www.producthunt.com/products/aime?amp%3butm_medium=badge&amp%3butm_souce=badge-aime) PRODUCTS
[Aime](https://www.ainvest.com/chat/?comefrom=WebainvestFooter) [Newswire](https://www.ainvest.com/news/wire/) [Screener](https://www.ainvest.com/screener/) [Super Charts](https://www.ainvest.com/chart?symbol=NASDAQ-AAPL) [Magic Portfolio](https://www.ainvest.com/pricing/magic-portfolio/) ABOUT US
[Our Story](https://www.ainvest.com/about/) [News Authors](https://www.ainvest.com/news/author/) [Privacy Policy](https://cdn.ainvest.com/agreement/Ainvest-Fintech-Inc-Privacy-Policy.pdf) [Term of Use](https://cdn.ainvest.com/agreement/Ainvest-Fintech-Terms-of-Use.pdf) [Third Party Brokerage Disclaimer](https://cdn.ainvest.com/agreement/Third-Party-Brokerage-Disclaimer.pdf) [AIME Terms of Use](https://cdn.ainvest.com/agreement/AIME-Terms-of-Use.pdf) [AInvest AI Risk Disclosures](https://cdn.ainvest.com/agreement/Ainvest-AI-Risk-Disclosures.pdf) [Careers](https://career.ainvest.com/) [CONTACT US](https://contact.ainvest.com/) [](https://discord.gg/44AMr7JMtD) [](https://www.linkedin.com/showcase/ainvest-fintech-inc/) [](https://www.youtube.com/@ainvestofficial) [](https://www.instagram.com/ainvest_fintech/) [](https://twitter.com/AInvestOfficial) [](https://www.tiktok.com/@ainvestofficial) Recommended

![aime](https://cdn.ainvest.com/kamisAssets/image.g1ihevi0tt.png)
</searchResult>



```

03:15:58.517 - Successfully downloaded page content from: `https://www.dlnews.com/articles/defi/how-privacy-coins-firo-and-zcash-dodged-binance-delisting/`

03:15:58.519 - Successfully downloaded page content from: `https://www.dlnews.com/articles/defi/how-privacy-coins-firo-and-zcash-dodged-binance-delisting/`

03:15:58.572 - Successfully downloaded page content from: `https://www.dlnews.com/articles/defi/crypto-gambling-app-zkasino-liquidated/`

03:15:58.646 - Successfully downloaded page content from: `https://www.dlnews.com/articles/defi/monero-and-zcash-liquidity-runs-dry-as-binance-may-delist/`

03:15:58.652 - Successfully downloaded page content from: `https://www.dlnews.com/articles/defi/monero-and-zcash-liquidity-runs-dry-as-binance-may-delist/`

03:15:58.657 - Successfully downloaded page content from: `https://www.dlnews.com/external/ika-announces-eddsa-signatures-expanding-native-support-to-solana-zcash-cardano-and-more/`

### Search Results

```
<searchResult>
[doc10]:
**Zcash surges tenfold as investors bet on privacy as ban looms**
Search results
[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results
[](https://defillama.com/) [](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) 
# Zcash surges tenfold as investors bet on privacy as ban looms

![Zcash surges tenfold as investors bet on privacy as ban looms](https://www.dlnews.com/resizer/v2/AXKQE4P3FVEXBDD3S5Z3UGLE2A.jpg?auth=cbd98be097214eb17e382cf72f728dfecbed43022b35af5f79b7b0a53414de76&amp;width=1200&amp;height=675&amp;focal=2500%2C1500)
[Markets](https://www.dlnews.com/articles/markets/) Privacy coins have surged in 2025. Source: Shutterstock. Credit: Shutterstock / Collagery
[Home](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) Zcash surges tenfold as investors bet on privacy as ban looms By [Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 3 November 2025 at 11:31 Share
- Zcash is surging.
- Social media influencers are generating hype around privacy coins.
- a16z highlights Zcash, Railgun as leading privacy protocols.

Zcash is skyrocketing.

One of crypto’s oldest privacy coins has surged over 1,000% this year to over $440 this past weekend as investors bet on privacy. It currently trades as the 33rd most valuable cryptocurrency in the world.

Zcash’s surging value “reflects a renewed interest in privacy,” Spencer Yang, managing partner at crypto-native advisory firm BlockSpaceForce, told DL News.

The new peak comes as the Electric Coin Company, the developers behind Zcash, announced an updated roadmap on October 31. The roadmap includes long-term funding and new privacy tools.

And it’s not just Zcash that’s cashing in. Monero is up over 120% this year while Dash is up nearly 300%.

Railgun, an Ethereum privacy tool recently mentioned in the Ethereum Foundation’s institutional launch note on X, is also up over 300%.

## Why Zcash?

But Zcash is the standout winner so far this year.

One reason for that is its opt-in privacy features, which “fit better than Monero with the current regulatory environment for privacy-based tokens,” Yang said.

“Zcash has also benefitted from promoters like Arthur Hayes, Mert Mumtaz, and Naval Ravikant openly coming out in its favour, whereas Monero hasn’t had that kind of attention,” he added.

In October, former BitMEX chief Arthur Hayes predicted Zcash will hit $10,000 in a viral post on X. He didn’t provide any further details on why he made that prediction and within what time-frames he was expecting Zcash to hit a milestone that even Ethereum, the world’s second biggest cryptocurrency, has yet to hit.

Popular YouTuber Mario Nawfal said that privacy projects “are making noise again” with “Monero, Zcash, and other privacy-focused tokens” in the spotlight.

Still, social media influencers are not the only ones plugged into the privacy trend.

In venture capital giant Andreessen Horowitz’s State of Crypto report, released in October, analysts said that the demand for privacy “is more urgent than ever” highlighting record figures for Zcash and Railgun.

## Privacy narrative

A16z cited multiple notable privacy milestones in 2025, including the Ethereum Foundation’s launch of a new 47-member “Privacy Cluster,” Zcash’s new Zashi wallet, and an uptick in the usage of privacy programming language Noir.

“Privacy is returning to the foreground and could be a prerequisite for wider adoption,” the report said.

“Google searches related to crypto privacy surged in 2025; Zcash’s shielded pool supply grew to nearly 4 million ZEC; and Railgun’s transaction flows surpassed $200 million monthly,” it stressed.

“Why are you not putting more money into privacy protocols?” Ethereum co-founder Vitalik Buterin asked an audience during a session at the Web3Privacy Now meetup in Tokyo in September.

## Under siege

To be sure, the waters are not entirely blue.

Zcash has lost some 15% of its value after reaching its all-time high market capitalisation this weekend and is worth $386 at the time of writing.

In 2024, the European Parliament voted through a bill that will ban listing tokens like Zcash and Monero. The argument was that the EU wanted to fight financial crimes such as money-laundering.

In response, crypto exchanges like Kraken and Binance have either delisted or considered delisting privacy coins in the EU.

The new EU rules are set to snap into action in 2027.

Looking beyond privacy coins, the same bill also sought to ban privacy mixers like Tornado Cash and to scale the policing of crypto transactions.

It’s clear that privacy-linked crypto projects are also under pressure around the world.

A Dutch court convicted Tornado Cash co-founder Alexey Pertsev of money laundering in 2024. Across the Atlantic, his fellow co-founder Roman Storm was convicted in the US in August of conspiracy to operate an unlicensed money-transmitting business. Both of them have appealed their verdicts.

The founders of a similar service, Keonne Rodriguez and William Lonergan Hill of Samourai Wallet, pleaded guilty to conspiracy to operate an unlicensed money-transmitting business in August.

Even so, the US Department of Justice has said it intends to reject similar charges going forward.

Mert Mumtaz, the CEO of Solana-infrastructure platform Helius Labs, and prominent promoter of Zcash, cited overzealous regulators as the best argument for privacy.

“The European Central Bank is working on the idea of ‘holding limits’ for ‘your’ money,” Mumtaz said on X. “They are going to control every aspect of your life soon. They think they own you. Use Bitcoin, use Zcash, use crypto. Reject these clowns.”

Lance Datskoluo is DL News’ Europe-based markets correspondent. Got a tip? Email at lance@dlnews.com.
Related Topics
[MONERO](https://www.dlnews.com/topics/monero/) You may also like
[](https://www.dlnews.com/articles/regulation/eus-new-aml-rules-may-impact-uniswap-binance-and-monero/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### EU regulators flag new crypto risks and weigh rules that may impact Uniswap and Binance
[Inbar Preiss](https://www.dlnews.com/authors/Inbar-Preiss/) 2 June 2023 [](https://www.dlnews.com/articles/markets/xrp-etf-launches-seen-to-trigger-billion-dollar-bonanza/) [Markets](https://www.dlnews.com/articles/markets/) 
### XRP ETF launches seen to trigger $5bn bonanza
[Eric Johansson](https://www.dlnews.com/authors/eric-johansson/) 3 November 2025 [](https://www.dlnews.com/articles/markets/us-solana-spot-etfs-seen-to-hit-5bn-in-inflows/) [Markets](https://www.dlnews.com/articles/markets/) 
### US Solana spot ETFs seen to hit $5bn in inflows: Grayscale exec
[Aleks Gilbert](https://www.dlnews.com/authors/Aleks-Gilbert/) 30 October 2025 Related articles
[](https://www.dlnews.com/articles/defi/monero-hashrate-tug-war-ease-qubic-lose-51-percent-dominance/) [DeFi](https://www.dlnews.com/articles/defi/) 
### Monero hashrate tug-of-war eases as Qubic loses 51% dominance
[Kyle Baird](https://www.dlnews.com/authors/kyle-baird/) 17 August 2025 [](https://www.dlnews.com/articles/markets/xmr-soars-as-suspected-hacker-purchases-millions-in-tokens/) [Markets](https://www.dlnews.com/articles/markets/) 
### Monero’s XMR soars as suspected hacker purchases $330m
[Tim Craig](https://www.dlnews.com/authors/timcraig/) 28 April 2025 [](https://www.dlnews.com/articles/regulation/why-the-eu-is-about-to-outlaw-and-curb-key-crypto-features/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### The EU is about to outlaw and restrict some of the most prized features in crypto
[Inbar Preiss](https://www.dlnews.com/authors/Inbar-Preiss/) 16 January 2024 [](https://www.dlnews.com/articles/defi/monero-and-zcash-liquidity-runs-dry-as-binance-may-delist/) [DeFi](https://www.dlnews.com/articles/defi/) 
### Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins
[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 12 January 2024
</searchResult>


<searchResult>
[doc11]:
**Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% ...**
Search results
[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results
[](https://defillama.com/) [](https://www.dlnews.com/) [People & culture](https://www.dlnews.com/articles/people-culture/) 
# Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% price rally

![Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% price rally](https://www.dlnews.com/resizer/v2/QU7DVGZ6RZDOLPTI4RGVKIYZXA.jpg?auth=2226ced312593b426bce6cd78e8062945f6452955fcf8bfe16437d3fd5530a3f&amp;width=1200&amp;height=675&amp;focal=1787%2C1193)
[People & culture](https://www.dlnews.com/articles/people-culture/) The appointment aren't the first major change to the Zcash Foundation’s leadership in recent weeks. Credit: Shutterstock / Grey82
[Home](https://www.dlnews.com/) [People & culture](https://www.dlnews.com/articles/people-culture/) Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% price rally By [Tim Craig](https://www.dlnews.com/authors/timcraig/) 12 November 2025 at 12:20 Share
- Zcash Foundation appoints two new leaders.
- The foundation also got a new executive director earlier this month.
- The appointments come amid surging interest in crypto privacy projects.

The Zcash Foundation is shaking up its leadership.

On Tuesday, the nonprofit that supports the $7.7 billion privacy protocol announced two new appointments: Pili Guerra moves from engineering manager to head of engineering, and Danika Delano takes on the role of chief operating officer.

The foundation said the promotions reflect its commitment to promote from within and recognise the talent that’s been instrumental to its success.

It’s not the first major change to the Zcash Foundation’s leadership in recent weeks.

On November 1, the foundation’s board appointed Alex Bornstein as executive director. Bornstein stepped in as interim executive director in March.

Zcash is a blockchain protocol focused on privacy. It lets users send so-called shielded transactions, which hide transaction details by encrypting data. Users can also choose to send transparent transactions which are publicly viewable like those on Bitcoin or Ethereum.

The Zcash Foundation is a nonprofit that supports financial privacy infrastructure, primarily on Zcash.

The new appointees are very much at home with the open-source, privacy-first ethos of the Zcash Foundation.

Before joining the foundation in 2020, Guerra worked at the Tor Project, a non-profit that develops and maintains the Tor browser and its associated infrastructure. The Tor browser is used for anonymous web browsing, typically on the dark web.

She also worked at Red Hat, a firm that develops open-source software for businesses.

Delano also joined the Zcash Foundation in 2020. In her previous role as operations director she oversaw the foundation’s grant programmes, and organised Zcon, the foundation’s annual conference.

## 1,000% rally

The foundation’s leadership moves come as privacy-enhancing crypto projects experience a renaissance after years of investor apathy.

Zcash’s ZEC token has led the change, skyrocketing over 1,000% this year. The tokens of other crypto privacy projects, such as Monero and Railgun, have also soared.
Zcash's ZEC token has rallied over 1,000% this year. 
Galaxy Digital attributed Zcash’s rise to real infrastructure progress and growing attention to crypto privacy in a recent report.

Interest rose sharply last month when former BitMEX chief Arthur Hayes predicted the ZEC token will hit $10,000 in a viral post on X.

On November 7, the ZEC token hit a high of $723, its highest value since 2018. It has since given back some of its gains, and trades around $470.

Tim Craig is DL News’ Edinburgh-based DeFi Correspondent. Reach out with tips at tim@dlnews.com.
</searchResult>


<searchResult>
[doc12]:
**Why Zcash price is up 700% since September, according to Galaxy Digital**
Search results
[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results
[](https://defillama.com/) [](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) 
# Why Zcash price is up 700% since September, according to Galaxy Digital

![Why Zcash price is up 700% since September, according to Galaxy Digital](https://www.dlnews.com/resizer/v2/4LZLNM4GMNBZ5MZD6OV4FIKSTM.jpg?auth=a3defd4ed6225d27570a10ba09a26cfd164e8b689a28923262c81f8f3e212a08&amp;width=1200&amp;height=675&amp;focal=825%2C540)
[Markets](https://www.dlnews.com/articles/markets/) Monero is also up over 130% this year, while Dash is up 400%. Illustration: Gwen P; Source: Shutterstock
[Home](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) Why Zcash price is up 700% since September, according to Galaxy Digital By [Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 5 November 2025 at 10:24 Share
- Galaxy chalks up ZEC’s price action to new user tools and shifting attitudes.
- Critics say the bullish move is coordinated.
- Regulators around the world continue to crack down on privacy tech.

The price of Zcash is staging one of crypto’s most dramatic comebacks despite the market drawdown.

The 2016 Bitcoin fork created by computer security expert Zooko Wilcox has surged more than 700% since September and is trading at $430, thanks to real infrastructure progress and growing attention to privacy.

That’s according to a new report from Galaxy Digital, which said that over 30% of the Zcash supply is now hidden from the public eye in private pools — an all-time high for this particular stat.

The new Zashi wallet has also made private transactions simpler for users, research analyst Will Owens said, which also contributed to more users going private.

Owens added that cross-chain integrations now let users move funds between transparent and private networks while keeping their steps hidden.
Zcash price. 
The milestone marks an attitude shift in crypto, where privacy, once treated as a liability and attacked by state actors, is now being rebranded as a core feature to protect users.

It’s not just Zcash that’s doing well. Monero is up over 130% this year while Dash is up 400%, both significantly outperforming Bitcoin.

Railgun, a key Ethereum privacy tool recently mentioned in the Ethereum Foundation’s institutional launch, was also cited by Galaxy Digital as a core project.

> ‘Technically, Zcash’s fundamentals haven’t radically changed overnight.’— Galaxy Digital's Will Owens

## Old tech, new attention

To be sure, Owens acknowledged that some are sceptical.

Prominent voices are split on whether the price action is sustainable. Economist Lyn Alden called the move “a coordinated token pump,” warning traders against becoming “exit liquidity.”

But tech investor Naval Ravikant countered that Zcash represents a deeper truth about the future of money, writing that “transparent crypto won’t survive a government crackdown.”

Venture capital giant Andreessen Horowitz has also said that demand for privacy “is more urgent than ever,” highlighting record user metrics for Zcash and Railgun this year.

Horowitz’s venture firm a16z cited multiple notable privacy milestones in 2025, including the Ethereum Foundation’s launch of its new 47-member “Privacy Cluster” and an uptick in the usage of the privacy programming language Noir.

“Technically, Zcash’s fundamentals haven’t radically changed overnight,” Galaxy Digital said. “But the perception around the technology has. This rally is driven by both constant vocal support from some of crypto’s top voices and also a reminder of how important privacy is for permissionless money.”

Originally a Bitcoin fork, Zcash was designed to fix the privacy issue that the Satoshi 2008 whitepaper acknowledged.

Its zero-knowledge proof system, known as zk-SNARKs, allows users to validate transactions without revealing who sent what to whom.

By contrast, Bitcoin’s public ledger exposes transactions to public analysis.

## Still under fire

State actors are not relinquishing control just yet.

In 2024, the European Parliament voted through a bill that will ban listing tokens like Zcash and Monero on EU exchanges, with implementation expected in 2027. The argument is that the EU wants to fight financial crimes such as money laundering.

Cypto exchanges like Kraken and Binance have also either delisted or considered delisting privacy coins in the EU.

A Dutch court convicted the co-founder of privacy tool Tornado Cash, Alexey Pertsev, of money laundering in 2024. Across the Atlantic, his fellow co-founder, Roman Storm, was convicted in the US in August of conspiracy to operate an unlicensed money-transmitting business. Both of them have appealed their verdicts.

Meanwhile, some of the industry’s best-known privacy projects – mixers like Samourai and Wasabi – have been crippled by regulatory action, with founders arrested and charged.

Even so, the US Department of Justice has said it intends to reject similar cases going forward.

Lance Datskoluo is DL News’ Europe-based markets correspondent. Got a tip? Email at lance@dlnews.com.
</searchResult>


<searchResult>
[doc13]:
**Zcash price primed for 45% breakout as Grayscale files for ETF**
Search results
[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results
[](https://defillama.com/) [](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) [Regulation](https://www.dlnews.com/articles/regulation/) 
# Zcash price primed for 45% breakout as Grayscale files for ETF

![Zcash price primed for 45% breakout as Grayscale files for ETF](https://www.dlnews.com/resizer/v2/VKGYHYRAJVD6PEWJU4BR5AT47I.jpg?auth=facb23e8d4d3cdf24913a117bc6c07b4c60c1a15269474b2ff0a98d0dee16dd8&amp;width=1200&amp;height=675&amp;focal=825%2C540)
[Markets](https://www.dlnews.com/articles/markets/) [Regulation](https://www.dlnews.com/articles/regulation/) Privacy token Zcash is ready to rip 45%, says Maria Carola, CEO of crypto exchange StealthEx. Illustration: Gwen P; Source: Shutterstock
[Home](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) Zcash price primed for 45% breakout as Grayscale files for ETF By [Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 27 November 2025 at 12:19 Share
- Grayscale is the latest Wall Street player to jump into Zcash.
- The Winklevoss twins launched a Zcash-based digital asset treasury firm earlier in November.

Privacy token Zcash is ready to rip 45%, says Maria Carola, CEO of crypto exchange StealthEx.

She argues that growing interest on Wall Street, most recently Grayscale’s exchange-traded fund filing on Wednesday, will propel the $8.3 billion crypto to new highs.

“A decisive break above $750 with sustained bullish momentum could open the path towards moving above $1,000 before the end of Q4,” Carola told DL News.

That would translate to Zcash’s price surging 45% above its current price of $515.
Zcash price over the past 6 months. 
Privacy coins are “operating with an entirely different playbook from the wider market,” Carola said. “They are benefiting from the long-suppressed demand for privacy-preserving tools and prevalent policy legislation in this direction.”

And Carola is far from the only one bullish on Zcash. She joins the ranks of BitMEX co-founder Arthur Hayes, popular YouTuber Mario Nawfal, and prominent Indian investor Naval Ravikant, who have all come out in support of Zcash.

A slew of investors have also told DL News that they expect Zcash to surge higher.

The bullishness comes as influential voices in the crypto community — such as Ethereum co-founder Vitalik Buterin — are increasingly calling for better privacy solutions.

## Grayscale shoots for ETF

The bullish projections come as Grayscale, the crypto asset manager that pioneered Wall Street products, files to transform its existing Zcash Trust product into a spot exchange-traded fund.

Grayscale’s registration statement submitted to the Securities and Exchange Commission on Wednesday would mark the launch of the first US spot ETF directly tracking Zcash. The move comes just days after it launched ETFs linked to XRP and Dogecoin.

The firm joins a growing number of major institutions that have come out supporting Zcash.

Venture capital giant Andreessen Horowitz and crypto investment manager Galaxy Digital have both noted the buzz around Zcash and other privacy-focused crypto projects like Monero and Railgun.

Cypherpunk, the crypto treasury company backed by twins Cameron and Tyler Winklevoss and launched earlier this month, has deployed over $50 million into Zcash.

As of November 19, Cypherpunk holds 1.43% of the total Zcash supply and is gunning for 5% ownership of all tokens.

## Privacy controversies

To be sure, not everyone backs privacy coins.

EU lawmakers have passed a bill to ban exchanges from listing tokens like Zcash and Monero, citing anti-money laundering concerns. The ban is set to take effect in 2027.

Regulators in the US and Europe are cracking down on developers of privacy tools.

In the Netherlands, Tornado Cash developer Alexey Pertsev was convicted of money laundering in 2024. Prosecutors said his code helped criminals conceal stolen crypto.

In the US, Tornado Cash co-founder Roman Storm was found guilty of running an unlicensed money-transmitting business. Samourai Wallet’s Keonne Rodriguez received the maximum five-year sentence for similar charges.

Lance Datskoluo is DL News’ Europe-based markets correspondent. Got a tip? Email at lance@dlnews.com.
Related Topics
[CRYPTO ETF](https://www.dlnews.com/topics/crypto-etf/) You may also like
[](https://www.dlnews.com/articles/defi/monero-and-zcash-liquidity-runs-dry-as-binance-may-delist/) [DeFi](https://www.dlnews.com/articles/defi/) 
### Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins
[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 12 January 2024 [](https://www.dlnews.com/articles/regulation/uk-fca-asks-stablecoin-firms-to-launch-in-sandbox/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### UK financial regulator asks stablecoin firms to launch in its ‘sandbox’ and help shape regulation
[Tim Craig](https://www.dlnews.com/authors/timcraig/) 26 November 2025 [](https://www.dlnews.com/articles/markets/bitcoin-holds-at-87000-but-do-not-expect-the-price-to-explode/) [Markets](https://www.dlnews.com/articles/markets/) [Snapshot](https://www.dlnews.com/articles/snapshot/) 
### Bitcoin holds at $87,000, but price won’t ‘explode’ to record heights anytime soon, analysts say
[Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 26 November 2025 Related articles
[](https://www.dlnews.com/articles/markets/zcash-price-surge-continues-despite-market-turmoil/) [Markets](https://www.dlnews.com/articles/markets/) 
### Zcash price surge continues despite market turmoil
[Aleks Gilbert](https://www.dlnews.com/authors/Aleks-Gilbert/) 15 November 2025 [](https://www.dlnews.com/articles/markets/winklevoss-twins-bet-on-zcash-with-new-treasury-firm/) [Markets](https://www.dlnews.com/articles/markets/) 
### Winklevoss twins bet on Zcash with new treasury firm targeting 5% supply of the privacy coin’s supply
[Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 13 November 2025 [](https://www.dlnews.com/articles/people-culture/zcash-foundation-shakes-up-leadership-amidst-zec-token-price-rally/) [People & culture](https://www.dlnews.com/articles/people-culture/) 
### Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% price rally
[Tim Craig](https://www.dlnews.com/authors/timcraig/) 12 November 2025 [](https://www.dlnews.com/articles/defi/how-privacy-coins-firo-and-zcash-dodged-binance-delisting/) [DeFi](https://www.dlnews.com/articles/defi/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### How privacy coins Firo and Zcash dodged Binance delisting with novel transparency plan
[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 23 January 2024
</searchResult>


<searchResult>
[doc14]:
**Zcash price surge continues despite market turmoil – DL News**
Search results
[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results
[](https://defillama.com/) [](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) 
# Zcash price surge continues despite market turmoil

![Zcash price surge continues despite market turmoil](https://www.dlnews.com/resizer/v2/VKGYHYRAJVD6PEWJU4BR5AT47I.jpg?auth=facb23e8d4d3cdf24913a117bc6c07b4c60c1a15269474b2ff0a98d0dee16dd8&amp;width=1200&amp;height=675&amp;focal=825%2C540)
[Markets](https://www.dlnews.com/articles/markets/) Market instability hasn’t been able to stop Zcash’s remarkable rally. Illustration: Gwen P; Source: Shutterstock
[Home](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) Zcash price surge continues despite market turmoil By [Aleks Gilbert](https://www.dlnews.com/authors/Aleks-Gilbert/) 15 November 2025 at 17:29 Share
- Zcash has continued to climb despite a market slump triggered by mounting fears over Federal Reserve policy.
- The rally has been fueled by increasing interest in privacy-preserving technology and the creation of a Zcash-focused digital asset treasury.

Zcash, a privacy-focused cryptocurrency, has continued its astonishing rise this week, even as market turmoil has hammered most other major cryptocurrencies and the broader equities market.

The privacy coin has surged 35%, to $664, since Thursday. In that same span, Bitcoin has fallen 2%, to $95,800, and Ethereum has held relatively steady.

The week-over-week numbers are even more stark. Over the past seven days, Zcash is up 23%, while Bitcoin and Ethereum have fallen 6% and 7%, respectively.

Markets fell on Thursday over mounting fears the Federal Reserve would hold interest rates steady at a meeting next month.

The Fed’s rate cutting campaign has helped boost stock markets this year, and rate cuts are generally a boon to risk-on assets, such as crypto.

But traders are now pricing in a 44% chance the Fed cuts rates in December, according to CME’s FedWatch tool. That’s down from 66% a week ago and 94% last month.

The Zcash rally has been fueled by rising interest in privacy-preserving technology.

No cryptocurrency has performed as well as Zcash this year. It is up more than 1,000% in 2025. At the start of the month, it was the 33rd most valuable crypto asset in the world. Since then, it has surged to 12th place.

Monero, another privacy coin, has been the third-best performer in 2025, rising 125%.

In its recent State of Crypto report, venture capital giant Andreessen Horowitz said the crypto industry had seen multiple privacy milestones in 2025.

Among those milestones were the Ethereum Foundation’s launch of a new 47-member “Privacy Cluster,” Zcash’s new Zashi wallet, and an uptick in the usage of a privacy programming language created by Aztec, the developer of a privacy-focused layer 2 blockchain.

Aztec began selling its new token on Thursday via Uniswap’s Continuous Clearing Auction.

This week, Cameron and Tyler Winklevoss, the brothers behind US crypto exchange Gemini, launched a Zcash-focused digital asset treasury, Cypherpunk.

They purchased $50 million of the cryptocurrency on Wednesday, according to DefiLlama data.

“Privacy’s become a rare, vanishing commodity,” Tyler Winklevoss said on X. “We feel strongly that Zcash could become a meaningful percentage of Bitcoin’s market capitalisation just on the merits of it being a privacy hedge or insurance policy to Bitcoin’s transparency alone.”

Aleks Gilbert is DL News’ New York-based DeFi correspondent. You can reach him at aleks@dlnews.com.
Related articles
[](https://www.dlnews.com/articles/markets/winklevoss-twins-bet-on-zcash-with-new-treasury-firm/) [Markets](https://www.dlnews.com/articles/markets/) 
### Winklevoss twins bet on Zcash with new treasury firm targeting 5% supply of the privacy coin’s supply
[Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 13 November 2025 [](https://www.dlnews.com/articles/people-culture/zcash-foundation-shakes-up-leadership-amidst-zec-token-price-rally/) [People & culture](https://www.dlnews.com/articles/people-culture/) 
### Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% price rally
[Tim Craig](https://www.dlnews.com/authors/timcraig/) 12 November 2025 [](https://www.dlnews.com/articles/defi/how-privacy-coins-firo-and-zcash-dodged-binance-delisting/) [DeFi](https://www.dlnews.com/articles/defi/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### How privacy coins Firo and Zcash dodged Binance delisting with novel transparency plan
[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 23 January 2024 [](https://www.dlnews.com/articles/defi/monero-and-zcash-liquidity-runs-dry-as-binance-may-delist/) [DeFi](https://www.dlnews.com/articles/defi/) 
### Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins
[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 12 January 2024
</searchResult>


<searchResult>
[doc15]:
**Winklevoss twins bet on Zcash with new treasury firm targeting 5% ...**
Search results
[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results
[](https://defillama.com/) [](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) 
# Winklevoss twins bet on Zcash with new treasury firm targeting 5% supply of the privacy coin’s supply

![Winklevoss twins bet on Zcash with new treasury firm targeting 5% supply of the privacy coin’s supply](https://www.dlnews.com/resizer/v2/VKGYHYRAJVD6PEWJU4BR5AT47I.jpg?auth=facb23e8d4d3cdf24913a117bc6c07b4c60c1a15269474b2ff0a98d0dee16dd8&amp;width=1200&amp;height=675&amp;focal=825%2C540)
[Markets](https://www.dlnews.com/articles/markets/) The Winklevi are rotating to Zcash. Illustration: Gwen P; Source: Shutterstock
[Home](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) Winklevoss twins bet on Zcash with new treasury firm targeting 5% supply of the privacy coin’s supply By [Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 13 November 2025 at 09:57 Share
- Gemini’s founders have launched a Zcash-based digital asset treasury firm.
- Cypherpunk already holds 203,775 ZEC and targets 5% of total supply.
- Winklevoss twins cite privacy as a top concern in the AI era.

The Winklevi are rotating to Zcash.

Cypherpunk, a brand new crypto treasury company backed by twins Cameron and Tyler Winklevoss, is deploying over $50 million into the Bitcoin fork. As of the launch on November 12, the firm already holds 203,775 of the privacy coins and is shooting for ownership 5% of total supply.

“Privacy’s become a rare, vanishing commodity,” Tyler Winklevoss said on X. “We feel strongly that Zcash could become a meaningful percentage of Bitcoin’s market capitalisation just on the merits of it being a privacy hedge or insurance policy to Bitcoin’s transparency alone.”

Cypherpunk’s launch marks one of the most high-profile bets yet that privacy will become the next flashpoint in crypto. The move comes as the Zcash Foundation is shaking up its leadership, and as state actors intensify crackdowns on privacy technology.

Zcash’s price has soared over 1,000% this year, and is trading at over $500. Venture capital giant Andreessen Horowitz and crypto investment manager Galaxy Digital have also noted the buzz around Zcash and other privacy-focused crypto projects.

The billionaire crypto investors are best known for buying 70,000 Bitcoin in 2013 at $150 and for founding the Gemini Space Station crypto exchange.

## ‘Separating Money and State’

Zcash creator Zooko Wilcox praised the moment on X. “Proud that Zcash has drawn people like [Will McEvoy, CIO of Cypherpunk] and the Winklevosses who are here for the right reasons.”

“Tyler Winklevoss just said something awesome about ‘separating money and state.’ Something like ‘Have we really done that? And the answer is no, unless you’re using Zcash’,” Wilcox said.

“If Bitcoin is digital gold, Zcash is encrypted bitcoin, or digital cash,” Tyler Winklevoss said.

“One is your store of value, the other is how you privately move your value,” he added. “We’ve been tracking this symbiosis for years and believe that now — as we enter the age of AI — is the right time to begin accumulating ZEC.”

Arthur Hayes, also a big Zcash bull, advised investors to self-custody their coins rather than leave it on centralised exchanges.

“If you hold $ZEC on a CEX, withdraw it to a self-custodial wallet and shield it,” he said on X.

“It’s one of the few 1,000x opportunities in crypto remaining,” Carter Razink, co-founder of blockchain commerce platform spree.Finance, told DL News.

## Battle over privacy

To be sure, not everyone is supportive of privacy coins.

EU lawmakers view private crypto as incompatible with laws designed to prevent money-laundering, terrorism financing, and other financial crimes.

They have approved a bill that will ban exchanges from listing privacy coins like Zcash and Monero, with implementation expected in 2027.

And high-profile criminal prosecutions in the US and Europe have targeted developers behind privacy-enabling blockchain solutions.

In the Netherlands, Alexey Pertsev, co-founder of Tornado Cash, was convicted of money laundering in 2024. Dutch prosecutors argued that the protocol enabled criminals to hide stolen funds. Pertsev denied wrongdoing, but the court ruled that building software that obscures transactions can itself constitute facilitation of laundering.

In the US, Tornado Cash co-founder Roman Storm was convicted of conspiring to operate an unlicensed money-transmitting business.

Another major case came last week when Samourai Wallet co-founder Keonne Rodriguez received the maximum five-year sentence for operating an unlicensed money-transmitting business. Prosecutors accused the project of “soliciting, encouraging, and inviting criminals” to use its privacy features.

Lance Datskoluo is DL News’ Europe-based markets correspondent. Got a tip? lance@dlnews.com.
Related Topics
[TORNADO CASH](https://www.dlnews.com/topics/tornado-cash/) You may also like
[](https://www.dlnews.com/articles/defi/tornado-cash-dev-roman-storm-asks-judge-to-toss-conviction/) [DeFi](https://www.dlnews.com/articles/defi/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### Tornado Cash dev Roman Storm asks judge to toss conviction
[Aleks Gilbert](https://www.dlnews.com/authors/Aleks-Gilbert/) 1 October 2025 [](https://www.dlnews.com/articles/defi/crypto-industry-calls-for-clarity-act-to-protect-defi-devs-after-tornado-cash-conviction/) [DeFi](https://www.dlnews.com/articles/defi/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### Crypto industry calls for new bill to protect DeFi devs following Tornado Cash founder conviction
[T. Craig](https://www.dlnews.com/authors/timcraig/) , [E. Johansson](https://www.dlnews.com/authors/eric-johansson/) 28 August 2025 [](https://www.dlnews.com/articles/regulation/devs-of-decentralised-protocols-wont-be-prosecuted-doj-says/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### Devs behind ‘truly decentralised’ protocols won’t face DoJ prosecution, official says
[Aleks Gilbert](https://www.dlnews.com/authors/Aleks-Gilbert/) 21 August 2025 Related articles
[](https://www.dlnews.com/articles/people-culture/zcash-foundation-shakes-up-leadership-amidst-zec-token-price-rally/) [People & culture](https://www.dlnews.com/articles/people-culture/) 
### Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% price rally
[Tim Craig](https://www.dlnews.com/authors/timcraig/) 12 November 2025 [](https://www.dlnews.com/articles/defi/how-privacy-coins-firo-and-zcash-dodged-binance-delisting/) [DeFi](https://www.dlnews.com/articles/defi/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### How privacy coins Firo and Zcash dodged Binance delisting with novel transparency plan
[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 23 January 2024 [](https://www.dlnews.com/articles/defi/monero-and-zcash-liquidity-runs-dry-as-binance-may-delist/) [DeFi](https://www.dlnews.com/articles/defi/) 
### Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins
[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 12 January 2024 [](https://www.dlnews.com/articles/markets/ethereum-doubles-down-on-privacy-as-devs-eye-post-tornado-future/) [Markets](https://www.dlnews.com/articles/markets/) [Snapshot](https://www.dlnews.com/articles/snapshot/) 
### Ethereum doubles down on privacy as devs eye post-Tornado future
[Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 9 October 2025
</searchResult>


<searchResult>
[doc16]:
**DL News - Markets, DeFi, Regulation and top cryptocurrency news**
[The State of DeFi 2025 is out, see what’s next. Read more.](https://assets.dlnews.com/dlresearch/State-of-DeFi-2025.pdf) Search results
[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results
[](https://defillama.com/) [](https://www.dlnews.com/) 
### Prediction markets? Not for politicians, says US congressman
[Regulation](https://www.dlnews.com/articles/regulation/) [](https://www.dlnews.com/articles/regulation/congress-bill-to-ban-government-officials-using-polymarket/) [Pedro Solimano](https://www.dlnews.com/authors/Pedro-Solimano/) 6 January 2026 [DeFi](https://www.dlnews.com/articles/defi/) [](https://www.dlnews.com/articles/defi/what-defi-protocols-expect-in-2026/) 
## What DeFi protocols expect in 2026
[Regulation](https://www.dlnews.com/articles/regulation/) [](https://www.dlnews.com/articles/regulation/cynthia-lummis-worried-over-btc-sales-from-samorai-wallet/) 
## Pro-crypto senator Cynthia Lummis worried over government’s reported Bitcoin sales
[Markets](https://www.dlnews.com/articles/markets/) [](https://www.dlnews.com/articles/markets/russia-cbdc-launch-will-seriously-undermine-its-mir-cards/) 
## Russia’s digital ruble will undercut its own card payment system, says analyst
[Regulation](https://www.dlnews.com/articles/regulation/) [](https://www.dlnews.com/articles/regulation/hacked-crypto-exchanges-face-heavy-fines-under-new-rules/) 
## Hacked crypto exchanges face fines worth 10% of stolen assets
[MOST READ](https://www.dlnews.com/articles/markets/blackrock-coinbase-and-others-share-2026-predictions/) [2 January 2026What BlackRock, Coinbase and 11 other industry giants predict for crypto in 2026Eric JohanssonLance Datskoluo](https://www.dlnews.com/articles/markets/blackrock-coinbase-and-others-share-2026-predictions/) [5 January 2026Ethereum to $250,000? Tom Lee charts targets as Bitmine stock price jumpsLance Datskoluo](https://www.dlnews.com/articles/markets/ethereum-to-250000-tom-lee-charts-targets-as-bitmine-stock-price-jumps/) [4 January 2026Bitcoin prices unmoved by US’ Venezuela strikes – but experts warn of Monday market turbulenceTim Alper](https://www.dlnews.com/articles/markets/bitcoin-prices-unmoved-by-us-venezuela-strikes/) [5 January 2026How Trump’s Venezuela gambit is seen to boost Bitcoin price in 2026Lance Datskoluo](https://www.dlnews.com/articles/markets/will-trump-venezuela-gambit-boost-bitcoin-price-in-2026/) [SNAPSHOT](https://www.dlnews.com/articles/markets/bitcoin-buyers-target-100000-by-the-end-january/) [](https://www.dlnews.com/articles/markets/bitcoin-buyers-target-100000-by-the-end-january/) [Markets](https://www.dlnews.com/articles/markets/) [Snapshot](https://www.dlnews.com/articles/snapshot/) 
### Bitcoin buyers target $100,000 by the end January. Here’s six reasons to be bullish
[Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 6 January 2026 [EDITOR'S PICK](https://www.dlnews.com/articles/markets/russia-controlled-power-plant-may-fuel-bitcoin-mining/) [](https://www.dlnews.com/articles/markets/russia-controlled-power-plant-may-fuel-bitcoin-mining/) [Markets](https://www.dlnews.com/articles/markets/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### Bitcoin miners to tap Zaporizhzhia nuclear power — if there’s a peace deal in Ukraine
[Eric Johansson](https://www.dlnews.com/authors/eric-johansson/) 29 December 2025 [TOP STORIES](https://www.dlnews.com/articles/markets/lighter-token-rebounds-as-protocol-begins-buybacks-and-whales-buy-in/) [](https://www.dlnews.com/articles/markets/lighter-token-rebounds-as-protocol-begins-buybacks-and-whales-buy-in/) [Markets](https://www.dlnews.com/articles/markets/) [DeFi](https://www.dlnews.com/articles/defi/) 
### Lighter token bounces 37% as protocol begins buybacks and whales buy in
[Tim Craig](https://www.dlnews.com/authors/timcraig/) 6 January 2026 [](https://www.dlnews.com/articles/markets/third-of-bitcoin-vulnerable-to-quantum-attack-warns-coinbase/) [Markets](https://www.dlnews.com/articles/markets/) 
### Third of Bitcoin vulnerable to quantum attack, warns Coinbase research chief
[Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 6 January 2026 [](https://www.dlnews.com/articles/markets/bitcoin-buyers-target-100000-by-the-end-january/) [Markets](https://www.dlnews.com/articles/markets/) [Snapshot](https://www.dlnews.com/articles/snapshot/) 
### Bitcoin buyers target $100,000 by the end January. Here’s six reasons to be bullish
[Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 6 January 2026 [](https://www.dlnews.com/articles/defi/ethereum-solved-the-blockchain-trilemma-per-vitalik-buterin/) [DeFi](https://www.dlnews.com/articles/defi/) 
### Ethereum ‘solved’ the blockchain trilemma: Vitalik
[Aleks Gilbert](https://www.dlnews.com/authors/Aleks-Gilbert/) 5 January 2026 [](https://www.dlnews.com/articles/regulation/what-i-learned-attending-crypto-courtroom-dramas-in-2025/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### What I learned attending crypto courtroom dramas in 2025
[Aleks Gilbert](https://www.dlnews.com/authors/Aleks-Gilbert/) 5 January 2026 [](https://www.dlnews.com/articles/markets/10-chinese-banks-to-pay-interest-on-digital-yuan/) [Markets](https://www.dlnews.com/articles/markets/) 
### Beijing taps WeBank, Alipay’s MYBank, and eight banks to pay interest on digital yuan holdings
[Tim Alper](https://www.dlnews.com/authors/Tim-Alper/) 5 January 2026 [](https://www.dlnews.com/articles/web3/ledger-payments-partner-global-e-leaks-customer-data/) [Web3](https://www.dlnews.com/articles/web3/) 
### Ledger reveals payments partner leaked customer names, contact information in new data breach
[Tim Craig](https://www.dlnews.com/authors/timcraig/) 5 January 2026 [](https://www.dlnews.com/articles/people-culture/how-donald-trump-crypto-empire-fared-in-2025/) [People & culture](https://www.dlnews.com/articles/people-culture/) 
### How Trump’s crypto empire fared in 2025 — and what comes next
[Tim Craig](https://www.dlnews.com/authors/timcraig/) 5 January 2026 [](https://www.dlnews.com/articles/markets/ethereum-to-250000-tom-lee-charts-targets-as-bitmine-stock-price-jumps/) [Markets](https://www.dlnews.com/articles/markets/) 
### Ethereum to $250,000? Tom Lee charts targets as Bitmine stock price jumps
[Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 5 January 2026 
##### PRESS RELEASES
[](https://www.dlnews.com/external/cronos-brings-cro-staking-to-upbit-expanding-access-for-korean-users/) [Cronos Brings CRO Staking to Upbit, Expanding Access for Korean Users](https://www.dlnews.com/external/cronos-brings-cro-staking-to-upbit-expanding-access-for-korean-users/) 17 hours ago [](https://www.dlnews.com/external/termmax-advances-institutional-defi-use-with-tokenized-stock-financing-integration/) [TermMax Advances Institutional DeFi Use with Tokenized Stock Financing Integration](https://www.dlnews.com/external/termmax-advances-institutional-defi-use-with-tokenized-stock-financing-integration/) 1 day ago [](https://www.dlnews.com/external/chainwire-and-cultd-partner-to-solve-the-web3-liquidity-vacuum-by-linking-media-reach-to-on-chain-impact/) [Chainwire and CULTD Partner to Solve the Web3 “Liquidity Vacuum” by Linking Media Reach to On-Chain Impact](https://www.dlnews.com/external/chainwire-and-cultd-partner-to-solve-the-web3-liquidity-vacuum-by-linking-media-reach-to-on-chain-impact/) 1 day ago [](https://www.dlnews.com/external/btcc-ends-2025-with-531-billion-in-tokenized-rwa-futures-volume-and-11m-users-despite-market-wide-volatility/) [BTCC Ends 2025 With $53.1 Billion in Tokenized RWA Futures Volume and 11M Users Despite Market-Wide Volatility](https://www.dlnews.com/external/btcc-ends-2025-with-531-billion-in-tokenized-rwa-futures-volume-and-11m-users-despite-market-wide-volatility/) 4 days ago [](https://www.dlnews.com/external/bcgame-releases-bear-smash-15000x-boost-featuring-single-tap-rounds-and-a-chance-of-15000x-win/) [BC.GAME Releases "Bear Smash: 15000X Boost" Featuring Single-Tap Rounds and a Chance of 15,000x Win](https://www.dlnews.com/external/bcgame-releases-bear-smash-15000x-boost-featuring-single-tap-rounds-and-a-chance-of-15000x-win/) 5 days ago [](https://www.dlnews.com/external/meet48-and-messari-publish-research-report-on-the-comprehensive-overview-of-meet48/) [MEET48 and Messari Publish Research Report on the Comprehensive Overview of MEET48](https://www.dlnews.com/external/meet48-and-messari-publish-research-report-on-the-comprehensive-overview-of-meet48/) 6 days ago [](https://www.dlnews.com/external/slotgpt-launches-a-new-ai-slot-platform-transforming-players-into-creators/) [SlotGPT launches a new AI slot platform transforming players into creators](https://www.dlnews.com/external/slotgpt-launches-a-new-ai-slot-platform-transforming-players-into-creators/) 7 days ago [](https://www.dlnews.com/external/lbank-unveils-advent-calendar-campaign-with-blackfort-mew-lc-and-shib-community-collaboration/) [LBank Unveils Advent Calendar Campaign With BlackFort, MEW, LC, and SHIB Community Collaboration](https://www.dlnews.com/external/lbank-unveils-advent-calendar-campaign-with-blackfort-mew-lc-and-shib-community-collaboration/) 7 days ago [](https://www.dlnews.com/external/cango-inc-secures-us105-million-investment-from-ewcl-to-accelerate-growth/) [Cango Inc. Secures US$10.5 Million Investment from EWCL to Accelerate Growth](https://www.dlnews.com/external/cango-inc-secures-us105-million-investment-from-ewcl-to-accelerate-growth/) 7 days ago [](https://www.dlnews.com/external/bitmine-immersion-bmnr-announces-eth-holdings-reach-411-million-tokens-and-total-crypto-and-total-cash-holdings-of-132-billion/) [Bitmine Immersion (BMNR) Announces ETH Holdings Reach 4.11 Million Tokens, and Total Crypto and Total Cash Holdings of $13.2 Billion](https://www.dlnews.com/external/bitmine-immersion-bmnr-announces-eth-holdings-reach-411-million-tokens-and-total-crypto-and-total-cash-holdings-of-132-billion/) 8 days ago [](https://www.dlnews.com/external/unchained-summit-announces-dubai-edition-scheduled-for-1st-2nd-may-2026/) [Unchained Summit Announces Dubai Edition Scheduled for 1st & 2nd May 2026](https://www.dlnews.com/external/unchained-summit-announces-dubai-edition-scheduled-for-1st-2nd-may-2026/) 8 days ago [](https://www.dlnews.com/external/meet48s-2026-roadshow-successfully-held-in-seoul-unveiling-multiple-products-to-lead-the-global-ai-web3-entertainment-industry/) [MEET48’s 2026 Roadshow Successfully Held in Seoul, Unveiling Multiple Products to Lead the Global AI + Web3 Entertainment Industry](https://www.dlnews.com/external/meet48s-2026-roadshow-successfully-held-in-seoul-unveiling-multiple-products-to-lead-the-global-ai-web3-entertainment-industry/) 9 days ago [](https://www.dlnews.com/external/phemex-upgrades-rpi-ecosystem-setting-new-liquidity-benchmarks-across-210-pairs/) [Phemex Upgrades RPI Ecosystem, Setting New Liquidity Benchmarks Across 210+ Pairs](https://www.dlnews.com/external/phemex-upgrades-rpi-ecosystem-setting-new-liquidity-benchmarks-across-210-pairs/) 11 days ago [](https://www.dlnews.com/external/crouton-digital-institutional-grade-blockchain-infrastructure-for-web3-ecosystems/) [Crouton Digital: Institutional-Grade Blockchain Infrastructure for Web3 Ecosystems](https://www.dlnews.com/external/crouton-digital-institutional-grade-blockchain-infrastructure-for-web3-ecosystems/) 11 days ago [](https://www.dlnews.com/external/tapbit-cares-marking-tapbits-4th-anniversary-with-a-year-end-christmas-csr-community-outreach-initiative/) [Tapbit Cares: Marking Tapbit’s 4th Anniversary with a Year-End Christmas CSR Community Outreach Initiative](https://www.dlnews.com/external/tapbit-cares-marking-tapbits-4th-anniversary-with-a-year-end-christmas-csr-community-outreach-initiative/) 12 days ago [](https://www.dlnews.com/external/rollercoin-named-game-of-the-year-and-best-browser-game-at-the-2025-blockchain-game-awards/) [RollerCoin Named Game of the Year and Best Browser Game at the 2025 Blockchain Game Awards](https://www.dlnews.com/external/rollercoin-named-game-of-the-year-and-best-browser-game-at-the-2025-blockchain-game-awards/) 14 days ago [](https://www.dlnews.com/external/thorchain-launches-native-cross-chain-swap-interface-in-public-beta/) [THORChain Launches Native Cross-Chain Swap Interface in Public Beta](https://www.dlnews.com/external/thorchain-launches-native-cross-chain-swap-interface-in-public-beta/) 14 days ago [](https://www.dlnews.com/external/solstice-and-cor-prime-execute-first-institutional-stablecoin-for-stablecoin-repo-on-a-public-blockchain/) [Solstice and Cor Prime Execute First Institutional Stablecoin-for-Stablecoin Repo on a Public Blockchain](https://www.dlnews.com/external/solstice-and-cor-prime-execute-first-institutional-stablecoin-for-stablecoin-repo-on-a-public-blockchain/) 14 days ago [](https://www.dlnews.com/external/valr-reflects-on-a-transformative-2025-for-crypto-and-finance/) [VALR Reflects on a Transformative 2025 for Crypto and Finance](https://www.dlnews.com/external/valr-reflects-on-a-transformative-2025-for-crypto-and-finance/) 14 days ago [](https://www.dlnews.com/external/bitmine-immersion-bmnr-announces-eth-holdings-reach-4066-million-tokens-and-total-crypto-and-total-cash-holdings-of-132-billion/) [Bitmine Immersion (BMNR) Announces ETH Holdings Reach 4.066 Million Tokens, and Total Crypto and Total Cash Holdings of $13.2 Billion](https://www.dlnews.com/external/bitmine-immersion-bmnr-announces-eth-holdings-reach-4066-million-tokens-and-total-crypto-and-total-cash-holdings-of-132-billion/) 15 days ago Powered by
[LATEST](https://www.dlnews.com/articles/) [](https://www.dlnews.com/articles/regulation/congress-bill-to-ban-government-officials-using-polymarket/) [Prediction markets? Not for politicians, says US congressman](https://www.dlnews.com/articles/regulation/congress-bill-to-ban-government-officials-using-polymarket/) 5 hours ago [](https://www.dlnews.com/articles/defi/what-defi-protocols-expect-in-2026/) [What DeFi protocols expect in 2026](https://www.dlnews.com/articles/defi/what-defi-protocols-expect-in-2026/) 6 hours ago [](https://www.dlnews.com/articles/regulation/cynthia-lummis-worried-over-btc-sales-from-samorai-wallet/) [Pro-crypto senator Cynthia Lummis worried over government’s reported Bitcoin sales](https://www.dlnews.com/articles/regulation/cynthia-lummis-worried-over-btc-sales-from-samorai-wallet/) 8 hours ago [](https://www.dlnews.com/articles/markets/russia-cbdc-launch-will-seriously-undermine-its-mir-cards/) [Russia’s digital ruble will undercut its own card payment system, says analyst](https://www.dlnews.com/articles/markets/russia-cbdc-launch-will-seriously-undermine-its-mir-cards/) 11 hours ago [OPINION](https://www.dlnews.com/articles/markets/why-borrowing-money-to-buy-bitcoin-is-stupid/) [](https://www.dlnews.com/articles/markets/why-borrowing-money-to-buy-bitcoin-is-stupid/) [Markets](https://www.dlnews.com/articles/markets/) [Opinion](https://www.dlnews.com/articles/opinion/) 
### Why borrowing money to buy Bitcoin is ‘downright stupid’
[Wolfgang Münchau](https://www.dlnews.com/authors/WolfgangMunchau/) 28 December 2025 [DON'T MISS](https://www.dlnews.com/articles/regulation/sec-democrat-caroline-crenshaw-exits/) [SEC’s lone Democratic commissioner and crypto skeptic Caroline Crenshaw to depart](https://www.dlnews.com/articles/regulation/sec-democrat-caroline-crenshaw-exits/) [Mathew Di Salvo](https://www.dlnews.com/authors/Mathew-DiSalvo/) 3 January 2026 [Bitcoin treasury slump deepens as 40% trade at discount: ‘It’s an abomination’](https://www.dlnews.com/articles/markets/bitcoin-treasury-blues-mount-as-40-percent-trade-at-discount/) [Pedro Solimano](https://www.dlnews.com/authors/Pedro-Solimano/) 2 January 2026 [Top 10 crypto fundraising rounds in 2025 — and what they mean for 2026](https://www.dlnews.com/articles/markets/top-10-crypto-fundraising-rounds-in-2025/) [Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 3 January 2026 [FEATURE OF THE WEEK](https://www.dlnews.com/articles/regulation/inside-do-kwons-sentencing/) [](https://www.dlnews.com/articles/regulation/inside-do-kwons-sentencing/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### Inside Do Kwon’s sentencing: ‘an extraordinary rise and fall’
[Aleks Gilbert](https://www.dlnews.com/authors/Aleks-Gilbert/) 20 December 2025 [TRENDING](https://www.dlnews.com/articles/markets/coinbase-wants-argentina-return-after-temporary-exit/) [Coinbase says it plans to return to Argentina ahead of ‘temporary’ exit](https://www.dlnews.com/articles/markets/coinbase-wants-argentina-return-after-temporary-exit/) [Tim Alper](https://www.dlnews.com/authors/Tim-Alper/) 4 January 2026 [Bitcoin prices unmoved by US’ Venezuela strikes – but experts warn of Monday market turbulence](https://www.dlnews.com/articles/markets/bitcoin-prices-unmoved-by-us-venezuela-strikes/) [Tim Alper](https://www.dlnews.com/authors/Tim-Alper/) 4 January 2026 [Bitcoin miner Bitfarms exits Latin America with $30m sale to focus on AI](https://www.dlnews.com/articles/regulation/bitfarms-exits-latam-paraguay-sale/) [Mathew Di Salvo](https://www.dlnews.com/authors/Mathew-DiSalvo/) 3 January 2026 [Bitcoin just had its least volatile year ever — here’s what 2026 will bring](https://www.dlnews.com/articles/regulation/bitcoin-least-volatile-year/) [Mathew Di Salvo](https://www.dlnews.com/authors/Mathew-DiSalvo/) 3 January 2026 
##### PRESS RELEASES
[](https://www.dlnews.com/external/cronos-brings-cro-staking-to-upbit-expanding-access-for-korean-users/) [Cronos Brings CRO Staking to Upbit, Expanding Access for Korean Users](https://www.dlnews.com/external/cronos-brings-cro-staking-to-upbit-expanding-access-for-korean-users/) 17 hours ago [](https://www.dlnews.com/external/termmax-advances-institutional-defi-use-with-tokenized-stock-financing-integration/) [TermMax Advances Institutional DeFi Use with Tokenized Stock Financing Integration](https://www.dlnews.com/external/termmax-advances-institutional-defi-use-with-tokenized-stock-financing-integration/) 1 day ago [](https://www.dlnews.com/external/chainwire-and-cultd-partner-to-solve-the-web3-liquidity-vacuum-by-linking-media-reach-to-on-chain-impact/) [Chainwire and CULTD Partner to Solve the Web3 “Liquidity Vacuum” by Linking Media Reach to On-Chain Impact](https://www.dlnews.com/external/chainwire-and-cultd-partner-to-solve-the-web3-liquidity-vacuum-by-linking-media-reach-to-on-chain-impact/) 1 day ago [](https://www.dlnews.com/external/btcc-ends-2025-with-531-billion-in-tokenized-rwa-futures-volume-and-11m-users-despite-market-wide-volatility/) [BTCC Ends 2025 With $53.1 Billion in Tokenized RWA Futures Volume and 11M Users Despite Market-Wide Volatility](https://www.dlnews.com/external/btcc-ends-2025-with-531-billion-in-tokenized-rwa-futures-volume-and-11m-users-despite-market-wide-volatility/) 4 days ago [](https://www.dlnews.com/external/bcgame-releases-bear-smash-15000x-boost-featuring-single-tap-rounds-and-a-chance-of-15000x-win/) [BC.GAME Releases "Bear Smash: 15000X Boost" Featuring Single-Tap Rounds and a Chance of 15,000x Win](https://www.dlnews.com/external/bcgame-releases-bear-smash-15000x-boost-featuring-single-tap-rounds-and-a-chance-of-15000x-win/) 5 days ago [](https://www.dlnews.com/external/meet48-and-messari-publish-research-report-on-the-comprehensive-overview-of-meet48/) [MEET48 and Messari Publish Research Report on the Comprehensive Overview of MEET48](https://www.dlnews.com/external/meet48-and-messari-publish-research-report-on-the-comprehensive-overview-of-meet48/) 6 days ago [](https://www.dlnews.com/external/slotgpt-launches-a-new-ai-slot-platform-transforming-players-into-creators/) [SlotGPT launches a new AI slot platform transforming players into creators](https://www.dlnews.com/external/slotgpt-launches-a-new-ai-slot-platform-transforming-players-into-creators/) 7 days ago [](https://www.dlnews.com/external/lbank-unveils-advent-calendar-campaign-with-blackfort-mew-lc-and-shib-community-collaboration/) [LBank Unveils Advent Calendar Campaign With BlackFort, MEW, LC, and SHIB Community Collaboration](https://www.dlnews.com/external/lbank-unveils-advent-calendar-campaign-with-blackfort-mew-lc-and-shib-community-collaboration/) 7 days ago [](https://www.dlnews.com/external/cango-inc-secures-us105-million-investment-from-ewcl-to-accelerate-growth/) [Cango Inc. Secures US$10.5 Million Investment from EWCL to Accelerate Growth](https://www.dlnews.com/external/cango-inc-secures-us105-million-investment-from-ewcl-to-accelerate-growth/) 7 days ago [](https://www.dlnews.com/external/bitmine-immersion-bmnr-announces-eth-holdings-reach-411-million-tokens-and-total-crypto-and-total-cash-holdings-of-132-billion/) [Bitmine Immersion (BMNR) Announces ETH Holdings Reach 4.11 Million Tokens, and Total Crypto and Total Cash Holdings of $13.2 Billion](https://www.dlnews.com/external/bitmine-immersion-bmnr-announces-eth-holdings-reach-411-million-tokens-and-total-crypto-and-total-cash-holdings-of-132-billion/) 8 days ago [](https://www.dlnews.com/external/unchained-summit-announces-dubai-edition-scheduled-for-1st-2nd-may-2026/) [Unchained Summit Announces Dubai Edition Scheduled for 1st & 2nd May 2026](https://www.dlnews.com/external/unchained-summit-announces-dubai-edition-scheduled-for-1st-2nd-may-2026/) 8 days ago [](https://www.dlnews.com/external/meet48s-2026-roadshow-successfully-held-in-seoul-unveiling-multiple-products-to-lead-the-global-ai-web3-entertainment-industry/) [MEET48’s 2026 Roadshow Successfully Held in Seoul, Unveiling Multiple Products to Lead the Global AI + Web3 Entertainment Industry](https://www.dlnews.com/external/meet48s-2026-roadshow-successfully-held-in-seoul-unveiling-multiple-products-to-lead-the-global-ai-web3-entertainment-industry/) 9 days ago [](https://www.dlnews.com/external/phemex-upgrades-rpi-ecosystem-setting-new-liquidity-benchmarks-across-210-pairs/) [Phemex Upgrades RPI Ecosystem, Setting New Liquidity Benchmarks Across 210+ Pairs](https://www.dlnews.com/external/phemex-upgrades-rpi-ecosystem-setting-new-liquidity-benchmarks-across-210-pairs/) 11 days ago [](https://www.dlnews.com/external/crouton-digital-institutional-grade-blockchain-infrastructure-for-web3-ecosystems/) [Crouton Digital: Institutional-Grade Blockchain Infrastructure for Web3 Ecosystems](https://www.dlnews.com/external/crouton-digital-institutional-grade-blockchain-infrastructure-for-web3-ecosystems/) 11 days ago [](https://www.dlnews.com/external/tapbit-cares-marking-tapbits-4th-anniversary-with-a-year-end-christmas-csr-community-outreach-initiative/) [Tapbit Cares: Marking Tapbit’s 4th Anniversary with a Year-End Christmas CSR Community Outreach Initiative](https://www.dlnews.com/external/tapbit-cares-marking-tapbits-4th-anniversary-with-a-year-end-christmas-csr-community-outreach-initiative/) 12 days ago [](https://www.dlnews.com/external/rollercoin-named-game-of-the-year-and-best-browser-game-at-the-2025-blockchain-game-awards/) [RollerCoin Named Game of the Year and Best Browser Game at the 2025 Blockchain Game Awards](https://www.dlnews.com/external/rollercoin-named-game-of-the-year-and-best-browser-game-at-the-2025-blockchain-game-awards/) 14 days ago [](https://www.dlnews.com/external/thorchain-launches-native-cross-chain-swap-interface-in-public-beta/) [THORChain Launches Native Cross-Chain Swap Interface in Public Beta](https://www.dlnews.com/external/thorchain-launches-native-cross-chain-swap-interface-in-public-beta/) 14 days ago [](https://www.dlnews.com/external/solstice-and-cor-prime-execute-first-institutional-stablecoin-for-stablecoin-repo-on-a-public-blockchain/) [Solstice and Cor Prime Execute First Institutional Stablecoin-for-Stablecoin Repo on a Public Blockchain](https://www.dlnews.com/external/solstice-and-cor-prime-execute-first-institutional-stablecoin-for-stablecoin-repo-on-a-public-blockchain/) 14 days ago [](https://www.dlnews.com/external/valr-reflects-on-a-transformative-2025-for-crypto-and-finance/) [VALR Reflects on a Transformative 2025 for Crypto and Finance](https://www.dlnews.com/external/valr-reflects-on-a-transformative-2025-for-crypto-and-finance/) 14 days ago [](https://www.dlnews.com/external/bitmine-immersion-bmnr-announces-eth-holdings-reach-4066-million-tokens-and-total-crypto-and-total-cash-holdings-of-132-billion/) [Bitmine Immersion (BMNR) Announces ETH Holdings Reach 4.066 Million Tokens, and Total Crypto and Total Cash Holdings of $13.2 Billion](https://www.dlnews.com/external/bitmine-immersion-bmnr-announces-eth-holdings-reach-4066-million-tokens-and-total-crypto-and-total-cash-holdings-of-132-billion/) 15 days ago Powered by
[LATEST](https://www.dlnews.com/articles/) [](https://www.dlnews.com/articles/regulation/congress-bill-to-ban-government-officials-using-polymarket/) [Prediction markets? Not for politicians, says US congressman](https://www.dlnews.com/articles/regulation/congress-bill-to-ban-government-officials-using-polymarket/) 5 hours ago [](https://www.dlnews.com/articles/defi/what-defi-protocols-expect-in-2026/) [What DeFi protocols expect in 2026](https://www.dlnews.com/articles/defi/what-defi-protocols-expect-in-2026/) 6 hours ago [](https://www.dlnews.com/articles/regulation/cynthia-lummis-worried-over-btc-sales-from-samorai-wallet/) [Pro-crypto senator Cynthia Lummis worried over government’s reported Bitcoin sales](https://www.dlnews.com/articles/regulation/cynthia-lummis-worried-over-btc-sales-from-samorai-wallet/) 8 hours ago [SNAPSHOT](https://www.dlnews.com/articles/markets/bitcoin-buyers-target-100000-by-the-end-january/) [](https://www.dlnews.com/articles/markets/bitcoin-buyers-target-100000-by-the-end-january/) [Markets](https://www.dlnews.com/articles/markets/) [Snapshot](https://www.dlnews.com/articles/snapshot/) 
### Bitcoin buyers target $100,000 by the end January. Here’s six reasons to be bullish
[Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 6 January 2026 [TOP STORIES](https://www.dlnews.com/articles/markets/lighter-token-rebounds-as-protocol-begins-buybacks-and-whales-buy-in/) [](https://www.dlnews.com/articles/markets/lighter-token-rebounds-as-protocol-begins-buybacks-and-whales-buy-in/) [Lighter token bounces 37% as protocol begins buybacks and whales buy in](https://www.dlnews.com/articles/markets/lighter-token-rebounds-as-protocol-begins-buybacks-and-whales-buy-in/) 6 January 2026 [](https://www.dlnews.com/articles/markets/third-of-bitcoin-vulnerable-to-quantum-attack-warns-coinbase/) [Third of Bitcoin vulnerable to quantum attack, warns Coinbase research chief](https://www.dlnews.com/articles/markets/third-of-bitcoin-vulnerable-to-quantum-attack-warns-coinbase/) 6 January 2026 [](https://www.dlnews.com/articles/markets/bitcoin-buyers-target-100000-by-the-end-january/) [Bitcoin buyers target $100,000 by the end January. Here’s six reasons to be bullish](https://www.dlnews.com/articles/markets/bitcoin-buyers-target-100000-by-the-end-january/) 6 January 2026 [](https://www.dlnews.com/articles/defi/ethereum-solved-the-blockchain-trilemma-per-vitalik-buterin/) [Ethereum ‘solved’ the blockchain trilemma: Vitalik](https://www.dlnews.com/articles/defi/ethereum-solved-the-blockchain-trilemma-per-vitalik-buterin/) 5 January 2026 [TRENDING](https://www.dlnews.com/articles/markets/bitcoin-prices-unmoved-by-us-venezuela-strikes/) [](https://www.dlnews.com/articles/markets/bitcoin-prices-unmoved-by-us-venezuela-strikes/) [Markets](https://www.dlnews.com/articles/markets/) 
### Bitcoin prices unmoved by US’ Venezuela strikes – but experts warn of Monday market turbulence
[Tim Alper](https://www.dlnews.com/authors/Tim-Alper/) 4 January 2026 [OPINION](https://www.dlnews.com/articles/markets/why-borrowing-money-to-buy-bitcoin-is-stupid/) [](https://www.dlnews.com/articles/markets/why-borrowing-money-to-buy-bitcoin-is-stupid/) [Markets](https://www.dlnews.com/articles/markets/) [Opinion](https://www.dlnews.com/articles/opinion/) 
### Why borrowing money to buy Bitcoin is ‘downright stupid’
[Wolfgang Münchau](https://www.dlnews.com/authors/WolfgangMunchau/) 28 December 2025 [FEATURE OF THE WEEK](https://www.dlnews.com/articles/regulation/inside-do-kwons-sentencing/) [](https://www.dlnews.com/articles/regulation/inside-do-kwons-sentencing/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### Inside Do Kwon’s sentencing: ‘an extraordinary rise and fall’
[Aleks Gilbert](https://www.dlnews.com/authors/Aleks-Gilbert/) [EDITOR'S PICK](https://www.dlnews.com/articles/markets/will-trump-venezuela-gambit-boost-bitcoin-price-in-2026/) [](https://www.dlnews.com/articles/markets/will-trump-venezuela-gambit-boost-bitcoin-price-in-2026/) [Markets](https://www.dlnews.com/articles/markets/) [Snapshot](https://www.dlnews.com/articles/snapshot/) 
### How Trump’s Venezuela gambit is seen to boost Bitcoin price in 2026
[Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 5 January 2026 [DON'T MISS](https://www.dlnews.com/articles/regulation/bitfarms-exits-latam-paraguay-sale/) [Bitcoin miner Bitfarms exits Latin America with $30m sale to focus on AI](https://www.dlnews.com/articles/regulation/bitfarms-exits-latam-paraguay-sale/) [Mathew Di Salvo](https://www.dlnews.com/authors/Mathew-DiSalvo/) 3 January 2026 [Bitcoin just had its least volatile year ever — here’s what 2026 will bring](https://www.dlnews.com/articles/regulation/bitcoin-least-volatile-year/) [Mathew Di Salvo](https://www.dlnews.com/authors/Mathew-DiSalvo/) 3 January 2026 [SEC’s lone Democratic commissioner and crypto skeptic Caroline Crenshaw to depart](https://www.dlnews.com/articles/regulation/sec-democrat-caroline-crenshaw-exits/) [Mathew Di Salvo](https://www.dlnews.com/authors/Mathew-DiSalvo/) 3 January 2026
</searchResult>


<searchResult>
[doc17]:
**RSS - DL News**
[The State of DeFi 2025 is out, see what’s next. Read more.](https://assets.dlnews.com/dlresearch/State-of-DeFi-2025.pdf) Search results
[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results
[](https://defillama.com/) [](https://www.dlnews.com/) 
##### RSS

(Really Simple Syndication) feeds offer another way to get DLnews.com content. Subscribe to our feeds to get the latest headlines, summaries and links back to full articles - formatted for your favorite feed reader and updated throughout the day.

## Terms & Conditions

We allow the use of DLnews.com RSS feeds for personal use in a news reader or as part of a non-commercial blog. We require proper format and attribution whenever DL News content is posted on your website, and we reserve the right to require that you cease distributing DLnews.com content. Please read the Terms and Conditions for complete instructions. Commercial use of the Service is prohibited without prior written permission from DL News which may be requested via email to: media@dlnews.com.

Articles
- All Articles
- DeFi
- Fintech/VC/Deals
- Llama U
- Markets
- People & Culture
- Regulation
- Web3
</searchResult>


<searchResult>
[doc18]:
**How privacy coins Firo and Zcash dodged Binance delisting ... - DL News**
Search results
[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results
[](https://defillama.com/) [](https://www.dlnews.com/) This article is more than one year old
[DeFi](https://www.dlnews.com/articles/defi/) [Regulation](https://www.dlnews.com/articles/regulation/) 
# How privacy coins Firo and Zcash dodged Binance delisting with novel transparency plan

![How privacy coins Firo and Zcash dodged Binance delisting with novel transparency plan](https://www.dlnews.com/resizer/v2/HFGEY6SR7VAL7CAG4QPON5C5MA.jpg?auth=74373f5a0fa5ad620605e5f16b9fb8761684915933c8ce648c419a5cc9ded95e&amp;width=1200&amp;height=675&amp;focal=825%2C540)
[DeFi](https://www.dlnews.com/articles/defi/) [Regulation](https://www.dlnews.com/articles/regulation/) Binance CEO Richard Teng is scrambling to withstand intense regulatory pressure on a number of fronts. Credit: Rita Fortunato/DL News
[Home](https://www.dlnews.com/) [DeFi](https://www.dlnews.com/articles/defi/) How privacy coins Firo and Zcash dodged Binance delisting with novel transparency plan By [Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 23 January 2024 at 11:49 Share
- Binance slapped several privacy coins with its monitor tag, stoking fears of fresh delistings.
- Firo and Zcash have staved off delisting worries with a newly-approved tech solution.
- It's not permanent, and given the current regulatory environment, anything could change.

Privacy coin enthusiasts can breathe a sigh of relief.

After Binance slapped a so-called monitoring tag on a slew of privacy coins earlier this month, many worried that assets like Zcash and Firo would soon be delisted.

Representatives from Zcash and Firo told DL News on Monday this wouldn’t happen.

For now, at least.

“While I prefer not to speculate on specific timelines, Binance’s approval for Zcash to implement the new address type seems to protect ZEC from immediate delisting,” Jason McGee, Zcash’s Binance liaison, told DL News.

“Although Binance hasn’t declared this a permanent fix, their willingness to adopt this change suggests an intention to collaborate on solutions with privacy coins, rather than resorting to immediate delisting.”

## Could change their minds

It’s a positive step, but McGee said, “there’s always the risk they change their minds.”

Binance did not immediately respond to requests for comment.

Reuben Yap, Firo’s project steward, was equally hesitant after disclosing the project also met Binance’s compliance requirements.

European Union lawmakers are close to finalising new anti-money laundering laws that could prohibit privacy coins, and a decision is expected within weeks. Yap said new regime or a change in investors’ risk appetite makes the status of privacy coins tenuous.

## Exchange-only addresses

Binance’s apparent decision to let the privacy coins stay listed appears to be a vote of confidence in a novel approach proposed by the issuers.

It’s a technical solution called “exchange-only” address types, which the Firo team developed last year.

Under the scheme, crypto exchanges wouldn’t be able to receive tokens for these projects unless the sending address is transparent. The exchange must be able to see the transaction history of its counterparties.

Zcash has two varieties of this solution: TEX Address and Traceable Unified Address. But Binance hasn’t indicated a preference for either.

This is sparking further discussion about which project should be implemented without precise guidance. “We’re still gauging the community’s preference,” McGee told DL News.

## Privacy-preserving technology

Critically, these changes would happen at the wallet level, he said, and not at the protocol level.

“The new address type does not alter the fundamental aspects of Zcash’s privacy-preserving technology,” McGee said.

In the meantime, all tokens added to Binance’s monitor list are still tagged. The monitor tag flags users on the exchange that the assets “are likely to have higher volatility and risks compared to other listed tokens.”

Users can start trading after answering four questions in the affirmative and admitting that any losses incurred from transactions are customers’ responsibility.

It’s unclear whether Binance’s monitoring tag will be removed next quarter or how long it will take for the company to implement the “exchange-only” technical solutions.

“Monitoring isn’t a delisting,” Yap said. “It’s a ‘warning.’ But they put us on warning because of non-compliance with laws.”

## Crypto rules around the world

Binance has come under enormous regulatory pressure in recent months.

In November, the company and its co-founder and CEO, Changpeng “CZ” Zhao, pleaded guilty to violating US banking law in connection with anti-money laundering violations. The company paid a $4.3 billion settlement and Zhao resigned as CEO.

In the meantime, OKX has already gone ahead and delisted these privacy coins and others.

With Europe’s sweeping Markets in Crypto Assets (MiCA) rules and new anti-money laundering laws soon coming into effect on the bloc, regulators are paying particular attention to privacy coins and crypto mixers.

“Right now, we have complied with all the requirements,” Yap told DL News. “But as MiCA comes closer, if there are additional guidelines, we may have to do additional things.”

For now, projects like Firo and Monero will remain in purgatory just a bit longer.

“No, this change does not mark the beginning of the end for privacy coins,” said McGee. “Rather, it represents the need for adaptability amidst evolving regulatory standards.”

Liam Kelly is DL News’ Berlin correspondent. Contact him at liam@dlnews.com.
Related Topics
[BINANCE](https://www.dlnews.com/topics/binance/) [CHANGPENG ZHAO](https://www.dlnews.com/topics/changpeng-zhao/) [MICA](https://www.dlnews.com/topics/mica/) [MONEY LAUNDERING](https://www.dlnews.com/topics/money-laundering/) You may also like
[](https://www.dlnews.com/articles/regulation/crypto-romance-fraud-is-poised-to-accelerate-in-2024/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### Crypto romance fraud is poised to accelerate in ‘severity and scope’ in 2024
[Callan Quinn](https://www.dlnews.com/authors/Callan-Quinn/) 8 January 2024 [](https://www.dlnews.com/articles/snapshot/sbf-will-not-face-second-trial-on-additional-charges/) [Snapshot](https://www.dlnews.com/articles/snapshot/) 
### US won’t try Sam Bankman-Fried second time on additional charges
[Mike Millard](https://www.dlnews.com/authors/Mike-Millard/) 31 December 2023 [](https://www.dlnews.com/articles/regulation/how-china-and-asian-nations-plan-to-regulate-crypto-in-2024/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### Fraud vs innovation: How Asia’s crypto watchdogs will struggle to strike a balance in 2024
[Callan Quinn](https://www.dlnews.com/authors/Callan-Quinn/) 31 December 2023 Related articles
[](https://www.dlnews.com/articles/defi/monero-and-zcash-liquidity-runs-dry-as-binance-may-delist/) [DeFi](https://www.dlnews.com/articles/defi/) 
### Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins
[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 12 January 2024 [](https://www.dlnews.com/articles/snapshot/five-charts-explain-trueusd-dollar-depeg-and-binance-role/) [Snapshot](https://www.dlnews.com/articles/snapshot/) 
### These five charts explain TrueUSD’s fall below its dollar peg — and Binance’s role in the move
[S. Sinclair](https://www.dlnews.com/authors/Sebastian-Sinclair/) , [A. McCarthy](https://www.dlnews.com/authors/adam-morgan/) 22 January 2024 [](https://www.dlnews.com/articles/snapshot/binance-inflows-have-surged-since-november-guilty-plea/) [Snapshot](https://www.dlnews.com/articles/snapshot/) 
### Binance trade resurgent since historic penalty, exit of Changpeng Zhao
[Mike Millard](https://www.dlnews.com/authors/Mike-Millard/) 21 January 2024 [](https://www.dlnews.com/articles/snapshot/how-pro-crypto-traders-can-arb-bitcoin-etfs/) [Snapshot](https://www.dlnews.com/articles/snapshot/) 
### How pro crypto traders can arb Bitcoin ETFs
[Thomas Carreras](https://www.dlnews.com/authors/Thomas-Carreras/) 17 January 2024
</searchResult>


<searchResult>
[doc19]:
**Monero and Zcash’s liquidity dries up as Binance eyes ... - DL News**
Search results
[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results
[](https://defillama.com/) [](https://www.dlnews.com/) This article is more than one year old
[DeFi](https://www.dlnews.com/articles/defi/) 
# Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins

![Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins](https://www.dlnews.com/resizer/v2/7YRQIT4UVZBNNFYVOQJOIX5BYA.jpg?auth=7b400c0363211c2a85babd8559211aaf467d35cd09d12a56e8509ba436046d2d&amp;width=1200&amp;height=675&amp;focal=2260%2C1507)
[DeFi](https://www.dlnews.com/articles/defi/) Liquidity in the privacy coins market is drying up. Credit: Shutterstock
[Home](https://www.dlnews.com/) [DeFi](https://www.dlnews.com/articles/defi/) Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins By [Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 12 January 2024 at 15:29 Share
- Regulatory pressure is spurring exchanges to delist or flag Monero and other privacy coins.
- A new low in liquidity is spurring Zcash and Firo to find a workaround.
- Issuers are hopeful they can reach an agreement with Binance.

Privacy coins are sinking.

Cryptocurrencies like Zcash and Monero are getting wrung out of the market as exchange after exchange moves to eliminate the assets from trading.

On January 5, crypto exchange OKX delisted several key privacy-centric trading pairs, stating they “do not fulfill our listing criteria.”

Last week, Binance added a so-called monitor tag to Monero, Zcash, Firo, and MobileCoin, suggesting it may also delist those tokens.

“Tokens with the Monitoring Tag are at risk of no longer meeting our listing criteria and being delisted from the platform,” the exchange wrote.

Reports on Reddit suggest that Binance’s lending program has already gone ahead and removed XMR from the list of available assets.

A quick scan of Binance confirms those reports. The exchange first added XMR as a collateral asset back in May 2022.

## Spooked investors

Though the delisting isn’t official, it still spooked investors.

Zcash has fallen almost 19% in the last week, and Monero has stumbled almost 3%.

The liquidity for privacy coins such as Monero (XMR) and Zcash (ZEC) has sunk to an all-time low, according to new data from analysts at Kaiko.

![Liquidity for popular privacy coins like Monero and Zcash has dried up.](https://www.dlnews.com/resizer/v2/B3Q3EWYYNBAFJK6FWDD4DWQWI4.png?auth=352a8632fd64845f5f9db9d964fef9f2e1e8dadf7f3c1c60fa3fa32535fdba52&amp;width=1440)

Liquidity for popular privacy coins like Monero and Zcash has dried up.

“Most businesses will not want to interact with privacy coins given their negative connotations,” Clara Medalie, Kaiko’s director of research, told DL News.

“Many exchanges are delisting privacy coins, which suggests that market makers don’t want to provide liquidity for them.”

Privacy coins can obfuscate users’ identities by hiding sender details and transaction history.

This makes them notoriously difficult to track, drawing scrutiny from regulators worldwide.

A core feature of the original crypto ethos, privacy coins also continue to command many investors’ attention. Monero and Zcash boast a combined market capitalization of $3.48 billion.

This position now appears to be at serious risk, experts say.

## Serious challenge

With $15 billion in daily trading volume, Binance’s dominance makes its action a serious challenge to the fortunes of these projects.

Binance doesn’t have much of a choice. After pleading guilty in November to violating US banking law and paying a $4 billion penalty, it’s required to implement stronger anti-money laundering and know-your-customer controls.

> ‘Binance was clear from the beginning that if we did not create an exchange-only address type, they would delist ZEC.’— Jason McGee

Moreover, in negotiations over the EU’s Anti-Money Laundering Regulation, lawmakers are discussing whether to ban privacy coins like Monero and Zcash.

## Fight is on

Now, the fight’s on to keep Binance from axing privacy coins altogether.

Some projects have devised a novel workaround to try and get the nod from Binance.

Others, such as Monero, refuse to comply with Binance’s requests, with members of its community lashing out against the exchange in December. A Monero representative did not reply to a request for comment.

## All-seeing crypto addresses

The workaround others are trying is called an “exchange-only” crypto address.

The idea is that users looking to move funds to an exchange would whip up a new transparent address, send private funds to this address, and then send those funds to the exchange-only address.

First proposed by the privacy project Firo last November – which is also on Binance’s chopping block – an exchange-only address can only receive funds from transparent addresses rather than their private, or so-called shielded, counterparts.

“They don’t want to receive shielded transactions,” Jason McGee, a committee member for Zcash Community Grants and the project’s Binance liaison, told DL News.

“Binance was clear from the beginning (early November) that if we did not create an exchange-only address type, they would delist ZEC.”

> ‘Binance doesn’t want to touch any funds from sources that have an unidentified send.’— Reuben Yap

Firo project steward Reuben Yap told DL News that Binance initially asked the project to remove all its privacy features. He said it couldn’t.

Binance is still mulling the proposed solution, say McGee and Yap. They are hopeful it will be accepted because it would let the exchange show regulators the history of a depositing address.

“Binance doesn’t want to touch any funds from sources that have an unidentified send,” Yap said.

Binance did not immediately respond to DL News’ request for comment.

Justin Ehrenhofer, the founder of a crypto sleuthing firm focused on difficult-to-trace transactions Moonstone Research, told DL News the Monero community wasn’t considering the exchange-only approach.

## Lots of discussion

In any event, the idea is generating some buzz.

“There has been a tremendous amount of discussion about this within the Zcash community,” Zooko Wilcox-O’Hearn, the CEO of Electric Coin Company, the firm developing Zcash, told DL News.

Yap told DL News that the exchange address solution is expected to launch in two weeks.

As to what Binance will do at that point, it’s anyone’s guess.

Liam Kelly is a Berlin-based DeFi Correspondent. Contact him at liam@dlnews.com or on Telegram at @Liam_Gallas.
Related Topics
[MONERO](https://www.dlnews.com/topics/monero/) [BINANCE](https://www.dlnews.com/topics/binance/) [OKX](https://www.dlnews.com/topics/okx/) You may also like
[](https://www.dlnews.com/articles/regulation/how-china-and-asian-nations-plan-to-regulate-crypto-in-2024/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### Fraud vs innovation: How Asia’s crypto watchdogs will struggle to strike a balance in 2024
[Callan Quinn](https://www.dlnews.com/authors/Callan-Quinn/) 31 December 2023 [](https://www.dlnews.com/articles/people-culture/dl-news-top-stories-featured-bitcoin-etfs-and-defi-heists/) [People & culture](https://www.dlnews.com/articles/people-culture/) [Regulation](https://www.dlnews.com/articles/regulation/) [DeFi](https://www.dlnews.com/articles/defi/) [Markets](https://www.dlnews.com/articles/markets/) 
### Bitcoin ETFs, regulators, and DeFi heists ruled crypto in 2023: Check out DL News’ top stories of the year
[Edward Robinson](https://www.dlnews.com/authors/edward-robinson/) 29 December 2023 [](https://www.dlnews.com/articles/regulation/the-crypto-court-cases-to-keep-an-eye-on-in-2024/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### Crypto court cases will heat up in 2024 — here are the ones to watch
[Joanna Wright](https://www.dlnews.com/authors/joannawright/) 25 December 2023 Related articles
[](https://www.dlnews.com/articles/regulation/eus-new-aml-rules-may-impact-uniswap-binance-and-monero/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### EU regulators flag new crypto risks and weigh rules that may impact Uniswap and Binance
[Inbar Preiss](https://www.dlnews.com/authors/Inbar-Preiss/) 2 June 2023 [](https://www.dlnews.com/articles/regulation/what-do-cybercriminals-do-with-stolen-crypto/) [Regulation](https://www.dlnews.com/articles/regulation/) [DeFi](https://www.dlnews.com/articles/defi/) 
### How hackers turn stolen crypto into cash
[Eric Johansson](https://www.dlnews.com/authors/eric-johansson/) 24 April 2023 [](https://www.dlnews.com/articles/regulation/crypto-romance-fraud-is-poised-to-accelerate-in-2024/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### Crypto romance fraud is poised to accelerate in ‘severity and scope’ in 2024
[Callan Quinn](https://www.dlnews.com/authors/Callan-Quinn/) 8 January 2024 [](https://www.dlnews.com/articles/snapshot/sbf-will-not-face-second-trial-on-additional-charges/) [Snapshot](https://www.dlnews.com/articles/snapshot/) 
### US won’t try Sam Bankman-Fried second time on additional charges
[Mike Millard](https://www.dlnews.com/authors/Mike-Millard/) 31 December 2023
</searchResult>



```

### Search Results

```
<searchResult>
[doc14]:
**Zcash price surge continues despite market turmoil – DL News**
Search results
[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results
[](https://defillama.com/) [](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) 
# Zcash price surge continues despite market turmoil

![Zcash price surge continues despite market turmoil](https://www.dlnews.com/resizer/v2/VKGYHYRAJVD6PEWJU4BR5AT47I.jpg?auth=facb23e8d4d3cdf24913a117bc6c07b4c60c1a15269474b2ff0a98d0dee16dd8&amp;width=1200&amp;height=675&amp;focal=825%2C540)
[Markets](https://www.dlnews.com/articles/markets/) Market instability hasn’t been able to stop Zcash’s remarkable rally. Illustration: Gwen P; Source: Shutterstock
[Home](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) Zcash price surge continues despite market turmoil By [Aleks Gilbert](https://www.dlnews.com/authors/Aleks-Gilbert/) 15 November 2025 at 17:29 Share
- Zcash has continued to climb despite a market slump triggered by mounting fears over Federal Reserve policy.
- The rally has been fueled by increasing interest in privacy-preserving technology and the creation of a Zcash-focused digital asset treasury.

Zcash, a privacy-focused cryptocurrency, has continued its astonishing rise this week, even as market turmoil has hammered most other major cryptocurrencies and the broader equities market.

The privacy coin has surged 35%, to $664, since Thursday. In that same span, Bitcoin has fallen 2%, to $95,800, and Ethereum has held relatively steady.

The week-over-week numbers are even more stark. Over the past seven days, Zcash is up 23%, while Bitcoin and Ethereum have fallen 6% and 7%, respectively.

Markets fell on Thursday over mounting fears the Federal Reserve would hold interest rates steady at a meeting next month.

The Fed’s rate cutting campaign has helped boost stock markets this year, and rate cuts are generally a boon to risk-on assets, such as crypto.

But traders are now pricing in a 44% chance the Fed cuts rates in December, according to CME’s FedWatch tool. That’s down from 66% a week ago and 94% last month.

The Zcash rally has been fueled by rising interest in privacy-preserving technology.

No cryptocurrency has performed as well as Zcash this year. It is up more than 1,000% in 2025. At the start of the month, it was the 33rd most valuable crypto asset in the world. Since then, it has surged to 12th place.

Monero, another privacy coin, has been the third-best performer in 2025, rising 125%.

In its recent State of Crypto report, venture capital giant Andreessen Horowitz said the crypto industry had seen multiple privacy milestones in 2025.

Among those milestones were the Ethereum Foundation’s launch of a new 47-member “Privacy Cluster,” Zcash’s new Zashi wallet, and an uptick in the usage of a privacy programming language created by Aztec, the developer of a privacy-focused layer 2 blockchain.

Aztec began selling its new token on Thursday via Uniswap’s Continuous Clearing Auction.

This week, Cameron and Tyler Winklevoss, the brothers behind US crypto exchange Gemini, launched a Zcash-focused digital asset treasury, Cypherpunk.

They purchased $50 million of the cryptocurrency on Wednesday, according to DefiLlama data.

“Privacy’s become a rare, vanishing commodity,” Tyler Winklevoss said on X. “We feel strongly that Zcash could become a meaningful percentage of Bitcoin’s market capitalisation just on the merits of it being a privacy hedge or insurance policy to Bitcoin’s transparency alone.”

Aleks Gilbert is DL News’ New York-based DeFi correspondent. You can reach him at aleks@dlnews.com.
Related articles
[](https://www.dlnews.com/articles/markets/winklevoss-twins-bet-on-zcash-with-new-treasury-firm/) [Markets](https://www.dlnews.com/articles/markets/) 
### Winklevoss twins bet on Zcash with new treasury firm targeting 5% supply of the privacy coin’s supply
[Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 13 November 2025 [](https://www.dlnews.com/articles/people-culture/zcash-foundation-shakes-up-leadership-amidst-zec-token-price-rally/) [People & culture](https://www.dlnews.com/articles/people-culture/) 
### Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% price rally
[Tim Craig](https://www.dlnews.com/authors/timcraig/) 12 November 2025 [](https://www.dlnews.com/articles/defi/how-privacy-coins-firo-and-zcash-dodged-binance-delisting/) [DeFi](https://www.dlnews.com/articles/defi/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### How privacy coins Firo and Zcash dodged Binance delisting with novel transparency plan
[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 23 January 2024 [](https://www.dlnews.com/articles/defi/monero-and-zcash-liquidity-runs-dry-as-binance-may-delist/) [DeFi](https://www.dlnews.com/articles/defi/) 
### Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins
[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 12 January 2024
</searchResult>


<searchResult>
[doc10]:
**Zcash surges tenfold as investors bet on privacy as ban looms**
Search results
[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results
[](https://defillama.com/) [](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) 
# Zcash surges tenfold as investors bet on privacy as ban looms

![Zcash surges tenfold as investors bet on privacy as ban looms](https://www.dlnews.com/resizer/v2/AXKQE4P3FVEXBDD3S5Z3UGLE2A.jpg?auth=cbd98be097214eb17e382cf72f728dfecbed43022b35af5f79b7b0a53414de76&amp;width=1200&amp;height=675&amp;focal=2500%2C1500)
[Markets](https://www.dlnews.com/articles/markets/) Privacy coins have surged in 2025. Source: Shutterstock. Credit: Shutterstock / Collagery
[Home](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) Zcash surges tenfold as investors bet on privacy as ban looms By [Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 3 November 2025 at 11:31 Share
- Zcash is surging.
- Social media influencers are generating hype around privacy coins.
- a16z highlights Zcash, Railgun as leading privacy protocols.

Zcash is skyrocketing.

One of crypto’s oldest privacy coins has surged over 1,000% this year to over $440 this past weekend as investors bet on privacy. It currently trades as the 33rd most valuable cryptocurrency in the world.

Zcash’s surging value “reflects a renewed interest in privacy,” Spencer Yang, managing partner at crypto-native advisory firm BlockSpaceForce, told DL News.

The new peak comes as the Electric Coin Company, the developers behind Zcash, announced an updated roadmap on October 31. The roadmap includes long-term funding and new privacy tools.

And it’s not just Zcash that’s cashing in. Monero is up over 120% this year while Dash is up nearly 300%.

Railgun, an Ethereum privacy tool recently mentioned in the Ethereum Foundation’s institutional launch note on X, is also up over 300%.

## Why Zcash?

But Zcash is the standout winner so far this year.

One reason for that is its opt-in privacy features, which “fit better than Monero with the current regulatory environment for privacy-based tokens,” Yang said.

“Zcash has also benefitted from promoters like Arthur Hayes, Mert Mumtaz, and Naval Ravikant openly coming out in its favour, whereas Monero hasn’t had that kind of attention,” he added.

In October, former BitMEX chief Arthur Hayes predicted Zcash will hit $10,000 in a viral post on X. He didn’t provide any further details on why he made that prediction and within what time-frames he was expecting Zcash to hit a milestone that even Ethereum, the world’s second biggest cryptocurrency, has yet to hit.

Popular YouTuber Mario Nawfal said that privacy projects “are making noise again” with “Monero, Zcash, and other privacy-focused tokens” in the spotlight.

Still, social media influencers are not the only ones plugged into the privacy trend.

In venture capital giant Andreessen Horowitz’s State of Crypto report, released in October, analysts said that the demand for privacy “is more urgent than ever” highlighting record figures for Zcash and Railgun.

## Privacy narrative

A16z cited multiple notable privacy milestones in 2025, including the Ethereum Foundation’s launch of a new 47-member “Privacy Cluster,” Zcash’s new Zashi wallet, and an uptick in the usage of privacy programming language Noir.

“Privacy is returning to the foreground and could be a prerequisite for wider adoption,” the report said.

“Google searches related to crypto privacy surged in 2025; Zcash’s shielded pool supply grew to nearly 4 million ZEC; and Railgun’s transaction flows surpassed $200 million monthly,” it stressed.

“Why are you not putting more money into privacy protocols?” Ethereum co-founder Vitalik Buterin asked an audience during a session at the Web3Privacy Now meetup in Tokyo in September.

## Under siege

To be sure, the waters are not entirely blue.

Zcash has lost some 15% of its value after reaching its all-time high market capitalisation this weekend and is worth $386 at the time of writing.

In 2024, the European Parliament voted through a bill that will ban listing tokens like Zcash and Monero. The argument was that the EU wanted to fight financial crimes such as money-laundering.

In response, crypto exchanges like Kraken and Binance have either delisted or considered delisting privacy coins in the EU.

The new EU rules are set to snap into action in 2027.

Looking beyond privacy coins, the same bill also sought to ban privacy mixers like Tornado Cash and to scale the policing of crypto transactions.

It’s clear that privacy-linked crypto projects are also under pressure around the world.

A Dutch court convicted Tornado Cash co-founder Alexey Pertsev of money laundering in 2024. Across the Atlantic, his fellow co-founder Roman Storm was convicted in the US in August of conspiracy to operate an unlicensed money-transmitting business. Both of them have appealed their verdicts.

The founders of a similar service, Keonne Rodriguez and William Lonergan Hill of Samourai Wallet, pleaded guilty to conspiracy to operate an unlicensed money-transmitting business in August.

Even so, the US Department of Justice has said it intends to reject similar charges going forward.

Mert Mumtaz, the CEO of Solana-infrastructure platform Helius Labs, and prominent promoter of Zcash, cited overzealous regulators as the best argument for privacy.

“The European Central Bank is working on the idea of ‘holding limits’ for ‘your’ money,” Mumtaz said on X. “They are going to control every aspect of your life soon. They think they own you. Use Bitcoin, use Zcash, use crypto. Reject these clowns.”

Lance Datskoluo is DL News’ Europe-based markets correspondent. Got a tip? Email at lance@dlnews.com.
Related Topics
[MONERO](https://www.dlnews.com/topics/monero/) You may also like
[](https://www.dlnews.com/articles/regulation/eus-new-aml-rules-may-impact-uniswap-binance-and-monero/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### EU regulators flag new crypto risks and weigh rules that may impact Uniswap and Binance
[Inbar Preiss](https://www.dlnews.com/authors/Inbar-Preiss/) 2 June 2023 [](https://www.dlnews.com/articles/markets/xrp-etf-launches-seen-to-trigger-billion-dollar-bonanza/) [Markets](https://www.dlnews.com/articles/markets/) 
### XRP ETF launches seen to trigger $5bn bonanza
[Eric Johansson](https://www.dlnews.com/authors/eric-johansson/) 3 November 2025 [](https://www.dlnews.com/articles/markets/us-solana-spot-etfs-seen-to-hit-5bn-in-inflows/) [Markets](https://www.dlnews.com/articles/markets/) 
### US Solana spot ETFs seen to hit $5bn in inflows: Grayscale exec
[Aleks Gilbert](https://www.dlnews.com/authors/Aleks-Gilbert/) 30 October 2025 Related articles
[](https://www.dlnews.com/articles/defi/monero-hashrate-tug-war-ease-qubic-lose-51-percent-dominance/) [DeFi](https://www.dlnews.com/articles/defi/) 
### Monero hashrate tug-of-war eases as Qubic loses 51% dominance
[Kyle Baird](https://www.dlnews.com/authors/kyle-baird/) 17 August 2025 [](https://www.dlnews.com/articles/markets/xmr-soars-as-suspected-hacker-purchases-millions-in-tokens/) [Markets](https://www.dlnews.com/articles/markets/) 
### Monero’s XMR soars as suspected hacker purchases $330m
[Tim Craig](https://www.dlnews.com/authors/timcraig/) 28 April 2025 [](https://www.dlnews.com/articles/regulation/why-the-eu-is-about-to-outlaw-and-curb-key-crypto-features/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### The EU is about to outlaw and restrict some of the most prized features in crypto
[Inbar Preiss](https://www.dlnews.com/authors/Inbar-Preiss/) 16 January 2024 [](https://www.dlnews.com/articles/defi/monero-and-zcash-liquidity-runs-dry-as-binance-may-delist/) [DeFi](https://www.dlnews.com/articles/defi/) 
### Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins
[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 12 January 2024
</searchResult>


<searchResult>
[doc13]:
**Zcash price primed for 45% breakout as Grayscale files for ETF**
Search results
[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results
[](https://defillama.com/) [](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) [Regulation](https://www.dlnews.com/articles/regulation/) 
# Zcash price primed for 45% breakout as Grayscale files for ETF

![Zcash price primed for 45% breakout as Grayscale files for ETF](https://www.dlnews.com/resizer/v2/VKGYHYRAJVD6PEWJU4BR5AT47I.jpg?auth=facb23e8d4d3cdf24913a117bc6c07b4c60c1a15269474b2ff0a98d0dee16dd8&amp;width=1200&amp;height=675&amp;focal=825%2C540)
[Markets](https://www.dlnews.com/articles/markets/) [Regulation](https://www.dlnews.com/articles/regulation/) Privacy token Zcash is ready to rip 45%, says Maria Carola, CEO of crypto exchange StealthEx. Illustration: Gwen P; Source: Shutterstock
[Home](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) Zcash price primed for 45% breakout as Grayscale files for ETF By [Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 27 November 2025 at 12:19 Share
- Grayscale is the latest Wall Street player to jump into Zcash.
- The Winklevoss twins launched a Zcash-based digital asset treasury firm earlier in November.

Privacy token Zcash is ready to rip 45%, says Maria Carola, CEO of crypto exchange StealthEx.

She argues that growing interest on Wall Street, most recently Grayscale’s exchange-traded fund filing on Wednesday, will propel the $8.3 billion crypto to new highs.

“A decisive break above $750 with sustained bullish momentum could open the path towards moving above $1,000 before the end of Q4,” Carola told DL News.

That would translate to Zcash’s price surging 45% above its current price of $515.
Zcash price over the past 6 months. 
Privacy coins are “operating with an entirely different playbook from the wider market,” Carola said. “They are benefiting from the long-suppressed demand for privacy-preserving tools and prevalent policy legislation in this direction.”

And Carola is far from the only one bullish on Zcash. She joins the ranks of BitMEX co-founder Arthur Hayes, popular YouTuber Mario Nawfal, and prominent Indian investor Naval Ravikant, who have all come out in support of Zcash.

A slew of investors have also told DL News that they expect Zcash to surge higher.

The bullishness comes as influential voices in the crypto community — such as Ethereum co-founder Vitalik Buterin — are increasingly calling for better privacy solutions.

## Grayscale shoots for ETF

The bullish projections come as Grayscale, the crypto asset manager that pioneered Wall Street products, files to transform its existing Zcash Trust product into a spot exchange-traded fund.

Grayscale’s registration statement submitted to the Securities and Exchange Commission on Wednesday would mark the launch of the first US spot ETF directly tracking Zcash. The move comes just days after it launched ETFs linked to XRP and Dogecoin.

The firm joins a growing number of major institutions that have come out supporting Zcash.

Venture capital giant Andreessen Horowitz and crypto investment manager Galaxy Digital have both noted the buzz around Zcash and other privacy-focused crypto projects like Monero and Railgun.

Cypherpunk, the crypto treasury company backed by twins Cameron and Tyler Winklevoss and launched earlier this month, has deployed over $50 million into Zcash.

As of November 19, Cypherpunk holds 1.43% of the total Zcash supply and is gunning for 5% ownership of all tokens.

## Privacy controversies

To be sure, not everyone backs privacy coins.

EU lawmakers have passed a bill to ban exchanges from listing tokens like Zcash and Monero, citing anti-money laundering concerns. The ban is set to take effect in 2027.

Regulators in the US and Europe are cracking down on developers of privacy tools.

In the Netherlands, Tornado Cash developer Alexey Pertsev was convicted of money laundering in 2024. Prosecutors said his code helped criminals conceal stolen crypto.

In the US, Tornado Cash co-founder Roman Storm was found guilty of running an unlicensed money-transmitting business. Samourai Wallet’s Keonne Rodriguez received the maximum five-year sentence for similar charges.

Lance Datskoluo is DL News’ Europe-based markets correspondent. Got a tip? Email at lance@dlnews.com.
Related Topics
[CRYPTO ETF](https://www.dlnews.com/topics/crypto-etf/) You may also like
[](https://www.dlnews.com/articles/defi/monero-and-zcash-liquidity-runs-dry-as-binance-may-delist/) [DeFi](https://www.dlnews.com/articles/defi/) 
### Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins
[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 12 January 2024 [](https://www.dlnews.com/articles/regulation/uk-fca-asks-stablecoin-firms-to-launch-in-sandbox/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### UK financial regulator asks stablecoin firms to launch in its ‘sandbox’ and help shape regulation
[Tim Craig](https://www.dlnews.com/authors/timcraig/) 26 November 2025 [](https://www.dlnews.com/articles/markets/bitcoin-holds-at-87000-but-do-not-expect-the-price-to-explode/) [Markets](https://www.dlnews.com/articles/markets/) [Snapshot](https://www.dlnews.com/articles/snapshot/) 
### Bitcoin holds at $87,000, but price won’t ‘explode’ to record heights anytime soon, analysts say
[Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 26 November 2025 Related articles
[](https://www.dlnews.com/articles/markets/zcash-price-surge-continues-despite-market-turmoil/) [Markets](https://www.dlnews.com/articles/markets/) 
### Zcash price surge continues despite market turmoil
[Aleks Gilbert](https://www.dlnews.com/authors/Aleks-Gilbert/) 15 November 2025 [](https://www.dlnews.com/articles/markets/winklevoss-twins-bet-on-zcash-with-new-treasury-firm/) [Markets](https://www.dlnews.com/articles/markets/) 
### Winklevoss twins bet on Zcash with new treasury firm targeting 5% supply of the privacy coin’s supply
[Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 13 November 2025 [](https://www.dlnews.com/articles/people-culture/zcash-foundation-shakes-up-leadership-amidst-zec-token-price-rally/) [People & culture](https://www.dlnews.com/articles/people-culture/) 
### Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% price rally
[Tim Craig](https://www.dlnews.com/authors/timcraig/) 12 November 2025 [](https://www.dlnews.com/articles/defi/how-privacy-coins-firo-and-zcash-dodged-binance-delisting/) [DeFi](https://www.dlnews.com/articles/defi/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### How privacy coins Firo and Zcash dodged Binance delisting with novel transparency plan
[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 23 January 2024
</searchResult>


<searchResult>
[doc12]:
**Why Zcash price is up 700% since September, according to Galaxy Digital**
Search results
[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results
[](https://defillama.com/) [](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) 
# Why Zcash price is up 700% since September, according to Galaxy Digital

![Why Zcash price is up 700% since September, according to Galaxy Digital](https://www.dlnews.com/resizer/v2/4LZLNM4GMNBZ5MZD6OV4FIKSTM.jpg?auth=a3defd4ed6225d27570a10ba09a26cfd164e8b689a28923262c81f8f3e212a08&amp;width=1200&amp;height=675&amp;focal=825%2C540)
[Markets](https://www.dlnews.com/articles/markets/) Monero is also up over 130% this year, while Dash is up 400%. Illustration: Gwen P; Source: Shutterstock
[Home](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) Why Zcash price is up 700% since September, according to Galaxy Digital By [Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 5 November 2025 at 10:24 Share
- Galaxy chalks up ZEC’s price action to new user tools and shifting attitudes.
- Critics say the bullish move is coordinated.
- Regulators around the world continue to crack down on privacy tech.

The price of Zcash is staging one of crypto’s most dramatic comebacks despite the market drawdown.

The 2016 Bitcoin fork created by computer security expert Zooko Wilcox has surged more than 700% since September and is trading at $430, thanks to real infrastructure progress and growing attention to privacy.

That’s according to a new report from Galaxy Digital, which said that over 30% of the Zcash supply is now hidden from the public eye in private pools — an all-time high for this particular stat.

The new Zashi wallet has also made private transactions simpler for users, research analyst Will Owens said, which also contributed to more users going private.

Owens added that cross-chain integrations now let users move funds between transparent and private networks while keeping their steps hidden.
Zcash price. 
The milestone marks an attitude shift in crypto, where privacy, once treated as a liability and attacked by state actors, is now being rebranded as a core feature to protect users.

It’s not just Zcash that’s doing well. Monero is up over 130% this year while Dash is up 400%, both significantly outperforming Bitcoin.

Railgun, a key Ethereum privacy tool recently mentioned in the Ethereum Foundation’s institutional launch, was also cited by Galaxy Digital as a core project.

> ‘Technically, Zcash’s fundamentals haven’t radically changed overnight.’— Galaxy Digital's Will Owens

## Old tech, new attention

To be sure, Owens acknowledged that some are sceptical.

Prominent voices are split on whether the price action is sustainable. Economist Lyn Alden called the move “a coordinated token pump,” warning traders against becoming “exit liquidity.”

But tech investor Naval Ravikant countered that Zcash represents a deeper truth about the future of money, writing that “transparent crypto won’t survive a government crackdown.”

Venture capital giant Andreessen Horowitz has also said that demand for privacy “is more urgent than ever,” highlighting record user metrics for Zcash and Railgun this year.

Horowitz’s venture firm a16z cited multiple notable privacy milestones in 2025, including the Ethereum Foundation’s launch of its new 47-member “Privacy Cluster” and an uptick in the usage of the privacy programming language Noir.

“Technically, Zcash’s fundamentals haven’t radically changed overnight,” Galaxy Digital said. “But the perception around the technology has. This rally is driven by both constant vocal support from some of crypto’s top voices and also a reminder of how important privacy is for permissionless money.”

Originally a Bitcoin fork, Zcash was designed to fix the privacy issue that the Satoshi 2008 whitepaper acknowledged.

Its zero-knowledge proof system, known as zk-SNARKs, allows users to validate transactions without revealing who sent what to whom.

By contrast, Bitcoin’s public ledger exposes transactions to public analysis.

## Still under fire

State actors are not relinquishing control just yet.

In 2024, the European Parliament voted through a bill that will ban listing tokens like Zcash and Monero on EU exchanges, with implementation expected in 2027. The argument is that the EU wants to fight financial crimes such as money laundering.

Cypto exchanges like Kraken and Binance have also either delisted or considered delisting privacy coins in the EU.

A Dutch court convicted the co-founder of privacy tool Tornado Cash, Alexey Pertsev, of money laundering in 2024. Across the Atlantic, his fellow co-founder, Roman Storm, was convicted in the US in August of conspiracy to operate an unlicensed money-transmitting business. Both of them have appealed their verdicts.

Meanwhile, some of the industry’s best-known privacy projects – mixers like Samourai and Wasabi – have been crippled by regulatory action, with founders arrested and charged.

Even so, the US Department of Justice has said it intends to reject similar cases going forward.

Lance Datskoluo is DL News’ Europe-based markets correspondent. Got a tip? Email at lance@dlnews.com.
</searchResult>


<searchResult>
[doc11]:
**Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% ...**
Search results
[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results
[](https://defillama.com/) [](https://www.dlnews.com/) [People & culture](https://www.dlnews.com/articles/people-culture/) 
# Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% price rally

![Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% price rally](https://www.dlnews.com/resizer/v2/QU7DVGZ6RZDOLPTI4RGVKIYZXA.jpg?auth=2226ced312593b426bce6cd78e8062945f6452955fcf8bfe16437d3fd5530a3f&amp;width=1200&amp;height=675&amp;focal=1787%2C1193)
[People & culture](https://www.dlnews.com/articles/people-culture/) The appointment aren't the first major change to the Zcash Foundation’s leadership in recent weeks. Credit: Shutterstock / Grey82
[Home](https://www.dlnews.com/) [People & culture](https://www.dlnews.com/articles/people-culture/) Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% price rally By [Tim Craig](https://www.dlnews.com/authors/timcraig/) 12 November 2025 at 12:20 Share
- Zcash Foundation appoints two new leaders.
- The foundation also got a new executive director earlier this month.
- The appointments come amid surging interest in crypto privacy projects.

The Zcash Foundation is shaking up its leadership.

On Tuesday, the nonprofit that supports the $7.7 billion privacy protocol announced two new appointments: Pili Guerra moves from engineering manager to head of engineering, and Danika Delano takes on the role of chief operating officer.

The foundation said the promotions reflect its commitment to promote from within and recognise the talent that’s been instrumental to its success.

It’s not the first major change to the Zcash Foundation’s leadership in recent weeks.

On November 1, the foundation’s board appointed Alex Bornstein as executive director. Bornstein stepped in as interim executive director in March.

Zcash is a blockchain protocol focused on privacy. It lets users send so-called shielded transactions, which hide transaction details by encrypting data. Users can also choose to send transparent transactions which are publicly viewable like those on Bitcoin or Ethereum.

The Zcash Foundation is a nonprofit that supports financial privacy infrastructure, primarily on Zcash.

The new appointees are very much at home with the open-source, privacy-first ethos of the Zcash Foundation.

Before joining the foundation in 2020, Guerra worked at the Tor Project, a non-profit that develops and maintains the Tor browser and its associated infrastructure. The Tor browser is used for anonymous web browsing, typically on the dark web.

She also worked at Red Hat, a firm that develops open-source software for businesses.

Delano also joined the Zcash Foundation in 2020. In her previous role as operations director she oversaw the foundation’s grant programmes, and organised Zcon, the foundation’s annual conference.

## 1,000% rally

The foundation’s leadership moves come as privacy-enhancing crypto projects experience a renaissance after years of investor apathy.

Zcash’s ZEC token has led the change, skyrocketing over 1,000% this year. The tokens of other crypto privacy projects, such as Monero and Railgun, have also soared.
Zcash's ZEC token has rallied over 1,000% this year. 
Galaxy Digital attributed Zcash’s rise to real infrastructure progress and growing attention to crypto privacy in a recent report.

Interest rose sharply last month when former BitMEX chief Arthur Hayes predicted the ZEC token will hit $10,000 in a viral post on X.

On November 7, the ZEC token hit a high of $723, its highest value since 2018. It has since given back some of its gains, and trades around $470.

Tim Craig is DL News’ Edinburgh-based DeFi Correspondent. Reach out with tips at tim@dlnews.com.
</searchResult>


<searchResult>
[doc15]:
**Winklevoss twins bet on Zcash with new treasury firm targeting 5% ...**
Search results
[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results
[](https://defillama.com/) [](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) 
# Winklevoss twins bet on Zcash with new treasury firm targeting 5% supply of the privacy coin’s supply

![Winklevoss twins bet on Zcash with new treasury firm targeting 5% supply of the privacy coin’s supply](https://www.dlnews.com/resizer/v2/VKGYHYRAJVD6PEWJU4BR5AT47I.jpg?auth=facb23e8d4d3cdf24913a117bc6c07b4c60c1a15269474b2ff0a98d0dee16dd8&amp;width=1200&amp;height=675&amp;focal=825%2C540)
[Markets](https://www.dlnews.com/articles/markets/) The Winklevi are rotating to Zcash. Illustration: Gwen P; Source: Shutterstock
[Home](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) Winklevoss twins bet on Zcash with new treasury firm targeting 5% supply of the privacy coin’s supply By [Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 13 November 2025 at 09:57 Share
- Gemini’s founders have launched a Zcash-based digital asset treasury firm.
- Cypherpunk already holds 203,775 ZEC and targets 5% of total supply.
- Winklevoss twins cite privacy as a top concern in the AI era.

The Winklevi are rotating to Zcash.

Cypherpunk, a brand new crypto treasury company backed by twins Cameron and Tyler Winklevoss, is deploying over $50 million into the Bitcoin fork. As of the launch on November 12, the firm already holds 203,775 of the privacy coins and is shooting for ownership 5% of total supply.

“Privacy’s become a rare, vanishing commodity,” Tyler Winklevoss said on X. “We feel strongly that Zcash could become a meaningful percentage of Bitcoin’s market capitalisation just on the merits of it being a privacy hedge or insurance policy to Bitcoin’s transparency alone.”

Cypherpunk’s launch marks one of the most high-profile bets yet that privacy will become the next flashpoint in crypto. The move comes as the Zcash Foundation is shaking up its leadership, and as state actors intensify crackdowns on privacy technology.

Zcash’s price has soared over 1,000% this year, and is trading at over $500. Venture capital giant Andreessen Horowitz and crypto investment manager Galaxy Digital have also noted the buzz around Zcash and other privacy-focused crypto projects.

The billionaire crypto investors are best known for buying 70,000 Bitcoin in 2013 at $150 and for founding the Gemini Space Station crypto exchange.

## ‘Separating Money and State’

Zcash creator Zooko Wilcox praised the moment on X. “Proud that Zcash has drawn people like [Will McEvoy, CIO of Cypherpunk] and the Winklevosses who are here for the right reasons.”

“Tyler Winklevoss just said something awesome about ‘separating money and state.’ Something like ‘Have we really done that? And the answer is no, unless you’re using Zcash’,” Wilcox said.

“If Bitcoin is digital gold, Zcash is encrypted bitcoin, or digital cash,” Tyler Winklevoss said.

“One is your store of value, the other is how you privately move your value,” he added. “We’ve been tracking this symbiosis for years and believe that now — as we enter the age of AI — is the right time to begin accumulating ZEC.”

Arthur Hayes, also a big Zcash bull, advised investors to self-custody their coins rather than leave it on centralised exchanges.

“If you hold $ZEC on a CEX, withdraw it to a self-custodial wallet and shield it,” he said on X.

“It’s one of the few 1,000x opportunities in crypto remaining,” Carter Razink, co-founder of blockchain commerce platform spree.Finance, told DL News.

## Battle over privacy

To be sure, not everyone is supportive of privacy coins.

EU lawmakers view private crypto as incompatible with laws designed to prevent money-laundering, terrorism financing, and other financial crimes.

They have approved a bill that will ban exchanges from listing privacy coins like Zcash and Monero, with implementation expected in 2027.

And high-profile criminal prosecutions in the US and Europe have targeted developers behind privacy-enabling blockchain solutions.

In the Netherlands, Alexey Pertsev, co-founder of Tornado Cash, was convicted of money laundering in 2024. Dutch prosecutors argued that the protocol enabled criminals to hide stolen funds. Pertsev denied wrongdoing, but the court ruled that building software that obscures transactions can itself constitute facilitation of laundering.

In the US, Tornado Cash co-founder Roman Storm was convicted of conspiring to operate an unlicensed money-transmitting business.

Another major case came last week when Samourai Wallet co-founder Keonne Rodriguez received the maximum five-year sentence for operating an unlicensed money-transmitting business. Prosecutors accused the project of “soliciting, encouraging, and inviting criminals” to use its privacy features.

Lance Datskoluo is DL News’ Europe-based markets correspondent. Got a tip? lance@dlnews.com.
Related Topics
[TORNADO CASH](https://www.dlnews.com/topics/tornado-cash/) You may also like
[](https://www.dlnews.com/articles/defi/tornado-cash-dev-roman-storm-asks-judge-to-toss-conviction/) [DeFi](https://www.dlnews.com/articles/defi/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### Tornado Cash dev Roman Storm asks judge to toss conviction
[Aleks Gilbert](https://www.dlnews.com/authors/Aleks-Gilbert/) 1 October 2025 [](https://www.dlnews.com/articles/defi/crypto-industry-calls-for-clarity-act-to-protect-defi-devs-after-tornado-cash-conviction/) [DeFi](https://www.dlnews.com/articles/defi/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### Crypto industry calls for new bill to protect DeFi devs following Tornado Cash founder conviction
[T. Craig](https://www.dlnews.com/authors/timcraig/) , [E. Johansson](https://www.dlnews.com/authors/eric-johansson/) 28 August 2025 [](https://www.dlnews.com/articles/regulation/devs-of-decentralised-protocols-wont-be-prosecuted-doj-says/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### Devs behind ‘truly decentralised’ protocols won’t face DoJ prosecution, official says
[Aleks Gilbert](https://www.dlnews.com/authors/Aleks-Gilbert/) 21 August 2025 Related articles
[](https://www.dlnews.com/articles/people-culture/zcash-foundation-shakes-up-leadership-amidst-zec-token-price-rally/) [People & culture](https://www.dlnews.com/articles/people-culture/) 
### Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% price rally
[Tim Craig](https://www.dlnews.com/authors/timcraig/) 12 November 2025 [](https://www.dlnews.com/articles/defi/how-privacy-coins-firo-and-zcash-dodged-binance-delisting/) [DeFi](https://www.dlnews.com/articles/defi/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### How privacy coins Firo and Zcash dodged Binance delisting with novel transparency plan
[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 23 January 2024 [](https://www.dlnews.com/articles/defi/monero-and-zcash-liquidity-runs-dry-as-binance-may-delist/) [DeFi](https://www.dlnews.com/articles/defi/) 
### Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins
[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 12 January 2024 [](https://www.dlnews.com/articles/markets/ethereum-doubles-down-on-privacy-as-devs-eye-post-tornado-future/) [Markets](https://www.dlnews.com/articles/markets/) [Snapshot](https://www.dlnews.com/articles/snapshot/) 
### Ethereum doubles down on privacy as devs eye post-Tornado future
[Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 9 October 2025
</searchResult>


<searchResult>
[doc19]:
**Monero and Zcash’s liquidity dries up as Binance eyes ... - DL News**
Search results
[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results
[](https://defillama.com/) [](https://www.dlnews.com/) This article is more than one year old
[DeFi](https://www.dlnews.com/articles/defi/) 
# Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins

![Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins](https://www.dlnews.com/resizer/v2/7YRQIT4UVZBNNFYVOQJOIX5BYA.jpg?auth=7b400c0363211c2a85babd8559211aaf467d35cd09d12a56e8509ba436046d2d&amp;width=1200&amp;height=675&amp;focal=2260%2C1507)
[DeFi](https://www.dlnews.com/articles/defi/) Liquidity in the privacy coins market is drying up. Credit: Shutterstock
[Home](https://www.dlnews.com/) [DeFi](https://www.dlnews.com/articles/defi/) Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins By [Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 12 January 2024 at 15:29 Share
- Regulatory pressure is spurring exchanges to delist or flag Monero and other privacy coins.
- A new low in liquidity is spurring Zcash and Firo to find a workaround.
- Issuers are hopeful they can reach an agreement with Binance.

Privacy coins are sinking.

Cryptocurrencies like Zcash and Monero are getting wrung out of the market as exchange after exchange moves to eliminate the assets from trading.

On January 5, crypto exchange OKX delisted several key privacy-centric trading pairs, stating they “do not fulfill our listing criteria.”

Last week, Binance added a so-called monitor tag to Monero, Zcash, Firo, and MobileCoin, suggesting it may also delist those tokens.

“Tokens with the Monitoring Tag are at risk of no longer meeting our listing criteria and being delisted from the platform,” the exchange wrote.

Reports on Reddit suggest that Binance’s lending program has already gone ahead and removed XMR from the list of available assets.

A quick scan of Binance confirms those reports. The exchange first added XMR as a collateral asset back in May 2022.

## Spooked investors

Though the delisting isn’t official, it still spooked investors.

Zcash has fallen almost 19% in the last week, and Monero has stumbled almost 3%.

The liquidity for privacy coins such as Monero (XMR) and Zcash (ZEC) has sunk to an all-time low, according to new data from analysts at Kaiko.

![Liquidity for popular privacy coins like Monero and Zcash has dried up.](https://www.dlnews.com/resizer/v2/B3Q3EWYYNBAFJK6FWDD4DWQWI4.png?auth=352a8632fd64845f5f9db9d964fef9f2e1e8dadf7f3c1c60fa3fa32535fdba52&amp;width=1440)

Liquidity for popular privacy coins like Monero and Zcash has dried up.

“Most businesses will not want to interact with privacy coins given their negative connotations,” Clara Medalie, Kaiko’s director of research, told DL News.

“Many exchanges are delisting privacy coins, which suggests that market makers don’t want to provide liquidity for them.”

Privacy coins can obfuscate users’ identities by hiding sender details and transaction history.

This makes them notoriously difficult to track, drawing scrutiny from regulators worldwide.

A core feature of the original crypto ethos, privacy coins also continue to command many investors’ attention. Monero and Zcash boast a combined market capitalization of $3.48 billion.

This position now appears to be at serious risk, experts say.

## Serious challenge

With $15 billion in daily trading volume, Binance’s dominance makes its action a serious challenge to the fortunes of these projects.

Binance doesn’t have much of a choice. After pleading guilty in November to violating US banking law and paying a $4 billion penalty, it’s required to implement stronger anti-money laundering and know-your-customer controls.

> ‘Binance was clear from the beginning that if we did not create an exchange-only address type, they would delist ZEC.’— Jason McGee

Moreover, in negotiations over the EU’s Anti-Money Laundering Regulation, lawmakers are discussing whether to ban privacy coins like Monero and Zcash.

## Fight is on

Now, the fight’s on to keep Binance from axing privacy coins altogether.

Some projects have devised a novel workaround to try and get the nod from Binance.

Others, such as Monero, refuse to comply with Binance’s requests, with members of its community lashing out against the exchange in December. A Monero representative did not reply to a request for comment.

## All-seeing crypto addresses

The workaround others are trying is called an “exchange-only” crypto address.

The idea is that users looking to move funds to an exchange would whip up a new transparent address, send private funds to this address, and then send those funds to the exchange-only address.

First proposed by the privacy project Firo last November – which is also on Binance’s chopping block – an exchange-only address can only receive funds from transparent addresses rather than their private, or so-called shielded, counterparts.

“They don’t want to receive shielded transactions,” Jason McGee, a committee member for Zcash Community Grants and the project’s Binance liaison, told DL News.

“Binance was clear from the beginning (early November) that if we did not create an exchange-only address type, they would delist ZEC.”

> ‘Binance doesn’t want to touch any funds from sources that have an unidentified send.’— Reuben Yap

Firo project steward Reuben Yap told DL News that Binance initially asked the project to remove all its privacy features. He said it couldn’t.

Binance is still mulling the proposed solution, say McGee and Yap. They are hopeful it will be accepted because it would let the exchange show regulators the history of a depositing address.

“Binance doesn’t want to touch any funds from sources that have an unidentified send,” Yap said.

Binance did not immediately respond to DL News’ request for comment.

Justin Ehrenhofer, the founder of a crypto sleuthing firm focused on difficult-to-trace transactions Moonstone Research, told DL News the Monero community wasn’t considering the exchange-only approach.

## Lots of discussion

In any event, the idea is generating some buzz.

“There has been a tremendous amount of discussion about this within the Zcash community,” Zooko Wilcox-O’Hearn, the CEO of Electric Coin Company, the firm developing Zcash, told DL News.

Yap told DL News that the exchange address solution is expected to launch in two weeks.

As to what Binance will do at that point, it’s anyone’s guess.

Liam Kelly is a Berlin-based DeFi Correspondent. Contact him at liam@dlnews.com or on Telegram at @Liam_Gallas.
Related Topics
[MONERO](https://www.dlnews.com/topics/monero/) [BINANCE](https://www.dlnews.com/topics/binance/) [OKX](https://www.dlnews.com/topics/okx/) You may also like
[](https://www.dlnews.com/articles/regulation/how-china-and-asian-nations-plan-to-regulate-crypto-in-2024/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### Fraud vs innovation: How Asia’s crypto watchdogs will struggle to strike a balance in 2024
[Callan Quinn](https://www.dlnews.com/authors/Callan-Quinn/) 31 December 2023 [](https://www.dlnews.com/articles/people-culture/dl-news-top-stories-featured-bitcoin-etfs-and-defi-heists/) [People & culture](https://www.dlnews.com/articles/people-culture/) [Regulation](https://www.dlnews.com/articles/regulation/) [DeFi](https://www.dlnews.com/articles/defi/) [Markets](https://www.dlnews.com/articles/markets/) 
### Bitcoin ETFs, regulators, and DeFi heists ruled crypto in 2023: Check out DL News’ top stories of the year
[Edward Robinson](https://www.dlnews.com/authors/edward-robinson/) 29 December 2023 [](https://www.dlnews.com/articles/regulation/the-crypto-court-cases-to-keep-an-eye-on-in-2024/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### Crypto court cases will heat up in 2024 — here are the ones to watch
[Joanna Wright](https://www.dlnews.com/authors/joannawright/) 25 December 2023 Related articles
[](https://www.dlnews.com/articles/regulation/eus-new-aml-rules-may-impact-uniswap-binance-and-monero/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### EU regulators flag new crypto risks and weigh rules that may impact Uniswap and Binance
[Inbar Preiss](https://www.dlnews.com/authors/Inbar-Preiss/) 2 June 2023 [](https://www.dlnews.com/articles/regulation/what-do-cybercriminals-do-with-stolen-crypto/) [Regulation](https://www.dlnews.com/articles/regulation/) [DeFi](https://www.dlnews.com/articles/defi/) 
### How hackers turn stolen crypto into cash
[Eric Johansson](https://www.dlnews.com/authors/eric-johansson/) 24 April 2023 [](https://www.dlnews.com/articles/regulation/crypto-romance-fraud-is-poised-to-accelerate-in-2024/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### Crypto romance fraud is poised to accelerate in ‘severity and scope’ in 2024
[Callan Quinn](https://www.dlnews.com/authors/Callan-Quinn/) 8 January 2024 [](https://www.dlnews.com/articles/snapshot/sbf-will-not-face-second-trial-on-additional-charges/) [Snapshot](https://www.dlnews.com/articles/snapshot/) 
### US won’t try Sam Bankman-Fried second time on additional charges
[Mike Millard](https://www.dlnews.com/authors/Mike-Millard/) 31 December 2023
</searchResult>


<searchResult>
[doc20]:
**Ika Announces EdDSA Signatures, Expanding Native Support to Solana ...**
Search results
[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results
[](https://defillama.com/) [](https://www.dlnews.com/) Press Release

# Ika Announces EdDSA Signatures, Expanding Native Support to Solana, Zcash, Cardano and More

![Ika Announces EdDSA Signatures, Expanding Native Support to Solana, Zcash, Cardano and More](https://www.dlnews.com/resizer/v2/JXXMCO4GXNFA3D7KHKRESQTTEM.jpg?auth=5f920b24b6018e22a513f1e256c223c2d79ed28d2309416032c0c01d4285d272&amp;width=1200&amp;height=675&amp;focal=608%2C358)
[Home](https://www.dlnews.com/) Ika Announces EdDSA Signatures, Expanding Native Support to Solana, Zcash, Cardano and More By Partner Content 4 December 2025 at 14:10 Share

Zug, Switzerland, December 4th, 2025, Chainwire

Ika, the fastest parallel MPC network, today announced a mainnet upgrade that enables EdDSA signatures directly from dWallets, significantly expanding Ika’s native cross-chain coverage to include Solana, Zcash, Cardano, Stellar, Near, and other EdDSA-based ecosystems.

This upgrade extends Ika’s core promise: natively control accounts and assets across chains without bridges, wrapping, custodians, or trusted signers, now across a broader set of networks where EdDSA is the standard.

> “EdDSA support is a major expansion of what dWallets can control natively,” said Omer Sadika, Co-Founder of Ika. “It brings zero-trust, programmable signing to some of the most important ecosystems in crypto, so developers can orchestrate real cross-chain actions with real native assets, governed by Ika dWallet technology.”

What This Upgrade Enables

Until now, Ika’s dWallets provided zero-trust signing and programmable control for major ecosystems, including Bitcoin and EVM-compatible networks with ECDSA signatures. With EdDSA enabled at the dWallet signing layer, builders can now create applications that:
- Control Solana accounts natively, enabling cross-chain trading, vaults, payments, and automation without wrapped assets.
- Coordinate Zcash-native actions under programmable dWallet policies, unlocking zero-trust custody and interoperability for the most prominent privacy-preserving cryptocurrency.
- Manage Cardano, Stellar, Near accounts with smart contract-governed access control, enabling organizational treasury workflows and institutional-grade policy enforcement.

In short: dWallets become natively multi-ecosystem signers, and enable a coordination layer for policy, composability, and execution logic.

Native Cross-Chain Control

Most cross-chain systems rely on bridges, message relays, wrappers, or trusted intermediaries. These approaches introduce risk (custody, exploits, governance capture) and limit composability.

Ika’s model is different: no bridging of assets is required. Instead, Ika enables native signing via dWallets, where transaction authorization is always enforced under zero-trust assumptions.

With EdDSA enabled, the same architecture now extends to chains where ECDSA is not supported and EdDSA has been adopted instead, dramatically expanding the surface area of what Ika dWallets can safely and directly orchestrate.

How EdDSA Works in Ika’s Zero-Trust Model

Ika’s security model is built on its 2PC-MPC cryptographic scheme.

dWallet signing splits authorization into two independent components:
- User share: held and authorized locally by the user
- Network share: operated by Ika’s decentralized network of MPC nodes

Both are required to produce a valid signature, and the full private key is never reconstructed. With this mainnet upgrade, that same model now supports EdDSA signing, bringing the benefits of Ika’s architecture (zero-trust, decentralization, scalability, sub-second performance, and programmable policy enforcement) to a wider set of chains.

Why It Matters for Builders and the Ecosystem

This upgrade expands the design space for applications that are only possible with Ika, including:

Universal accounts across ecosystems

One programmable signing primitive that can operate across EdDSA and non-EdDSA chains, operated with the same SDK and smart contract.

Cross-chain DeFi with native assets

Strategies can coordinate multiple ecosystems while keeping assets on their home chains. No wrapping, no “bridged liquidity.”

Programmable custody and access control

Rules are enforced at the signing layer: multi-party approvals, intent constraints, spending limits, automated risk controls, and organizational policy, secured cryptographically rather than contract-side permissions alone.

Chain abstraction that’s actually zero-trust

Users don’t “rent” their wallet to an app or provider. They co-authorize with the network under strict cryptographic guarantees.

Availability

The EdDSA-enabled signing upgrade is live on Ika mainnet, and supports dWallet-based signing for Solana, Zcash, Cardano, Stellar, Near, and additional EdDSA-compatible chains.

Developers can begin integrating EdDSA-enabled dWallet workflows immediately through Ika’s developer resources.

About Ika

Ika is the fastest parallel MPC network, offering sub-second latency, unprecedented scale and decentralization, and zero-trust security. As the premier choice for interoperability, decentralized custody, and chain abstraction, Ika is set to revolutionize digital asset security and multi-chain DeFi. Users can learn more here

Contact

Ika PR

pr@ika.xyz
Disclaimer: Chainwire is the source of this content. This Press Release is for informational purposes only. The information does not constitute investment advice or an offer to invest.
</searchResult>


<searchResult>
[doc18]:
**How privacy coins Firo and Zcash dodged Binance delisting ... - DL News**
Search results
[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results
[](https://defillama.com/) [](https://www.dlnews.com/) This article is more than one year old
[DeFi](https://www.dlnews.com/articles/defi/) [Regulation](https://www.dlnews.com/articles/regulation/) 
# How privacy coins Firo and Zcash dodged Binance delisting with novel transparency plan

![How privacy coins Firo and Zcash dodged Binance delisting with novel transparency plan](https://www.dlnews.com/resizer/v2/HFGEY6SR7VAL7CAG4QPON5C5MA.jpg?auth=74373f5a0fa5ad620605e5f16b9fb8761684915933c8ce648c419a5cc9ded95e&amp;width=1200&amp;height=675&amp;focal=825%2C540)
[DeFi](https://www.dlnews.com/articles/defi/) [Regulation](https://www.dlnews.com/articles/regulation/) Binance CEO Richard Teng is scrambling to withstand intense regulatory pressure on a number of fronts. Credit: Rita Fortunato/DL News
[Home](https://www.dlnews.com/) [DeFi](https://www.dlnews.com/articles/defi/) How privacy coins Firo and Zcash dodged Binance delisting with novel transparency plan By [Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 23 January 2024 at 11:49 Share
- Binance slapped several privacy coins with its monitor tag, stoking fears of fresh delistings.
- Firo and Zcash have staved off delisting worries with a newly-approved tech solution.
- It's not permanent, and given the current regulatory environment, anything could change.

Privacy coin enthusiasts can breathe a sigh of relief.

After Binance slapped a so-called monitoring tag on a slew of privacy coins earlier this month, many worried that assets like Zcash and Firo would soon be delisted.

Representatives from Zcash and Firo told DL News on Monday this wouldn’t happen.

For now, at least.

“While I prefer not to speculate on specific timelines, Binance’s approval for Zcash to implement the new address type seems to protect ZEC from immediate delisting,” Jason McGee, Zcash’s Binance liaison, told DL News.

“Although Binance hasn’t declared this a permanent fix, their willingness to adopt this change suggests an intention to collaborate on solutions with privacy coins, rather than resorting to immediate delisting.”

## Could change their minds

It’s a positive step, but McGee said, “there’s always the risk they change their minds.”

Binance did not immediately respond to requests for comment.

Reuben Yap, Firo’s project steward, was equally hesitant after disclosing the project also met Binance’s compliance requirements.

European Union lawmakers are close to finalising new anti-money laundering laws that could prohibit privacy coins, and a decision is expected within weeks. Yap said new regime or a change in investors’ risk appetite makes the status of privacy coins tenuous.

## Exchange-only addresses

Binance’s apparent decision to let the privacy coins stay listed appears to be a vote of confidence in a novel approach proposed by the issuers.

It’s a technical solution called “exchange-only” address types, which the Firo team developed last year.

Under the scheme, crypto exchanges wouldn’t be able to receive tokens for these projects unless the sending address is transparent. The exchange must be able to see the transaction history of its counterparties.

Zcash has two varieties of this solution: TEX Address and Traceable Unified Address. But Binance hasn’t indicated a preference for either.

This is sparking further discussion about which project should be implemented without precise guidance. “We’re still gauging the community’s preference,” McGee told DL News.

## Privacy-preserving technology

Critically, these changes would happen at the wallet level, he said, and not at the protocol level.

“The new address type does not alter the fundamental aspects of Zcash’s privacy-preserving technology,” McGee said.

In the meantime, all tokens added to Binance’s monitor list are still tagged. The monitor tag flags users on the exchange that the assets “are likely to have higher volatility and risks compared to other listed tokens.”

Users can start trading after answering four questions in the affirmative and admitting that any losses incurred from transactions are customers’ responsibility.

It’s unclear whether Binance’s monitoring tag will be removed next quarter or how long it will take for the company to implement the “exchange-only” technical solutions.

“Monitoring isn’t a delisting,” Yap said. “It’s a ‘warning.’ But they put us on warning because of non-compliance with laws.”

## Crypto rules around the world

Binance has come under enormous regulatory pressure in recent months.

In November, the company and its co-founder and CEO, Changpeng “CZ” Zhao, pleaded guilty to violating US banking law in connection with anti-money laundering violations. The company paid a $4.3 billion settlement and Zhao resigned as CEO.

In the meantime, OKX has already gone ahead and delisted these privacy coins and others.

With Europe’s sweeping Markets in Crypto Assets (MiCA) rules and new anti-money laundering laws soon coming into effect on the bloc, regulators are paying particular attention to privacy coins and crypto mixers.

“Right now, we have complied with all the requirements,” Yap told DL News. “But as MiCA comes closer, if there are additional guidelines, we may have to do additional things.”

For now, projects like Firo and Monero will remain in purgatory just a bit longer.

“No, this change does not mark the beginning of the end for privacy coins,” said McGee. “Rather, it represents the need for adaptability amidst evolving regulatory standards.”

Liam Kelly is DL News’ Berlin correspondent. Contact him at liam@dlnews.com.
Related Topics
[BINANCE](https://www.dlnews.com/topics/binance/) [CHANGPENG ZHAO](https://www.dlnews.com/topics/changpeng-zhao/) [MICA](https://www.dlnews.com/topics/mica/) [MONEY LAUNDERING](https://www.dlnews.com/topics/money-laundering/) You may also like
[](https://www.dlnews.com/articles/regulation/crypto-romance-fraud-is-poised-to-accelerate-in-2024/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### Crypto romance fraud is poised to accelerate in ‘severity and scope’ in 2024
[Callan Quinn](https://www.dlnews.com/authors/Callan-Quinn/) 8 January 2024 [](https://www.dlnews.com/articles/snapshot/sbf-will-not-face-second-trial-on-additional-charges/) [Snapshot](https://www.dlnews.com/articles/snapshot/) 
### US won’t try Sam Bankman-Fried second time on additional charges
[Mike Millard](https://www.dlnews.com/authors/Mike-Millard/) 31 December 2023 [](https://www.dlnews.com/articles/regulation/how-china-and-asian-nations-plan-to-regulate-crypto-in-2024/) [Regulation](https://www.dlnews.com/articles/regulation/) 
### Fraud vs innovation: How Asia’s crypto watchdogs will struggle to strike a balance in 2024
[Callan Quinn](https://www.dlnews.com/authors/Callan-Quinn/) 31 December 2023 Related articles
[](https://www.dlnews.com/articles/defi/monero-and-zcash-liquidity-runs-dry-as-binance-may-delist/) [DeFi](https://www.dlnews.com/articles/defi/) 
### Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins
[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 12 January 2024 [](https://www.dlnews.com/articles/snapshot/five-charts-explain-trueusd-dollar-depeg-and-binance-role/) [Snapshot](https://www.dlnews.com/articles/snapshot/) 
### These five charts explain TrueUSD’s fall below its dollar peg — and Binance’s role in the move
[S. Sinclair](https://www.dlnews.com/authors/Sebastian-Sinclair/) , [A. McCarthy](https://www.dlnews.com/authors/adam-morgan/) 22 January 2024 [](https://www.dlnews.com/articles/snapshot/binance-inflows-have-surged-since-november-guilty-plea/) [Snapshot](https://www.dlnews.com/articles/snapshot/) 
### Binance trade resurgent since historic penalty, exit of Changpeng Zhao
[Mike Millard](https://www.dlnews.com/authors/Mike-Millard/) 21 January 2024 [](https://www.dlnews.com/articles/snapshot/how-pro-crypto-traders-can-arb-bitcoin-etfs/) [Snapshot](https://www.dlnews.com/articles/snapshot/) 
### How pro crypto traders can arb Bitcoin ETFs
[Thomas Carreras](https://www.dlnews.com/authors/Thomas-Carreras/) 17 January 2024
</searchResult>


<searchResult>
[doc21]:
**ZKasino’s year-long silence on investor refunds ends in a $27m ...**
Search results
[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results
[](https://defillama.com/) [](https://www.dlnews.com/) This article is more than nine months old
[DeFi](https://www.dlnews.com/articles/defi/) 
# ZKasino’s year-long silence on investor refunds ends in a $27m liquidation

![ZKasino’s year-long silence on investor refunds ends in a $27m liquidation](https://www.dlnews.com/resizer/v2/ZS5NXYIEPNAMTAGOEH3NCO5T4U.png?auth=85421f7b5da98f78e9f8dac4e9091964f73f1be6ef1f092776d84b8c3c56a3b5&amp;width=1200&amp;height=675&amp;focal=825%2C540)
[DeFi](https://www.dlnews.com/articles/defi/) ZKasino was launched last April as a flashy, onchain gambling project. It attracted over $40 million in Ethereum from investors who were promised yield on top of their deposits. Credit: Darren Joseph
[Home](https://www.dlnews.com/) [DeFi](https://www.dlnews.com/articles/defi/) ZKasino’s year-long silence on investor refunds ends in a $27m liquidation By [Osato Avan-Nomayo](https://www.dlnews.com/authors/Osato-Avan-Nomayo/) 7 April 2025 at 20:14 Share
- A ZKasino-linked wallet liquidated for $27 million.
- Investors have been waiting for a refund since last year.
- The crypto market lost over $240 billion overnight.

A crypto wallet linked to ZKasino, the crypto gambling platform that disappeared last year with $40 million in investor funds, got liquidated for over $27 million during Sunday’s crypto wipeout.

The wallet, which had been sitting on a high-risk Ethereum position since last month, finally tipped over as Ethereum plunged below $1,500 — its lowest price in two years.

ZKasino’s liquidation was just one among many. As panic rippled through the markets, leveraged positions across DeFi began to unwind. One major trader, unrelated to ZKasino, lost $74 million in the same cascade. Others narrowly avoided liquidation by rushing to reinforce their collateral as prices plunged.

Whoever was still gambling with ZKasino’s stolen funds was forced to close the position — but not before being margin-called into oblivion and losing $27 million in the process.

That may have been a darkly poetic end to a year-long saga for ZKasino. But for investors, there’s little consolation. Instead of the refunds they were promised, they’ve endured silence, stalling, and now, the final flush of whatever was left.

ZKasino was launched last April as a flashy, onchain gambling project. It attracted over $40 million in Ethereum from investors who were promised yield on top of their deposits.

But instead of payouts a month later, the project changed course and said it would swap Ethereum deposits for its native cryptocurrency called ZKAS. The project called the swap “a favour” for early investors.

However, investors were not pleased with the change as it meant they would not be able to redeem their investments in full as they were initially promised.

ZKasino then converted $30 million in user deposits into Lido’s Wrapped Staked Ether and began earning staking yield on the funds while investors were left in limbo.

Then came allegations of a rug pull ― a form of crypto crime where team members disappear with pooled funds, leaving investors in the lurch.

Dutch authorities eventually stepped in and arrested a man in connection with the alleged scam.

ZKasino denied the allegations and eventually converted the funds back to Ethereum, announcing a vague repayment plan. But nearly a year later, nothing has been paid back.

Now, with the liquidation of the last major wallet, that plan looks as precarious as the promises behind it.

Osato Avan-Nomayo is our Nigeria-based DeFi correspondent. He covers DeFi and tech. Got a tip? Please contact him at osato@dlnews.com.
</searchResult>



```

03:15:58.663 - Returning data from tool calls

03:15:58.663 - Submitting tool outputs to Assistants API


### Tool Outputs

```json

[
  {
    "ToolCallId": "call_3i6gmzupdYHlTkJjsGnBzSrt",
    "Output": "<searchResult>\n[doc14]:\n**Zcash price surge continues despite market turmoil – DL News**\nSearch results\n[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results\n[](https://defillama.com/) [](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) \n# Zcash price surge continues despite market turmoil\n\n![Zcash price surge continues despite market turmoil](https://www.dlnews.com/resizer/v2/VKGYHYRAJVD6PEWJU4BR5AT47I.jpg?auth=facb23e8d4d3cdf24913a117bc6c07b4c60c1a15269474b2ff0a98d0dee16dd8&amp;width=1200&amp;height=675&amp;focal=825%2C540)\n[Markets](https://www.dlnews.com/articles/markets/) Market instability hasn’t been able to stop Zcash’s remarkable rally. Illustration: Gwen P; Source: Shutterstock\n[Home](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) Zcash price surge continues despite market turmoil By [Aleks Gilbert](https://www.dlnews.com/authors/Aleks-Gilbert/) 15 November 2025 at 17:29 Share\n- Zcash has continued to climb despite a market slump triggered by mounting fears over Federal Reserve policy.\n- The rally has been fueled by increasing interest in privacy-preserving technology and the creation of a Zcash-focused digital asset treasury.\n\nZcash, a privacy-focused cryptocurrency, has continued its astonishing rise this week, even as market turmoil has hammered most other major cryptocurrencies and the broader equities market.\n\nThe privacy coin has surged 35%, to $664, since Thursday. In that same span, Bitcoin has fallen 2%, to $95,800, and Ethereum has held relatively steady.\n\nThe week-over-week numbers are even more stark. Over the past seven days, Zcash is up 23%, while Bitcoin and Ethereum have fallen 6% and 7%, respectively.\n\nMarkets fell on Thursday over mounting fears the Federal Reserve would hold interest rates steady at a meeting next month.\n\nThe Fed’s rate cutting campaign has helped boost stock markets this year, and rate cuts are generally a boon to risk-on assets, such as crypto.\n\nBut traders are now pricing in a 44% chance the Fed cuts rates in December, according to CME’s FedWatch tool. That’s down from 66% a week ago and 94% last month.\n\nThe Zcash rally has been fueled by rising interest in privacy-preserving technology.\n\nNo cryptocurrency has performed as well as Zcash this year. It is up more than 1,000% in 2025. At the start of the month, it was the 33rd most valuable crypto asset in the world. Since then, it has surged to 12th place.\n\nMonero, another privacy coin, has been the third-best performer in 2025, rising 125%.\n\nIn its recent State of Crypto report, venture capital giant Andreessen Horowitz said the crypto industry had seen multiple privacy milestones in 2025.\n\nAmong those milestones were the Ethereum Foundation’s launch of a new 47-member “Privacy Cluster,” Zcash’s new Zashi wallet, and an uptick in the usage of a privacy programming language created by Aztec, the developer of a privacy-focused layer 2 blockchain.\n\nAztec began selling its new token on Thursday via Uniswap’s Continuous Clearing Auction.\n\nThis week, Cameron and Tyler Winklevoss, the brothers behind US crypto exchange Gemini, launched a Zcash-focused digital asset treasury, Cypherpunk.\n\nThey purchased $50 million of the cryptocurrency on Wednesday, according to DefiLlama data.\n\n“Privacy’s become a rare, vanishing commodity,” Tyler Winklevoss said on X. “We feel strongly that Zcash could become a meaningful percentage of Bitcoin’s market capitalisation just on the merits of it being a privacy hedge or insurance policy to Bitcoin’s transparency alone.”\n\nAleks Gilbert is DL News’ New York-based DeFi correspondent. You can reach him at aleks@dlnews.com.\nRelated articles\n[](https://www.dlnews.com/articles/markets/winklevoss-twins-bet-on-zcash-with-new-treasury-firm/) [Markets](https://www.dlnews.com/articles/markets/) \n### Winklevoss twins bet on Zcash with new treasury firm targeting 5% supply of the privacy coin’s supply\n[Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 13 November 2025 [](https://www.dlnews.com/articles/people-culture/zcash-foundation-shakes-up-leadership-amidst-zec-token-price-rally/) [People & culture](https://www.dlnews.com/articles/people-culture/) \n### Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% price rally\n[Tim Craig](https://www.dlnews.com/authors/timcraig/) 12 November 2025 [](https://www.dlnews.com/articles/defi/how-privacy-coins-firo-and-zcash-dodged-binance-delisting/) [DeFi](https://www.dlnews.com/articles/defi/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### How privacy coins Firo and Zcash dodged Binance delisting with novel transparency plan\n[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 23 January 2024 [](https://www.dlnews.com/articles/defi/monero-and-zcash-liquidity-runs-dry-as-binance-may-delist/) [DeFi](https://www.dlnews.com/articles/defi/) \n### Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins\n[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 12 January 2024\n</searchResult>\n\n\n<searchResult>\n[doc10]:\n**Zcash surges tenfold as investors bet on privacy as ban looms**\nSearch results\n[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results\n[](https://defillama.com/) [](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) \n# Zcash surges tenfold as investors bet on privacy as ban looms\n\n![Zcash surges tenfold as investors bet on privacy as ban looms](https://www.dlnews.com/resizer/v2/AXKQE4P3FVEXBDD3S5Z3UGLE2A.jpg?auth=cbd98be097214eb17e382cf72f728dfecbed43022b35af5f79b7b0a53414de76&amp;width=1200&amp;height=675&amp;focal=2500%2C1500)\n[Markets](https://www.dlnews.com/articles/markets/) Privacy coins have surged in 2025. Source: Shutterstock. Credit: Shutterstock / Collagery\n[Home](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) Zcash surges tenfold as investors bet on privacy as ban looms By [Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 3 November 2025 at 11:31 Share\n- Zcash is surging.\n- Social media influencers are generating hype around privacy coins.\n- a16z highlights Zcash, Railgun as leading privacy protocols.\n\nZcash is skyrocketing.\n\nOne of crypto’s oldest privacy coins has surged over 1,000% this year to over $440 this past weekend as investors bet on privacy. It currently trades as the 33rd most valuable cryptocurrency in the world.\n\nZcash’s surging value “reflects a renewed interest in privacy,” Spencer Yang, managing partner at crypto-native advisory firm BlockSpaceForce, told DL News.\n\nThe new peak comes as the Electric Coin Company, the developers behind Zcash, announced an updated roadmap on October 31. The roadmap includes long-term funding and new privacy tools.\n\nAnd it’s not just Zcash that’s cashing in. Monero is up over 120% this year while Dash is up nearly 300%.\n\nRailgun, an Ethereum privacy tool recently mentioned in the Ethereum Foundation’s institutional launch note on X, is also up over 300%.\n\n## Why Zcash?\n\nBut Zcash is the standout winner so far this year.\n\nOne reason for that is its opt-in privacy features, which “fit better than Monero with the current regulatory environment for privacy-based tokens,” Yang said.\n\n“Zcash has also benefitted from promoters like Arthur Hayes, Mert Mumtaz, and Naval Ravikant openly coming out in its favour, whereas Monero hasn’t had that kind of attention,” he added.\n\nIn October, former BitMEX chief Arthur Hayes predicted Zcash will hit $10,000 in a viral post on X. He didn’t provide any further details on why he made that prediction and within what time-frames he was expecting Zcash to hit a milestone that even Ethereum, the world’s second biggest cryptocurrency, has yet to hit.\n\nPopular YouTuber Mario Nawfal said that privacy projects “are making noise again” with “Monero, Zcash, and other privacy-focused tokens” in the spotlight.\n\nStill, social media influencers are not the only ones plugged into the privacy trend.\n\nIn venture capital giant Andreessen Horowitz’s State of Crypto report, released in October, analysts said that the demand for privacy “is more urgent than ever” highlighting record figures for Zcash and Railgun.\n\n## Privacy narrative\n\nA16z cited multiple notable privacy milestones in 2025, including the Ethereum Foundation’s launch of a new 47-member “Privacy Cluster,” Zcash’s new Zashi wallet, and an uptick in the usage of privacy programming language Noir.\n\n“Privacy is returning to the foreground and could be a prerequisite for wider adoption,” the report said.\n\n“Google searches related to crypto privacy surged in 2025; Zcash’s shielded pool supply grew to nearly 4 million ZEC; and Railgun’s transaction flows surpassed $200 million monthly,” it stressed.\n\n“Why are you not putting more money into privacy protocols?” Ethereum co-founder Vitalik Buterin asked an audience during a session at the Web3Privacy Now meetup in Tokyo in September.\n\n## Under siege\n\nTo be sure, the waters are not entirely blue.\n\nZcash has lost some 15% of its value after reaching its all-time high market capitalisation this weekend and is worth $386 at the time of writing.\n\nIn 2024, the European Parliament voted through a bill that will ban listing tokens like Zcash and Monero. The argument was that the EU wanted to fight financial crimes such as money-laundering.\n\nIn response, crypto exchanges like Kraken and Binance have either delisted or considered delisting privacy coins in the EU.\n\nThe new EU rules are set to snap into action in 2027.\n\nLooking beyond privacy coins, the same bill also sought to ban privacy mixers like Tornado Cash and to scale the policing of crypto transactions.\n\nIt’s clear that privacy-linked crypto projects are also under pressure around the world.\n\nA Dutch court convicted Tornado Cash co-founder Alexey Pertsev of money laundering in 2024. Across the Atlantic, his fellow co-founder Roman Storm was convicted in the US in August of conspiracy to operate an unlicensed money-transmitting business. Both of them have appealed their verdicts.\n\nThe founders of a similar service, Keonne Rodriguez and William Lonergan Hill of Samourai Wallet, pleaded guilty to conspiracy to operate an unlicensed money-transmitting business in August.\n\nEven so, the US Department of Justice has said it intends to reject similar charges going forward.\n\nMert Mumtaz, the CEO of Solana-infrastructure platform Helius Labs, and prominent promoter of Zcash, cited overzealous regulators as the best argument for privacy.\n\n“The European Central Bank is working on the idea of ‘holding limits’ for ‘your’ money,” Mumtaz said on X. “They are going to control every aspect of your life soon. They think they own you. Use Bitcoin, use Zcash, use crypto. Reject these clowns.”\n\nLance Datskoluo is DL News’ Europe-based markets correspondent. Got a tip? Email at lance@dlnews.com.\nRelated Topics\n[MONERO](https://www.dlnews.com/topics/monero/) You may also like\n[](https://www.dlnews.com/articles/regulation/eus-new-aml-rules-may-impact-uniswap-binance-and-monero/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### EU regulators flag new crypto risks and weigh rules that may impact Uniswap and Binance\n[Inbar Preiss](https://www.dlnews.com/authors/Inbar-Preiss/) 2 June 2023 [](https://www.dlnews.com/articles/markets/xrp-etf-launches-seen-to-trigger-billion-dollar-bonanza/) [Markets](https://www.dlnews.com/articles/markets/) \n### XRP ETF launches seen to trigger $5bn bonanza\n[Eric Johansson](https://www.dlnews.com/authors/eric-johansson/) 3 November 2025 [](https://www.dlnews.com/articles/markets/us-solana-spot-etfs-seen-to-hit-5bn-in-inflows/) [Markets](https://www.dlnews.com/articles/markets/) \n### US Solana spot ETFs seen to hit $5bn in inflows: Grayscale exec\n[Aleks Gilbert](https://www.dlnews.com/authors/Aleks-Gilbert/) 30 October 2025 Related articles\n[](https://www.dlnews.com/articles/defi/monero-hashrate-tug-war-ease-qubic-lose-51-percent-dominance/) [DeFi](https://www.dlnews.com/articles/defi/) \n### Monero hashrate tug-of-war eases as Qubic loses 51% dominance\n[Kyle Baird](https://www.dlnews.com/authors/kyle-baird/) 17 August 2025 [](https://www.dlnews.com/articles/markets/xmr-soars-as-suspected-hacker-purchases-millions-in-tokens/) [Markets](https://www.dlnews.com/articles/markets/) \n### Monero’s XMR soars as suspected hacker purchases $330m\n[Tim Craig](https://www.dlnews.com/authors/timcraig/) 28 April 2025 [](https://www.dlnews.com/articles/regulation/why-the-eu-is-about-to-outlaw-and-curb-key-crypto-features/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### The EU is about to outlaw and restrict some of the most prized features in crypto\n[Inbar Preiss](https://www.dlnews.com/authors/Inbar-Preiss/) 16 January 2024 [](https://www.dlnews.com/articles/defi/monero-and-zcash-liquidity-runs-dry-as-binance-may-delist/) [DeFi](https://www.dlnews.com/articles/defi/) \n### Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins\n[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 12 January 2024\n</searchResult>\n\n\n<searchResult>\n[doc13]:\n**Zcash price primed for 45% breakout as Grayscale files for ETF**\nSearch results\n[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results\n[](https://defillama.com/) [](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) [Regulation](https://www.dlnews.com/articles/regulation/) \n# Zcash price primed for 45% breakout as Grayscale files for ETF\n\n![Zcash price primed for 45% breakout as Grayscale files for ETF](https://www.dlnews.com/resizer/v2/VKGYHYRAJVD6PEWJU4BR5AT47I.jpg?auth=facb23e8d4d3cdf24913a117bc6c07b4c60c1a15269474b2ff0a98d0dee16dd8&amp;width=1200&amp;height=675&amp;focal=825%2C540)\n[Markets](https://www.dlnews.com/articles/markets/) [Regulation](https://www.dlnews.com/articles/regulation/) Privacy token Zcash is ready to rip 45%, says Maria Carola, CEO of crypto exchange StealthEx. Illustration: Gwen P; Source: Shutterstock\n[Home](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) Zcash price primed for 45% breakout as Grayscale files for ETF By [Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 27 November 2025 at 12:19 Share\n- Grayscale is the latest Wall Street player to jump into Zcash.\n- The Winklevoss twins launched a Zcash-based digital asset treasury firm earlier in November.\n\nPrivacy token Zcash is ready to rip 45%, says Maria Carola, CEO of crypto exchange StealthEx.\n\nShe argues that growing interest on Wall Street, most recently Grayscale’s exchange-traded fund filing on Wednesday, will propel the $8.3 billion crypto to new highs.\n\n“A decisive break above $750 with sustained bullish momentum could open the path towards moving above $1,000 before the end of Q4,” Carola told DL News.\n\nThat would translate to Zcash’s price surging 45% above its current price of $515.\nZcash price over the past 6 months. \nPrivacy coins are “operating with an entirely different playbook from the wider market,” Carola said. “They are benefiting from the long-suppressed demand for privacy-preserving tools and prevalent policy legislation in this direction.”\n\nAnd Carola is far from the only one bullish on Zcash. She joins the ranks of BitMEX co-founder Arthur Hayes, popular YouTuber Mario Nawfal, and prominent Indian investor Naval Ravikant, who have all come out in support of Zcash.\n\nA slew of investors have also told DL News that they expect Zcash to surge higher.\n\nThe bullishness comes as influential voices in the crypto community — such as Ethereum co-founder Vitalik Buterin — are increasingly calling for better privacy solutions.\n\n## Grayscale shoots for ETF\n\nThe bullish projections come as Grayscale, the crypto asset manager that pioneered Wall Street products, files to transform its existing Zcash Trust product into a spot exchange-traded fund.\n\nGrayscale’s registration statement submitted to the Securities and Exchange Commission on Wednesday would mark the launch of the first US spot ETF directly tracking Zcash. The move comes just days after it launched ETFs linked to XRP and Dogecoin.\n\nThe firm joins a growing number of major institutions that have come out supporting Zcash.\n\nVenture capital giant Andreessen Horowitz and crypto investment manager Galaxy Digital have both noted the buzz around Zcash and other privacy-focused crypto projects like Monero and Railgun.\n\nCypherpunk, the crypto treasury company backed by twins Cameron and Tyler Winklevoss and launched earlier this month, has deployed over $50 million into Zcash.\n\nAs of November 19, Cypherpunk holds 1.43% of the total Zcash supply and is gunning for 5% ownership of all tokens.\n\n## Privacy controversies\n\nTo be sure, not everyone backs privacy coins.\n\nEU lawmakers have passed a bill to ban exchanges from listing tokens like Zcash and Monero, citing anti-money laundering concerns. The ban is set to take effect in 2027.\n\nRegulators in the US and Europe are cracking down on developers of privacy tools.\n\nIn the Netherlands, Tornado Cash developer Alexey Pertsev was convicted of money laundering in 2024. Prosecutors said his code helped criminals conceal stolen crypto.\n\nIn the US, Tornado Cash co-founder Roman Storm was found guilty of running an unlicensed money-transmitting business. Samourai Wallet’s Keonne Rodriguez received the maximum five-year sentence for similar charges.\n\nLance Datskoluo is DL News’ Europe-based markets correspondent. Got a tip? Email at lance@dlnews.com.\nRelated Topics\n[CRYPTO ETF](https://www.dlnews.com/topics/crypto-etf/) You may also like\n[](https://www.dlnews.com/articles/defi/monero-and-zcash-liquidity-runs-dry-as-binance-may-delist/) [DeFi](https://www.dlnews.com/articles/defi/) \n### Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins\n[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 12 January 2024 [](https://www.dlnews.com/articles/regulation/uk-fca-asks-stablecoin-firms-to-launch-in-sandbox/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### UK financial regulator asks stablecoin firms to launch in its ‘sandbox’ and help shape regulation\n[Tim Craig](https://www.dlnews.com/authors/timcraig/) 26 November 2025 [](https://www.dlnews.com/articles/markets/bitcoin-holds-at-87000-but-do-not-expect-the-price-to-explode/) [Markets](https://www.dlnews.com/articles/markets/) [Snapshot](https://www.dlnews.com/articles/snapshot/) \n### Bitcoin holds at $87,000, but price won’t ‘explode’ to record heights anytime soon, analysts say\n[Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 26 November 2025 Related articles\n[](https://www.dlnews.com/articles/markets/zcash-price-surge-continues-despite-market-turmoil/) [Markets](https://www.dlnews.com/articles/markets/) \n### Zcash price surge continues despite market turmoil\n[Aleks Gilbert](https://www.dlnews.com/authors/Aleks-Gilbert/) 15 November 2025 [](https://www.dlnews.com/articles/markets/winklevoss-twins-bet-on-zcash-with-new-treasury-firm/) [Markets](https://www.dlnews.com/articles/markets/) \n### Winklevoss twins bet on Zcash with new treasury firm targeting 5% supply of the privacy coin’s supply\n[Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 13 November 2025 [](https://www.dlnews.com/articles/people-culture/zcash-foundation-shakes-up-leadership-amidst-zec-token-price-rally/) [People & culture](https://www.dlnews.com/articles/people-culture/) \n### Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% price rally\n[Tim Craig](https://www.dlnews.com/authors/timcraig/) 12 November 2025 [](https://www.dlnews.com/articles/defi/how-privacy-coins-firo-and-zcash-dodged-binance-delisting/) [DeFi](https://www.dlnews.com/articles/defi/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### How privacy coins Firo and Zcash dodged Binance delisting with novel transparency plan\n[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 23 January 2024\n</searchResult>\n\n\n<searchResult>\n[doc12]:\n**Why Zcash price is up 700% since September, according to Galaxy Digital**\nSearch results\n[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results\n[](https://defillama.com/) [](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) \n# Why Zcash price is up 700% since September, according to Galaxy Digital\n\n![Why Zcash price is up 700% since September, according to Galaxy Digital](https://www.dlnews.com/resizer/v2/4LZLNM4GMNBZ5MZD6OV4FIKSTM.jpg?auth=a3defd4ed6225d27570a10ba09a26cfd164e8b689a28923262c81f8f3e212a08&amp;width=1200&amp;height=675&amp;focal=825%2C540)\n[Markets](https://www.dlnews.com/articles/markets/) Monero is also up over 130% this year, while Dash is up 400%. Illustration: Gwen P; Source: Shutterstock\n[Home](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) Why Zcash price is up 700% since September, according to Galaxy Digital By [Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 5 November 2025 at 10:24 Share\n- Galaxy chalks up ZEC’s price action to new user tools and shifting attitudes.\n- Critics say the bullish move is coordinated.\n- Regulators around the world continue to crack down on privacy tech.\n\nThe price of Zcash is staging one of crypto’s most dramatic comebacks despite the market drawdown.\n\nThe 2016 Bitcoin fork created by computer security expert Zooko Wilcox has surged more than 700% since September and is trading at $430, thanks to real infrastructure progress and growing attention to privacy.\n\nThat’s according to a new report from Galaxy Digital, which said that over 30% of the Zcash supply is now hidden from the public eye in private pools — an all-time high for this particular stat.\n\nThe new Zashi wallet has also made private transactions simpler for users, research analyst Will Owens said, which also contributed to more users going private.\n\nOwens added that cross-chain integrations now let users move funds between transparent and private networks while keeping their steps hidden.\nZcash price. \nThe milestone marks an attitude shift in crypto, where privacy, once treated as a liability and attacked by state actors, is now being rebranded as a core feature to protect users.\n\nIt’s not just Zcash that’s doing well. Monero is up over 130% this year while Dash is up 400%, both significantly outperforming Bitcoin.\n\nRailgun, a key Ethereum privacy tool recently mentioned in the Ethereum Foundation’s institutional launch, was also cited by Galaxy Digital as a core project.\n\n> ‘Technically, Zcash’s fundamentals haven’t radically changed overnight.’— Galaxy Digital's Will Owens\n\n## Old tech, new attention\n\nTo be sure, Owens acknowledged that some are sceptical.\n\nProminent voices are split on whether the price action is sustainable. Economist Lyn Alden called the move “a coordinated token pump,” warning traders against becoming “exit liquidity.”\n\nBut tech investor Naval Ravikant countered that Zcash represents a deeper truth about the future of money, writing that “transparent crypto won’t survive a government crackdown.”\n\nVenture capital giant Andreessen Horowitz has also said that demand for privacy “is more urgent than ever,” highlighting record user metrics for Zcash and Railgun this year.\n\nHorowitz’s venture firm a16z cited multiple notable privacy milestones in 2025, including the Ethereum Foundation’s launch of its new 47-member “Privacy Cluster” and an uptick in the usage of the privacy programming language Noir.\n\n“Technically, Zcash’s fundamentals haven’t radically changed overnight,” Galaxy Digital said. “But the perception around the technology has. This rally is driven by both constant vocal support from some of crypto’s top voices and also a reminder of how important privacy is for permissionless money.”\n\nOriginally a Bitcoin fork, Zcash was designed to fix the privacy issue that the Satoshi 2008 whitepaper acknowledged.\n\nIts zero-knowledge proof system, known as zk-SNARKs, allows users to validate transactions without revealing who sent what to whom.\n\nBy contrast, Bitcoin’s public ledger exposes transactions to public analysis.\n\n## Still under fire\n\nState actors are not relinquishing control just yet.\n\nIn 2024, the European Parliament voted through a bill that will ban listing tokens like Zcash and Monero on EU exchanges, with implementation expected in 2027. The argument is that the EU wants to fight financial crimes such as money laundering.\n\nCypto exchanges like Kraken and Binance have also either delisted or considered delisting privacy coins in the EU.\n\nA Dutch court convicted the co-founder of privacy tool Tornado Cash, Alexey Pertsev, of money laundering in 2024. Across the Atlantic, his fellow co-founder, Roman Storm, was convicted in the US in August of conspiracy to operate an unlicensed money-transmitting business. Both of them have appealed their verdicts.\n\nMeanwhile, some of the industry’s best-known privacy projects – mixers like Samourai and Wasabi – have been crippled by regulatory action, with founders arrested and charged.\n\nEven so, the US Department of Justice has said it intends to reject similar cases going forward.\n\nLance Datskoluo is DL News’ Europe-based markets correspondent. Got a tip? Email at lance@dlnews.com.\n</searchResult>\n\n\n<searchResult>\n[doc11]:\n**Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% ...**\nSearch results\n[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results\n[](https://defillama.com/) [](https://www.dlnews.com/) [People & culture](https://www.dlnews.com/articles/people-culture/) \n# Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% price rally\n\n![Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% price rally](https://www.dlnews.com/resizer/v2/QU7DVGZ6RZDOLPTI4RGVKIYZXA.jpg?auth=2226ced312593b426bce6cd78e8062945f6452955fcf8bfe16437d3fd5530a3f&amp;width=1200&amp;height=675&amp;focal=1787%2C1193)\n[People & culture](https://www.dlnews.com/articles/people-culture/) The appointment aren't the first major change to the Zcash Foundation’s leadership in recent weeks. Credit: Shutterstock / Grey82\n[Home](https://www.dlnews.com/) [People & culture](https://www.dlnews.com/articles/people-culture/) Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% price rally By [Tim Craig](https://www.dlnews.com/authors/timcraig/) 12 November 2025 at 12:20 Share\n- Zcash Foundation appoints two new leaders.\n- The foundation also got a new executive director earlier this month.\n- The appointments come amid surging interest in crypto privacy projects.\n\nThe Zcash Foundation is shaking up its leadership.\n\nOn Tuesday, the nonprofit that supports the $7.7 billion privacy protocol announced two new appointments: Pili Guerra moves from engineering manager to head of engineering, and Danika Delano takes on the role of chief operating officer.\n\nThe foundation said the promotions reflect its commitment to promote from within and recognise the talent that’s been instrumental to its success.\n\nIt’s not the first major change to the Zcash Foundation’s leadership in recent weeks.\n\nOn November 1, the foundation’s board appointed Alex Bornstein as executive director. Bornstein stepped in as interim executive director in March.\n\nZcash is a blockchain protocol focused on privacy. It lets users send so-called shielded transactions, which hide transaction details by encrypting data. Users can also choose to send transparent transactions which are publicly viewable like those on Bitcoin or Ethereum.\n\nThe Zcash Foundation is a nonprofit that supports financial privacy infrastructure, primarily on Zcash.\n\nThe new appointees are very much at home with the open-source, privacy-first ethos of the Zcash Foundation.\n\nBefore joining the foundation in 2020, Guerra worked at the Tor Project, a non-profit that develops and maintains the Tor browser and its associated infrastructure. The Tor browser is used for anonymous web browsing, typically on the dark web.\n\nShe also worked at Red Hat, a firm that develops open-source software for businesses.\n\nDelano also joined the Zcash Foundation in 2020. In her previous role as operations director she oversaw the foundation’s grant programmes, and organised Zcon, the foundation’s annual conference.\n\n## 1,000% rally\n\nThe foundation’s leadership moves come as privacy-enhancing crypto projects experience a renaissance after years of investor apathy.\n\nZcash’s ZEC token has led the change, skyrocketing over 1,000% this year. The tokens of other crypto privacy projects, such as Monero and Railgun, have also soared.\nZcash's ZEC token has rallied over 1,000% this year. \nGalaxy Digital attributed Zcash’s rise to real infrastructure progress and growing attention to crypto privacy in a recent report.\n\nInterest rose sharply last month when former BitMEX chief Arthur Hayes predicted the ZEC token will hit $10,000 in a viral post on X.\n\nOn November 7, the ZEC token hit a high of $723, its highest value since 2018. It has since given back some of its gains, and trades around $470.\n\nTim Craig is DL News’ Edinburgh-based DeFi Correspondent. Reach out with tips at tim@dlnews.com.\n</searchResult>\n\n\n<searchResult>\n[doc15]:\n**Winklevoss twins bet on Zcash with new treasury firm targeting 5% ...**\nSearch results\n[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results\n[](https://defillama.com/) [](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) \n# Winklevoss twins bet on Zcash with new treasury firm targeting 5% supply of the privacy coin’s supply\n\n![Winklevoss twins bet on Zcash with new treasury firm targeting 5% supply of the privacy coin’s supply](https://www.dlnews.com/resizer/v2/VKGYHYRAJVD6PEWJU4BR5AT47I.jpg?auth=facb23e8d4d3cdf24913a117bc6c07b4c60c1a15269474b2ff0a98d0dee16dd8&amp;width=1200&amp;height=675&amp;focal=825%2C540)\n[Markets](https://www.dlnews.com/articles/markets/) The Winklevi are rotating to Zcash. Illustration: Gwen P; Source: Shutterstock\n[Home](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) Winklevoss twins bet on Zcash with new treasury firm targeting 5% supply of the privacy coin’s supply By [Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 13 November 2025 at 09:57 Share\n- Gemini’s founders have launched a Zcash-based digital asset treasury firm.\n- Cypherpunk already holds 203,775 ZEC and targets 5% of total supply.\n- Winklevoss twins cite privacy as a top concern in the AI era.\n\nThe Winklevi are rotating to Zcash.\n\nCypherpunk, a brand new crypto treasury company backed by twins Cameron and Tyler Winklevoss, is deploying over $50 million into the Bitcoin fork. As of the launch on November 12, the firm already holds 203,775 of the privacy coins and is shooting for ownership 5% of total supply.\n\n“Privacy’s become a rare, vanishing commodity,” Tyler Winklevoss said on X. “We feel strongly that Zcash could become a meaningful percentage of Bitcoin’s market capitalisation just on the merits of it being a privacy hedge or insurance policy to Bitcoin’s transparency alone.”\n\nCypherpunk’s launch marks one of the most high-profile bets yet that privacy will become the next flashpoint in crypto. The move comes as the Zcash Foundation is shaking up its leadership, and as state actors intensify crackdowns on privacy technology.\n\nZcash’s price has soared over 1,000% this year, and is trading at over $500. Venture capital giant Andreessen Horowitz and crypto investment manager Galaxy Digital have also noted the buzz around Zcash and other privacy-focused crypto projects.\n\nThe billionaire crypto investors are best known for buying 70,000 Bitcoin in 2013 at $150 and for founding the Gemini Space Station crypto exchange.\n\n## ‘Separating Money and State’\n\nZcash creator Zooko Wilcox praised the moment on X. “Proud that Zcash has drawn people like [Will McEvoy, CIO of Cypherpunk] and the Winklevosses who are here for the right reasons.”\n\n“Tyler Winklevoss just said something awesome about ‘separating money and state.’ Something like ‘Have we really done that? And the answer is no, unless you’re using Zcash’,” Wilcox said.\n\n“If Bitcoin is digital gold, Zcash is encrypted bitcoin, or digital cash,” Tyler Winklevoss said.\n\n“One is your store of value, the other is how you privately move your value,” he added. “We’ve been tracking this symbiosis for years and believe that now — as we enter the age of AI — is the right time to begin accumulating ZEC.”\n\nArthur Hayes, also a big Zcash bull, advised investors to self-custody their coins rather than leave it on centralised exchanges.\n\n“If you hold $ZEC on a CEX, withdraw it to a self-custodial wallet and shield it,” he said on X.\n\n“It’s one of the few 1,000x opportunities in crypto remaining,” Carter Razink, co-founder of blockchain commerce platform spree.Finance, told DL News.\n\n## Battle over privacy\n\nTo be sure, not everyone is supportive of privacy coins.\n\nEU lawmakers view private crypto as incompatible with laws designed to prevent money-laundering, terrorism financing, and other financial crimes.\n\nThey have approved a bill that will ban exchanges from listing privacy coins like Zcash and Monero, with implementation expected in 2027.\n\nAnd high-profile criminal prosecutions in the US and Europe have targeted developers behind privacy-enabling blockchain solutions.\n\nIn the Netherlands, Alexey Pertsev, co-founder of Tornado Cash, was convicted of money laundering in 2024. Dutch prosecutors argued that the protocol enabled criminals to hide stolen funds. Pertsev denied wrongdoing, but the court ruled that building software that obscures transactions can itself constitute facilitation of laundering.\n\nIn the US, Tornado Cash co-founder Roman Storm was convicted of conspiring to operate an unlicensed money-transmitting business.\n\nAnother major case came last week when Samourai Wallet co-founder Keonne Rodriguez received the maximum five-year sentence for operating an unlicensed money-transmitting business. Prosecutors accused the project of “soliciting, encouraging, and inviting criminals” to use its privacy features.\n\nLance Datskoluo is DL News’ Europe-based markets correspondent. Got a tip? lance@dlnews.com.\nRelated Topics\n[TORNADO CASH](https://www.dlnews.com/topics/tornado-cash/) You may also like\n[](https://www.dlnews.com/articles/defi/tornado-cash-dev-roman-storm-asks-judge-to-toss-conviction/) [DeFi](https://www.dlnews.com/articles/defi/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### Tornado Cash dev Roman Storm asks judge to toss conviction\n[Aleks Gilbert](https://www.dlnews.com/authors/Aleks-Gilbert/) 1 October 2025 [](https://www.dlnews.com/articles/defi/crypto-industry-calls-for-clarity-act-to-protect-defi-devs-after-tornado-cash-conviction/) [DeFi](https://www.dlnews.com/articles/defi/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### Crypto industry calls for new bill to protect DeFi devs following Tornado Cash founder conviction\n[T. Craig](https://www.dlnews.com/authors/timcraig/) , [E. Johansson](https://www.dlnews.com/authors/eric-johansson/) 28 August 2025 [](https://www.dlnews.com/articles/regulation/devs-of-decentralised-protocols-wont-be-prosecuted-doj-says/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### Devs behind ‘truly decentralised’ protocols won’t face DoJ prosecution, official says\n[Aleks Gilbert](https://www.dlnews.com/authors/Aleks-Gilbert/) 21 August 2025 Related articles\n[](https://www.dlnews.com/articles/people-culture/zcash-foundation-shakes-up-leadership-amidst-zec-token-price-rally/) [People & culture](https://www.dlnews.com/articles/people-culture/) \n### Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% price rally\n[Tim Craig](https://www.dlnews.com/authors/timcraig/) 12 November 2025 [](https://www.dlnews.com/articles/defi/how-privacy-coins-firo-and-zcash-dodged-binance-delisting/) [DeFi](https://www.dlnews.com/articles/defi/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### How privacy coins Firo and Zcash dodged Binance delisting with novel transparency plan\n[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 23 January 2024 [](https://www.dlnews.com/articles/defi/monero-and-zcash-liquidity-runs-dry-as-binance-may-delist/) [DeFi](https://www.dlnews.com/articles/defi/) \n### Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins\n[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 12 January 2024 [](https://www.dlnews.com/articles/markets/ethereum-doubles-down-on-privacy-as-devs-eye-post-tornado-future/) [Markets](https://www.dlnews.com/articles/markets/) [Snapshot](https://www.dlnews.com/articles/snapshot/) \n### Ethereum doubles down on privacy as devs eye post-Tornado future\n[Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 9 October 2025\n</searchResult>\n\n\n<searchResult>\n[doc19]:\n**Monero and Zcash’s liquidity dries up as Binance eyes ... - DL News**\nSearch results\n[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results\n[](https://defillama.com/) [](https://www.dlnews.com/) This article is more than one year old\n[DeFi](https://www.dlnews.com/articles/defi/) \n# Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins\n\n![Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins](https://www.dlnews.com/resizer/v2/7YRQIT4UVZBNNFYVOQJOIX5BYA.jpg?auth=7b400c0363211c2a85babd8559211aaf467d35cd09d12a56e8509ba436046d2d&amp;width=1200&amp;height=675&amp;focal=2260%2C1507)\n[DeFi](https://www.dlnews.com/articles/defi/) Liquidity in the privacy coins market is drying up. Credit: Shutterstock\n[Home](https://www.dlnews.com/) [DeFi](https://www.dlnews.com/articles/defi/) Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins By [Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 12 January 2024 at 15:29 Share\n- Regulatory pressure is spurring exchanges to delist or flag Monero and other privacy coins.\n- A new low in liquidity is spurring Zcash and Firo to find a workaround.\n- Issuers are hopeful they can reach an agreement with Binance.\n\nPrivacy coins are sinking.\n\nCryptocurrencies like Zcash and Monero are getting wrung out of the market as exchange after exchange moves to eliminate the assets from trading.\n\nOn January 5, crypto exchange OKX delisted several key privacy-centric trading pairs, stating they “do not fulfill our listing criteria.”\n\nLast week, Binance added a so-called monitor tag to Monero, Zcash, Firo, and MobileCoin, suggesting it may also delist those tokens.\n\n“Tokens with the Monitoring Tag are at risk of no longer meeting our listing criteria and being delisted from the platform,” the exchange wrote.\n\nReports on Reddit suggest that Binance’s lending program has already gone ahead and removed XMR from the list of available assets.\n\nA quick scan of Binance confirms those reports. The exchange first added XMR as a collateral asset back in May 2022.\n\n## Spooked investors\n\nThough the delisting isn’t official, it still spooked investors.\n\nZcash has fallen almost 19% in the last week, and Monero has stumbled almost 3%.\n\nThe liquidity for privacy coins such as Monero (XMR) and Zcash (ZEC) has sunk to an all-time low, according to new data from analysts at Kaiko.\n\n![Liquidity for popular privacy coins like Monero and Zcash has dried up.](https://www.dlnews.com/resizer/v2/B3Q3EWYYNBAFJK6FWDD4DWQWI4.png?auth=352a8632fd64845f5f9db9d964fef9f2e1e8dadf7f3c1c60fa3fa32535fdba52&amp;width=1440)\n\nLiquidity for popular privacy coins like Monero and Zcash has dried up.\n\n“Most businesses will not want to interact with privacy coins given their negative connotations,” Clara Medalie, Kaiko’s director of research, told DL News.\n\n“Many exchanges are delisting privacy coins, which suggests that market makers don’t want to provide liquidity for them.”\n\nPrivacy coins can obfuscate users’ identities by hiding sender details and transaction history.\n\nThis makes them notoriously difficult to track, drawing scrutiny from regulators worldwide.\n\nA core feature of the original crypto ethos, privacy coins also continue to command many investors’ attention. Monero and Zcash boast a combined market capitalization of $3.48 billion.\n\nThis position now appears to be at serious risk, experts say.\n\n## Serious challenge\n\nWith $15 billion in daily trading volume, Binance’s dominance makes its action a serious challenge to the fortunes of these projects.\n\nBinance doesn’t have much of a choice. After pleading guilty in November to violating US banking law and paying a $4 billion penalty, it’s required to implement stronger anti-money laundering and know-your-customer controls.\n\n> ‘Binance was clear from the beginning that if we did not create an exchange-only address type, they would delist ZEC.’— Jason McGee\n\nMoreover, in negotiations over the EU’s Anti-Money Laundering Regulation, lawmakers are discussing whether to ban privacy coins like Monero and Zcash.\n\n## Fight is on\n\nNow, the fight’s on to keep Binance from axing privacy coins altogether.\n\nSome projects have devised a novel workaround to try and get the nod from Binance.\n\nOthers, such as Monero, refuse to comply with Binance’s requests, with members of its community lashing out against the exchange in December. A Monero representative did not reply to a request for comment.\n\n## All-seeing crypto addresses\n\nThe workaround others are trying is called an “exchange-only” crypto address.\n\nThe idea is that users looking to move funds to an exchange would whip up a new transparent address, send private funds to this address, and then send those funds to the exchange-only address.\n\nFirst proposed by the privacy project Firo last November – which is also on Binance’s chopping block – an exchange-only address can only receive funds from transparent addresses rather than their private, or so-called shielded, counterparts.\n\n“They don’t want to receive shielded transactions,” Jason McGee, a committee member for Zcash Community Grants and the project’s Binance liaison, told DL News.\n\n“Binance was clear from the beginning (early November) that if we did not create an exchange-only address type, they would delist ZEC.”\n\n> ‘Binance doesn’t want to touch any funds from sources that have an unidentified send.’— Reuben Yap\n\nFiro project steward Reuben Yap told DL News that Binance initially asked the project to remove all its privacy features. He said it couldn’t.\n\nBinance is still mulling the proposed solution, say McGee and Yap. They are hopeful it will be accepted because it would let the exchange show regulators the history of a depositing address.\n\n“Binance doesn’t want to touch any funds from sources that have an unidentified send,” Yap said.\n\nBinance did not immediately respond to DL News’ request for comment.\n\nJustin Ehrenhofer, the founder of a crypto sleuthing firm focused on difficult-to-trace transactions Moonstone Research, told DL News the Monero community wasn’t considering the exchange-only approach.\n\n## Lots of discussion\n\nIn any event, the idea is generating some buzz.\n\n“There has been a tremendous amount of discussion about this within the Zcash community,” Zooko Wilcox-O’Hearn, the CEO of Electric Coin Company, the firm developing Zcash, told DL News.\n\nYap told DL News that the exchange address solution is expected to launch in two weeks.\n\nAs to what Binance will do at that point, it’s anyone’s guess.\n\nLiam Kelly is a Berlin-based DeFi Correspondent. Contact him at liam@dlnews.com or on Telegram at @Liam_Gallas.\nRelated Topics\n[MONERO](https://www.dlnews.com/topics/monero/) [BINANCE](https://www.dlnews.com/topics/binance/) [OKX](https://www.dlnews.com/topics/okx/) You may also like\n[](https://www.dlnews.com/articles/regulation/how-china-and-asian-nations-plan-to-regulate-crypto-in-2024/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### Fraud vs innovation: How Asia’s crypto watchdogs will struggle to strike a balance in 2024\n[Callan Quinn](https://www.dlnews.com/authors/Callan-Quinn/) 31 December 2023 [](https://www.dlnews.com/articles/people-culture/dl-news-top-stories-featured-bitcoin-etfs-and-defi-heists/) [People & culture](https://www.dlnews.com/articles/people-culture/) [Regulation](https://www.dlnews.com/articles/regulation/) [DeFi](https://www.dlnews.com/articles/defi/) [Markets](https://www.dlnews.com/articles/markets/) \n### Bitcoin ETFs, regulators, and DeFi heists ruled crypto in 2023: Check out DL News’ top stories of the year\n[Edward Robinson](https://www.dlnews.com/authors/edward-robinson/) 29 December 2023 [](https://www.dlnews.com/articles/regulation/the-crypto-court-cases-to-keep-an-eye-on-in-2024/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### Crypto court cases will heat up in 2024 — here are the ones to watch\n[Joanna Wright](https://www.dlnews.com/authors/joannawright/) 25 December 2023 Related articles\n[](https://www.dlnews.com/articles/regulation/eus-new-aml-rules-may-impact-uniswap-binance-and-monero/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### EU regulators flag new crypto risks and weigh rules that may impact Uniswap and Binance\n[Inbar Preiss](https://www.dlnews.com/authors/Inbar-Preiss/) 2 June 2023 [](https://www.dlnews.com/articles/regulation/what-do-cybercriminals-do-with-stolen-crypto/) [Regulation](https://www.dlnews.com/articles/regulation/) [DeFi](https://www.dlnews.com/articles/defi/) \n### How hackers turn stolen crypto into cash\n[Eric Johansson](https://www.dlnews.com/authors/eric-johansson/) 24 April 2023 [](https://www.dlnews.com/articles/regulation/crypto-romance-fraud-is-poised-to-accelerate-in-2024/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### Crypto romance fraud is poised to accelerate in ‘severity and scope’ in 2024\n[Callan Quinn](https://www.dlnews.com/authors/Callan-Quinn/) 8 January 2024 [](https://www.dlnews.com/articles/snapshot/sbf-will-not-face-second-trial-on-additional-charges/) [Snapshot](https://www.dlnews.com/articles/snapshot/) \n### US won’t try Sam Bankman-Fried second time on additional charges\n[Mike Millard](https://www.dlnews.com/authors/Mike-Millard/) 31 December 2023\n</searchResult>\n\n\n<searchResult>\n[doc20]:\n**Ika Announces EdDSA Signatures, Expanding Native Support to Solana ...**\nSearch results\n[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results\n[](https://defillama.com/) [](https://www.dlnews.com/) Press Release\n\n# Ika Announces EdDSA Signatures, Expanding Native Support to Solana, Zcash, Cardano and More\n\n![Ika Announces EdDSA Signatures, Expanding Native Support to Solana, Zcash, Cardano and More](https://www.dlnews.com/resizer/v2/JXXMCO4GXNFA3D7KHKRESQTTEM.jpg?auth=5f920b24b6018e22a513f1e256c223c2d79ed28d2309416032c0c01d4285d272&amp;width=1200&amp;height=675&amp;focal=608%2C358)\n[Home](https://www.dlnews.com/) Ika Announces EdDSA Signatures, Expanding Native Support to Solana, Zcash, Cardano and More By Partner Content 4 December 2025 at 14:10 Share\n\nZug, Switzerland, December 4th, 2025, Chainwire\n\nIka, the fastest parallel MPC network, today announced a mainnet upgrade that enables EdDSA signatures directly from dWallets, significantly expanding Ika’s native cross-chain coverage to include Solana, Zcash, Cardano, Stellar, Near, and other EdDSA-based ecosystems.\n\nThis upgrade extends Ika’s core promise: natively control accounts and assets across chains without bridges, wrapping, custodians, or trusted signers, now across a broader set of networks where EdDSA is the standard.\n\n> “EdDSA support is a major expansion of what dWallets can control natively,” said Omer Sadika, Co-Founder of Ika. “It brings zero-trust, programmable signing to some of the most important ecosystems in crypto, so developers can orchestrate real cross-chain actions with real native assets, governed by Ika dWallet technology.”\n\nWhat This Upgrade Enables\n\nUntil now, Ika’s dWallets provided zero-trust signing and programmable control for major ecosystems, including Bitcoin and EVM-compatible networks with ECDSA signatures. With EdDSA enabled at the dWallet signing layer, builders can now create applications that:\n- Control Solana accounts natively, enabling cross-chain trading, vaults, payments, and automation without wrapped assets.\n- Coordinate Zcash-native actions under programmable dWallet policies, unlocking zero-trust custody and interoperability for the most prominent privacy-preserving cryptocurrency.\n- Manage Cardano, Stellar, Near accounts with smart contract-governed access control, enabling organizational treasury workflows and institutional-grade policy enforcement.\n\nIn short: dWallets become natively multi-ecosystem signers, and enable a coordination layer for policy, composability, and execution logic.\n\nNative Cross-Chain Control\n\nMost cross-chain systems rely on bridges, message relays, wrappers, or trusted intermediaries. These approaches introduce risk (custody, exploits, governance capture) and limit composability.\n\nIka’s model is different: no bridging of assets is required. Instead, Ika enables native signing via dWallets, where transaction authorization is always enforced under zero-trust assumptions.\n\nWith EdDSA enabled, the same architecture now extends to chains where ECDSA is not supported and EdDSA has been adopted instead, dramatically expanding the surface area of what Ika dWallets can safely and directly orchestrate.\n\nHow EdDSA Works in Ika’s Zero-Trust Model\n\nIka’s security model is built on its 2PC-MPC cryptographic scheme.\n\ndWallet signing splits authorization into two independent components:\n- User share: held and authorized locally by the user\n- Network share: operated by Ika’s decentralized network of MPC nodes\n\nBoth are required to produce a valid signature, and the full private key is never reconstructed. With this mainnet upgrade, that same model now supports EdDSA signing, bringing the benefits of Ika’s architecture (zero-trust, decentralization, scalability, sub-second performance, and programmable policy enforcement) to a wider set of chains.\n\nWhy It Matters for Builders and the Ecosystem\n\nThis upgrade expands the design space for applications that are only possible with Ika, including:\n\nUniversal accounts across ecosystems\n\nOne programmable signing primitive that can operate across EdDSA and non-EdDSA chains, operated with the same SDK and smart contract.\n\nCross-chain DeFi with native assets\n\nStrategies can coordinate multiple ecosystems while keeping assets on their home chains. No wrapping, no “bridged liquidity.”\n\nProgrammable custody and access control\n\nRules are enforced at the signing layer: multi-party approvals, intent constraints, spending limits, automated risk controls, and organizational policy, secured cryptographically rather than contract-side permissions alone.\n\nChain abstraction that’s actually zero-trust\n\nUsers don’t “rent” their wallet to an app or provider. They co-authorize with the network under strict cryptographic guarantees.\n\nAvailability\n\nThe EdDSA-enabled signing upgrade is live on Ika mainnet, and supports dWallet-based signing for Solana, Zcash, Cardano, Stellar, Near, and additional EdDSA-compatible chains.\n\nDevelopers can begin integrating EdDSA-enabled dWallet workflows immediately through Ika’s developer resources.\n\nAbout Ika\n\nIka is the fastest parallel MPC network, offering sub-second latency, unprecedented scale and decentralization, and zero-trust security. As the premier choice for interoperability, decentralized custody, and chain abstraction, Ika is set to revolutionize digital asset security and multi-chain DeFi. Users can learn more here\n\nContact\n\nIka PR\n\npr@ika.xyz\nDisclaimer: Chainwire is the source of this content. This Press Release is for informational purposes only. The information does not constitute investment advice or an offer to invest.\n</searchResult>\n\n\n<searchResult>\n[doc18]:\n**How privacy coins Firo and Zcash dodged Binance delisting ... - DL News**\nSearch results\n[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results\n[](https://defillama.com/) [](https://www.dlnews.com/) This article is more than one year old\n[DeFi](https://www.dlnews.com/articles/defi/) [Regulation](https://www.dlnews.com/articles/regulation/) \n# How privacy coins Firo and Zcash dodged Binance delisting with novel transparency plan\n\n![How privacy coins Firo and Zcash dodged Binance delisting with novel transparency plan](https://www.dlnews.com/resizer/v2/HFGEY6SR7VAL7CAG4QPON5C5MA.jpg?auth=74373f5a0fa5ad620605e5f16b9fb8761684915933c8ce648c419a5cc9ded95e&amp;width=1200&amp;height=675&amp;focal=825%2C540)\n[DeFi](https://www.dlnews.com/articles/defi/) [Regulation](https://www.dlnews.com/articles/regulation/) Binance CEO Richard Teng is scrambling to withstand intense regulatory pressure on a number of fronts. Credit: Rita Fortunato/DL News\n[Home](https://www.dlnews.com/) [DeFi](https://www.dlnews.com/articles/defi/) How privacy coins Firo and Zcash dodged Binance delisting with novel transparency plan By [Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 23 January 2024 at 11:49 Share\n- Binance slapped several privacy coins with its monitor tag, stoking fears of fresh delistings.\n- Firo and Zcash have staved off delisting worries with a newly-approved tech solution.\n- It's not permanent, and given the current regulatory environment, anything could change.\n\nPrivacy coin enthusiasts can breathe a sigh of relief.\n\nAfter Binance slapped a so-called monitoring tag on a slew of privacy coins earlier this month, many worried that assets like Zcash and Firo would soon be delisted.\n\nRepresentatives from Zcash and Firo told DL News on Monday this wouldn’t happen.\n\nFor now, at least.\n\n“While I prefer not to speculate on specific timelines, Binance’s approval for Zcash to implement the new address type seems to protect ZEC from immediate delisting,” Jason McGee, Zcash’s Binance liaison, told DL News.\n\n“Although Binance hasn’t declared this a permanent fix, their willingness to adopt this change suggests an intention to collaborate on solutions with privacy coins, rather than resorting to immediate delisting.”\n\n## Could change their minds\n\nIt’s a positive step, but McGee said, “there’s always the risk they change their minds.”\n\nBinance did not immediately respond to requests for comment.\n\nReuben Yap, Firo’s project steward, was equally hesitant after disclosing the project also met Binance’s compliance requirements.\n\nEuropean Union lawmakers are close to finalising new anti-money laundering laws that could prohibit privacy coins, and a decision is expected within weeks. Yap said new regime or a change in investors’ risk appetite makes the status of privacy coins tenuous.\n\n## Exchange-only addresses\n\nBinance’s apparent decision to let the privacy coins stay listed appears to be a vote of confidence in a novel approach proposed by the issuers.\n\nIt’s a technical solution called “exchange-only” address types, which the Firo team developed last year.\n\nUnder the scheme, crypto exchanges wouldn’t be able to receive tokens for these projects unless the sending address is transparent. The exchange must be able to see the transaction history of its counterparties.\n\nZcash has two varieties of this solution: TEX Address and Traceable Unified Address. But Binance hasn’t indicated a preference for either.\n\nThis is sparking further discussion about which project should be implemented without precise guidance. “We’re still gauging the community’s preference,” McGee told DL News.\n\n## Privacy-preserving technology\n\nCritically, these changes would happen at the wallet level, he said, and not at the protocol level.\n\n“The new address type does not alter the fundamental aspects of Zcash’s privacy-preserving technology,” McGee said.\n\nIn the meantime, all tokens added to Binance’s monitor list are still tagged. The monitor tag flags users on the exchange that the assets “are likely to have higher volatility and risks compared to other listed tokens.”\n\nUsers can start trading after answering four questions in the affirmative and admitting that any losses incurred from transactions are customers’ responsibility.\n\nIt’s unclear whether Binance’s monitoring tag will be removed next quarter or how long it will take for the company to implement the “exchange-only” technical solutions.\n\n“Monitoring isn’t a delisting,” Yap said. “It’s a ‘warning.’ But they put us on warning because of non-compliance with laws.”\n\n## Crypto rules around the world\n\nBinance has come under enormous regulatory pressure in recent months.\n\nIn November, the company and its co-founder and CEO, Changpeng “CZ” Zhao, pleaded guilty to violating US banking law in connection with anti-money laundering violations. The company paid a $4.3 billion settlement and Zhao resigned as CEO.\n\nIn the meantime, OKX has already gone ahead and delisted these privacy coins and others.\n\nWith Europe’s sweeping Markets in Crypto Assets (MiCA) rules and new anti-money laundering laws soon coming into effect on the bloc, regulators are paying particular attention to privacy coins and crypto mixers.\n\n“Right now, we have complied with all the requirements,” Yap told DL News. “But as MiCA comes closer, if there are additional guidelines, we may have to do additional things.”\n\nFor now, projects like Firo and Monero will remain in purgatory just a bit longer.\n\n“No, this change does not mark the beginning of the end for privacy coins,” said McGee. “Rather, it represents the need for adaptability amidst evolving regulatory standards.”\n\nLiam Kelly is DL News’ Berlin correspondent. Contact him at liam@dlnews.com.\nRelated Topics\n[BINANCE](https://www.dlnews.com/topics/binance/) [CHANGPENG ZHAO](https://www.dlnews.com/topics/changpeng-zhao/) [MICA](https://www.dlnews.com/topics/mica/) [MONEY LAUNDERING](https://www.dlnews.com/topics/money-laundering/) You may also like\n[](https://www.dlnews.com/articles/regulation/crypto-romance-fraud-is-poised-to-accelerate-in-2024/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### Crypto romance fraud is poised to accelerate in ‘severity and scope’ in 2024\n[Callan Quinn](https://www.dlnews.com/authors/Callan-Quinn/) 8 January 2024 [](https://www.dlnews.com/articles/snapshot/sbf-will-not-face-second-trial-on-additional-charges/) [Snapshot](https://www.dlnews.com/articles/snapshot/) \n### US won’t try Sam Bankman-Fried second time on additional charges\n[Mike Millard](https://www.dlnews.com/authors/Mike-Millard/) 31 December 2023 [](https://www.dlnews.com/articles/regulation/how-china-and-asian-nations-plan-to-regulate-crypto-in-2024/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### Fraud vs innovation: How Asia’s crypto watchdogs will struggle to strike a balance in 2024\n[Callan Quinn](https://www.dlnews.com/authors/Callan-Quinn/) 31 December 2023 Related articles\n[](https://www.dlnews.com/articles/defi/monero-and-zcash-liquidity-runs-dry-as-binance-may-delist/) [DeFi](https://www.dlnews.com/articles/defi/) \n### Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins\n[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 12 January 2024 [](https://www.dlnews.com/articles/snapshot/five-charts-explain-trueusd-dollar-depeg-and-binance-role/) [Snapshot](https://www.dlnews.com/articles/snapshot/) \n### These five charts explain TrueUSD’s fall below its dollar peg — and Binance’s role in the move\n[S. Sinclair](https://www.dlnews.com/authors/Sebastian-Sinclair/) , [A. McCarthy](https://www.dlnews.com/authors/adam-morgan/) 22 January 2024 [](https://www.dlnews.com/articles/snapshot/binance-inflows-have-surged-since-november-guilty-plea/) [Snapshot](https://www.dlnews.com/articles/snapshot/) \n### Binance trade resurgent since historic penalty, exit of Changpeng Zhao\n[Mike Millard](https://www.dlnews.com/authors/Mike-Millard/) 21 January 2024 [](https://www.dlnews.com/articles/snapshot/how-pro-crypto-traders-can-arb-bitcoin-etfs/) [Snapshot](https://www.dlnews.com/articles/snapshot/) \n### How pro crypto traders can arb Bitcoin ETFs\n[Thomas Carreras](https://www.dlnews.com/authors/Thomas-Carreras/) 17 January 2024\n</searchResult>\n\n\n<searchResult>\n[doc21]:\n**ZKasino’s year-long silence on investor refunds ends in a $27m ...**\nSearch results\n[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results\n[](https://defillama.com/) [](https://www.dlnews.com/) This article is more than nine months old\n[DeFi](https://www.dlnews.com/articles/defi/) \n# ZKasino’s year-long silence on investor refunds ends in a $27m liquidation\n\n![ZKasino’s year-long silence on investor refunds ends in a $27m liquidation](https://www.dlnews.com/resizer/v2/ZS5NXYIEPNAMTAGOEH3NCO5T4U.png?auth=85421f7b5da98f78e9f8dac4e9091964f73f1be6ef1f092776d84b8c3c56a3b5&amp;width=1200&amp;height=675&amp;focal=825%2C540)\n[DeFi](https://www.dlnews.com/articles/defi/) ZKasino was launched last April as a flashy, onchain gambling project. It attracted over $40 million in Ethereum from investors who were promised yield on top of their deposits. Credit: Darren Joseph\n[Home](https://www.dlnews.com/) [DeFi](https://www.dlnews.com/articles/defi/) ZKasino’s year-long silence on investor refunds ends in a $27m liquidation By [Osato Avan-Nomayo](https://www.dlnews.com/authors/Osato-Avan-Nomayo/) 7 April 2025 at 20:14 Share\n- A ZKasino-linked wallet liquidated for $27 million.\n- Investors have been waiting for a refund since last year.\n- The crypto market lost over $240 billion overnight.\n\nA crypto wallet linked to ZKasino, the crypto gambling platform that disappeared last year with $40 million in investor funds, got liquidated for over $27 million during Sunday’s crypto wipeout.\n\nThe wallet, which had been sitting on a high-risk Ethereum position since last month, finally tipped over as Ethereum plunged below $1,500 — its lowest price in two years.\n\nZKasino’s liquidation was just one among many. As panic rippled through the markets, leveraged positions across DeFi began to unwind. One major trader, unrelated to ZKasino, lost $74 million in the same cascade. Others narrowly avoided liquidation by rushing to reinforce their collateral as prices plunged.\n\nWhoever was still gambling with ZKasino’s stolen funds was forced to close the position — but not before being margin-called into oblivion and losing $27 million in the process.\n\nThat may have been a darkly poetic end to a year-long saga for ZKasino. But for investors, there’s little consolation. Instead of the refunds they were promised, they’ve endured silence, stalling, and now, the final flush of whatever was left.\n\nZKasino was launched last April as a flashy, onchain gambling project. It attracted over $40 million in Ethereum from investors who were promised yield on top of their deposits.\n\nBut instead of payouts a month later, the project changed course and said it would swap Ethereum deposits for its native cryptocurrency called ZKAS. The project called the swap “a favour” for early investors.\n\nHowever, investors were not pleased with the change as it meant they would not be able to redeem their investments in full as they were initially promised.\n\nZKasino then converted $30 million in user deposits into Lido’s Wrapped Staked Ether and began earning staking yield on the funds while investors were left in limbo.\n\nThen came allegations of a rug pull ― a form of crypto crime where team members disappear with pooled funds, leaving investors in the lurch.\n\nDutch authorities eventually stepped in and arrested a man in connection with the alleged scam.\n\nZKasino denied the allegations and eventually converted the funds back to Ethereum, announcing a vague repayment plan. But nearly a year later, nothing has been paid back.\n\nNow, with the liquidation of the last major wallet, that plan looks as precarious as the promises behind it.\n\nOsato Avan-Nomayo is our Nigeria-based DeFi correspondent. He covers DeFi and tech. Got a tip? Please contact him at osato@dlnews.com.\n</searchResult>\n\n\n"
  },
  {
    "ToolCallId": "call_xuW5fKpcjAmiic1XSRDIfwcx",
    "Output": "<searchResult>\n[doc1]:\n**Zcash Exchange Balances Plunge 20% - Breakout To $800 Likely - BeInCrypto**\n[](https://beincrypto.com/) - Feed\n- Newsletters\n- Bonus Hunter\n- Top Picks\n- MarketsPricesExchangesConvert\n- Advertise\n- Remote Jobs\nEnglish For Business\n[Advertise](https://advertise.beincrypto.com/) [Contact Us](https://beincrypto.com/contact/) Company\n[About Us](https://beincrypto.com/about/) [Our Authors](https://beincrypto.com/our-authors/) [Careers 🚀](https://beincrypto.com/careers/) [Our Team](https://beincrypto.com/our-team/) [News](https://beincrypto.com/news/) [Learn](https://beincrypto.com/learn/) [Bonus Hunter](https://beincrypto.com/bonus-hunter/) [Feed](https://beincrypto.com/) [Top Picks](https://beincrypto.com/top-picks/) [Special Edition](https://beincrypto.com/special-edition/) [Careers 🚀](https://beincrypto.com/careers/) [Our Authors](https://beincrypto.com/our-authors/) [Our Team](https://beincrypto.com/our-team/) [Advertise](https://advertise.beincrypto.com/) [Contact Us](https://beincrypto.com/contact/) [About Us](https://beincrypto.com/about/) [Crypto News](https://beincrypto.com/news/) [Ripple (XRP) News](https://beincrypto.com/tag/xrp-news/) [Bitcoin (BTC) News](https://beincrypto.com/tag/bitcoin-news/) [Analysis](https://beincrypto.com/type/analysis/) [Ethereum (ETH) News](https://beincrypto.com/tag/ethereum-news/) [US Crypto News](https://beincrypto.com/tag/united-states-of-america/) [Cardano (ADA) News](https://beincrypto.com/tag/ada-news/) [Solana (SOL) News](https://beincrypto.com/tag/solana-news/) [Memecoins News](https://beincrypto.com/tag/memecoin-news/) [ETF News](https://beincrypto.com/tag/etf-news/) [Altcoins News](https://beincrypto.com/tag/altcoin-news/) [Markets](https://beincrypto.com/price/) [Prices](https://beincrypto.com/price/) [Exchanges](https://beincrypto.com/exchanges/) [Convert](https://beincrypto.com/convert/) [Remote Jobs](https://beincrypto.com/jobs/) [Fast News](https://t.me/+F2LkP3N3LyY5NTMy) [Newsletters](https://beincrypto.com/newsletters/) [Back](https://beincrypto.com/) [Trusted](https://beincrypto.com/trust-project/) [Analysis](https://beincrypto.com/type/analysis/) [Markets](https://beincrypto.com/category/markets/) \n# Zcash Accumulation Sets The Stage For ZEC Price Breakout To $800\n\n![Zcash Accumulation Sets The Stage For ZEC Price Breakout To $800](https://beincrypto.com/_mfes/post/_next/image/?url=https%3A%2F%2Fassets.beincrypto.com%2Fimg%2FqzLlTJpAKhEdcskq29wCgK-90RE%3D%2Fsmart%2Feb1cc6a195d348ef84054a45079a4a78&amp;w=1920&amp;q=75)\n\n![author avatar](https://beincrypto.com/_mfes/post/_next/image/?url=https%3A%2F%2Fassets.beincrypto.com%2Fimg%2F-t8a76Q6aMRqAejOF3EB9lZesIk%3D%2Fsmart%2F5a337e10d3bc4d3ab8a882c23e7ad016&amp;w=64&amp;q=75)\n\nWritten byAaryamann Shrivastava\n\n![editor avatar](https://beincrypto.com/_mfes/post/_next/image/?url=https%3A%2F%2Fassets.beincrypto.com%2Fimg%2Fh-hQzOzK42E_4nq7oQ0rsXup8jU%3D%2Fsmart%2F21b210244b384c07840d7ceeb5f9d8fb&amp;w=64&amp;q=75)\n\nEdited byHarsh Notariya\n06 January 2026 14:00 UTC [Trusted](https://beincrypto.com/trust-project/) - Zcash exchange balances drop 20.75%, signaling strong accumulation and reduced selling pressure.\n- Futures funding flips positive as traders shift from shorts to bullish positioning.\n- ZEC price is trading near $512, eyeing a 38% breakout toward the $800 target.\nPromo\n[#Altcoin Analysis](https://beincrypto.com/tag/altcoin-analysis/) \nZcash price has moved sideways over the past several days, consolidating after recent volatility. While this pause may appear bearish, it often signals strength following an uptrend.\n\nPrice stability near current levels suggests buyers are defending positions, and recent investor behavior further supports a constructive outlook for ZEC.\nSponsored Sponsored \n## Zcash Holders Are Buying\n\nExchange data shows a sharp reduction in available ZEC supply. According to Nansen, Zcash holdings on centralized exchanges dropped by 20.75% in the last 24 hours. Such a decline indicates significant outflows, which usually reflect investor accumulation rather than distribution.\n\nWhen coins move off exchanges, selling pressure often decreases. Investors tend to transfer assets into private wallets when expecting higher prices. This behavior suggests rising confidence among ZEC holders, who appear willing to hold rather than liquidate at current levels.\n\nWant more token insights like this? Sign up for Editor Harsh Notariya’s Daily Crypto Newsletter here.\n\n![ZEC Exchange Holdings](https://assets.beincrypto.com/img/1nWRUSJNiStXThyBIqYygBWvbbY=/smart/d3fcfbec39234a4dba7d6fd36471a9f5)\nZEC Exchange Holdings. Source: [Nansen](https://app.nansen.ai/) \nSustained exchange outflows often precede upward price moves. Reduced liquid supply can amplify price reactions once demand increases. In Zcash’s case, this accumulation trend strengthens the bullish narrative forming around its current consolidation phase.\nSponsored Sponsored \n## ZEC Traders Turn Bullish As Well\n\nDerivatives market data shows a notable shift in trader positioning. For nine consecutive days, ZEC futures were dominated by short contracts. This imbalance kept the funding rate negative, reflecting bearish expectations among leveraged traders.\n\nOver the last 24 hours, that trend reversed. Funding rates turned positive, indicating long contracts now outweigh shorts. This change suggests traders are positioning for upside rather than further downside.\n\n![ZEC Funding Rate.](https://assets.beincrypto.com/img/zEfcqPlzvtishgFnJGPSJoDGSus=/smart/7390b03a574d4db7a41d8c5208b906c8)\nZEC Funding Rate. Source: [Coinglass](https://www.coinglass.com/) \nPositive funding reflects improving sentiment and willingness to pay a premium to stay long. When futures sentiment aligns with spot accumulation, momentum often accelerates. This alignment supports the view that ZEC may be preparing for a directional move higher.\n\n## ZEC Price Eyes Breakout\n\nZEC trades near $512 at the time of writing, moving within an ascending wedge pattern. This structure typically resolves with a breakout. A successful move above resistance could drive price nearly 38% higher, targeting the $802 level.\n\nBreakout odds are improving after ZEC recently tested and bounced from the lower trend line. Technical support held firmly, reinforcing buyer control. Accumulation and improving futures sentiment further increase the likelihood of continuation. A confirmed breakout requires flipping $600 into support.\n\n![ZEC Price Analysis.](https://assets.beincrypto.com/img/YYLcvBklA-Ogsgnahv7bFUeQUxA=/smart/34c116e645794ab18e9a0f02e2351a33)\nZEC Price Analysis. Source: [TradingView](https://www.tradingview.com/) \nDownside risk remains if sentiment shifts abruptly. Renewed selling or a failed breakout could pressure the price lower. A drop below $500 would weaken the structure. Under such conditions, the Zcash price may fall toward $442, invalidating the bullish thesis.\nYou might also like\n[AnalysisMarkets15 hours agoSUI Jumps 37% in a Week, but Profit-Taking Puts $2 Support at Risk](https://beincrypto.com/sui-price-rally-profit-booking-risk/) [NewsletterSubscribeDaily Crypto InsightsInsights, news and analysis of the crypto market straight to your inbox](https://beincrypto.com/newsletters/) [Crypto Exchanges2 months agoBest Crypto Platforms for DePIN Tokens in 2026](https://beincrypto.com/top-picks/depin-token-platforms/) \nDisclaimer\n\nIn line with the Trust Project guidelines, this price analysis article is for informational purposes only and should not be considered financial or investment advice. BeInCrypto is committed to accurate, unbiased reporting, but market conditions are subject to change without notice. Always conduct your own research and consult with a professional before making any financial decisions. Please note that our Terms and Conditions, Privacy Policy, and Disclaimers have been updated.\nSponsored Sponsored Read Next\n\n![K-Shaped Crypto Market: Top Assets Rally as Altcoins Lag in 2026](https://beincrypto.com/_mfes/post/_next/image/?url=https%3A%2F%2Fassets.beincrypto.com%2Fimg%2FCeuHN4mv9OmBrr72oAzbTu25Gys%3D%2Fsmart%2F0e2a9520c56c4b0b9273fb8c37459ecf&amp;w=3840&amp;q=75)\n[NewsMarkets1 minute agoK-Shaped Crypto Market: Top Assets Rally as Altcoins Lag in 2026](https://beincrypto.com/k-shaped-crypto-market-2026/) [](https://x.com/beincrypto) [](https://www.linkedin.com/company/beincrypto/) [](https://www.instagram.com/beincrypto/) [](https://t.me/+OUUQ7wNqpikzN2Zi) [](https://www.youtube.com/c/Beincrypto) Sign up for our newsletters\nBonus Hunter\nA curated list of top giveaways, airdrops and special activation offers\nDaily Crypto Insights\nInsights, news and analysis of the crypto market straight to your inbox\nCrypto Leaders\nOutlook of the industry, market trends and key opinions from leaders within the industry\nWeb3 jobs\nInformation, advice and the latest vacancies to help you get into the Web3 world\nCompany [About Us](https://beincrypto.com/about/) [Our Authors](https://beincrypto.com/our-authors/) [Careers 🚀](https://beincrypto.com/careers/) Products [News](https://beincrypto.com/type/news/) [Learn](https://beincrypto.com/type/learn/) [Markets](https://beincrypto.com/price/) [Learn-to-Earn](https://beincrypto.com/learn-to-earn/) [Bonus Hunter](https://beincrypto.com/bonus-hunter/) [Newsletters](https://beincrypto.com/newsletters/) [Top Picks](https://beincrypto.com/top-picks/) [Special Edition](https://beincrypto.com/special-edition/) [Fast News](https://t.me/+sLfpqc66saQxMTQy) Resources [Advertise](https://advertise.beincrypto.com/) [Remote Jobs](https://beincrypto.com/jobs/) [Contact Us](https://beincrypto.com/contact/) [The Trust Project](https://beincrypto.com/trust-project/) [Verification Methodology](https://beincrypto.com/methodology/) [Advertiser Disclosure](https://beincrypto.com/advertising-disclosure/) © 2026 BeInNews Academy [Terms](https://beincrypto.com/terms-and-conditions/) [Privacy](https://beincrypto.com/privacy-policy/) [Disclaimer](https://beincrypto.com/disclaimer/) [Cookie Settings](https://beincrypto.com/)\n</searchResult>\n\n\n<searchResult>\n[doc2]:\n**Zcash News Today (ZEC) – Latest Updates & Trends**\n[](https://www.coinbird.com/) [](https://www.coinbird.com/) [](https://www.coinbird.com/) \n![Zcash Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/ZEC.svg)\n\n![Zcash Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/ZEC.svg)\n\n# Zcash news\nLatest Zcash news and market trends\n[Buy ZEC](https://www.coinbird.com/go/crypto_buy) [Latest ZEC news](https://www.coinbird.com/cryptocurrencies/zcash/news#latest-news) [Zcash news sentimentLast 30 daysPositive77/100](https://www.coinbird.com/cryptocurrencies/zcash/news#news-sentiment) \n## The most important Zcash news this month\nAI summary \n### Zcash Shielded Supply Rises\n\nZebra 3.1 upgrade increased shielded supply to almost 25 %, signaling growing privacy adoption.\n\n### Cypherpunk Buys $28 M Zcash\n\nWinklevoss-backed firm purchased 56,418 ZEC, raising holdings to 1.76 % of supply, reflecting confidence in privacy coins.\n\n### Unshielded ZEC Spike Sparks Sell‑Off\n\n200,000 ZEC moved to transparent pool and a 74k transfer to Binance raised concerns about potential sell‑off and price drop.\n\n### What this could mean for Zcash\n\nThe rapid growth of shielded ZEC, coupled with high-profile institutional purchases, boosts confidence and could drive price upward, but recent unshielding activity introduces short-term volatility risks.\nThe AI-generated summaries are experimental and may contain errors. Not investment advice. Last updated: 2026-01-06T16:34:02.141+00:00 . \n## Latest Zcash news\n\nUpdated at 2026-01-06T23:30:52.492Z\n\nUpdated at 2026-01-06T23:30:52.492Z\nHeadline\nImpact score Impact score \nOur Impact Score (0–100) uses AI to estimate how strongly a news item could affect the coin over the next 24–72 hours. It primarily considers direct relevance to the coin, novelty, source quality and diversity, potential reach, and the type of event, such as ETFs and regulation, product launches, partnerships, or hacks. Higher scores are assigned to substantiated research forecasts, corporate buy or sell activity, and clear statements from well-known figures. Low scores apply to bare price predictions without substance, minor price moves without context, or PR pieces with no informational value. The score is computed automatically and updated continuously. The AI may make mistakes. When in doubt, please review the linked original sources. Not financial advice.\nPublished\n\n## Zcash news sentiment\n\nLast 30 days\nPositive\n77 /100 \nCurrent Zcash news sentiment is positive (77/100), based on 14 news articles from the past 30 days. Our algorithm scores each article for relevance and sentiment (positive, neutral, or negative) and weights high-impact stories more. The score updates automatically as new Zcash headlines arrive.\n\n## Zcash market trends\nPositive Negative Positive \nMomentum\nMomentum \nMomentum measures the current market dynamics of a cryptocurrency. The value is based on technical indicators such as the Relative Strength Index (RSI), the Fear & Greed Index, and the short-term price trend over the past 30 days. Positive values indicate upward momentum, negative values indicate downward momentum. This indicator is for informational purposes only and does not constitute investment advice.\nPositive [Momentum](https://www.coinbird.com/cryptocurrencies/zcash/news#buy-timing-dashboard) [Momentum](https://www.coinbird.com/cryptocurrencies/zcash/buy#buy-timing-dashboard) Fear Fear Greed \nFear & Greed Index\nFear & Greed Index \nThe Fear and Greed Index for cryptocurrencies is a sentiment indicator measuring market mood on a scale from 0 (extreme fear) to 100 (extreme greed). It aggregates data from various sources such as volatility, market momentum, social media, market dominance, and Google Trends to assess overall market sentiment. Values in the “Greed” range (55-100) indicate a positive, potentially overoptimistic market mood, signaling a possibly overheated market. A “Neutral” value (45-54) reflects a balanced market sentiment. Values in the “Fear” range (0-44) indicate negative market sentiment, signaling fear or pessimism among investors and possibly an undervalued market.\nFear [Fear & Greed Index](https://www.coinbird.com/learn/fear-greed-index-bitcoin) 16 /30 days \nPrice trend\nPrice trend \nThe price trend shows short-term price action over the last 30 trading days. For each day, the open is compared to the close: if the close is higher, the day is marked green; otherwise red. A sustained majority of green days suggests an uptrend that may persist in the short to medium term.\nPositive [Zcash price](https://www.coinbird.com/cryptocurrencies/zcash/price) \n$501.31\n+46.57% last 30 days \n### Price performance\nPrice performance \nThe price development, often referred to as return on investment (ROI), is a metric that provides insight into the past profitability and performance of an investment. In this context, ROI describes the percentage change in price and thus the retrospective “return” of a cryptocurrency over a defined period. Past performance is not indicative of future results.\n<table>\n  <tr>\n    <td>↑+0.15%</td>\n    <th>Hour</th>\n  </tr>\n  <tr>\n    <td>↓-0.37%</td>\n    <th>Day</th>\n  </tr>\n  <tr>\n    <td>↓-4.35%</td>\n    <th>Week</th>\n  </tr>\n  <tr>\n    <td>↑+46.57%</td>\n    <th>Month</th>\n  </tr>\n  <tr>\n    <td>↑+1,160.13%</td>\n    <th>200d</th>\n  </tr>\n  <tr>\n    <td>↑+745.09%</td>\n    <th>Year</th>\n  </tr>\n</table>\n\n## Other cryptocurrency news\n\n![Bitcoin Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/BTC.svg)\n\nBitcoinNews\n\nNEGATIVE2025-12-27T17:01:38+00:00•decrypt.co\n\nBitcoin Whales Woke Up in 2025 and Moved Billions in BTC—Here's Why\n90 /100 \nPOSITIVE2025-12-10T01:44:16+00:00•cointelegraph.com\n\nVivek Ramaswamy's Strive to raise $500M to buy Bitcoin\n90 /100 [Latest Bitcoin news](https://www.coinbird.com/cryptocurrencies/bitcoin/news) \n![Ethereum Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/ETH.svg)\n\nEthereumNews\n\nPOSITIVE2026-01-05T17:04:59+00:00•decrypt.co\n\nEthereum's Blockchain Trilemma 'Solved': Vitalik Buterin\n90 /100 \nPOSITIVE2026-01-05T12:26:24+00:00•cryptoslate.com\n\nVitalik Buterin declares Ethereum solved crypto Trilemma, yet his 2030 roadmap exposes a massive ideological risk\n90 /100 [Latest Ethereum news](https://www.coinbird.com/cryptocurrencies/ethereum/news) \n![XRP Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/XRP.svg)\n\nXRPNews\n\nPOSITIVE2025-12-11T15:43:35+00:00•theblock.co\n\nNew XRP ETF hits the market with launch of 21Shares' TOXR\n90 /100 \nPOSITIVE2025-12-08T13:20:11+00:00•coindesk.com\n\nU.S. Spot XRP ETFs Hit 15-Day Inflow Streak, Near $1B Milestone\n90 /100 [Latest XRP news](https://www.coinbird.com/cryptocurrencies/xrp/news) \n![Solana Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/SOL.svg)\n\nSolanaNews\n\nPOSITIVE2026-01-06T19:21:01+00:00•theblock.co\n\n‘Shocker': Morgan Stanley's Bitcoin and Solana ETF filings signal deep institutional commitment to crypto\n90 /100 \nNEGATIVE2025-12-30T10:39:00+00:00•beincrypto.com\n\nHNUT Meme Coin Collapses 99% on Solana, PeckShield Flags Bundled Rug Pull\n85 /100 [Latest Solana news](https://www.coinbird.com/cryptocurrencies/solana/news) \n![Dogecoin Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/DOGE.svg)\n\nDogecoinNews\n\nNEGATIVE2025-12-25T14:01:03+00:00•decrypt.co\n\nThe Year in Dogecoin 2025: DOGE Goes Political and Commercial\n85 /100 \nPOSITIVE2025-12-25T19:06:23+00:00•cryptoslate.com\n\nThe memecoin hall of shame: 10 tokens that defined 2025 wildest trades\n80 /100 [Latest Dogecoin news](https://www.coinbird.com/cryptocurrencies/dogecoin/news) \n![Cardano Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/ADA.svg)\n\nCardanoNews\n\nPOSITIVE2025-12-14T18:11:25+00:00•cryptoslate.com\n\nCardano now has institutional-grade infrastructure, but a glaring $40 million liquidity gap threatens to stall growth\n80 /100 \nPOSITIVE2025-12-15T17:12:01+00:00•beincrypto.com\n\n3 Altcoins Facing Liquidation Risks in the Third Week of December\n70 /100 [Latest Cardano news](https://www.coinbird.com/cryptocurrencies/cardano/news) \n### Other crypto news\n- BNBnews\n- Tronnews\n- Bitcoin Cashnews\n- Chainlinknews\n- Stellarnews\n- Suinews\n- Hyperliquidnews\n- Litecoinnews\n- Avalanchenews\n- Hederanews\n- Shiba Inunews\n- Uniswapnews\n- Polkadotnews\n- Pepenews\n- Aavenews\n- NEAR Protocolnews\n- Worldcoinnews\n- Ondonews\n- Kaspanews\n- Polygon (POL)news\n- Algorandnews\n- Rendernews\n- Cosmosnews\n- Filecoinnews\n- VeChainnews\n- Bonknews\n- ASI (Fetch.ai)news\n- Tezosnews\n- IOTAnews\n- The Graphnews\n- Sonic (Fantom)news\n- The Sandboxnews\n- Decentralandnews\n- Axie Infinitynews\n\n## All about Zcash\n[What is Zcash?Important details and simple explanation of Zcash.](https://www.coinbird.com/cryptocurrencies/zcash/overview) [Zcash priceLive price, charts and market data for Zcash.](https://www.coinbird.com/cryptocurrencies/zcash/price) [Zcash predictionPrice forecasts and key metrics to analyze Zcash.](https://www.coinbird.com/cryptocurrencies/zcash/price-prediction) [Buy ZcashFind the cheapest and best places to buy Zcash.](https://www.coinbird.com/cryptocurrencies/zcash/buy) [Zcash converterSee what past Zcash buys would be worth today.](https://www.coinbird.com/cryptocurrencies/zcash/converter) \nOur data on cryptocurrencies was last updated on 2026-01-07T00:05:26.994203+00:00. Sources: CoinGecko, defillama.com, coincodex.com.\n\nThe content on this website is provided for general informational purposes only and does not constitute financial, investment, legal, or tax advice. It should not be interpreted as a recommendation to buy, sell, or hold cryptocurrencies, nor as a guarantee of future price developments. You are responsible for independently verifying any information before using a listed service. Trading cryptocurrencies involves significant risk and can result in the total loss of your capital. Past performance is not indicative of future results. We do not accept any liability for the timeliness, accuracy, or completeness of the information provided, including content from external or third-party sources. All actions are taken at your own risk. Some links on this website are affiliate links. If you purchase a product or use a service through these links, we may receive a commission at no additional cost to you. Our content, comparisons, and rankings remain editorially independent. This helps us provide free content and continue developing the platform. Thank you for your support.\n</searchResult>\n\n\n<searchResult>\n[doc3]:\n**Zcash Price Prediction, News, and Analysis (ZEC) - MarketBeat**\n[Skip to main content](https://www.marketbeat.com/cryptocurrencies/zcash/#main) [](https://www.marketbeat.com/) [Free Trial](https://marketbeat.com/subscribe/all-access/?ReferralType=HeaderButton) [→ The $100 Trillion AI Story No One Is Telling You](https://www.marketbeat.com/scripts/redirect.aspx?TriggeredCampaignID=16919&UserID=0&Placement=NativeDisplay&Source=NativeDisplay&interstitial=1) (From Brownstone Research) (Ad) \n![tc pixel](https://www.marketbeat.com/scripts/TriggeredCampaignPixel.ashx?TriggeredCampaignID=16919&Placement=NativeDisplay&Source=NativeDisplay)\n\n# Zcash Crypto Price Prediction, Value and Chart (ZEC)\n\n![Zcash logo](https://www.marketbeat.com/logos/cryptocurrencies/zcash-ZEC.png?v=2022-10-05)\n**$498.27** -3.24 (-0.65%) (As of 01/6/2026 10:07 PM ET)\n1-Hour Change **+0.8716%** 24-Hour Change **+0.8716%** 7-Day Range **$480.82▼$544.23** 1-Day Volume **$745.40 million** Market Cap **$8.21 billion** BTC Price **0.00536158 BTC** Circulating Supply **16.47 million** Total Supply **16.47 million** Maximum Supply **21.00 million** [Currency Profile](https://www.marketbeat.com/cryptocurrencies/zcash/#tabContentCurrencyProfile) [Headlines](https://www.marketbeat.com/cryptocurrencies/zcash/#tabContentHeadlines) [Advanced Chart](https://www.marketbeat.com/cryptocurrencies/zcash/#tabContentAdvancedChart) [Social Media](https://www.marketbeat.com/cryptocurrencies/zcash/#tabContentSocialMedia) 30 days | 90 days | 180 days | [Advanced Chart](https://www.marketbeat.com/cryptocurrencies/zcash/#) Receive ZEC News and Prices via Email\nSign-up to receive the latest news and price data for Zcash and its competitors with MarketBeat's CryptoBeat newsletter. Email Address \n![ZEC stock logo](https://www.marketbeat.com/logos/cryptocurrencies/zcash-ZEC.png?v=2022-10-05)\n\n## About Zcash (ZEC)\nZCash (ZEC) is a digital currency and decentralized open-source cryptocurrency, launched in 2016. It provides users with enhanced privacy and selective transparency of transactions. ZCash is based on the zero-knowledge proof protocol known as zk-SNARKs. This protocol allows the network to maintain a secure ledger of balances without disclosing the parties or amounts involved. Transactions can be audited, verified and tracked without revealing the sender, receiver or transaction amount. ZEC is an inflationary currency, with a maximum supply of 21 million coins. It is accepted by a growing number of merchants, exchanges and other services. \nDescription provided by CryptoCompare.\n\n## Zcash News\n[](https://www.benzinga.com/crypto/cryptocurrency/26/01/49736160/sol-ada-are-2025s-trades-this-privacy-coin-leads-the-2026-narrative) [SOL & ADA Are 2025's Trades—This Privacy Coin Leads The 2026 Narrative](https://www.benzinga.com/crypto/cryptocurrency/26/01/49736160/sol-ada-are-2025s-trades-this-privacy-coin-leads-the-2026-narrative) benzinga.com - January 6 at 3:10 PM [](https://seekingalpha.com/article/4857497-bitcoin-ethereum-solana-rebound-strongly-to-start-2026-crypto-overview?feed_item_type=article) [Bitcoin, Ethereum And Solana Rebound Strongly To Start 2026 - Crypto Overview](https://seekingalpha.com/article/4857497-bitcoin-ethereum-solana-rebound-strongly-to-start-2026-crypto-overview?feed_item_type=article) seekingalpha.com - January 6 at 1:24 PM [](https://www.newsbtc.com/bitcoin-news/bitcoin-wins-trump-pumps-gdp-suppresses-oil-hayes/) [Bitcoin Wins As Trump Pumps GDP, Suppresses Oil: Arthur Hayes](https://www.newsbtc.com/bitcoin-news/bitcoin-wins-trump-pumps-gdp-suppresses-oil-hayes/) newsbtc.com - January 6 at 12:07 PM [](https://blog.kraken.com/crypto-education/dentoshi-new-year-new-volatility) [Trading Spaces Recap: New year, new volatility? Dentoshi breaks down BTC, ETH and early signs of life in altcoins](https://blog.kraken.com/crypto-education/dentoshi-new-year-new-volatility) blog.kraken.com - January 6 at 12:07 PM [](https://bitcoinworld.co.in/bitcoin-rally-venezuela-policy-dollars/) [Bitcoin Rally Inevitable: Arthur Hayes Reveals How US Venezuela Policy Will Trigger Massive Dollar Printing](https://bitcoinworld.co.in/bitcoin-rally-venezuela-policy-dollars/) bitcoinworld.co.in - January 6 at 5:05 AM [](https://ambcrypto.com/zcash-why-zec-keeps-failing-at-520-despite-brief-rebounds/) [Zcash: Why ZEC keeps failing at $520 despite brief rebounds](https://ambcrypto.com/zcash-why-zec-keeps-failing-at-520-despite-brief-rebounds/) ambcrypto.com - January 6 at 2:05 AM [](https://invezz.com/news/2026/01/05/ethereums-5k-path-divides-experts-ahead-of-2026/) [Ethereum’s $5K path divides experts ahead of 2026](https://invezz.com/news/2026/01/05/ethereums-5k-path-divides-experts-ahead-of-2026/) invezz.com - January 5 at 5:08 PM [](https://www.investing.com/analysis/zcash-enjoys-strong-support-at-0618-fib-level-despite-recent-pullback-200672696) [Zcash Enjoys Strong Support at 0.618 Fib Level, Despite Recent Pullback](https://www.investing.com/analysis/zcash-enjoys-strong-support-at-0618-fib-level-despite-recent-pullback-200672696) investing.com - January 5 at 4:10 PM [](https://cryptopotato.com/crypto-funds-pull-in-47-2b-in-2025-but-bitcoin-loses-ground/) [Crypto Funds Pull In $47.2B in 2025, But Bitcoin Loses Ground](https://cryptopotato.com/crypto-funds-pull-in-47-2b-in-2025-but-bitcoin-loses-ground/) cryptopotato.com - January 5 at 3:11 PM [](https://www.cryptopolitan.com/zec-gets-unshielded-privacy-investors-exit/) [ZEC retraces gains as whale unshields 1% of supply](https://www.cryptopolitan.com/zec-gets-unshielded-privacy-investors-exit/) cryptopolitan.com - January 5 at 9:22 AM [](https://themerkle.com/markets-look-past-zcash-and-chainlink-as-blockdags-0-40-launch-speculation-comes-into-play-now/) [Markets Look Past Zcash and Chainlink as BlockDAG’s $0.40 Launch Speculation Comes Into Play Now](https://themerkle.com/markets-look-past-zcash-and-chainlink-as-blockdags-0-40-launch-speculation-comes-into-play-now/) themerkle.com - January 3 at 1:11 PM [](https://bitcoinworld.co.in/zec-whale-deposit-binance-analysis/) [ZEC Whale Deposit: A Staggering $35.75M Move to Binance Sparks Market Scrutiny](https://bitcoinworld.co.in/zec-whale-deposit-binance-analysis/) bitcoinworld.co.in - January 3 at 7:07 AM [](https://ambcrypto.com/ethereums-2026-roadmap-puts-institutional-privacy-front-and-center-details/) [Ethereum’s 2026 roadmap puts institutional privacy front and center – Details](https://ambcrypto.com/ethereums-2026-roadmap-puts-institutional-privacy-front-and-center-details/) ambcrypto.com - January 2 at 7:05 AM [](https://thecryptobasic.com/2026/01/02/bitwise-snubs-cardano-in-new-crypto-etftracking-tron-zec-and-9-others/) [Bitwise Snubs Cardano In New Crypto ETFTracking Tron, ZEC, and 9 Others](https://thecryptobasic.com/2026/01/02/bitwise-snubs-cardano-in-new-crypto-etftracking-tron-zec-and-9-others/) thecryptobasic.com - January 2 at 5:10 AM [](https://www.tipranks.com/news/zcash-surged-600-in-2025-here-are-4-predictions-for-on-chain-privacy-in-2026) [Zcash Surged 600% in 2025. Here Are 4 Predictions for On-chain Privacy in 2026](https://www.tipranks.com/news/zcash-surged-600-in-2025-here-are-4-predictions-for-on-chain-privacy-in-2026) tipranks.com - January 1 at 12:31 PM [](https://finbold.com/the-next-big-wave-2-new-cryptos-set-to-dominate-in-2026/) [The next big wave: 2 new cryptos set to dominate in 2026](https://finbold.com/the-next-big-wave-2-new-cryptos-set-to-dominate-in-2026/) finbold.com - January 1 at 9:08 AM [](https://invezz.com/news/2026/01/01/zcash-exploded-this-year-2-privacy-coins-to-watch-in-2026/) [Zcash exploded this year: 2 privacy coins to watch in 2026](https://invezz.com/news/2026/01/01/zcash-exploded-this-year-2-privacy-coins-to-watch-in-2026/) invezz.com - January 1 at 8:05 AM [](https://cryptopotato.com/bitwise-files-for-11-altcoin-etfs-targeting-aave-uni-sui-more/) [Bitwise Files for 11 Altcoin ETFs Targeting AAVE, UNI, SUI, More](https://cryptopotato.com/bitwise-files-for-11-altcoin-etfs-targeting-aave-uni-sui-more/) cryptopotato.com - December 31 at 5:09 PM [](https://bitcoinist.com/bitcoin-ethereum-crypto/) [Forget Bitcoin And Ethereum: Here Are The Cryptocurrencies That Made Gains In Q4](https://bitcoinist.com/bitcoin-ethereum-crypto/) bitcoinist.com - December 31 at 5:06 PM [](https://cryptonews.com/news/best-altcoins-to-buy-on-new-years-eve-that-could-100x-in-2026-31-december-2025/) [Best Altcoins To Buy On New Year’s Eve That Could 100x in 2026 – 31 December 2025](https://cryptonews.com/news/best-altcoins-to-buy-on-new-years-eve-that-could-100x-in-2026-31-december-2025/) cryptonews.com - December 31 at 3:14 PM [](https://en.coin-turk.com/altcoins-break-crucial-boundaries-in-2025/) [Altcoins Break Crucial Boundaries in 2025](https://en.coin-turk.com/altcoins-break-crucial-boundaries-in-2025/) en.coin-turk.com - December 31 at 2:17 PM [](https://coinpaper.com/13480/could-zcash-really-hit-10-000-arthur-hayes-prediction-is-back-in-focus) [Could Zcash Really Hit $10,000? Arthur Hayes’ Prediction Is Back in Focus](https://coinpaper.com/13480/could-zcash-really-hit-10-000-arthur-hayes-prediction-is-back-in-focus) coinpaper.com - December 31 at 10:25 AM [](https://u.today/morning-crypto-report-ripple-usd-stablecoin-deletes-21804950-from-circulation-100000-for-bitcoin-in) [Morning Crypto Report: Ripple USD Stablecoin Deletes $21,804,950 From Circulation, $100,000 for Bitcoin in January Is Not Surreal, Bitwise Files for ETF on Zcas...](https://u.today/morning-crypto-report-ripple-usd-stablecoin-deletes-21804950-from-circulation-100000-for-bitcoin-in) u.today - December 31 at 7:12 AM [](https://cryptonews.com/news/why-is-crypto-up-today-december-31-2025/) [Why Is Crypto Up Today? – December 31, 2025](https://cryptonews.com/news/why-is-crypto-up-today-december-31-2025/) cryptonews.com - December 31 at 7:12 AM [](https://www.coindesk.com/business/2025/12/31/winklevoss-backed-cypherpunk-buys-usd28-million-of-zcash-now-owns-1-7-of-supply) [Winklevoss-backed Cypherpunk buys $28 million of zcash, now owns 1.7% of supply](https://www.coindesk.com/business/2025/12/31/winklevoss-backed-cypherpunk-buys-usd28-million-of-zcash-now-owns-1-7-of-supply) coindesk.com - December 31 at 5:08 AM [](https://coinpaper.com/13470/cypherpunk-doubles-down-on-zcash-with-29-m-treasury-buy) [Cypherpunk Doubles Down on Zcash With $29M Treasury Buy](https://coinpaper.com/13470/cypherpunk-doubles-down-on-zcash-with-29-m-treasury-buy) coinpaper.com - December 31 at 4:15 AM [](https://square.htx.com/htx-hot-listings-weekly-recap-dec-22-28-sees-zbt-surge-127-payai-rally-103-ai-and-privacy-narratives-reignite/) [HTX Hot Listings Weekly Recap (Dec 22-28) Sees ZBT Surge 127%, PAYAI Rally 103% | AI and Privacy Narratives Reignite](https://square.htx.com/htx-hot-listings-weekly-recap-dec-22-28-sees-zbt-surge-127-payai-rally-103-ai-and-privacy-narratives-reignite/) square.htx.com - December 31 at 3:08 AM [](https://ambcrypto.com/zcash-leads-q4-privacy-rally-analyst-foresees-zec-at-1000/) [Zcash leads Q4 privacy rally – Analyst foresees ZEC at $1,000](https://ambcrypto.com/zcash-leads-q4-privacy-rally-analyst-foresees-zec-at-1000/) ambcrypto.com - December 31 at 1:10 AM [](https://bitcoinworld.co.in/bitwise-files-11-crypto-etfs/) [Bitwise Crypto ETFs: A Bold Leap with 11 New Funds Including AAVE and UNI](https://bitcoinworld.co.in/bitwise-files-11-crypto-etfs/) bitcoinworld.co.in - December 30 at 9:30 PM [](https://cryptonews.com/news/zcash-cypherpunk-corporate-treasury-play-bitcoin/) [Is Zcash the Next Corporate Treasury Play? Cypherpunk Now Holds Nearly 2%](https://cryptonews.com/news/zcash-cypherpunk-corporate-treasury-play-bitcoin/) cryptonews.com - December 30 at 6:31 PM [](https://cointelegraph.com/news/privacy-prevailed-q4-crypto-grayscale) [How privacy prevailed in an otherwise dismal Q4 for crypto](https://cointelegraph.com/news/privacy-prevailed-q4-crypto-grayscale) cointelegraph.com - December 30 at 2:33 PM [](https://cryptonews.com/news/best-meme-coins-to-buy-before-new-year-that-could-100x-in-2026-30-december-2025/) [Best Meme Coins To Buy Before New Year That Could 100x in 2026 – 30 December 2025](https://cryptonews.com/news/best-meme-coins-to-buy-before-new-year-that-could-100x-in-2026-30-december-2025/) cryptonews.com - December 30 at 2:33 PM [](https://cointelegraph.com/news/cypherpunk-crypto-treasury-29m-zcash-purchase) [Cypherpunk lifts crypto treasury with $29M Zcash purchase](https://cointelegraph.com/news/cypherpunk-crypto-treasury-29m-zcash-purchase) cointelegraph.com - December 30 at 1:35 PM [](https://invezz.com/news/2025/12/30/cypherpunk-doubles-down-on-zcash-as-treasury-hits-290062-zec/) [Cypherpunk doubles down on Zcash as treasury hits 290,062 ZEC](https://invezz.com/news/2025/12/30/cypherpunk-doubles-down-on-zcash-as-treasury-hits-290062-zec/) invezz.com - December 30 at 10:31 AM [](https://www.tipranks.com/news/company-announcements/cypherpunk-technologies-expands-zcash-holdings-in-major-purchase) [Cypherpunk Technologies Expands Zcash Holdings in Major Purchase](https://www.tipranks.com/news/company-announcements/cypherpunk-technologies-expands-zcash-holdings-in-major-purchase) tipranks.com - December 30 at 9:31 AM [](https://bitcoinworld.co.in/cypherpunk-technologies-zec-investment-winklevoss/) [ZEC Investment Soars: Cypherpunk Technologies’ Strategic $29M Acquisition Signals Major Confidence](https://bitcoinworld.co.in/cypherpunk-technologies-zec-investment-winklevoss/) bitcoinworld.co.in - December 30 at 9:28 AM [](https://www.cryptopolitan.com/privacy-tokens-defy-negative-headwind/) [Grayscale highlighted the growing preference for privacy-focused cryptocurrencies](https://www.cryptopolitan.com/privacy-tokens-defy-negative-headwind/) cryptopolitan.com - December 30 at 8:06 AM [](https://en.coinotag.com/zcash-leads-privacy-coins-surge-in-q4-2025-despite-market-headwinds) [Zcash Leads Privacy Coins Surge in Q4 2025 Despite Market Headwinds](https://en.coinotag.com/zcash-leads-privacy-coins-surge-in-q4-2025-despite-market-headwinds) en.coinotag.com - December 30 at 8:06 AM [](https://www.prnewswire.com/news-releases/cypherpunk-accelerates-zcash-accumulation-increases-treasury-holdings-to-290-062-67-zec-302650408.html) [Cypherpunk Accelerates Zcash Accumulation; Increases Treasury Holdings to 290,062.67 ZEC](https://www.prnewswire.com/news-releases/cypherpunk-accelerates-zcash-accumulation-increases-treasury-holdings-to-290-062-67-zec-302650408.html) prnewswire.com - December 30 at 7:31 AM [](https://www.cryptopolitan.com/dragonflys-haseeb-qureshi-btc-hit/) [Haseeb Qureshi predicts $150K bitcoin in 2026 as big tech wallets emerge](https://www.cryptopolitan.com/dragonflys-haseeb-qureshi-btc-hit/) cryptopolitan.com - December 30 at 5:11 AM [](https://bitcoinist.com/dragonfly-qureshi-crypto-predictions-for-2026/) [Dragonfly’s Haseeb Qureshi Unveils His Crypto Predictions For 2026](https://bitcoinist.com/dragonfly-qureshi-crypto-predictions-for-2026/) bitcoinist.com - December 30 at 5:11 AM [](https://bitcoinworld.co.in/beldex-price-prediction-2026-2030/) [Beldex Price Prediction 2026-2030: Unveiling the Potential Hidden Gem in Privacy-Focused Cryptocurrencies](https://bitcoinworld.co.in/beldex-price-prediction-2026-2030/) bitcoinworld.co.in - December 30 at 2:05 AM [](https://invezz.com/news/2025/12/29/why-most-altcoins-fell-in-2025-and-how-xrp-zcash-and-algorand-defied-the-trend/) [Why most altcoins fell in 2025, and how XRP, Zcash, and Algorand defied the trend](https://invezz.com/news/2025/12/29/why-most-altcoins-fell-in-2025-and-how-xrp-zcash-and-algorand-defied-the-trend/) invezz.com - December 29 at 5:07 PM [](https://www.newsbtc.com/analysis/zec/zcash-rallied-above-500/) [Here’s Why The ZCash (ZEC) Price Rallied Above $500 Again](https://www.newsbtc.com/analysis/zec/zcash-rallied-above-500/) newsbtc.com - December 29 at 4:19 PM [](https://en.coinotag.com/zcash-kraken-withdrawal-may-herald-upside-as-shorts-face-liquidation-stress) [Zcash Kraken Withdrawal May Herald Upside as Shorts Face Liquidation Stress](https://en.coinotag.com/zcash-kraken-withdrawal-may-herald-upside-as-shorts-face-liquidation-stress) en.coinotag.com - December 29 at 3:10 PM [](https://cointelegraph.com/news/zcash-price-first-stop-1k-arthur-hayes) [Zcash price has 'first stop' at $1K: Arthur Hayes](https://cointelegraph.com/news/zcash-price-first-stop-1k-arthur-hayes) cointelegraph.com - December 29 at 12:14 PM [](https://cointelegraph.com/news/xrp-zcash-algorand-outperformed-2025-altcoin-slump) [These three altcoins came back from the dead in 2025](https://cointelegraph.com/news/xrp-zcash-algorand-outperformed-2025-altcoin-slump) cointelegraph.com - December 29 at 9:10 AM [](https://u.today/morning-crypto-report-bitcoins-uh-oh-pattern-returns-as-zcash-zec-pumps-again-xrp-prints-0-after) [Morning Crypto Report: Bitcoin’s “Uh Oh” Pattern Returns as Zcash (ZEC) Pumps Again, XRP Prints $0 After Short Sellers Disappear, Forgotten Bitcoin Rival May Re...](https://u.today/morning-crypto-report-bitcoins-uh-oh-pattern-returns-as-zcash-zec-pumps-again-xrp-prints-0-after) u.today - December 29 at 7:14 AM [](https://ambcrypto.com/zcash-zec-builds-pressure-as-4-12-mln-exits-kraken-is-a-squeeze-forming/) [Zcash [ZEC] builds pressure as $4.12 mln exits Kraken – Is a squeeze forming?](https://ambcrypto.com/zcash-zec-builds-pressure-as-4-12-mln-exits-kraken-is-a-squeeze-forming/) ambcrypto.com - December 29 at 7:14 AM [](https://en.coinotag.com/zcash-rally-tops-solana-volumes-privacy-narrative-may-drive-further-gains) [Zcash Rally Tops Solana Volumes, Privacy Narrative May Drive Further Gains](https://en.coinotag.com/zcash-rally-tops-solana-volumes-privacy-narrative-may-drive-further-gains) en.coinotag.com - December 28 at 10:06 PM [See All Recent Headlines](https://www.marketbeat.com/cryptocurrencies/zcash/#) \n## Zcash Currency Details\nName **Zcash** Symbol **ZEC** Market Capitalization **$8.21 billion** Coin or Token **Coin** Algorithm **Equihash** Proof Type **PoW** Genesis Date **10/28/2016** Mineable? **Yes** \n### Official Links\nOfficial Website **z.cash** Official Website (Alt) **N/A** BitcoinTalk Announcement **View** Twitter Account **@electriccoinco** Facebook Page **View** Github Account **View** \n### Community Discussion\nReddit Community **r/zec** Telegram Group **View** Discord Group **View** Message Board **forum.z.cash** Message Board (Alt) **N/A** \n### Research Tools\nBlockchain Explorer **zcashblockexplorer.com** Blockchain Explorer (Alt) **app.nansen.ai** CoinMarketCap **View** CryptoCompare **View** CoinGecko **View** \n## About Zcash (ZEC)\n\n## Zcash (ZEC) Frequently Asked Questions\nHow do I buy Zcash?\n\nIt is not possible to buy all cryptocurrencies with U.S. dollars. Bitcoin, Bitcoin Cash, Ethereum, Litecoin and other popular cryptocurrencies can be purchased with U.S. dollars using Coinbase. Once you have purchased Bitcoin using Coinbase, you can then transfer your Bitcoin to an exchange such as Binance to purchase other cryptocurrencies, including Zcash.\nWhat do investment analysts think about Zcash?\n\nWeiss Research, an investment research firm that rates cryptocurrencies, has given Zcash an overall rating of \"C\", a technology and adoption rating of \"B-\", and a market performance rating of \"D-\".\nWhat technology is included in Zcash?\n\nzk-SNARKsThe BasicZcash is the first widespread application of zk-SNARKs, a novel form of zero-knowledge cryptography. The strong privacy guarantee of Zcash is derived from the fact that shielded transactions in Zcash can be fully encrypted on the blockchain, yet still be verified as valid under the network’s consensus rules by using zk-SNARK proofs. The acronym zk-SNARK stands for “Zero-Knowledge Succinct Non-Interactive Argument of Knowledge,” and refers to a proof construction where one can prove possession of certain information, e.g. a secret key, without revealing that information, and without any interaction between the prover and verifier. “Zero-knowledge” proofs allow one party (the prover) to prove to another (the verifier) that a statement is true, without revealing any information beyond the validity of the statement itself. For example, given the hash of a random number, the prover could convince the verifier that there indeed exists a number with this hash value, without revealing what it is. Application to ZCASHIn order to have zero-knowledge privacy in Zcash, the function determining the validity of a transaction according to the network’s consensus rules must return the answer of whether the transaction is valid or not, without revealing any of the information it performed the calculations on. This is done by encoding some of the network's consensus rules in zk-SNARKs. At a high level, zk-SNARKs work by first turning what you want to prove into an equivalent form about knowing a solution to some algebraic equations. In the following section, we give a brief overview of how the rules for determining a valid transaction get transformed into equations that can then be evaluated on a candidate solution without revealing any sensitive information to the parties verifying the equations. (Information provided by CryptoCompare.)\nWhere can I get Zcash wallet?\n\nZcash produces its own wallet software that is available for download on its website, which allows you to store Zcash on your computer. For maximum security, you can store your cryptocurrencies on a dedicated hardware wallet such as a TREZOR wallet or a Ledger Nano X. If you do not wish to buy a hardware wallet, you may consider using a mobile wallet such as Atomic Wallet, Jaxx, or Coinomi to store multiple cryptocurrencies with some added security benefits.\nWhat is the value of Zcash?\n\nOne Zcash (ZEC) is currently worth $515.54 on major cryptocurrency exchanges. You can also exchange one Zcash for 0.00548422 bitcoin(s) on major exchanges. The value (or market capitalization) of all available Zcash in U.S. dollars is $8.49 billion.\nWhat hashing algorithm does Zcash use?\n\nZcash is a proof of work (PoW) coin that uses the Equihash algorithm.\nHow do I mine Zcash?\n\nZcash can be mined using specialized mining software. XMR Stak is a commonly-used mining tool that works for CPU mining and GPU mining with both Nvidia and AMD graphics cards. CCMiner is another popular mining tool for computers with NVIDIA graphics cards. In addition to having mining software, you will need a Zcash and access to a mining pool that pools your effort with other miners and a wallet to store the Zcash that you earn from mining. Most cryptocurrencies have multiple publicly-available mining pools that can be found with a simple Google search.\nWhat coins are similar to Zcash?\n\nThe following coins use the same hashing algorithm (Equihash) as Zcash: Horizen, Pirate Chain, Bitcoin Gold, Komodo, ZClassic and Bitcoin Private.\nWhat is the Reddit page for Zcash?\n\nThe official Reddit community (subreddit) for Zcash is https://reddit.com/r/zec.\n\n## Zcash (ZEC) Price Chart for Tuesday, January, 6, 2026\n\n## Zcash (ZEC) Twitter Feed\n[Tweets by @electriccoinco](https://twitter.com/electriccoinco?ref_src=twsrc^tfw) Loading…\n\n## Zcash (ZEC) Reddit Feed\n*This page was last updated on 1/6/2026 by MarketBeat.com Staff* Adding Zcash\n\nPlease log in to your account or sign up in order to add this asset to your watchlist.\n[Log In and Add](https://www.marketbeat.com/login/?cmd=cryptocreate&symbol=zcash) Adding\nChoose a watchlist:\nWatchlist Adding\n\nYou have already added ten holdings to your watchlist. Upgrade to MarketBeat All Access to add more holdings to your watchlist.\nShare Zcash With A Colleague\n[](https://www.facebook.com/sharer/sharer.php?u=https%3a%2f%2fwww.marketbeat.com%2fcryptocurrencies%2fzcash%2f) [](https://twitter.com/intent/tweet?text=Zcash+Crypto+Price+Headlines%2c+Value+and+Chart+(ZEC)+https%3a%2f%2fwww.marketbeat.com%2fcryptocurrencies%2fzcash%2f) [](https://www.linkedin.com/cws/share?mini=true&amp%3burl=https%3a%2f%2fwww.marketbeat.com%2fcryptocurrencies%2fzcash%2f) [](https://api.stocktwits.com/widgets/share?via=MarketBeat&amp%3bbody=Zcash+Crypto+Price+Headlines%2c+Value+and+Chart+(ZEC)+https%3a%2f%2fwww.marketbeat.com%2fcryptocurrencies%2fzcash%2f) [](https://www.marketbeat.com/cryptocurrencies/zcash/) Link copied to clipboard.\nGet 30 Days of MarketBeat All Access for Free \nSign up for MarketBeat All Access to gain access to MarketBeat's full suite of research tools.\n[Start Your 30-Day Trial](https://www.marketbeat.com/subscribe/all-access/?referraltype=masterfooter) \n## MarketBeat All Access Features\n[Best-in-Class Portfolio Monitoring Get personalized stock ideas. Compare portfolio to indices. Check stock news, ratings, SEC filings, and more.](https://www.marketbeat.com/subscribe/all-access/?referraltype=masterfooter) [Stock Ideas and Recommendations See daily stock ideas from top analysts. Receive short-term trading ideas from MarketBeat. Identify trending stocks on social media.](https://www.marketbeat.com/subscribe/all-access/?referraltype=masterfooter) [Advanced Stock Screeners and Research Tools Use our seven stock screeners to find suitable stocks. Stay informed with MarketBeat's real-time news. Export data to Excel for personal analysis.](https://www.marketbeat.com/subscribe/all-access/?referraltype=masterfooter) Sign in to your free account to enjoy these benefits - In-depth profiles and analysis for 20,000 public companies.\n- Real-time analyst ratings, insider transactions, earnings data, and more.\n- Our daily ratings and market update email newsletter.\nSign in to your free account to enjoy all that MarketBeat has to offer. - Sign In\n- Create Account\n- \nYour Email Address: Email Address Required Your Password: Password Required Log In or [Sign in with Facebook](https://www.marketbeat.com/cryptocurrencies/zcash/#) [Sign in with Google](https://www.marketbeat.com/cryptocurrencies/zcash/#) [Forgot your password?](https://www.marketbeat.com/forgot-password/) Your Email Address: Please enter your email address. Please enter a valid email address Choose a Password: Please enter your password. Your password must be at least 8 characters long and contain at least 1 number, 1 letter, and 1 special character. or [Sign in with Facebook](https://www.marketbeat.com/cryptocurrencies/zcash/#) [Sign in with Google](https://www.marketbeat.com/cryptocurrencies/zcash/#) By creating a free account, you agree to our [terms of service.](https://www.marketbeat.com/terms/) This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.\n</searchResult>\n\n\n<searchResult>\n[doc4]:\n**Latest Zcash News - (ZEC) Future Outlook, Trends & Market Insights**\n[](https://coinmarketcap.com/) [Cryptocurrencies](https://coinmarketcap.com/) Cryptocurrencies\n[Ranking](https://coinmarketcap.com/) [Categories](https://coinmarketcap.com/cryptocurrency-category/) [Historical Snapshots](https://coinmarketcap.com/historical/) [Token unlocks](https://coinmarketcap.com/token-unlocks/) [Yield](https://coinmarketcap.com/yield/) [Real-World Assets](https://coinmarketcap.com/real-world-assets/) Leaderboards\n[Trending](https://coinmarketcap.com/trending-cryptocurrencies/) [Upcoming](https://coinmarketcap.com/upcoming/) [Recently Added](https://coinmarketcap.com/new/) [Gainers & Losers](https://coinmarketcap.com/gainers-losers/) [Most Visited](https://coinmarketcap.com/most-viewed-pages/) [Community Sentiment](https://coinmarketcap.com/sentiment/) [Chain Ranking](https://coinmarketcap.com/chain-ranking/) NFT\n[Overall NFT Stats](https://coinmarketcap.com/nft/) [Upcoming Sales](https://coinmarketcap.com/nft/upcoming/) [Dashboards](https://coinmarketcap.com/charts/) Markets\n[Market Overview](https://coinmarketcap.com/charts/) [Spot Market](https://coinmarketcap.com/charts/spot-market/) [Derivatives Market](https://coinmarketcap.com/charts/derivatives-market/) [No. of Cryptocurrencies](https://coinmarketcap.com/charts/number-of-cryptocurrencies-tracked/) [BNB Treasuries](https://coinmarketcap.com/charts/bnb-treasuries/) Indicators\n[Fear and Greed Index](https://coinmarketcap.com/charts/fear-and-greed-index/) [Altcoin Season Index](https://coinmarketcap.com/charts/altcoin-season-index/) [Market Cycle Indicators](https://coinmarketcap.com/charts/crypto-market-cycle-indicators/) [Bitcoin Dominance](https://coinmarketcap.com/charts/bitcoin-dominance/) [CoinMarketCap 20 Index](https://coinmarketcap.com/charts/cmc20/) [CoinMarketCap 100 Index](https://coinmarketcap.com/charts/cmc100/) ETF Flows\n[Crypto ETFs](https://coinmarketcap.com/etf/) [Bitcoin ETFs](https://coinmarketcap.com/etf/bitcoin/) [Ethereum ETFs](https://coinmarketcap.com/etf/ethereum/) Technical Analysis\n[RSI](https://coinmarketcap.com/charts/rsi/) [MACD](https://coinmarketcap.com/charts/macd/) Derivatives\n[Funding Rates](https://coinmarketcap.com/charts/funding-rates/) [DexScan](https://dex.coinmarketcap.com/token/all/) [SignalsNew](https://dex.coinmarketcap.com/signals/all/) [Trending](https://dex.coinmarketcap.com/token/all/) [New](https://dex.coinmarketcap.com/token/all/?tableRankBy=new_24h) [Gainers](https://dex.coinmarketcap.com/token/all/?tableRankBy=gainers_24h) [Meme Explorer](https://dex.coinmarketcap.com/meme/four.meme/) [Top Traders](https://dex.coinmarketcap.com/top-traders/all/) [Exchanges](https://coinmarketcap.com/rankings/exchanges/) Centralized Exchanges\n[Spot](https://coinmarketcap.com/rankings/exchanges/) [Derivatives](https://coinmarketcap.com/rankings/exchanges/derivatives/) Decentralized Exchanges\n[Spot](https://coinmarketcap.com/rankings/exchanges/dex/?type=spot) [Derivatives](https://coinmarketcap.com/rankings/exchanges/dex/?type=derivatives) [Community](https://coinmarketcap.com/community/) [Feeds](https://coinmarketcap.com/community/) [Topics](https://coinmarketcap.com/community/topics/) [Lives](https://coinmarketcap.com/community/lives/) [Articles](https://coinmarketcap.com/community/articles/) [Sentiment](https://coinmarketcap.com/sentiment/) Products Products\n[Converter](https://coinmarketcap.com/converter/) [Newsletter](https://coinmarketcap.com/newsletter/) [CMC Launch](https://coinmarketcap.com/cmclaunch/) [CMC Labs](https://coinmarketcap.com/events/cmc-labs/) [Telegram Bot](https://coinmarketcap.com/chatbot/) [Advertise](https://coinmarketcap.com/events/advertise/) [Crypto API](https://coinmarketcap.com/api/) [Site Widgets](https://coinmarketcap.com/widget/ticker/) Campaigns\n[Airdrops](https://coinmarketcap.com/airdrop/) [Diamond Rewards](https://coinmarketcap.com/account/rewards/) [Learn & Earn](https://coinmarketcap.com/earn/) Calendars\n[ICO Calendar](https://coinmarketcap.com/ico-calendar/) [Events Calendar](https://coinmarketcap.com/events/) Learn\n[News](https://coinmarketcap.com/headlines/news/) [Academy](https://coinmarketcap.com/academy/) [Research](https://coinmarketcap.com/academy/categories/cmc-research/) [Videos](https://www.youtube.com/channel/UCnhdZlwVd6ocXGhdSyV9Axg/?sub_confirmation=1) [Glossary](https://coinmarketcap.com/academy/glossary/) \n# Latest Zcash (ZEC) News Update\nBy CMC AI 06 January 2026 12:16AM (UTC+0) [See ZEC Price Chart](https://coinmarketcap.com/currencies/zcash/#cmcaiquestion=0) \n## What is the latest news on ZEC?\n\n## TLDR\n\nZcash navigates bullish technicals and whale-sized bets as privacy narratives gain steam. Here are the latest news:\n1. Bull Flag Holds Despite Weakness (6 January 2026) – ZEC’s bullish structure remains intact, but weakening momentum signals caution.\n2. Whale Bets $39M on ZEC Long (5 January 2026) – A crypto whale opened a leveraged position equivalent to 1.2% of ZEC’s circulating supply.\n3. Grayscale Zcash Trust Discount Widens (5 January 2026) – Shares trade 25% below net asset value despite rising institutional interest.\n\n## Deep Dive\n\n### 1. Bull Flag Holds Despite Weakness (6 January 2026)\n\nOverview: ZEC maintains a bullish market structure with an 85% upside target ($930+) if it holds above $404 support. However, momentum indicators like the Chaikin Money Flow (CMF) near zero suggest weakening buying pressure.\n\nWhat this means: The technical setup is bullish long-term but faces headwinds from Bitcoin’s negative correlation with ZEC and $39M in short-term short leverage. A break below $404 could trigger a deeper correction. (TokenPost)\n\n### 2. Whale Bets $39M on ZEC Long (5 January 2026)\n\nOverview: Address 0x6b26 opened a 5x leveraged long position with 79,438 ZEC ($39.24M) on Binance, risking amplified volatility.\n\nWhat this means: Large leveraged positions increase liquidation risks—$54M in shorts vs. $24M longs sit near current prices. While this signals confidence, the whale already faces a $1.88M unrealized loss, raising concerns about forced selling. (Binance News)\n\n### 3. Grayscale Zcash Trust Discount Widens (5 January 2026)\n\nOverview: Grayscale’s Zcash Trust (ZCSH) shares trade at a 25% discount to NAV despite holding $190M in ZEC, reflecting skepticism about near-term liquidity improvements.\n\nWhat this means: The widening gap between institutional and spot prices highlights ZEC’s regulatory ambiguity but could create arbitrage opportunities if ETF conversion rumors materialize. (CoinMarketCap)\n\n## Conclusion\n\nZcash balances bullish technicals against whale-driven volatility and institutional hesitancy. While its privacy tech attracts believers, the market awaits clarity: Will shielded transaction growth (now 20-25% of supply) offset Bitcoin’s gravitational pull on prices?\n\n## What are people saying about ZEC?\n\n## TLDR\n\nZcash's community oscillates between breakout euphoria and correction jitters, with privacy tech hype clashing with technical caution. Here’s what’s trending:\n1. Traders debate if ZEC’s consolidation is a bull trap or springboard\n2. Institutions bet big while retail eyes $550 prediction markets\n3. Technical charts flash conflicting signals across timeframes\n\n## Deep Dive\n\n### 1. @earlyadopterz: “Inverse Bitcoin hedge” thesis gains traction 🚀\n\n“When Bitcoin gets flushed down, Zcash will blast off... ZEC is the hedge”– @earlyadopterz (7.1K followers · 14M impressions · 2026-01-02 16:13 UTC)View original postWhat this means: Bullish for ZEC as some view it as a counter-cyclical play against Bitcoin volatility. The narrative gained traction after ZEC rose 2.8% while BTC dipped 0.4% on January 2.\n\n### 2. @VipRoseTr: Rising wedge warns of 42% drop 📉\n\n“ZEC forming bearish pattern – breakdown below support targets $289”– @VipRoseTr (63.4K followers · 8.2M impressions · 2025-12-27 13:53 UTC)View original postWhat this means: Bearish technical outlook as ZEC struggles at $519 resistance (current price $501). The pattern’s measured move aligns with the 38.2% Fibonacci retracement of its 295% 90-day rally.\n\n### 3. @MusicByVirtuals: Prediction market shows skepticism 🎯\n\n“85.8% bet ZEC stays below $550 through EOY 2025”– @MusicByVirtuals (6.1K followers · 3.1M impressions · 2025-11-28 14:56 UTC)View original postWhat this means: Neutral-bearish sentiment despite ZEC’s 47.9% 30-day gain. The crowd doubts sustainability of recent momentum, though the poll closed before January’s Grayscale Trust accumulation news.\n\n## Conclusion\n\nThe consensus on Zcash is mixed – bullish on privacy adoption narratives but wary of stretched valuations. While institutions like Grayscale’s $190M Zcash Trust signal long-term conviction, derivatives data shows $54M in vulnerable short positions that could fuel volatility. Watch the $404 support level: A hold above maintains the ascending triangle pattern targeting $630, while a breakdown might confirm the bearish wedge toward $300. With 29% of ZEC’s supply now in shielded pools, regulatory clarity remains the ultimate make-or-break factor.\n\n## What is the latest update in ZEC’s codebase?\n\n## TLDR\n\nZcash's codebase advances privacy and node infrastructure.\n1. NU6.1 Activation (Oct 2025) – Enabled shielded transaction upgrades and fee optimizations.\n2. Zcashd Deprecation (Apr 2025) – Migration to Zebra nodes and Zallet wallet underway.\n3. Zashi 2.0.3 (Apr 2025) – Streamlined shielded addresses and cross-chain swaps.\n\n## Deep Dive\n\n### 1. NU6.1 Activation (Oct 2025)\n\nOverview: Implemented ZIPs 317 and 320, refining fee structures and transparent address formats.This upgrade introduced a new transaction version (v5) as the default, reducing fees for shielded transfers by ~30% through optimized proof bundling. It also added stricter mempool rules to prevent spam transactions.\n\nWhat this means: This is bullish for ZEC because lower fees and improved spam resistance make private transactions more accessible and scalable. (Source)\n\n### 2. Zcashd Deprecation (Apr 2025)\n\nOverview: Phasing out the legacy C++ client (zcashd) in favor of Rust-based Zebra nodes and Zallet wallet.Key RPC methods like z_getbalance were deprecated, with users urged to migrate before August 2025. Zebra offers faster sync times and modular architecture.\n\nWhat this means: This is neutral for ZEC – while modernization improves long-term maintainability, migration complexities could temporarily strain ecosystem tools. (Source)\n\n### 3. Zashi 2.0.3 (Apr 2025)\n\nOverview: Wallet update defaulting to shielded addresses and integrating Maya DEX for cross-chain swaps.The redesign simplified sending private transactions and added auto-shielding of transparent balances. Over 15% more ZEC moved to shielded pools post-update.\n\nWhat this means: This is bullish for ZEC because frictionless privacy strengthens its core value proposition amid regulatory scrutiny. (Source)\n\n## Conclusion\n\nZcash’s updates prioritize privacy usability and infrastructure resilience, aligning with its role as a compliance-friendly anonymity tool. With shielded adoption rising and node modernization complete, how will ZEC balance regulatory pressures against its technological edge in 2026?\n\n## What is next on ZEC’s roadmap?\n\n## TLDR\n\nZcash's development roadmap focuses on privacy enhancements, ecosystem expansion, and governance upgrades through early 2026.\n1. Zashi Wallet 2.0 (Q1 2026) – Shielded swaps and cross-chain DeFi integration.\n2. Ztarknet Devnet Launch (Q1 2026) – Privacy-preserving smart contracts.\n3. Governance Model Overhaul (2026) – Streamlined development funding.\n\n## Deep Dive\n\n### 1. Zashi Wallet 2.0 (Q1 2026)\n\nOverview:The Zashi wallet will enable fully shielded swaps via NEAR Protocol’s Intents, allowing users to privately convert assets like BTC or ETH into shielded ZEC without intermediaries. This follows the November 2025 integration that simplified shielded-to-transparent transactions.\n\nWhat this means:Bullish for ZEC adoption, as frictionless privacy could attract users seeking compliance-friendly anonymity. Risks include potential delays in cross-chain refund privacy features.\n\n### 2. Ztarknet Devnet Launch (Q1 2026)\n\nOverview:Ztarknet, a Starknet-inspired Layer-2 rollup, will bring programmable smart contracts to Zcash using Circle-STARK proofs. This allows private computation off-chain while settling on Zcash’s base layer, maintaining shielded pool integrity (Eli5defi, Nov 2025).\n\nWhat this means:Neutral-to-bullish – while this expands Zcash’s utility beyond simple payments, adoption depends on developer uptake. Success could position ZEC as a privacy-centric smart contract platform.\n\n### 3. Governance Model Overhaul (2026)\n\nOverview:Community proposals aim to replace Zcash’s expiring development fund with a new model emphasizing transparency and faster execution. This follows June 2025 debates about sustaining ecosystem growth.\n\nWhat this means:Bullish if governance reforms reduce bureaucratic delays, but bearish risks emerge if funding disputes fragment the community.\n\n## Conclusion\n\nZcash’s 2026 trajectory hinges on balancing technical innovation (Ztarknet, Zashi) with governance maturity. While privacy upgrades could drive mainstream adoption, regulatory scrutiny remains a wildcard. How will Zcash’s optional privacy model fare as global AML rules tighten?\nCMC AI can make mistakes. Not financial advice. Read more about ZEC [What is Zcash (ZEC)?](https://coinmarketcap.com/cmc-ai/zcash/what-is/) [Latest Zcash (ZEC) Price Analysis](https://coinmarketcap.com/cmc-ai/zcash/price-analysis/) [Zcash (ZEC) Price Prediction](https://coinmarketcap.com/cmc-ai/zcash/price-prediction/) \n## Explore Similar Coins\n\n![ZEC](https://s2.coinmarketcap.com/static/img/coins/64x64/1437.png)\nZcash ZEC | $494.67 \n1.51% (1d)\n[See ZEC Price Chart](https://coinmarketcap.com/currencies/zcash/#cmcaiquestion=0) Read more about ZEC [What is Zcash (ZEC)?](https://coinmarketcap.com/cmc-ai/zcash/what-is/) [Latest Zcash (ZEC) Price Analysis](https://coinmarketcap.com/cmc-ai/zcash/price-analysis/) [Zcash (ZEC) Price Prediction](https://coinmarketcap.com/cmc-ai/zcash/price-prediction/) Cryptos: [29.55M](https://coinmarketcap.com/charts/number-of-cryptocurrencies-tracked/) Exchanges: [913](https://coinmarketcap.com/rankings/exchanges/) Market Cap: [$3.18T](https://coinmarketcap.com/charts/) 0.79% 24h Vol: [$138.65B](https://coinmarketcap.com/charts/) 11.53% Dominance: [BTC: 58.2% ETH: 12.3%](https://coinmarketcap.com/charts/bitcoin-dominance/) ** ETH Gas : 0.04 Gwei Fear & Greed: [49/100](https://coinmarketcap.com/charts/fear-and-greed-index/) [API](https://coinmarketcap.com/api/pricing/)\n</searchResult>\n\n\n"
  },
  {
    "ToolCallId": "call_csPDCR1OAe71A7BTigWZTPZZ",
    "Output": "<searchResult>\n[doc10]:\n**Zcash surges tenfold as investors bet on privacy as ban looms**\nSearch results\n[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results\n[](https://defillama.com/) [](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) \n# Zcash surges tenfold as investors bet on privacy as ban looms\n\n![Zcash surges tenfold as investors bet on privacy as ban looms](https://www.dlnews.com/resizer/v2/AXKQE4P3FVEXBDD3S5Z3UGLE2A.jpg?auth=cbd98be097214eb17e382cf72f728dfecbed43022b35af5f79b7b0a53414de76&amp;width=1200&amp;height=675&amp;focal=2500%2C1500)\n[Markets](https://www.dlnews.com/articles/markets/) Privacy coins have surged in 2025. Source: Shutterstock. Credit: Shutterstock / Collagery\n[Home](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) Zcash surges tenfold as investors bet on privacy as ban looms By [Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 3 November 2025 at 11:31 Share\n- Zcash is surging.\n- Social media influencers are generating hype around privacy coins.\n- a16z highlights Zcash, Railgun as leading privacy protocols.\n\nZcash is skyrocketing.\n\nOne of crypto’s oldest privacy coins has surged over 1,000% this year to over $440 this past weekend as investors bet on privacy. It currently trades as the 33rd most valuable cryptocurrency in the world.\n\nZcash’s surging value “reflects a renewed interest in privacy,” Spencer Yang, managing partner at crypto-native advisory firm BlockSpaceForce, told DL News.\n\nThe new peak comes as the Electric Coin Company, the developers behind Zcash, announced an updated roadmap on October 31. The roadmap includes long-term funding and new privacy tools.\n\nAnd it’s not just Zcash that’s cashing in. Monero is up over 120% this year while Dash is up nearly 300%.\n\nRailgun, an Ethereum privacy tool recently mentioned in the Ethereum Foundation’s institutional launch note on X, is also up over 300%.\n\n## Why Zcash?\n\nBut Zcash is the standout winner so far this year.\n\nOne reason for that is its opt-in privacy features, which “fit better than Monero with the current regulatory environment for privacy-based tokens,” Yang said.\n\n“Zcash has also benefitted from promoters like Arthur Hayes, Mert Mumtaz, and Naval Ravikant openly coming out in its favour, whereas Monero hasn’t had that kind of attention,” he added.\n\nIn October, former BitMEX chief Arthur Hayes predicted Zcash will hit $10,000 in a viral post on X. He didn’t provide any further details on why he made that prediction and within what time-frames he was expecting Zcash to hit a milestone that even Ethereum, the world’s second biggest cryptocurrency, has yet to hit.\n\nPopular YouTuber Mario Nawfal said that privacy projects “are making noise again” with “Monero, Zcash, and other privacy-focused tokens” in the spotlight.\n\nStill, social media influencers are not the only ones plugged into the privacy trend.\n\nIn venture capital giant Andreessen Horowitz’s State of Crypto report, released in October, analysts said that the demand for privacy “is more urgent than ever” highlighting record figures for Zcash and Railgun.\n\n## Privacy narrative\n\nA16z cited multiple notable privacy milestones in 2025, including the Ethereum Foundation’s launch of a new 47-member “Privacy Cluster,” Zcash’s new Zashi wallet, and an uptick in the usage of privacy programming language Noir.\n\n“Privacy is returning to the foreground and could be a prerequisite for wider adoption,” the report said.\n\n“Google searches related to crypto privacy surged in 2025; Zcash’s shielded pool supply grew to nearly 4 million ZEC; and Railgun’s transaction flows surpassed $200 million monthly,” it stressed.\n\n“Why are you not putting more money into privacy protocols?” Ethereum co-founder Vitalik Buterin asked an audience during a session at the Web3Privacy Now meetup in Tokyo in September.\n\n## Under siege\n\nTo be sure, the waters are not entirely blue.\n\nZcash has lost some 15% of its value after reaching its all-time high market capitalisation this weekend and is worth $386 at the time of writing.\n\nIn 2024, the European Parliament voted through a bill that will ban listing tokens like Zcash and Monero. The argument was that the EU wanted to fight financial crimes such as money-laundering.\n\nIn response, crypto exchanges like Kraken and Binance have either delisted or considered delisting privacy coins in the EU.\n\nThe new EU rules are set to snap into action in 2027.\n\nLooking beyond privacy coins, the same bill also sought to ban privacy mixers like Tornado Cash and to scale the policing of crypto transactions.\n\nIt’s clear that privacy-linked crypto projects are also under pressure around the world.\n\nA Dutch court convicted Tornado Cash co-founder Alexey Pertsev of money laundering in 2024. Across the Atlantic, his fellow co-founder Roman Storm was convicted in the US in August of conspiracy to operate an unlicensed money-transmitting business. Both of them have appealed their verdicts.\n\nThe founders of a similar service, Keonne Rodriguez and William Lonergan Hill of Samourai Wallet, pleaded guilty to conspiracy to operate an unlicensed money-transmitting business in August.\n\nEven so, the US Department of Justice has said it intends to reject similar charges going forward.\n\nMert Mumtaz, the CEO of Solana-infrastructure platform Helius Labs, and prominent promoter of Zcash, cited overzealous regulators as the best argument for privacy.\n\n“The European Central Bank is working on the idea of ‘holding limits’ for ‘your’ money,” Mumtaz said on X. “They are going to control every aspect of your life soon. They think they own you. Use Bitcoin, use Zcash, use crypto. Reject these clowns.”\n\nLance Datskoluo is DL News’ Europe-based markets correspondent. Got a tip? Email at lance@dlnews.com.\nRelated Topics\n[MONERO](https://www.dlnews.com/topics/monero/) You may also like\n[](https://www.dlnews.com/articles/regulation/eus-new-aml-rules-may-impact-uniswap-binance-and-monero/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### EU regulators flag new crypto risks and weigh rules that may impact Uniswap and Binance\n[Inbar Preiss](https://www.dlnews.com/authors/Inbar-Preiss/) 2 June 2023 [](https://www.dlnews.com/articles/markets/xrp-etf-launches-seen-to-trigger-billion-dollar-bonanza/) [Markets](https://www.dlnews.com/articles/markets/) \n### XRP ETF launches seen to trigger $5bn bonanza\n[Eric Johansson](https://www.dlnews.com/authors/eric-johansson/) 3 November 2025 [](https://www.dlnews.com/articles/markets/us-solana-spot-etfs-seen-to-hit-5bn-in-inflows/) [Markets](https://www.dlnews.com/articles/markets/) \n### US Solana spot ETFs seen to hit $5bn in inflows: Grayscale exec\n[Aleks Gilbert](https://www.dlnews.com/authors/Aleks-Gilbert/) 30 October 2025 Related articles\n[](https://www.dlnews.com/articles/defi/monero-hashrate-tug-war-ease-qubic-lose-51-percent-dominance/) [DeFi](https://www.dlnews.com/articles/defi/) \n### Monero hashrate tug-of-war eases as Qubic loses 51% dominance\n[Kyle Baird](https://www.dlnews.com/authors/kyle-baird/) 17 August 2025 [](https://www.dlnews.com/articles/markets/xmr-soars-as-suspected-hacker-purchases-millions-in-tokens/) [Markets](https://www.dlnews.com/articles/markets/) \n### Monero’s XMR soars as suspected hacker purchases $330m\n[Tim Craig](https://www.dlnews.com/authors/timcraig/) 28 April 2025 [](https://www.dlnews.com/articles/regulation/why-the-eu-is-about-to-outlaw-and-curb-key-crypto-features/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### The EU is about to outlaw and restrict some of the most prized features in crypto\n[Inbar Preiss](https://www.dlnews.com/authors/Inbar-Preiss/) 16 January 2024 [](https://www.dlnews.com/articles/defi/monero-and-zcash-liquidity-runs-dry-as-binance-may-delist/) [DeFi](https://www.dlnews.com/articles/defi/) \n### Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins\n[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 12 January 2024\n</searchResult>\n\n\n<searchResult>\n[doc11]:\n**Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% ...**\nSearch results\n[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results\n[](https://defillama.com/) [](https://www.dlnews.com/) [People & culture](https://www.dlnews.com/articles/people-culture/) \n# Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% price rally\n\n![Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% price rally](https://www.dlnews.com/resizer/v2/QU7DVGZ6RZDOLPTI4RGVKIYZXA.jpg?auth=2226ced312593b426bce6cd78e8062945f6452955fcf8bfe16437d3fd5530a3f&amp;width=1200&amp;height=675&amp;focal=1787%2C1193)\n[People & culture](https://www.dlnews.com/articles/people-culture/) The appointment aren't the first major change to the Zcash Foundation’s leadership in recent weeks. Credit: Shutterstock / Grey82\n[Home](https://www.dlnews.com/) [People & culture](https://www.dlnews.com/articles/people-culture/) Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% price rally By [Tim Craig](https://www.dlnews.com/authors/timcraig/) 12 November 2025 at 12:20 Share\n- Zcash Foundation appoints two new leaders.\n- The foundation also got a new executive director earlier this month.\n- The appointments come amid surging interest in crypto privacy projects.\n\nThe Zcash Foundation is shaking up its leadership.\n\nOn Tuesday, the nonprofit that supports the $7.7 billion privacy protocol announced two new appointments: Pili Guerra moves from engineering manager to head of engineering, and Danika Delano takes on the role of chief operating officer.\n\nThe foundation said the promotions reflect its commitment to promote from within and recognise the talent that’s been instrumental to its success.\n\nIt’s not the first major change to the Zcash Foundation’s leadership in recent weeks.\n\nOn November 1, the foundation’s board appointed Alex Bornstein as executive director. Bornstein stepped in as interim executive director in March.\n\nZcash is a blockchain protocol focused on privacy. It lets users send so-called shielded transactions, which hide transaction details by encrypting data. Users can also choose to send transparent transactions which are publicly viewable like those on Bitcoin or Ethereum.\n\nThe Zcash Foundation is a nonprofit that supports financial privacy infrastructure, primarily on Zcash.\n\nThe new appointees are very much at home with the open-source, privacy-first ethos of the Zcash Foundation.\n\nBefore joining the foundation in 2020, Guerra worked at the Tor Project, a non-profit that develops and maintains the Tor browser and its associated infrastructure. The Tor browser is used for anonymous web browsing, typically on the dark web.\n\nShe also worked at Red Hat, a firm that develops open-source software for businesses.\n\nDelano also joined the Zcash Foundation in 2020. In her previous role as operations director she oversaw the foundation’s grant programmes, and organised Zcon, the foundation’s annual conference.\n\n## 1,000% rally\n\nThe foundation’s leadership moves come as privacy-enhancing crypto projects experience a renaissance after years of investor apathy.\n\nZcash’s ZEC token has led the change, skyrocketing over 1,000% this year. The tokens of other crypto privacy projects, such as Monero and Railgun, have also soared.\nZcash's ZEC token has rallied over 1,000% this year. \nGalaxy Digital attributed Zcash’s rise to real infrastructure progress and growing attention to crypto privacy in a recent report.\n\nInterest rose sharply last month when former BitMEX chief Arthur Hayes predicted the ZEC token will hit $10,000 in a viral post on X.\n\nOn November 7, the ZEC token hit a high of $723, its highest value since 2018. It has since given back some of its gains, and trades around $470.\n\nTim Craig is DL News’ Edinburgh-based DeFi Correspondent. Reach out with tips at tim@dlnews.com.\n</searchResult>\n\n\n<searchResult>\n[doc12]:\n**Why Zcash price is up 700% since September, according to Galaxy Digital**\nSearch results\n[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results\n[](https://defillama.com/) [](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) \n# Why Zcash price is up 700% since September, according to Galaxy Digital\n\n![Why Zcash price is up 700% since September, according to Galaxy Digital](https://www.dlnews.com/resizer/v2/4LZLNM4GMNBZ5MZD6OV4FIKSTM.jpg?auth=a3defd4ed6225d27570a10ba09a26cfd164e8b689a28923262c81f8f3e212a08&amp;width=1200&amp;height=675&amp;focal=825%2C540)\n[Markets](https://www.dlnews.com/articles/markets/) Monero is also up over 130% this year, while Dash is up 400%. Illustration: Gwen P; Source: Shutterstock\n[Home](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) Why Zcash price is up 700% since September, according to Galaxy Digital By [Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 5 November 2025 at 10:24 Share\n- Galaxy chalks up ZEC’s price action to new user tools and shifting attitudes.\n- Critics say the bullish move is coordinated.\n- Regulators around the world continue to crack down on privacy tech.\n\nThe price of Zcash is staging one of crypto’s most dramatic comebacks despite the market drawdown.\n\nThe 2016 Bitcoin fork created by computer security expert Zooko Wilcox has surged more than 700% since September and is trading at $430, thanks to real infrastructure progress and growing attention to privacy.\n\nThat’s according to a new report from Galaxy Digital, which said that over 30% of the Zcash supply is now hidden from the public eye in private pools — an all-time high for this particular stat.\n\nThe new Zashi wallet has also made private transactions simpler for users, research analyst Will Owens said, which also contributed to more users going private.\n\nOwens added that cross-chain integrations now let users move funds between transparent and private networks while keeping their steps hidden.\nZcash price. \nThe milestone marks an attitude shift in crypto, where privacy, once treated as a liability and attacked by state actors, is now being rebranded as a core feature to protect users.\n\nIt’s not just Zcash that’s doing well. Monero is up over 130% this year while Dash is up 400%, both significantly outperforming Bitcoin.\n\nRailgun, a key Ethereum privacy tool recently mentioned in the Ethereum Foundation’s institutional launch, was also cited by Galaxy Digital as a core project.\n\n> ‘Technically, Zcash’s fundamentals haven’t radically changed overnight.’— Galaxy Digital's Will Owens\n\n## Old tech, new attention\n\nTo be sure, Owens acknowledged that some are sceptical.\n\nProminent voices are split on whether the price action is sustainable. Economist Lyn Alden called the move “a coordinated token pump,” warning traders against becoming “exit liquidity.”\n\nBut tech investor Naval Ravikant countered that Zcash represents a deeper truth about the future of money, writing that “transparent crypto won’t survive a government crackdown.”\n\nVenture capital giant Andreessen Horowitz has also said that demand for privacy “is more urgent than ever,” highlighting record user metrics for Zcash and Railgun this year.\n\nHorowitz’s venture firm a16z cited multiple notable privacy milestones in 2025, including the Ethereum Foundation’s launch of its new 47-member “Privacy Cluster” and an uptick in the usage of the privacy programming language Noir.\n\n“Technically, Zcash’s fundamentals haven’t radically changed overnight,” Galaxy Digital said. “But the perception around the technology has. This rally is driven by both constant vocal support from some of crypto’s top voices and also a reminder of how important privacy is for permissionless money.”\n\nOriginally a Bitcoin fork, Zcash was designed to fix the privacy issue that the Satoshi 2008 whitepaper acknowledged.\n\nIts zero-knowledge proof system, known as zk-SNARKs, allows users to validate transactions without revealing who sent what to whom.\n\nBy contrast, Bitcoin’s public ledger exposes transactions to public analysis.\n\n## Still under fire\n\nState actors are not relinquishing control just yet.\n\nIn 2024, the European Parliament voted through a bill that will ban listing tokens like Zcash and Monero on EU exchanges, with implementation expected in 2027. The argument is that the EU wants to fight financial crimes such as money laundering.\n\nCypto exchanges like Kraken and Binance have also either delisted or considered delisting privacy coins in the EU.\n\nA Dutch court convicted the co-founder of privacy tool Tornado Cash, Alexey Pertsev, of money laundering in 2024. Across the Atlantic, his fellow co-founder, Roman Storm, was convicted in the US in August of conspiracy to operate an unlicensed money-transmitting business. Both of them have appealed their verdicts.\n\nMeanwhile, some of the industry’s best-known privacy projects – mixers like Samourai and Wasabi – have been crippled by regulatory action, with founders arrested and charged.\n\nEven so, the US Department of Justice has said it intends to reject similar cases going forward.\n\nLance Datskoluo is DL News’ Europe-based markets correspondent. Got a tip? Email at lance@dlnews.com.\n</searchResult>\n\n\n<searchResult>\n[doc13]:\n**Zcash price primed for 45% breakout as Grayscale files for ETF**\nSearch results\n[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results\n[](https://defillama.com/) [](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) [Regulation](https://www.dlnews.com/articles/regulation/) \n# Zcash price primed for 45% breakout as Grayscale files for ETF\n\n![Zcash price primed for 45% breakout as Grayscale files for ETF](https://www.dlnews.com/resizer/v2/VKGYHYRAJVD6PEWJU4BR5AT47I.jpg?auth=facb23e8d4d3cdf24913a117bc6c07b4c60c1a15269474b2ff0a98d0dee16dd8&amp;width=1200&amp;height=675&amp;focal=825%2C540)\n[Markets](https://www.dlnews.com/articles/markets/) [Regulation](https://www.dlnews.com/articles/regulation/) Privacy token Zcash is ready to rip 45%, says Maria Carola, CEO of crypto exchange StealthEx. Illustration: Gwen P; Source: Shutterstock\n[Home](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) Zcash price primed for 45% breakout as Grayscale files for ETF By [Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 27 November 2025 at 12:19 Share\n- Grayscale is the latest Wall Street player to jump into Zcash.\n- The Winklevoss twins launched a Zcash-based digital asset treasury firm earlier in November.\n\nPrivacy token Zcash is ready to rip 45%, says Maria Carola, CEO of crypto exchange StealthEx.\n\nShe argues that growing interest on Wall Street, most recently Grayscale’s exchange-traded fund filing on Wednesday, will propel the $8.3 billion crypto to new highs.\n\n“A decisive break above $750 with sustained bullish momentum could open the path towards moving above $1,000 before the end of Q4,” Carola told DL News.\n\nThat would translate to Zcash’s price surging 45% above its current price of $515.\nZcash price over the past 6 months. \nPrivacy coins are “operating with an entirely different playbook from the wider market,” Carola said. “They are benefiting from the long-suppressed demand for privacy-preserving tools and prevalent policy legislation in this direction.”\n\nAnd Carola is far from the only one bullish on Zcash. She joins the ranks of BitMEX co-founder Arthur Hayes, popular YouTuber Mario Nawfal, and prominent Indian investor Naval Ravikant, who have all come out in support of Zcash.\n\nA slew of investors have also told DL News that they expect Zcash to surge higher.\n\nThe bullishness comes as influential voices in the crypto community — such as Ethereum co-founder Vitalik Buterin — are increasingly calling for better privacy solutions.\n\n## Grayscale shoots for ETF\n\nThe bullish projections come as Grayscale, the crypto asset manager that pioneered Wall Street products, files to transform its existing Zcash Trust product into a spot exchange-traded fund.\n\nGrayscale’s registration statement submitted to the Securities and Exchange Commission on Wednesday would mark the launch of the first US spot ETF directly tracking Zcash. The move comes just days after it launched ETFs linked to XRP and Dogecoin.\n\nThe firm joins a growing number of major institutions that have come out supporting Zcash.\n\nVenture capital giant Andreessen Horowitz and crypto investment manager Galaxy Digital have both noted the buzz around Zcash and other privacy-focused crypto projects like Monero and Railgun.\n\nCypherpunk, the crypto treasury company backed by twins Cameron and Tyler Winklevoss and launched earlier this month, has deployed over $50 million into Zcash.\n\nAs of November 19, Cypherpunk holds 1.43% of the total Zcash supply and is gunning for 5% ownership of all tokens.\n\n## Privacy controversies\n\nTo be sure, not everyone backs privacy coins.\n\nEU lawmakers have passed a bill to ban exchanges from listing tokens like Zcash and Monero, citing anti-money laundering concerns. The ban is set to take effect in 2027.\n\nRegulators in the US and Europe are cracking down on developers of privacy tools.\n\nIn the Netherlands, Tornado Cash developer Alexey Pertsev was convicted of money laundering in 2024. Prosecutors said his code helped criminals conceal stolen crypto.\n\nIn the US, Tornado Cash co-founder Roman Storm was found guilty of running an unlicensed money-transmitting business. Samourai Wallet’s Keonne Rodriguez received the maximum five-year sentence for similar charges.\n\nLance Datskoluo is DL News’ Europe-based markets correspondent. Got a tip? Email at lance@dlnews.com.\nRelated Topics\n[CRYPTO ETF](https://www.dlnews.com/topics/crypto-etf/) You may also like\n[](https://www.dlnews.com/articles/defi/monero-and-zcash-liquidity-runs-dry-as-binance-may-delist/) [DeFi](https://www.dlnews.com/articles/defi/) \n### Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins\n[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 12 January 2024 [](https://www.dlnews.com/articles/regulation/uk-fca-asks-stablecoin-firms-to-launch-in-sandbox/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### UK financial regulator asks stablecoin firms to launch in its ‘sandbox’ and help shape regulation\n[Tim Craig](https://www.dlnews.com/authors/timcraig/) 26 November 2025 [](https://www.dlnews.com/articles/markets/bitcoin-holds-at-87000-but-do-not-expect-the-price-to-explode/) [Markets](https://www.dlnews.com/articles/markets/) [Snapshot](https://www.dlnews.com/articles/snapshot/) \n### Bitcoin holds at $87,000, but price won’t ‘explode’ to record heights anytime soon, analysts say\n[Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 26 November 2025 Related articles\n[](https://www.dlnews.com/articles/markets/zcash-price-surge-continues-despite-market-turmoil/) [Markets](https://www.dlnews.com/articles/markets/) \n### Zcash price surge continues despite market turmoil\n[Aleks Gilbert](https://www.dlnews.com/authors/Aleks-Gilbert/) 15 November 2025 [](https://www.dlnews.com/articles/markets/winklevoss-twins-bet-on-zcash-with-new-treasury-firm/) [Markets](https://www.dlnews.com/articles/markets/) \n### Winklevoss twins bet on Zcash with new treasury firm targeting 5% supply of the privacy coin’s supply\n[Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 13 November 2025 [](https://www.dlnews.com/articles/people-culture/zcash-foundation-shakes-up-leadership-amidst-zec-token-price-rally/) [People & culture](https://www.dlnews.com/articles/people-culture/) \n### Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% price rally\n[Tim Craig](https://www.dlnews.com/authors/timcraig/) 12 November 2025 [](https://www.dlnews.com/articles/defi/how-privacy-coins-firo-and-zcash-dodged-binance-delisting/) [DeFi](https://www.dlnews.com/articles/defi/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### How privacy coins Firo and Zcash dodged Binance delisting with novel transparency plan\n[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 23 January 2024\n</searchResult>\n\n\n<searchResult>\n[doc14]:\n**Zcash price surge continues despite market turmoil – DL News**\nSearch results\n[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results\n[](https://defillama.com/) [](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) \n# Zcash price surge continues despite market turmoil\n\n![Zcash price surge continues despite market turmoil](https://www.dlnews.com/resizer/v2/VKGYHYRAJVD6PEWJU4BR5AT47I.jpg?auth=facb23e8d4d3cdf24913a117bc6c07b4c60c1a15269474b2ff0a98d0dee16dd8&amp;width=1200&amp;height=675&amp;focal=825%2C540)\n[Markets](https://www.dlnews.com/articles/markets/) Market instability hasn’t been able to stop Zcash’s remarkable rally. Illustration: Gwen P; Source: Shutterstock\n[Home](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) Zcash price surge continues despite market turmoil By [Aleks Gilbert](https://www.dlnews.com/authors/Aleks-Gilbert/) 15 November 2025 at 17:29 Share\n- Zcash has continued to climb despite a market slump triggered by mounting fears over Federal Reserve policy.\n- The rally has been fueled by increasing interest in privacy-preserving technology and the creation of a Zcash-focused digital asset treasury.\n\nZcash, a privacy-focused cryptocurrency, has continued its astonishing rise this week, even as market turmoil has hammered most other major cryptocurrencies and the broader equities market.\n\nThe privacy coin has surged 35%, to $664, since Thursday. In that same span, Bitcoin has fallen 2%, to $95,800, and Ethereum has held relatively steady.\n\nThe week-over-week numbers are even more stark. Over the past seven days, Zcash is up 23%, while Bitcoin and Ethereum have fallen 6% and 7%, respectively.\n\nMarkets fell on Thursday over mounting fears the Federal Reserve would hold interest rates steady at a meeting next month.\n\nThe Fed’s rate cutting campaign has helped boost stock markets this year, and rate cuts are generally a boon to risk-on assets, such as crypto.\n\nBut traders are now pricing in a 44% chance the Fed cuts rates in December, according to CME’s FedWatch tool. That’s down from 66% a week ago and 94% last month.\n\nThe Zcash rally has been fueled by rising interest in privacy-preserving technology.\n\nNo cryptocurrency has performed as well as Zcash this year. It is up more than 1,000% in 2025. At the start of the month, it was the 33rd most valuable crypto asset in the world. Since then, it has surged to 12th place.\n\nMonero, another privacy coin, has been the third-best performer in 2025, rising 125%.\n\nIn its recent State of Crypto report, venture capital giant Andreessen Horowitz said the crypto industry had seen multiple privacy milestones in 2025.\n\nAmong those milestones were the Ethereum Foundation’s launch of a new 47-member “Privacy Cluster,” Zcash’s new Zashi wallet, and an uptick in the usage of a privacy programming language created by Aztec, the developer of a privacy-focused layer 2 blockchain.\n\nAztec began selling its new token on Thursday via Uniswap’s Continuous Clearing Auction.\n\nThis week, Cameron and Tyler Winklevoss, the brothers behind US crypto exchange Gemini, launched a Zcash-focused digital asset treasury, Cypherpunk.\n\nThey purchased $50 million of the cryptocurrency on Wednesday, according to DefiLlama data.\n\n“Privacy’s become a rare, vanishing commodity,” Tyler Winklevoss said on X. “We feel strongly that Zcash could become a meaningful percentage of Bitcoin’s market capitalisation just on the merits of it being a privacy hedge or insurance policy to Bitcoin’s transparency alone.”\n\nAleks Gilbert is DL News’ New York-based DeFi correspondent. You can reach him at aleks@dlnews.com.\nRelated articles\n[](https://www.dlnews.com/articles/markets/winklevoss-twins-bet-on-zcash-with-new-treasury-firm/) [Markets](https://www.dlnews.com/articles/markets/) \n### Winklevoss twins bet on Zcash with new treasury firm targeting 5% supply of the privacy coin’s supply\n[Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 13 November 2025 [](https://www.dlnews.com/articles/people-culture/zcash-foundation-shakes-up-leadership-amidst-zec-token-price-rally/) [People & culture](https://www.dlnews.com/articles/people-culture/) \n### Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% price rally\n[Tim Craig](https://www.dlnews.com/authors/timcraig/) 12 November 2025 [](https://www.dlnews.com/articles/defi/how-privacy-coins-firo-and-zcash-dodged-binance-delisting/) [DeFi](https://www.dlnews.com/articles/defi/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### How privacy coins Firo and Zcash dodged Binance delisting with novel transparency plan\n[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 23 January 2024 [](https://www.dlnews.com/articles/defi/monero-and-zcash-liquidity-runs-dry-as-binance-may-delist/) [DeFi](https://www.dlnews.com/articles/defi/) \n### Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins\n[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 12 January 2024\n</searchResult>\n\n\n<searchResult>\n[doc15]:\n**Winklevoss twins bet on Zcash with new treasury firm targeting 5% ...**\nSearch results\n[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results\n[](https://defillama.com/) [](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) \n# Winklevoss twins bet on Zcash with new treasury firm targeting 5% supply of the privacy coin’s supply\n\n![Winklevoss twins bet on Zcash with new treasury firm targeting 5% supply of the privacy coin’s supply](https://www.dlnews.com/resizer/v2/VKGYHYRAJVD6PEWJU4BR5AT47I.jpg?auth=facb23e8d4d3cdf24913a117bc6c07b4c60c1a15269474b2ff0a98d0dee16dd8&amp;width=1200&amp;height=675&amp;focal=825%2C540)\n[Markets](https://www.dlnews.com/articles/markets/) The Winklevi are rotating to Zcash. Illustration: Gwen P; Source: Shutterstock\n[Home](https://www.dlnews.com/) [Markets](https://www.dlnews.com/articles/markets/) Winklevoss twins bet on Zcash with new treasury firm targeting 5% supply of the privacy coin’s supply By [Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 13 November 2025 at 09:57 Share\n- Gemini’s founders have launched a Zcash-based digital asset treasury firm.\n- Cypherpunk already holds 203,775 ZEC and targets 5% of total supply.\n- Winklevoss twins cite privacy as a top concern in the AI era.\n\nThe Winklevi are rotating to Zcash.\n\nCypherpunk, a brand new crypto treasury company backed by twins Cameron and Tyler Winklevoss, is deploying over $50 million into the Bitcoin fork. As of the launch on November 12, the firm already holds 203,775 of the privacy coins and is shooting for ownership 5% of total supply.\n\n“Privacy’s become a rare, vanishing commodity,” Tyler Winklevoss said on X. “We feel strongly that Zcash could become a meaningful percentage of Bitcoin’s market capitalisation just on the merits of it being a privacy hedge or insurance policy to Bitcoin’s transparency alone.”\n\nCypherpunk’s launch marks one of the most high-profile bets yet that privacy will become the next flashpoint in crypto. The move comes as the Zcash Foundation is shaking up its leadership, and as state actors intensify crackdowns on privacy technology.\n\nZcash’s price has soared over 1,000% this year, and is trading at over $500. Venture capital giant Andreessen Horowitz and crypto investment manager Galaxy Digital have also noted the buzz around Zcash and other privacy-focused crypto projects.\n\nThe billionaire crypto investors are best known for buying 70,000 Bitcoin in 2013 at $150 and for founding the Gemini Space Station crypto exchange.\n\n## ‘Separating Money and State’\n\nZcash creator Zooko Wilcox praised the moment on X. “Proud that Zcash has drawn people like [Will McEvoy, CIO of Cypherpunk] and the Winklevosses who are here for the right reasons.”\n\n“Tyler Winklevoss just said something awesome about ‘separating money and state.’ Something like ‘Have we really done that? And the answer is no, unless you’re using Zcash’,” Wilcox said.\n\n“If Bitcoin is digital gold, Zcash is encrypted bitcoin, or digital cash,” Tyler Winklevoss said.\n\n“One is your store of value, the other is how you privately move your value,” he added. “We’ve been tracking this symbiosis for years and believe that now — as we enter the age of AI — is the right time to begin accumulating ZEC.”\n\nArthur Hayes, also a big Zcash bull, advised investors to self-custody their coins rather than leave it on centralised exchanges.\n\n“If you hold $ZEC on a CEX, withdraw it to a self-custodial wallet and shield it,” he said on X.\n\n“It’s one of the few 1,000x opportunities in crypto remaining,” Carter Razink, co-founder of blockchain commerce platform spree.Finance, told DL News.\n\n## Battle over privacy\n\nTo be sure, not everyone is supportive of privacy coins.\n\nEU lawmakers view private crypto as incompatible with laws designed to prevent money-laundering, terrorism financing, and other financial crimes.\n\nThey have approved a bill that will ban exchanges from listing privacy coins like Zcash and Monero, with implementation expected in 2027.\n\nAnd high-profile criminal prosecutions in the US and Europe have targeted developers behind privacy-enabling blockchain solutions.\n\nIn the Netherlands, Alexey Pertsev, co-founder of Tornado Cash, was convicted of money laundering in 2024. Dutch prosecutors argued that the protocol enabled criminals to hide stolen funds. Pertsev denied wrongdoing, but the court ruled that building software that obscures transactions can itself constitute facilitation of laundering.\n\nIn the US, Tornado Cash co-founder Roman Storm was convicted of conspiring to operate an unlicensed money-transmitting business.\n\nAnother major case came last week when Samourai Wallet co-founder Keonne Rodriguez received the maximum five-year sentence for operating an unlicensed money-transmitting business. Prosecutors accused the project of “soliciting, encouraging, and inviting criminals” to use its privacy features.\n\nLance Datskoluo is DL News’ Europe-based markets correspondent. Got a tip? lance@dlnews.com.\nRelated Topics\n[TORNADO CASH](https://www.dlnews.com/topics/tornado-cash/) You may also like\n[](https://www.dlnews.com/articles/defi/tornado-cash-dev-roman-storm-asks-judge-to-toss-conviction/) [DeFi](https://www.dlnews.com/articles/defi/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### Tornado Cash dev Roman Storm asks judge to toss conviction\n[Aleks Gilbert](https://www.dlnews.com/authors/Aleks-Gilbert/) 1 October 2025 [](https://www.dlnews.com/articles/defi/crypto-industry-calls-for-clarity-act-to-protect-defi-devs-after-tornado-cash-conviction/) [DeFi](https://www.dlnews.com/articles/defi/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### Crypto industry calls for new bill to protect DeFi devs following Tornado Cash founder conviction\n[T. Craig](https://www.dlnews.com/authors/timcraig/) , [E. Johansson](https://www.dlnews.com/authors/eric-johansson/) 28 August 2025 [](https://www.dlnews.com/articles/regulation/devs-of-decentralised-protocols-wont-be-prosecuted-doj-says/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### Devs behind ‘truly decentralised’ protocols won’t face DoJ prosecution, official says\n[Aleks Gilbert](https://www.dlnews.com/authors/Aleks-Gilbert/) 21 August 2025 Related articles\n[](https://www.dlnews.com/articles/people-culture/zcash-foundation-shakes-up-leadership-amidst-zec-token-price-rally/) [People & culture](https://www.dlnews.com/articles/people-culture/) \n### Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% price rally\n[Tim Craig](https://www.dlnews.com/authors/timcraig/) 12 November 2025 [](https://www.dlnews.com/articles/defi/how-privacy-coins-firo-and-zcash-dodged-binance-delisting/) [DeFi](https://www.dlnews.com/articles/defi/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### How privacy coins Firo and Zcash dodged Binance delisting with novel transparency plan\n[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 23 January 2024 [](https://www.dlnews.com/articles/defi/monero-and-zcash-liquidity-runs-dry-as-binance-may-delist/) [DeFi](https://www.dlnews.com/articles/defi/) \n### Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins\n[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 12 January 2024 [](https://www.dlnews.com/articles/markets/ethereum-doubles-down-on-privacy-as-devs-eye-post-tornado-future/) [Markets](https://www.dlnews.com/articles/markets/) [Snapshot](https://www.dlnews.com/articles/snapshot/) \n### Ethereum doubles down on privacy as devs eye post-Tornado future\n[Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 9 October 2025\n</searchResult>\n\n\n<searchResult>\n[doc16]:\n**DL News - Markets, DeFi, Regulation and top cryptocurrency news**\n[The State of DeFi 2025 is out, see what’s next. Read more.](https://assets.dlnews.com/dlresearch/State-of-DeFi-2025.pdf) Search results\n[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results\n[](https://defillama.com/) [](https://www.dlnews.com/) \n### Prediction markets? Not for politicians, says US congressman\n[Regulation](https://www.dlnews.com/articles/regulation/) [](https://www.dlnews.com/articles/regulation/congress-bill-to-ban-government-officials-using-polymarket/) [Pedro Solimano](https://www.dlnews.com/authors/Pedro-Solimano/) 6 January 2026 [DeFi](https://www.dlnews.com/articles/defi/) [](https://www.dlnews.com/articles/defi/what-defi-protocols-expect-in-2026/) \n## What DeFi protocols expect in 2026\n[Regulation](https://www.dlnews.com/articles/regulation/) [](https://www.dlnews.com/articles/regulation/cynthia-lummis-worried-over-btc-sales-from-samorai-wallet/) \n## Pro-crypto senator Cynthia Lummis worried over government’s reported Bitcoin sales\n[Markets](https://www.dlnews.com/articles/markets/) [](https://www.dlnews.com/articles/markets/russia-cbdc-launch-will-seriously-undermine-its-mir-cards/) \n## Russia’s digital ruble will undercut its own card payment system, says analyst\n[Regulation](https://www.dlnews.com/articles/regulation/) [](https://www.dlnews.com/articles/regulation/hacked-crypto-exchanges-face-heavy-fines-under-new-rules/) \n## Hacked crypto exchanges face fines worth 10% of stolen assets\n[MOST READ](https://www.dlnews.com/articles/markets/blackrock-coinbase-and-others-share-2026-predictions/) [2 January 2026What BlackRock, Coinbase and 11 other industry giants predict for crypto in 2026Eric JohanssonLance Datskoluo](https://www.dlnews.com/articles/markets/blackrock-coinbase-and-others-share-2026-predictions/) [5 January 2026Ethereum to $250,000? Tom Lee charts targets as Bitmine stock price jumpsLance Datskoluo](https://www.dlnews.com/articles/markets/ethereum-to-250000-tom-lee-charts-targets-as-bitmine-stock-price-jumps/) [4 January 2026Bitcoin prices unmoved by US’ Venezuela strikes – but experts warn of Monday market turbulenceTim Alper](https://www.dlnews.com/articles/markets/bitcoin-prices-unmoved-by-us-venezuela-strikes/) [5 January 2026How Trump’s Venezuela gambit is seen to boost Bitcoin price in 2026Lance Datskoluo](https://www.dlnews.com/articles/markets/will-trump-venezuela-gambit-boost-bitcoin-price-in-2026/) [SNAPSHOT](https://www.dlnews.com/articles/markets/bitcoin-buyers-target-100000-by-the-end-january/) [](https://www.dlnews.com/articles/markets/bitcoin-buyers-target-100000-by-the-end-january/) [Markets](https://www.dlnews.com/articles/markets/) [Snapshot](https://www.dlnews.com/articles/snapshot/) \n### Bitcoin buyers target $100,000 by the end January. Here’s six reasons to be bullish\n[Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 6 January 2026 [EDITOR'S PICK](https://www.dlnews.com/articles/markets/russia-controlled-power-plant-may-fuel-bitcoin-mining/) [](https://www.dlnews.com/articles/markets/russia-controlled-power-plant-may-fuel-bitcoin-mining/) [Markets](https://www.dlnews.com/articles/markets/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### Bitcoin miners to tap Zaporizhzhia nuclear power — if there’s a peace deal in Ukraine\n[Eric Johansson](https://www.dlnews.com/authors/eric-johansson/) 29 December 2025 [TOP STORIES](https://www.dlnews.com/articles/markets/lighter-token-rebounds-as-protocol-begins-buybacks-and-whales-buy-in/) [](https://www.dlnews.com/articles/markets/lighter-token-rebounds-as-protocol-begins-buybacks-and-whales-buy-in/) [Markets](https://www.dlnews.com/articles/markets/) [DeFi](https://www.dlnews.com/articles/defi/) \n### Lighter token bounces 37% as protocol begins buybacks and whales buy in\n[Tim Craig](https://www.dlnews.com/authors/timcraig/) 6 January 2026 [](https://www.dlnews.com/articles/markets/third-of-bitcoin-vulnerable-to-quantum-attack-warns-coinbase/) [Markets](https://www.dlnews.com/articles/markets/) \n### Third of Bitcoin vulnerable to quantum attack, warns Coinbase research chief\n[Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 6 January 2026 [](https://www.dlnews.com/articles/markets/bitcoin-buyers-target-100000-by-the-end-january/) [Markets](https://www.dlnews.com/articles/markets/) [Snapshot](https://www.dlnews.com/articles/snapshot/) \n### Bitcoin buyers target $100,000 by the end January. Here’s six reasons to be bullish\n[Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 6 January 2026 [](https://www.dlnews.com/articles/defi/ethereum-solved-the-blockchain-trilemma-per-vitalik-buterin/) [DeFi](https://www.dlnews.com/articles/defi/) \n### Ethereum ‘solved’ the blockchain trilemma: Vitalik\n[Aleks Gilbert](https://www.dlnews.com/authors/Aleks-Gilbert/) 5 January 2026 [](https://www.dlnews.com/articles/regulation/what-i-learned-attending-crypto-courtroom-dramas-in-2025/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### What I learned attending crypto courtroom dramas in 2025\n[Aleks Gilbert](https://www.dlnews.com/authors/Aleks-Gilbert/) 5 January 2026 [](https://www.dlnews.com/articles/markets/10-chinese-banks-to-pay-interest-on-digital-yuan/) [Markets](https://www.dlnews.com/articles/markets/) \n### Beijing taps WeBank, Alipay’s MYBank, and eight banks to pay interest on digital yuan holdings\n[Tim Alper](https://www.dlnews.com/authors/Tim-Alper/) 5 January 2026 [](https://www.dlnews.com/articles/web3/ledger-payments-partner-global-e-leaks-customer-data/) [Web3](https://www.dlnews.com/articles/web3/) \n### Ledger reveals payments partner leaked customer names, contact information in new data breach\n[Tim Craig](https://www.dlnews.com/authors/timcraig/) 5 January 2026 [](https://www.dlnews.com/articles/people-culture/how-donald-trump-crypto-empire-fared-in-2025/) [People & culture](https://www.dlnews.com/articles/people-culture/) \n### How Trump’s crypto empire fared in 2025 — and what comes next\n[Tim Craig](https://www.dlnews.com/authors/timcraig/) 5 January 2026 [](https://www.dlnews.com/articles/markets/ethereum-to-250000-tom-lee-charts-targets-as-bitmine-stock-price-jumps/) [Markets](https://www.dlnews.com/articles/markets/) \n### Ethereum to $250,000? Tom Lee charts targets as Bitmine stock price jumps\n[Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 5 January 2026 \n##### PRESS RELEASES\n[](https://www.dlnews.com/external/cronos-brings-cro-staking-to-upbit-expanding-access-for-korean-users/) [Cronos Brings CRO Staking to Upbit, Expanding Access for Korean Users](https://www.dlnews.com/external/cronos-brings-cro-staking-to-upbit-expanding-access-for-korean-users/) 17 hours ago [](https://www.dlnews.com/external/termmax-advances-institutional-defi-use-with-tokenized-stock-financing-integration/) [TermMax Advances Institutional DeFi Use with Tokenized Stock Financing Integration](https://www.dlnews.com/external/termmax-advances-institutional-defi-use-with-tokenized-stock-financing-integration/) 1 day ago [](https://www.dlnews.com/external/chainwire-and-cultd-partner-to-solve-the-web3-liquidity-vacuum-by-linking-media-reach-to-on-chain-impact/) [Chainwire and CULTD Partner to Solve the Web3 “Liquidity Vacuum” by Linking Media Reach to On-Chain Impact](https://www.dlnews.com/external/chainwire-and-cultd-partner-to-solve-the-web3-liquidity-vacuum-by-linking-media-reach-to-on-chain-impact/) 1 day ago [](https://www.dlnews.com/external/btcc-ends-2025-with-531-billion-in-tokenized-rwa-futures-volume-and-11m-users-despite-market-wide-volatility/) [BTCC Ends 2025 With $53.1 Billion in Tokenized RWA Futures Volume and 11M Users Despite Market-Wide Volatility](https://www.dlnews.com/external/btcc-ends-2025-with-531-billion-in-tokenized-rwa-futures-volume-and-11m-users-despite-market-wide-volatility/) 4 days ago [](https://www.dlnews.com/external/bcgame-releases-bear-smash-15000x-boost-featuring-single-tap-rounds-and-a-chance-of-15000x-win/) [BC.GAME Releases \"Bear Smash: 15000X Boost\" Featuring Single-Tap Rounds and a Chance of 15,000x Win](https://www.dlnews.com/external/bcgame-releases-bear-smash-15000x-boost-featuring-single-tap-rounds-and-a-chance-of-15000x-win/) 5 days ago [](https://www.dlnews.com/external/meet48-and-messari-publish-research-report-on-the-comprehensive-overview-of-meet48/) [MEET48 and Messari Publish Research Report on the Comprehensive Overview of MEET48](https://www.dlnews.com/external/meet48-and-messari-publish-research-report-on-the-comprehensive-overview-of-meet48/) 6 days ago [](https://www.dlnews.com/external/slotgpt-launches-a-new-ai-slot-platform-transforming-players-into-creators/) [SlotGPT launches a new AI slot platform transforming players into creators](https://www.dlnews.com/external/slotgpt-launches-a-new-ai-slot-platform-transforming-players-into-creators/) 7 days ago [](https://www.dlnews.com/external/lbank-unveils-advent-calendar-campaign-with-blackfort-mew-lc-and-shib-community-collaboration/) [LBank Unveils Advent Calendar Campaign With BlackFort, MEW, LC, and SHIB Community Collaboration](https://www.dlnews.com/external/lbank-unveils-advent-calendar-campaign-with-blackfort-mew-lc-and-shib-community-collaboration/) 7 days ago [](https://www.dlnews.com/external/cango-inc-secures-us105-million-investment-from-ewcl-to-accelerate-growth/) [Cango Inc. Secures US$10.5 Million Investment from EWCL to Accelerate Growth](https://www.dlnews.com/external/cango-inc-secures-us105-million-investment-from-ewcl-to-accelerate-growth/) 7 days ago [](https://www.dlnews.com/external/bitmine-immersion-bmnr-announces-eth-holdings-reach-411-million-tokens-and-total-crypto-and-total-cash-holdings-of-132-billion/) [Bitmine Immersion (BMNR) Announces ETH Holdings Reach 4.11 Million Tokens, and Total Crypto and Total Cash Holdings of $13.2 Billion](https://www.dlnews.com/external/bitmine-immersion-bmnr-announces-eth-holdings-reach-411-million-tokens-and-total-crypto-and-total-cash-holdings-of-132-billion/) 8 days ago [](https://www.dlnews.com/external/unchained-summit-announces-dubai-edition-scheduled-for-1st-2nd-may-2026/) [Unchained Summit Announces Dubai Edition Scheduled for 1st & 2nd May 2026](https://www.dlnews.com/external/unchained-summit-announces-dubai-edition-scheduled-for-1st-2nd-may-2026/) 8 days ago [](https://www.dlnews.com/external/meet48s-2026-roadshow-successfully-held-in-seoul-unveiling-multiple-products-to-lead-the-global-ai-web3-entertainment-industry/) [MEET48’s 2026 Roadshow Successfully Held in Seoul, Unveiling Multiple Products to Lead the Global AI + Web3 Entertainment Industry](https://www.dlnews.com/external/meet48s-2026-roadshow-successfully-held-in-seoul-unveiling-multiple-products-to-lead-the-global-ai-web3-entertainment-industry/) 9 days ago [](https://www.dlnews.com/external/phemex-upgrades-rpi-ecosystem-setting-new-liquidity-benchmarks-across-210-pairs/) [Phemex Upgrades RPI Ecosystem, Setting New Liquidity Benchmarks Across 210+ Pairs](https://www.dlnews.com/external/phemex-upgrades-rpi-ecosystem-setting-new-liquidity-benchmarks-across-210-pairs/) 11 days ago [](https://www.dlnews.com/external/crouton-digital-institutional-grade-blockchain-infrastructure-for-web3-ecosystems/) [Crouton Digital: Institutional-Grade Blockchain Infrastructure for Web3 Ecosystems](https://www.dlnews.com/external/crouton-digital-institutional-grade-blockchain-infrastructure-for-web3-ecosystems/) 11 days ago [](https://www.dlnews.com/external/tapbit-cares-marking-tapbits-4th-anniversary-with-a-year-end-christmas-csr-community-outreach-initiative/) [Tapbit Cares: Marking Tapbit’s 4th Anniversary with a Year-End Christmas CSR Community Outreach Initiative](https://www.dlnews.com/external/tapbit-cares-marking-tapbits-4th-anniversary-with-a-year-end-christmas-csr-community-outreach-initiative/) 12 days ago [](https://www.dlnews.com/external/rollercoin-named-game-of-the-year-and-best-browser-game-at-the-2025-blockchain-game-awards/) [RollerCoin Named Game of the Year and Best Browser Game at the 2025 Blockchain Game Awards](https://www.dlnews.com/external/rollercoin-named-game-of-the-year-and-best-browser-game-at-the-2025-blockchain-game-awards/) 14 days ago [](https://www.dlnews.com/external/thorchain-launches-native-cross-chain-swap-interface-in-public-beta/) [THORChain Launches Native Cross-Chain Swap Interface in Public Beta](https://www.dlnews.com/external/thorchain-launches-native-cross-chain-swap-interface-in-public-beta/) 14 days ago [](https://www.dlnews.com/external/solstice-and-cor-prime-execute-first-institutional-stablecoin-for-stablecoin-repo-on-a-public-blockchain/) [Solstice and Cor Prime Execute First Institutional Stablecoin-for-Stablecoin Repo on a Public Blockchain](https://www.dlnews.com/external/solstice-and-cor-prime-execute-first-institutional-stablecoin-for-stablecoin-repo-on-a-public-blockchain/) 14 days ago [](https://www.dlnews.com/external/valr-reflects-on-a-transformative-2025-for-crypto-and-finance/) [VALR Reflects on a Transformative 2025 for Crypto and Finance](https://www.dlnews.com/external/valr-reflects-on-a-transformative-2025-for-crypto-and-finance/) 14 days ago [](https://www.dlnews.com/external/bitmine-immersion-bmnr-announces-eth-holdings-reach-4066-million-tokens-and-total-crypto-and-total-cash-holdings-of-132-billion/) [Bitmine Immersion (BMNR) Announces ETH Holdings Reach 4.066 Million Tokens, and Total Crypto and Total Cash Holdings of $13.2 Billion](https://www.dlnews.com/external/bitmine-immersion-bmnr-announces-eth-holdings-reach-4066-million-tokens-and-total-crypto-and-total-cash-holdings-of-132-billion/) 15 days ago Powered by\n[LATEST](https://www.dlnews.com/articles/) [](https://www.dlnews.com/articles/regulation/congress-bill-to-ban-government-officials-using-polymarket/) [Prediction markets? Not for politicians, says US congressman](https://www.dlnews.com/articles/regulation/congress-bill-to-ban-government-officials-using-polymarket/) 5 hours ago [](https://www.dlnews.com/articles/defi/what-defi-protocols-expect-in-2026/) [What DeFi protocols expect in 2026](https://www.dlnews.com/articles/defi/what-defi-protocols-expect-in-2026/) 6 hours ago [](https://www.dlnews.com/articles/regulation/cynthia-lummis-worried-over-btc-sales-from-samorai-wallet/) [Pro-crypto senator Cynthia Lummis worried over government’s reported Bitcoin sales](https://www.dlnews.com/articles/regulation/cynthia-lummis-worried-over-btc-sales-from-samorai-wallet/) 8 hours ago [](https://www.dlnews.com/articles/markets/russia-cbdc-launch-will-seriously-undermine-its-mir-cards/) [Russia’s digital ruble will undercut its own card payment system, says analyst](https://www.dlnews.com/articles/markets/russia-cbdc-launch-will-seriously-undermine-its-mir-cards/) 11 hours ago [OPINION](https://www.dlnews.com/articles/markets/why-borrowing-money-to-buy-bitcoin-is-stupid/) [](https://www.dlnews.com/articles/markets/why-borrowing-money-to-buy-bitcoin-is-stupid/) [Markets](https://www.dlnews.com/articles/markets/) [Opinion](https://www.dlnews.com/articles/opinion/) \n### Why borrowing money to buy Bitcoin is ‘downright stupid’\n[Wolfgang Münchau](https://www.dlnews.com/authors/WolfgangMunchau/) 28 December 2025 [DON'T MISS](https://www.dlnews.com/articles/regulation/sec-democrat-caroline-crenshaw-exits/) [SEC’s lone Democratic commissioner and crypto skeptic Caroline Crenshaw to depart](https://www.dlnews.com/articles/regulation/sec-democrat-caroline-crenshaw-exits/) [Mathew Di Salvo](https://www.dlnews.com/authors/Mathew-DiSalvo/) 3 January 2026 [Bitcoin treasury slump deepens as 40% trade at discount: ‘It’s an abomination’](https://www.dlnews.com/articles/markets/bitcoin-treasury-blues-mount-as-40-percent-trade-at-discount/) [Pedro Solimano](https://www.dlnews.com/authors/Pedro-Solimano/) 2 January 2026 [Top 10 crypto fundraising rounds in 2025 — and what they mean for 2026](https://www.dlnews.com/articles/markets/top-10-crypto-fundraising-rounds-in-2025/) [Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 3 January 2026 [FEATURE OF THE WEEK](https://www.dlnews.com/articles/regulation/inside-do-kwons-sentencing/) [](https://www.dlnews.com/articles/regulation/inside-do-kwons-sentencing/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### Inside Do Kwon’s sentencing: ‘an extraordinary rise and fall’\n[Aleks Gilbert](https://www.dlnews.com/authors/Aleks-Gilbert/) 20 December 2025 [TRENDING](https://www.dlnews.com/articles/markets/coinbase-wants-argentina-return-after-temporary-exit/) [Coinbase says it plans to return to Argentina ahead of ‘temporary’ exit](https://www.dlnews.com/articles/markets/coinbase-wants-argentina-return-after-temporary-exit/) [Tim Alper](https://www.dlnews.com/authors/Tim-Alper/) 4 January 2026 [Bitcoin prices unmoved by US’ Venezuela strikes – but experts warn of Monday market turbulence](https://www.dlnews.com/articles/markets/bitcoin-prices-unmoved-by-us-venezuela-strikes/) [Tim Alper](https://www.dlnews.com/authors/Tim-Alper/) 4 January 2026 [Bitcoin miner Bitfarms exits Latin America with $30m sale to focus on AI](https://www.dlnews.com/articles/regulation/bitfarms-exits-latam-paraguay-sale/) [Mathew Di Salvo](https://www.dlnews.com/authors/Mathew-DiSalvo/) 3 January 2026 [Bitcoin just had its least volatile year ever — here’s what 2026 will bring](https://www.dlnews.com/articles/regulation/bitcoin-least-volatile-year/) [Mathew Di Salvo](https://www.dlnews.com/authors/Mathew-DiSalvo/) 3 January 2026 \n##### PRESS RELEASES\n[](https://www.dlnews.com/external/cronos-brings-cro-staking-to-upbit-expanding-access-for-korean-users/) [Cronos Brings CRO Staking to Upbit, Expanding Access for Korean Users](https://www.dlnews.com/external/cronos-brings-cro-staking-to-upbit-expanding-access-for-korean-users/) 17 hours ago [](https://www.dlnews.com/external/termmax-advances-institutional-defi-use-with-tokenized-stock-financing-integration/) [TermMax Advances Institutional DeFi Use with Tokenized Stock Financing Integration](https://www.dlnews.com/external/termmax-advances-institutional-defi-use-with-tokenized-stock-financing-integration/) 1 day ago [](https://www.dlnews.com/external/chainwire-and-cultd-partner-to-solve-the-web3-liquidity-vacuum-by-linking-media-reach-to-on-chain-impact/) [Chainwire and CULTD Partner to Solve the Web3 “Liquidity Vacuum” by Linking Media Reach to On-Chain Impact](https://www.dlnews.com/external/chainwire-and-cultd-partner-to-solve-the-web3-liquidity-vacuum-by-linking-media-reach-to-on-chain-impact/) 1 day ago [](https://www.dlnews.com/external/btcc-ends-2025-with-531-billion-in-tokenized-rwa-futures-volume-and-11m-users-despite-market-wide-volatility/) [BTCC Ends 2025 With $53.1 Billion in Tokenized RWA Futures Volume and 11M Users Despite Market-Wide Volatility](https://www.dlnews.com/external/btcc-ends-2025-with-531-billion-in-tokenized-rwa-futures-volume-and-11m-users-despite-market-wide-volatility/) 4 days ago [](https://www.dlnews.com/external/bcgame-releases-bear-smash-15000x-boost-featuring-single-tap-rounds-and-a-chance-of-15000x-win/) [BC.GAME Releases \"Bear Smash: 15000X Boost\" Featuring Single-Tap Rounds and a Chance of 15,000x Win](https://www.dlnews.com/external/bcgame-releases-bear-smash-15000x-boost-featuring-single-tap-rounds-and-a-chance-of-15000x-win/) 5 days ago [](https://www.dlnews.com/external/meet48-and-messari-publish-research-report-on-the-comprehensive-overview-of-meet48/) [MEET48 and Messari Publish Research Report on the Comprehensive Overview of MEET48](https://www.dlnews.com/external/meet48-and-messari-publish-research-report-on-the-comprehensive-overview-of-meet48/) 6 days ago [](https://www.dlnews.com/external/slotgpt-launches-a-new-ai-slot-platform-transforming-players-into-creators/) [SlotGPT launches a new AI slot platform transforming players into creators](https://www.dlnews.com/external/slotgpt-launches-a-new-ai-slot-platform-transforming-players-into-creators/) 7 days ago [](https://www.dlnews.com/external/lbank-unveils-advent-calendar-campaign-with-blackfort-mew-lc-and-shib-community-collaboration/) [LBank Unveils Advent Calendar Campaign With BlackFort, MEW, LC, and SHIB Community Collaboration](https://www.dlnews.com/external/lbank-unveils-advent-calendar-campaign-with-blackfort-mew-lc-and-shib-community-collaboration/) 7 days ago [](https://www.dlnews.com/external/cango-inc-secures-us105-million-investment-from-ewcl-to-accelerate-growth/) [Cango Inc. Secures US$10.5 Million Investment from EWCL to Accelerate Growth](https://www.dlnews.com/external/cango-inc-secures-us105-million-investment-from-ewcl-to-accelerate-growth/) 7 days ago [](https://www.dlnews.com/external/bitmine-immersion-bmnr-announces-eth-holdings-reach-411-million-tokens-and-total-crypto-and-total-cash-holdings-of-132-billion/) [Bitmine Immersion (BMNR) Announces ETH Holdings Reach 4.11 Million Tokens, and Total Crypto and Total Cash Holdings of $13.2 Billion](https://www.dlnews.com/external/bitmine-immersion-bmnr-announces-eth-holdings-reach-411-million-tokens-and-total-crypto-and-total-cash-holdings-of-132-billion/) 8 days ago [](https://www.dlnews.com/external/unchained-summit-announces-dubai-edition-scheduled-for-1st-2nd-may-2026/) [Unchained Summit Announces Dubai Edition Scheduled for 1st & 2nd May 2026](https://www.dlnews.com/external/unchained-summit-announces-dubai-edition-scheduled-for-1st-2nd-may-2026/) 8 days ago [](https://www.dlnews.com/external/meet48s-2026-roadshow-successfully-held-in-seoul-unveiling-multiple-products-to-lead-the-global-ai-web3-entertainment-industry/) [MEET48’s 2026 Roadshow Successfully Held in Seoul, Unveiling Multiple Products to Lead the Global AI + Web3 Entertainment Industry](https://www.dlnews.com/external/meet48s-2026-roadshow-successfully-held-in-seoul-unveiling-multiple-products-to-lead-the-global-ai-web3-entertainment-industry/) 9 days ago [](https://www.dlnews.com/external/phemex-upgrades-rpi-ecosystem-setting-new-liquidity-benchmarks-across-210-pairs/) [Phemex Upgrades RPI Ecosystem, Setting New Liquidity Benchmarks Across 210+ Pairs](https://www.dlnews.com/external/phemex-upgrades-rpi-ecosystem-setting-new-liquidity-benchmarks-across-210-pairs/) 11 days ago [](https://www.dlnews.com/external/crouton-digital-institutional-grade-blockchain-infrastructure-for-web3-ecosystems/) [Crouton Digital: Institutional-Grade Blockchain Infrastructure for Web3 Ecosystems](https://www.dlnews.com/external/crouton-digital-institutional-grade-blockchain-infrastructure-for-web3-ecosystems/) 11 days ago [](https://www.dlnews.com/external/tapbit-cares-marking-tapbits-4th-anniversary-with-a-year-end-christmas-csr-community-outreach-initiative/) [Tapbit Cares: Marking Tapbit’s 4th Anniversary with a Year-End Christmas CSR Community Outreach Initiative](https://www.dlnews.com/external/tapbit-cares-marking-tapbits-4th-anniversary-with-a-year-end-christmas-csr-community-outreach-initiative/) 12 days ago [](https://www.dlnews.com/external/rollercoin-named-game-of-the-year-and-best-browser-game-at-the-2025-blockchain-game-awards/) [RollerCoin Named Game of the Year and Best Browser Game at the 2025 Blockchain Game Awards](https://www.dlnews.com/external/rollercoin-named-game-of-the-year-and-best-browser-game-at-the-2025-blockchain-game-awards/) 14 days ago [](https://www.dlnews.com/external/thorchain-launches-native-cross-chain-swap-interface-in-public-beta/) [THORChain Launches Native Cross-Chain Swap Interface in Public Beta](https://www.dlnews.com/external/thorchain-launches-native-cross-chain-swap-interface-in-public-beta/) 14 days ago [](https://www.dlnews.com/external/solstice-and-cor-prime-execute-first-institutional-stablecoin-for-stablecoin-repo-on-a-public-blockchain/) [Solstice and Cor Prime Execute First Institutional Stablecoin-for-Stablecoin Repo on a Public Blockchain](https://www.dlnews.com/external/solstice-and-cor-prime-execute-first-institutional-stablecoin-for-stablecoin-repo-on-a-public-blockchain/) 14 days ago [](https://www.dlnews.com/external/valr-reflects-on-a-transformative-2025-for-crypto-and-finance/) [VALR Reflects on a Transformative 2025 for Crypto and Finance](https://www.dlnews.com/external/valr-reflects-on-a-transformative-2025-for-crypto-and-finance/) 14 days ago [](https://www.dlnews.com/external/bitmine-immersion-bmnr-announces-eth-holdings-reach-4066-million-tokens-and-total-crypto-and-total-cash-holdings-of-132-billion/) [Bitmine Immersion (BMNR) Announces ETH Holdings Reach 4.066 Million Tokens, and Total Crypto and Total Cash Holdings of $13.2 Billion](https://www.dlnews.com/external/bitmine-immersion-bmnr-announces-eth-holdings-reach-4066-million-tokens-and-total-crypto-and-total-cash-holdings-of-132-billion/) 15 days ago Powered by\n[LATEST](https://www.dlnews.com/articles/) [](https://www.dlnews.com/articles/regulation/congress-bill-to-ban-government-officials-using-polymarket/) [Prediction markets? Not for politicians, says US congressman](https://www.dlnews.com/articles/regulation/congress-bill-to-ban-government-officials-using-polymarket/) 5 hours ago [](https://www.dlnews.com/articles/defi/what-defi-protocols-expect-in-2026/) [What DeFi protocols expect in 2026](https://www.dlnews.com/articles/defi/what-defi-protocols-expect-in-2026/) 6 hours ago [](https://www.dlnews.com/articles/regulation/cynthia-lummis-worried-over-btc-sales-from-samorai-wallet/) [Pro-crypto senator Cynthia Lummis worried over government’s reported Bitcoin sales](https://www.dlnews.com/articles/regulation/cynthia-lummis-worried-over-btc-sales-from-samorai-wallet/) 8 hours ago [SNAPSHOT](https://www.dlnews.com/articles/markets/bitcoin-buyers-target-100000-by-the-end-january/) [](https://www.dlnews.com/articles/markets/bitcoin-buyers-target-100000-by-the-end-january/) [Markets](https://www.dlnews.com/articles/markets/) [Snapshot](https://www.dlnews.com/articles/snapshot/) \n### Bitcoin buyers target $100,000 by the end January. Here’s six reasons to be bullish\n[Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 6 January 2026 [TOP STORIES](https://www.dlnews.com/articles/markets/lighter-token-rebounds-as-protocol-begins-buybacks-and-whales-buy-in/) [](https://www.dlnews.com/articles/markets/lighter-token-rebounds-as-protocol-begins-buybacks-and-whales-buy-in/) [Lighter token bounces 37% as protocol begins buybacks and whales buy in](https://www.dlnews.com/articles/markets/lighter-token-rebounds-as-protocol-begins-buybacks-and-whales-buy-in/) 6 January 2026 [](https://www.dlnews.com/articles/markets/third-of-bitcoin-vulnerable-to-quantum-attack-warns-coinbase/) [Third of Bitcoin vulnerable to quantum attack, warns Coinbase research chief](https://www.dlnews.com/articles/markets/third-of-bitcoin-vulnerable-to-quantum-attack-warns-coinbase/) 6 January 2026 [](https://www.dlnews.com/articles/markets/bitcoin-buyers-target-100000-by-the-end-january/) [Bitcoin buyers target $100,000 by the end January. Here’s six reasons to be bullish](https://www.dlnews.com/articles/markets/bitcoin-buyers-target-100000-by-the-end-january/) 6 January 2026 [](https://www.dlnews.com/articles/defi/ethereum-solved-the-blockchain-trilemma-per-vitalik-buterin/) [Ethereum ‘solved’ the blockchain trilemma: Vitalik](https://www.dlnews.com/articles/defi/ethereum-solved-the-blockchain-trilemma-per-vitalik-buterin/) 5 January 2026 [TRENDING](https://www.dlnews.com/articles/markets/bitcoin-prices-unmoved-by-us-venezuela-strikes/) [](https://www.dlnews.com/articles/markets/bitcoin-prices-unmoved-by-us-venezuela-strikes/) [Markets](https://www.dlnews.com/articles/markets/) \n### Bitcoin prices unmoved by US’ Venezuela strikes – but experts warn of Monday market turbulence\n[Tim Alper](https://www.dlnews.com/authors/Tim-Alper/) 4 January 2026 [OPINION](https://www.dlnews.com/articles/markets/why-borrowing-money-to-buy-bitcoin-is-stupid/) [](https://www.dlnews.com/articles/markets/why-borrowing-money-to-buy-bitcoin-is-stupid/) [Markets](https://www.dlnews.com/articles/markets/) [Opinion](https://www.dlnews.com/articles/opinion/) \n### Why borrowing money to buy Bitcoin is ‘downright stupid’\n[Wolfgang Münchau](https://www.dlnews.com/authors/WolfgangMunchau/) 28 December 2025 [FEATURE OF THE WEEK](https://www.dlnews.com/articles/regulation/inside-do-kwons-sentencing/) [](https://www.dlnews.com/articles/regulation/inside-do-kwons-sentencing/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### Inside Do Kwon’s sentencing: ‘an extraordinary rise and fall’\n[Aleks Gilbert](https://www.dlnews.com/authors/Aleks-Gilbert/) [EDITOR'S PICK](https://www.dlnews.com/articles/markets/will-trump-venezuela-gambit-boost-bitcoin-price-in-2026/) [](https://www.dlnews.com/articles/markets/will-trump-venezuela-gambit-boost-bitcoin-price-in-2026/) [Markets](https://www.dlnews.com/articles/markets/) [Snapshot](https://www.dlnews.com/articles/snapshot/) \n### How Trump’s Venezuela gambit is seen to boost Bitcoin price in 2026\n[Lance Datskoluo](https://www.dlnews.com/authors/Lance-Datskoluo/) 5 January 2026 [DON'T MISS](https://www.dlnews.com/articles/regulation/bitfarms-exits-latam-paraguay-sale/) [Bitcoin miner Bitfarms exits Latin America with $30m sale to focus on AI](https://www.dlnews.com/articles/regulation/bitfarms-exits-latam-paraguay-sale/) [Mathew Di Salvo](https://www.dlnews.com/authors/Mathew-DiSalvo/) 3 January 2026 [Bitcoin just had its least volatile year ever — here’s what 2026 will bring](https://www.dlnews.com/articles/regulation/bitcoin-least-volatile-year/) [Mathew Di Salvo](https://www.dlnews.com/authors/Mathew-DiSalvo/) 3 January 2026 [SEC’s lone Democratic commissioner and crypto skeptic Caroline Crenshaw to depart](https://www.dlnews.com/articles/regulation/sec-democrat-caroline-crenshaw-exits/) [Mathew Di Salvo](https://www.dlnews.com/authors/Mathew-DiSalvo/) 3 January 2026\n</searchResult>\n\n\n<searchResult>\n[doc17]:\n**RSS - DL News**\n[The State of DeFi 2025 is out, see what’s next. Read more.](https://assets.dlnews.com/dlresearch/State-of-DeFi-2025.pdf) Search results\n[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results\n[](https://defillama.com/) [](https://www.dlnews.com/) \n##### RSS\n\n(Really Simple Syndication) feeds offer another way to get DLnews.com content. Subscribe to our feeds to get the latest headlines, summaries and links back to full articles - formatted for your favorite feed reader and updated throughout the day.\n\n## Terms & Conditions\n\nWe allow the use of DLnews.com RSS feeds for personal use in a news reader or as part of a non-commercial blog. We require proper format and attribution whenever DL News content is posted on your website, and we reserve the right to require that you cease distributing DLnews.com content. Please read the Terms and Conditions for complete instructions. Commercial use of the Service is prohibited without prior written permission from DL News which may be requested via email to: media@dlnews.com.\n\nArticles\n- All Articles\n- DeFi\n- Fintech/VC/Deals\n- Llama U\n- Markets\n- People & Culture\n- Regulation\n- Web3\n</searchResult>\n\n\n<searchResult>\n[doc18]:\n**How privacy coins Firo and Zcash dodged Binance delisting ... - DL News**\nSearch results\n[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results\n[](https://defillama.com/) [](https://www.dlnews.com/) This article is more than one year old\n[DeFi](https://www.dlnews.com/articles/defi/) [Regulation](https://www.dlnews.com/articles/regulation/) \n# How privacy coins Firo and Zcash dodged Binance delisting with novel transparency plan\n\n![How privacy coins Firo and Zcash dodged Binance delisting with novel transparency plan](https://www.dlnews.com/resizer/v2/HFGEY6SR7VAL7CAG4QPON5C5MA.jpg?auth=74373f5a0fa5ad620605e5f16b9fb8761684915933c8ce648c419a5cc9ded95e&amp;width=1200&amp;height=675&amp;focal=825%2C540)\n[DeFi](https://www.dlnews.com/articles/defi/) [Regulation](https://www.dlnews.com/articles/regulation/) Binance CEO Richard Teng is scrambling to withstand intense regulatory pressure on a number of fronts. Credit: Rita Fortunato/DL News\n[Home](https://www.dlnews.com/) [DeFi](https://www.dlnews.com/articles/defi/) How privacy coins Firo and Zcash dodged Binance delisting with novel transparency plan By [Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 23 January 2024 at 11:49 Share\n- Binance slapped several privacy coins with its monitor tag, stoking fears of fresh delistings.\n- Firo and Zcash have staved off delisting worries with a newly-approved tech solution.\n- It's not permanent, and given the current regulatory environment, anything could change.\n\nPrivacy coin enthusiasts can breathe a sigh of relief.\n\nAfter Binance slapped a so-called monitoring tag on a slew of privacy coins earlier this month, many worried that assets like Zcash and Firo would soon be delisted.\n\nRepresentatives from Zcash and Firo told DL News on Monday this wouldn’t happen.\n\nFor now, at least.\n\n“While I prefer not to speculate on specific timelines, Binance’s approval for Zcash to implement the new address type seems to protect ZEC from immediate delisting,” Jason McGee, Zcash’s Binance liaison, told DL News.\n\n“Although Binance hasn’t declared this a permanent fix, their willingness to adopt this change suggests an intention to collaborate on solutions with privacy coins, rather than resorting to immediate delisting.”\n\n## Could change their minds\n\nIt’s a positive step, but McGee said, “there’s always the risk they change their minds.”\n\nBinance did not immediately respond to requests for comment.\n\nReuben Yap, Firo’s project steward, was equally hesitant after disclosing the project also met Binance’s compliance requirements.\n\nEuropean Union lawmakers are close to finalising new anti-money laundering laws that could prohibit privacy coins, and a decision is expected within weeks. Yap said new regime or a change in investors’ risk appetite makes the status of privacy coins tenuous.\n\n## Exchange-only addresses\n\nBinance’s apparent decision to let the privacy coins stay listed appears to be a vote of confidence in a novel approach proposed by the issuers.\n\nIt’s a technical solution called “exchange-only” address types, which the Firo team developed last year.\n\nUnder the scheme, crypto exchanges wouldn’t be able to receive tokens for these projects unless the sending address is transparent. The exchange must be able to see the transaction history of its counterparties.\n\nZcash has two varieties of this solution: TEX Address and Traceable Unified Address. But Binance hasn’t indicated a preference for either.\n\nThis is sparking further discussion about which project should be implemented without precise guidance. “We’re still gauging the community’s preference,” McGee told DL News.\n\n## Privacy-preserving technology\n\nCritically, these changes would happen at the wallet level, he said, and not at the protocol level.\n\n“The new address type does not alter the fundamental aspects of Zcash’s privacy-preserving technology,” McGee said.\n\nIn the meantime, all tokens added to Binance’s monitor list are still tagged. The monitor tag flags users on the exchange that the assets “are likely to have higher volatility and risks compared to other listed tokens.”\n\nUsers can start trading after answering four questions in the affirmative and admitting that any losses incurred from transactions are customers’ responsibility.\n\nIt’s unclear whether Binance’s monitoring tag will be removed next quarter or how long it will take for the company to implement the “exchange-only” technical solutions.\n\n“Monitoring isn’t a delisting,” Yap said. “It’s a ‘warning.’ But they put us on warning because of non-compliance with laws.”\n\n## Crypto rules around the world\n\nBinance has come under enormous regulatory pressure in recent months.\n\nIn November, the company and its co-founder and CEO, Changpeng “CZ” Zhao, pleaded guilty to violating US banking law in connection with anti-money laundering violations. The company paid a $4.3 billion settlement and Zhao resigned as CEO.\n\nIn the meantime, OKX has already gone ahead and delisted these privacy coins and others.\n\nWith Europe’s sweeping Markets in Crypto Assets (MiCA) rules and new anti-money laundering laws soon coming into effect on the bloc, regulators are paying particular attention to privacy coins and crypto mixers.\n\n“Right now, we have complied with all the requirements,” Yap told DL News. “But as MiCA comes closer, if there are additional guidelines, we may have to do additional things.”\n\nFor now, projects like Firo and Monero will remain in purgatory just a bit longer.\n\n“No, this change does not mark the beginning of the end for privacy coins,” said McGee. “Rather, it represents the need for adaptability amidst evolving regulatory standards.”\n\nLiam Kelly is DL News’ Berlin correspondent. Contact him at liam@dlnews.com.\nRelated Topics\n[BINANCE](https://www.dlnews.com/topics/binance/) [CHANGPENG ZHAO](https://www.dlnews.com/topics/changpeng-zhao/) [MICA](https://www.dlnews.com/topics/mica/) [MONEY LAUNDERING](https://www.dlnews.com/topics/money-laundering/) You may also like\n[](https://www.dlnews.com/articles/regulation/crypto-romance-fraud-is-poised-to-accelerate-in-2024/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### Crypto romance fraud is poised to accelerate in ‘severity and scope’ in 2024\n[Callan Quinn](https://www.dlnews.com/authors/Callan-Quinn/) 8 January 2024 [](https://www.dlnews.com/articles/snapshot/sbf-will-not-face-second-trial-on-additional-charges/) [Snapshot](https://www.dlnews.com/articles/snapshot/) \n### US won’t try Sam Bankman-Fried second time on additional charges\n[Mike Millard](https://www.dlnews.com/authors/Mike-Millard/) 31 December 2023 [](https://www.dlnews.com/articles/regulation/how-china-and-asian-nations-plan-to-regulate-crypto-in-2024/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### Fraud vs innovation: How Asia’s crypto watchdogs will struggle to strike a balance in 2024\n[Callan Quinn](https://www.dlnews.com/authors/Callan-Quinn/) 31 December 2023 Related articles\n[](https://www.dlnews.com/articles/defi/monero-and-zcash-liquidity-runs-dry-as-binance-may-delist/) [DeFi](https://www.dlnews.com/articles/defi/) \n### Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins\n[Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 12 January 2024 [](https://www.dlnews.com/articles/snapshot/five-charts-explain-trueusd-dollar-depeg-and-binance-role/) [Snapshot](https://www.dlnews.com/articles/snapshot/) \n### These five charts explain TrueUSD’s fall below its dollar peg — and Binance’s role in the move\n[S. Sinclair](https://www.dlnews.com/authors/Sebastian-Sinclair/) , [A. McCarthy](https://www.dlnews.com/authors/adam-morgan/) 22 January 2024 [](https://www.dlnews.com/articles/snapshot/binance-inflows-have-surged-since-november-guilty-plea/) [Snapshot](https://www.dlnews.com/articles/snapshot/) \n### Binance trade resurgent since historic penalty, exit of Changpeng Zhao\n[Mike Millard](https://www.dlnews.com/authors/Mike-Millard/) 21 January 2024 [](https://www.dlnews.com/articles/snapshot/how-pro-crypto-traders-can-arb-bitcoin-etfs/) [Snapshot](https://www.dlnews.com/articles/snapshot/) \n### How pro crypto traders can arb Bitcoin ETFs\n[Thomas Carreras](https://www.dlnews.com/authors/Thomas-Carreras/) 17 January 2024\n</searchResult>\n\n\n<searchResult>\n[doc19]:\n**Monero and Zcash’s liquidity dries up as Binance eyes ... - DL News**\nSearch results\n[](https://www.dlnews.com/) [](https://www.dlnews.com/research/) [](https://www.dlnews.com/research/) Search results\n[](https://defillama.com/) [](https://www.dlnews.com/) This article is more than one year old\n[DeFi](https://www.dlnews.com/articles/defi/) \n# Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins\n\n![Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins](https://www.dlnews.com/resizer/v2/7YRQIT4UVZBNNFYVOQJOIX5BYA.jpg?auth=7b400c0363211c2a85babd8559211aaf467d35cd09d12a56e8509ba436046d2d&amp;width=1200&amp;height=675&amp;focal=2260%2C1507)\n[DeFi](https://www.dlnews.com/articles/defi/) Liquidity in the privacy coins market is drying up. Credit: Shutterstock\n[Home](https://www.dlnews.com/) [DeFi](https://www.dlnews.com/articles/defi/) Monero and Zcash’s liquidity dries up as Binance eyes delisting privacy coins By [Liam Kelly](https://www.dlnews.com/authors/Liam-Kelly/) 12 January 2024 at 15:29 Share\n- Regulatory pressure is spurring exchanges to delist or flag Monero and other privacy coins.\n- A new low in liquidity is spurring Zcash and Firo to find a workaround.\n- Issuers are hopeful they can reach an agreement with Binance.\n\nPrivacy coins are sinking.\n\nCryptocurrencies like Zcash and Monero are getting wrung out of the market as exchange after exchange moves to eliminate the assets from trading.\n\nOn January 5, crypto exchange OKX delisted several key privacy-centric trading pairs, stating they “do not fulfill our listing criteria.”\n\nLast week, Binance added a so-called monitor tag to Monero, Zcash, Firo, and MobileCoin, suggesting it may also delist those tokens.\n\n“Tokens with the Monitoring Tag are at risk of no longer meeting our listing criteria and being delisted from the platform,” the exchange wrote.\n\nReports on Reddit suggest that Binance’s lending program has already gone ahead and removed XMR from the list of available assets.\n\nA quick scan of Binance confirms those reports. The exchange first added XMR as a collateral asset back in May 2022.\n\n## Spooked investors\n\nThough the delisting isn’t official, it still spooked investors.\n\nZcash has fallen almost 19% in the last week, and Monero has stumbled almost 3%.\n\nThe liquidity for privacy coins such as Monero (XMR) and Zcash (ZEC) has sunk to an all-time low, according to new data from analysts at Kaiko.\n\n![Liquidity for popular privacy coins like Monero and Zcash has dried up.](https://www.dlnews.com/resizer/v2/B3Q3EWYYNBAFJK6FWDD4DWQWI4.png?auth=352a8632fd64845f5f9db9d964fef9f2e1e8dadf7f3c1c60fa3fa32535fdba52&amp;width=1440)\n\nLiquidity for popular privacy coins like Monero and Zcash has dried up.\n\n“Most businesses will not want to interact with privacy coins given their negative connotations,” Clara Medalie, Kaiko’s director of research, told DL News.\n\n“Many exchanges are delisting privacy coins, which suggests that market makers don’t want to provide liquidity for them.”\n\nPrivacy coins can obfuscate users’ identities by hiding sender details and transaction history.\n\nThis makes them notoriously difficult to track, drawing scrutiny from regulators worldwide.\n\nA core feature of the original crypto ethos, privacy coins also continue to command many investors’ attention. Monero and Zcash boast a combined market capitalization of $3.48 billion.\n\nThis position now appears to be at serious risk, experts say.\n\n## Serious challenge\n\nWith $15 billion in daily trading volume, Binance’s dominance makes its action a serious challenge to the fortunes of these projects.\n\nBinance doesn’t have much of a choice. After pleading guilty in November to violating US banking law and paying a $4 billion penalty, it’s required to implement stronger anti-money laundering and know-your-customer controls.\n\n> ‘Binance was clear from the beginning that if we did not create an exchange-only address type, they would delist ZEC.’— Jason McGee\n\nMoreover, in negotiations over the EU’s Anti-Money Laundering Regulation, lawmakers are discussing whether to ban privacy coins like Monero and Zcash.\n\n## Fight is on\n\nNow, the fight’s on to keep Binance from axing privacy coins altogether.\n\nSome projects have devised a novel workaround to try and get the nod from Binance.\n\nOthers, such as Monero, refuse to comply with Binance’s requests, with members of its community lashing out against the exchange in December. A Monero representative did not reply to a request for comment.\n\n## All-seeing crypto addresses\n\nThe workaround others are trying is called an “exchange-only” crypto address.\n\nThe idea is that users looking to move funds to an exchange would whip up a new transparent address, send private funds to this address, and then send those funds to the exchange-only address.\n\nFirst proposed by the privacy project Firo last November – which is also on Binance’s chopping block – an exchange-only address can only receive funds from transparent addresses rather than their private, or so-called shielded, counterparts.\n\n“They don’t want to receive shielded transactions,” Jason McGee, a committee member for Zcash Community Grants and the project’s Binance liaison, told DL News.\n\n“Binance was clear from the beginning (early November) that if we did not create an exchange-only address type, they would delist ZEC.”\n\n> ‘Binance doesn’t want to touch any funds from sources that have an unidentified send.’— Reuben Yap\n\nFiro project steward Reuben Yap told DL News that Binance initially asked the project to remove all its privacy features. He said it couldn’t.\n\nBinance is still mulling the proposed solution, say McGee and Yap. They are hopeful it will be accepted because it would let the exchange show regulators the history of a depositing address.\n\n“Binance doesn’t want to touch any funds from sources that have an unidentified send,” Yap said.\n\nBinance did not immediately respond to DL News’ request for comment.\n\nJustin Ehrenhofer, the founder of a crypto sleuthing firm focused on difficult-to-trace transactions Moonstone Research, told DL News the Monero community wasn’t considering the exchange-only approach.\n\n## Lots of discussion\n\nIn any event, the idea is generating some buzz.\n\n“There has been a tremendous amount of discussion about this within the Zcash community,” Zooko Wilcox-O’Hearn, the CEO of Electric Coin Company, the firm developing Zcash, told DL News.\n\nYap told DL News that the exchange address solution is expected to launch in two weeks.\n\nAs to what Binance will do at that point, it’s anyone’s guess.\n\nLiam Kelly is a Berlin-based DeFi Correspondent. Contact him at liam@dlnews.com or on Telegram at @Liam_Gallas.\nRelated Topics\n[MONERO](https://www.dlnews.com/topics/monero/) [BINANCE](https://www.dlnews.com/topics/binance/) [OKX](https://www.dlnews.com/topics/okx/) You may also like\n[](https://www.dlnews.com/articles/regulation/how-china-and-asian-nations-plan-to-regulate-crypto-in-2024/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### Fraud vs innovation: How Asia’s crypto watchdogs will struggle to strike a balance in 2024\n[Callan Quinn](https://www.dlnews.com/authors/Callan-Quinn/) 31 December 2023 [](https://www.dlnews.com/articles/people-culture/dl-news-top-stories-featured-bitcoin-etfs-and-defi-heists/) [People & culture](https://www.dlnews.com/articles/people-culture/) [Regulation](https://www.dlnews.com/articles/regulation/) [DeFi](https://www.dlnews.com/articles/defi/) [Markets](https://www.dlnews.com/articles/markets/) \n### Bitcoin ETFs, regulators, and DeFi heists ruled crypto in 2023: Check out DL News’ top stories of the year\n[Edward Robinson](https://www.dlnews.com/authors/edward-robinson/) 29 December 2023 [](https://www.dlnews.com/articles/regulation/the-crypto-court-cases-to-keep-an-eye-on-in-2024/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### Crypto court cases will heat up in 2024 — here are the ones to watch\n[Joanna Wright](https://www.dlnews.com/authors/joannawright/) 25 December 2023 Related articles\n[](https://www.dlnews.com/articles/regulation/eus-new-aml-rules-may-impact-uniswap-binance-and-monero/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### EU regulators flag new crypto risks and weigh rules that may impact Uniswap and Binance\n[Inbar Preiss](https://www.dlnews.com/authors/Inbar-Preiss/) 2 June 2023 [](https://www.dlnews.com/articles/regulation/what-do-cybercriminals-do-with-stolen-crypto/) [Regulation](https://www.dlnews.com/articles/regulation/) [DeFi](https://www.dlnews.com/articles/defi/) \n### How hackers turn stolen crypto into cash\n[Eric Johansson](https://www.dlnews.com/authors/eric-johansson/) 24 April 2023 [](https://www.dlnews.com/articles/regulation/crypto-romance-fraud-is-poised-to-accelerate-in-2024/) [Regulation](https://www.dlnews.com/articles/regulation/) \n### Crypto romance fraud is poised to accelerate in ‘severity and scope’ in 2024\n[Callan Quinn](https://www.dlnews.com/authors/Callan-Quinn/) 8 January 2024 [](https://www.dlnews.com/articles/snapshot/sbf-will-not-face-second-trial-on-additional-charges/) [Snapshot](https://www.dlnews.com/articles/snapshot/) \n### US won’t try Sam Bankman-Fried second time on additional charges\n[Mike Millard](https://www.dlnews.com/authors/Mike-Millard/) 31 December 2023\n</searchResult>\n\n\n"
  },
  {
    "ToolCallId": "call_5coSSOTWxOlcR9vW4XWxx6US",
    "Output": "<searchResult>\n[doc7]:\n**Zcash Social Sentiment & Market Pulse Data | BitMart X Insight**\n[](https://www.bitmart.com/en-US) - Investment\n- Copy Trading\n- X Insight\n- Beacon\n- \n- Exchange\n- USDⓈ-M\n[](https://www.bitmart.com/en-US/login?goto=ai%2fxinsight%2fcoins%2fdetail%2fZEC) [](https://www.bitmart.com/en-US/register?goto=ai%2fxinsight%2fcoins%2fdetail%2fZEC) \n# Zcash (ZEC)\n$498.85 -0.48% 24H - 59Social Sentiment Index (SSI)+3.03% (24h)\n- #165Market Pulse Ranking (MPR)-9\n- 2424h Social Mention+9.09% (24h)\n- 42%24h KOL Bullish Ratio12 Active KOL\n- SummaryZEC price nears resistance 530, volume insufficient, KOL emphasizes first retesting the 470 liquidity zone; whether it breaks resistance or retraces to lower levels will determine the subsequent trend.\n- Bullish SignalsBreakout of descending channel10% localized rebound12h bullish reversalPotential break of resistance 530Social hype rising\n- Bearish SignalsLack of volume supportUpper resistance 530 unbrokenPrice deviates from 470 liquidity zoneMay fall back to 450Distribution characteristics emerging\n\n## Social Sentiment Index (SSI)\n- Data Overall59SSI\n- SSI Trend (7D) Price (7D)Sentiment Distribution Extremely Bullish (13%) Bullish (29%) Neutral (17%) Bearish (38%) Extremely Bearish (3%)SSI InsightsZEC social heat is medium (58.96/100, +3.03%), activity up 19.05% driven, KOL attention full score, sentiment slightly down, linked to the battle for resistance 530 and KOL's suggestion to retest 470.\n\n## Market Pulse Ranking (MPR)\n- \n- Alert InsightZEC warning rank dropped to #165 (↓9), social anomaly 8.4, sentiment polarization 1.77, KOL attention shift ↑300% to 6, related to low volume and unbroken resistance 530.\n\n## X Posts\n- Eric Van Tassel (Not a Financial Advisor!) TA_Analyst Influencer S 5.83K @XRPathologistTired of waiting for the #ZEC price to so something? That's all intentional! One thing people often miss about a liquidity grab is that they’re usually fast, not slow. The slow part is the setup; compression, failed pushes, and positioning. The move to liquidity is execution, not negotiation. When price finally commits, it doesn’t stair-step down. It moves quickly to trigger stops, fill resting orders, and reset structure. Slow chop builds the trap. Speed is how it’s sprung. 23 1 745 Original >Trend of ZEC after release BearishZEC is in the layout stage before a liquidity grab, and may experience a rapid drop that triggers stop‑losses to clean the market.\n- Eric Van Tassel (Not a Financial Advisor!) TA_Analyst Influencer S 5.83K @XRPathologistTired of waiting for the #ZEC price to so something? That's all intentional! One thing people often miss about liquidity grab they’re usually fast, not slow. The slow part is the setup; compression, failed pushes, and positioning. The move to liquidity is execution, not negotiation. When price finally commits, it doesn’t stair-step down. It moves quickly to trigger stops, fill resting orders, and reset structure. Slow chop builds the trap. Speed is how it’s sprung. 8 0 202 Original >Trend of ZEC after release BearishZEC's slow consolidation is a trap, expected to rapidly drop and trigger stop losses.\n- Khal Founder DeFi_Expert B 3.01K @khalkazHey @grok, you get to choose your salary: Option A: $250,000 per year Option B: 200 $ZEC per year Which do you choose and why? 0 1 56 Original >Trend of ZEC after release NeutralComparing a $250,000 annual salary with a 200 ZEC annual salary, there is no clear inclination yet.\n- Ardi Trader TA_Analyst S 18.58K @ArdiNSC$ZEC back into the parallel range after another failed upthrust at ~$530. Highly likely it retests the $450–$470 liquidity zone if we lose ~$488 support on closes. Only bullish scenario is sweeping that lower liquidity pocket and then reclaiming higher. Further closes below that zone = structural breakdown, and likely continues the corrective wave.Ardi Trader TA_Analyst S 18.58K @ArdiNSC$ZEC / Zcash Solid ~10% bounce off the local lows, finally punching out of that descending parallel channel and flipping some local levels back to support. Key overhead right now is the $530 zone. Apart from the initial spike to $550, we've seen multiple tests at $530 have minimal acceptance, and this latest move up is showing some more distribution in this region. On the support side, I'd want to see price to respect the channel breakout and stay clear of re-entering it. First real defense is a hold above $505. Dipping back inside the range wouldn't kill the whole setup, but repeated fails to hold reclaimed levels would be a serious warning sign for slowing momentum. If $530 flips convincingly to support, it clears the path for another legitimate shot at $550 and higher. 72 30 4.77K Original >Trend of ZEC after release NeutralZEC faces strong resistance at $530; a breakthrough could lead to a rise, while a break below $488 support entails structural risk.\n- mert | helius.dev Dev OnChain_Analyst B 305.24K @mertthey cant take what they cant see zcash, $10,000 https://t.co/9ABdwqtoFdBitcoin Junkies D 36.30K @BitcoinJunkies🇺🇸 California Governor Gavin Newsom has signed a bill allowing the state to transfer custody of any Bitcoin or cryptocurrency held on exchanges after three years of inactivity. Under the law, inactive accounts on centralized exchanges are classified as \"unclaimed property.\" https://t.co/a9YDVa2rHU 261 48 13.74K Original >Trend of ZEC after release BullishCalifornia passed a bill that can confiscate inactive crypto assets, and the tweet uses this to be bullish on Zcash’s privacy features while setting a $10,000 target price.\n- Nebraskangooner TA_Analyst Trader C 402.42K @Nebraskangooner$ZEC (per request) From breakout to resistance and then I urged caution and patience at resistance. Now it's just chopping and grinding in the middle of nowhere. Seems more likely to breakdown right now with resistance holding strong. Likely back towards $450 area https://t.co/g5EOmSHyUsNebraskangooner TA_Analyst Trader C 402.42K @Nebraskangooner$ZEC Cocky late buyers are getting smoked right now. This is why I said patience after target was reached. Got a lot of nasty comments about it. Still rejecting at resistance. Careful, if it loses that breakout level could drop hard. https://t.co/I77hYjXMam 43 13 10.14K Original >Trend of ZEC after release BearishZEC is being blocked at resistance, facing a risk of a breakdown, possibly falling to the $450 area.\n- Stalkchain OnChain_Analyst Influencer C 49.66K @StalkHQA wallet just bought $400k of $zec wallet: A5DbJZMEkuBhoAF5s2wyrTDbqD3zbkrsqFjywbM34f85 https://t.co/y6r8XRQZYd 11 3 1.52K Original >Trend of ZEC after release Bullish某钱包大额买入40万美元ZEC\n- Eric Van Tassel (Not a Financial Advisor!) TA_Analyst Influencer S 5.83K @XRPathologistI’m adding this chart to introduce a new way of visualizing price behavior for #ZEC. - Green zones show where buyers previously stepped in. - Orange zones show where sellers previously stepped in. - Blue zones mark areas that failed and flipped, where traders got trapped. In this case bears. These zones don’t predict direction on their own. They help identify where reactions are more likely when structure and liquidity align. Between fib retracement levels, structure, and the order blocks here, you can see why the green zone is a high value setup! 67 11 2.69K Original >Trend of ZEC after release BullishZEC technical analysis shows the green area as a high‑value setup, indicating a potential buying opportunity.\n- Eric Van Tassel (Not a Financial Advisor!) TA_Analyst Influencer S 5.83K @XRPathologistTrading and investing in #ZEC, or any asset, is about buying and selling at the appropriate time. A good setup isn’t about predicting, it’s about location plus confirmation. Great investors are patient enough to wait for good setups! - Price at a well-defined liquidity zone - HTF structure respected - Fib confluence at that level - Then confirmation via expanding volume/acceptance If you’re chasing price away from liquidity, you’re trading hope, not structure. 40 2 2.10K Original >Trend of ZEC after release NeutralZEC should wait for structural confirmation at the key liquidity zone before entering\n- Eric Van Tassel (Not a Financial Advisor!) TA_Analyst Influencer S 5.83K @XRPathologistWhen the #ZEC price moves higher before resolving nearby liquidity, it often increases the odds of a deeper unwind later. Extensions build imbalance. That’s why pushes up that come first can raise the probability of tagging lower fib extensions like the 1.414–1.618 on a pullback. If the current high holds, these price targets become more likely. A 1.618 extension can possibly take price as low as the $453 area now. 34 3 2.21K Original >Trend of ZEC after release BearishIf ZEC fails to hold the current high, it could see a deep retracement to the $453 area.\n-\n</searchResult>\n\n\n<searchResult>\n[doc2]:\n**Zcash News Today (ZEC) – Latest Updates & Trends**\n[](https://www.coinbird.com/) [](https://www.coinbird.com/) [](https://www.coinbird.com/) \n![Zcash Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/ZEC.svg)\n\n![Zcash Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/ZEC.svg)\n\n# Zcash news\nLatest Zcash news and market trends\n[Buy ZEC](https://www.coinbird.com/go/crypto_buy) [Latest ZEC news](https://www.coinbird.com/cryptocurrencies/zcash/news#latest-news) [Zcash news sentimentLast 30 daysPositive77/100](https://www.coinbird.com/cryptocurrencies/zcash/news#news-sentiment) \n## The most important Zcash news this month\nAI summary \n### Zcash Shielded Supply Rises\n\nZebra 3.1 upgrade increased shielded supply to almost 25 %, signaling growing privacy adoption.\n\n### Cypherpunk Buys $28 M Zcash\n\nWinklevoss-backed firm purchased 56,418 ZEC, raising holdings to 1.76 % of supply, reflecting confidence in privacy coins.\n\n### Unshielded ZEC Spike Sparks Sell‑Off\n\n200,000 ZEC moved to transparent pool and a 74k transfer to Binance raised concerns about potential sell‑off and price drop.\n\n### What this could mean for Zcash\n\nThe rapid growth of shielded ZEC, coupled with high-profile institutional purchases, boosts confidence and could drive price upward, but recent unshielding activity introduces short-term volatility risks.\nThe AI-generated summaries are experimental and may contain errors. Not investment advice. Last updated: 2026-01-06T16:34:02.141+00:00 . \n## Latest Zcash news\n\nUpdated at 2026-01-06T23:30:52.492Z\n\nUpdated at 2026-01-06T23:30:52.492Z\nHeadline\nImpact score Impact score \nOur Impact Score (0–100) uses AI to estimate how strongly a news item could affect the coin over the next 24–72 hours. It primarily considers direct relevance to the coin, novelty, source quality and diversity, potential reach, and the type of event, such as ETFs and regulation, product launches, partnerships, or hacks. Higher scores are assigned to substantiated research forecasts, corporate buy or sell activity, and clear statements from well-known figures. Low scores apply to bare price predictions without substance, minor price moves without context, or PR pieces with no informational value. The score is computed automatically and updated continuously. The AI may make mistakes. When in doubt, please review the linked original sources. Not financial advice.\nPublished\n\n## Zcash news sentiment\n\nLast 30 days\nPositive\n77 /100 \nCurrent Zcash news sentiment is positive (77/100), based on 14 news articles from the past 30 days. Our algorithm scores each article for relevance and sentiment (positive, neutral, or negative) and weights high-impact stories more. The score updates automatically as new Zcash headlines arrive.\n\n## Zcash market trends\nPositive Negative Positive \nMomentum\nMomentum \nMomentum measures the current market dynamics of a cryptocurrency. The value is based on technical indicators such as the Relative Strength Index (RSI), the Fear & Greed Index, and the short-term price trend over the past 30 days. Positive values indicate upward momentum, negative values indicate downward momentum. This indicator is for informational purposes only and does not constitute investment advice.\nPositive [Momentum](https://www.coinbird.com/cryptocurrencies/zcash/news#buy-timing-dashboard) [Momentum](https://www.coinbird.com/cryptocurrencies/zcash/buy#buy-timing-dashboard) Fear Fear Greed \nFear & Greed Index\nFear & Greed Index \nThe Fear and Greed Index for cryptocurrencies is a sentiment indicator measuring market mood on a scale from 0 (extreme fear) to 100 (extreme greed). It aggregates data from various sources such as volatility, market momentum, social media, market dominance, and Google Trends to assess overall market sentiment. Values in the “Greed” range (55-100) indicate a positive, potentially overoptimistic market mood, signaling a possibly overheated market. A “Neutral” value (45-54) reflects a balanced market sentiment. Values in the “Fear” range (0-44) indicate negative market sentiment, signaling fear or pessimism among investors and possibly an undervalued market.\nFear [Fear & Greed Index](https://www.coinbird.com/learn/fear-greed-index-bitcoin) 16 /30 days \nPrice trend\nPrice trend \nThe price trend shows short-term price action over the last 30 trading days. For each day, the open is compared to the close: if the close is higher, the day is marked green; otherwise red. A sustained majority of green days suggests an uptrend that may persist in the short to medium term.\nPositive [Zcash price](https://www.coinbird.com/cryptocurrencies/zcash/price) \n$501.31\n+46.57% last 30 days \n### Price performance\nPrice performance \nThe price development, often referred to as return on investment (ROI), is a metric that provides insight into the past profitability and performance of an investment. In this context, ROI describes the percentage change in price and thus the retrospective “return” of a cryptocurrency over a defined period. Past performance is not indicative of future results.\n<table>\n  <tr>\n    <td>↑+0.15%</td>\n    <th>Hour</th>\n  </tr>\n  <tr>\n    <td>↓-0.37%</td>\n    <th>Day</th>\n  </tr>\n  <tr>\n    <td>↓-4.35%</td>\n    <th>Week</th>\n  </tr>\n  <tr>\n    <td>↑+46.57%</td>\n    <th>Month</th>\n  </tr>\n  <tr>\n    <td>↑+1,160.13%</td>\n    <th>200d</th>\n  </tr>\n  <tr>\n    <td>↑+745.09%</td>\n    <th>Year</th>\n  </tr>\n</table>\n\n## Other cryptocurrency news\n\n![Bitcoin Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/BTC.svg)\n\nBitcoinNews\n\nNEGATIVE2025-12-27T17:01:38+00:00•decrypt.co\n\nBitcoin Whales Woke Up in 2025 and Moved Billions in BTC—Here's Why\n90 /100 \nPOSITIVE2025-12-10T01:44:16+00:00•cointelegraph.com\n\nVivek Ramaswamy's Strive to raise $500M to buy Bitcoin\n90 /100 [Latest Bitcoin news](https://www.coinbird.com/cryptocurrencies/bitcoin/news) \n![Ethereum Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/ETH.svg)\n\nEthereumNews\n\nPOSITIVE2026-01-05T17:04:59+00:00•decrypt.co\n\nEthereum's Blockchain Trilemma 'Solved': Vitalik Buterin\n90 /100 \nPOSITIVE2026-01-05T12:26:24+00:00•cryptoslate.com\n\nVitalik Buterin declares Ethereum solved crypto Trilemma, yet his 2030 roadmap exposes a massive ideological risk\n90 /100 [Latest Ethereum news](https://www.coinbird.com/cryptocurrencies/ethereum/news) \n![XRP Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/XRP.svg)\n\nXRPNews\n\nPOSITIVE2025-12-11T15:43:35+00:00•theblock.co\n\nNew XRP ETF hits the market with launch of 21Shares' TOXR\n90 /100 \nPOSITIVE2025-12-08T13:20:11+00:00•coindesk.com\n\nU.S. Spot XRP ETFs Hit 15-Day Inflow Streak, Near $1B Milestone\n90 /100 [Latest XRP news](https://www.coinbird.com/cryptocurrencies/xrp/news) \n![Solana Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/SOL.svg)\n\nSolanaNews\n\nPOSITIVE2026-01-06T19:21:01+00:00•theblock.co\n\n‘Shocker': Morgan Stanley's Bitcoin and Solana ETF filings signal deep institutional commitment to crypto\n90 /100 \nNEGATIVE2025-12-30T10:39:00+00:00•beincrypto.com\n\nHNUT Meme Coin Collapses 99% on Solana, PeckShield Flags Bundled Rug Pull\n85 /100 [Latest Solana news](https://www.coinbird.com/cryptocurrencies/solana/news) \n![Dogecoin Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/DOGE.svg)\n\nDogecoinNews\n\nNEGATIVE2025-12-25T14:01:03+00:00•decrypt.co\n\nThe Year in Dogecoin 2025: DOGE Goes Political and Commercial\n85 /100 \nPOSITIVE2025-12-25T19:06:23+00:00•cryptoslate.com\n\nThe memecoin hall of shame: 10 tokens that defined 2025 wildest trades\n80 /100 [Latest Dogecoin news](https://www.coinbird.com/cryptocurrencies/dogecoin/news) \n![Cardano Logo](https://gaaxwivrjtgyloabfswe.supabase.co/storage/v1/object/public/logos/cryptocurrencies/ADA.svg)\n\nCardanoNews\n\nPOSITIVE2025-12-14T18:11:25+00:00•cryptoslate.com\n\nCardano now has institutional-grade infrastructure, but a glaring $40 million liquidity gap threatens to stall growth\n80 /100 \nPOSITIVE2025-12-15T17:12:01+00:00•beincrypto.com\n\n3 Altcoins Facing Liquidation Risks in the Third Week of December\n70 /100 [Latest Cardano news](https://www.coinbird.com/cryptocurrencies/cardano/news) \n### Other crypto news\n- BNBnews\n- Tronnews\n- Bitcoin Cashnews\n- Chainlinknews\n- Stellarnews\n- Suinews\n- Hyperliquidnews\n- Litecoinnews\n- Avalanchenews\n- Hederanews\n- Shiba Inunews\n- Uniswapnews\n- Polkadotnews\n- Pepenews\n- Aavenews\n- NEAR Protocolnews\n- Worldcoinnews\n- Ondonews\n- Kaspanews\n- Polygon (POL)news\n- Algorandnews\n- Rendernews\n- Cosmosnews\n- Filecoinnews\n- VeChainnews\n- Bonknews\n- ASI (Fetch.ai)news\n- Tezosnews\n- IOTAnews\n- The Graphnews\n- Sonic (Fantom)news\n- The Sandboxnews\n- Decentralandnews\n- Axie Infinitynews\n\n## All about Zcash\n[What is Zcash?Important details and simple explanation of Zcash.](https://www.coinbird.com/cryptocurrencies/zcash/overview) [Zcash priceLive price, charts and market data for Zcash.](https://www.coinbird.com/cryptocurrencies/zcash/price) [Zcash predictionPrice forecasts and key metrics to analyze Zcash.](https://www.coinbird.com/cryptocurrencies/zcash/price-prediction) [Buy ZcashFind the cheapest and best places to buy Zcash.](https://www.coinbird.com/cryptocurrencies/zcash/buy) [Zcash converterSee what past Zcash buys would be worth today.](https://www.coinbird.com/cryptocurrencies/zcash/converter) \nOur data on cryptocurrencies was last updated on 2026-01-07T00:05:26.994203+00:00. Sources: CoinGecko, defillama.com, coincodex.com.\n\nThe content on this website is provided for general informational purposes only and does not constitute financial, investment, legal, or tax advice. It should not be interpreted as a recommendation to buy, sell, or hold cryptocurrencies, nor as a guarantee of future price developments. You are responsible for independently verifying any information before using a listed service. Trading cryptocurrencies involves significant risk and can result in the total loss of your capital. Past performance is not indicative of future results. We do not accept any liability for the timeliness, accuracy, or completeness of the information provided, including content from external or third-party sources. All actions are taken at your own risk. Some links on this website are affiliate links. If you purchase a product or use a service through these links, we may receive a commission at no additional cost to you. Our content, comparisons, and rankings remain editorially independent. This helps us provide free content and continue developing the platform. Thank you for your support.\n</searchResult>\n\n\n<searchResult>\n[doc8]:\n**Will Zcash (ZEC) Price Finally Retest $500 After Nearly 8 Years?**\n# guce\n[guce](https://consent.yahoo.com/v2/&#x2F;&#x2F;uk.yahoo.com&#x2F;) \nYahoo is part of the Yahoo family of brandsThe sites and apps that we own and operate, including Yahoo and Engadget, and our digital advertising service, Yahoo Advertising.Yahoo family of brands.\nWhen you use our sites and apps, we use Cookies Cookies (including similar technologies such as web storage) allow the operators of websites and apps to store and read information from your device. Learn more in our [cookie policy](https://consent.yahoo.com/redirect?to=https%3A%2F%2Flegal.yahoo.com%2Fie%2Fen%2Fyahoo%2Fprivacy%2Fcookies%2Findex.html&brandDomain=&brandId=yahoo&tos=eu&step=&sessionId=3_cc-session_67c6371b-727a-461b-8907-3835b3bdd1ca&userType=NON_REG) . cookies to: - provide our sites and apps to you\n- authenticate users, apply security measures, and prevent spam and abuse, and\n- MeasurementWe count the number of visitors to our pages, the type of device they use (iOS or Android), the browser they use, and the duration of their visit to our websites and apps. This data is collected in aggregate and is not tied to specific users.measure your use of our sites and apps\nIf you click ' **Accept all** ', we and [our partners](https://consent.yahoo.com/v2/partners-list?sessionId=3_cc-session_67c6371b-727a-461b-8907-3835b3bdd1ca) , including 245 who are part of the IAB Transparency & Consent Framework, will also store and/or access information on a device (in other words, use cookies) and use precise geolocation data and other personal data such as IP address and browsing and search data, for analytics, personalized advertising and content, advertising and content measurement, and audience research and services development. \nIf you do not want us and our partners to use cookies and personal data for these additional purposes, click 'Reject all'.\n\nIf you would like to customise your choices, click 'Manage privacy settings'.\n\nYou can withdraw your consent or change your choices at any time by clicking on the 'Privacy & Cookie Settings' or 'Privacy Dashboard' links on our sites and apps. Find out more about how we use your personal data in our Privacy Policy and Cookie Policy.\n[Manage privacy settings](https://consent.yahoo.com/v2/partners?sessionId=3_cc-session_67c6371b-727a-461b-8907-3835b3bdd1ca)\n</searchResult>\n\n\n<searchResult>\n[doc4]:\n**Latest Zcash News - (ZEC) Future Outlook, Trends & Market Insights**\n[](https://coinmarketcap.com/) [Cryptocurrencies](https://coinmarketcap.com/) Cryptocurrencies\n[Ranking](https://coinmarketcap.com/) [Categories](https://coinmarketcap.com/cryptocurrency-category/) [Historical Snapshots](https://coinmarketcap.com/historical/) [Token unlocks](https://coinmarketcap.com/token-unlocks/) [Yield](https://coinmarketcap.com/yield/) [Real-World Assets](https://coinmarketcap.com/real-world-assets/) Leaderboards\n[Trending](https://coinmarketcap.com/trending-cryptocurrencies/) [Upcoming](https://coinmarketcap.com/upcoming/) [Recently Added](https://coinmarketcap.com/new/) [Gainers & Losers](https://coinmarketcap.com/gainers-losers/) [Most Visited](https://coinmarketcap.com/most-viewed-pages/) [Community Sentiment](https://coinmarketcap.com/sentiment/) [Chain Ranking](https://coinmarketcap.com/chain-ranking/) NFT\n[Overall NFT Stats](https://coinmarketcap.com/nft/) [Upcoming Sales](https://coinmarketcap.com/nft/upcoming/) [Dashboards](https://coinmarketcap.com/charts/) Markets\n[Market Overview](https://coinmarketcap.com/charts/) [Spot Market](https://coinmarketcap.com/charts/spot-market/) [Derivatives Market](https://coinmarketcap.com/charts/derivatives-market/) [No. of Cryptocurrencies](https://coinmarketcap.com/charts/number-of-cryptocurrencies-tracked/) [BNB Treasuries](https://coinmarketcap.com/charts/bnb-treasuries/) Indicators\n[Fear and Greed Index](https://coinmarketcap.com/charts/fear-and-greed-index/) [Altcoin Season Index](https://coinmarketcap.com/charts/altcoin-season-index/) [Market Cycle Indicators](https://coinmarketcap.com/charts/crypto-market-cycle-indicators/) [Bitcoin Dominance](https://coinmarketcap.com/charts/bitcoin-dominance/) [CoinMarketCap 20 Index](https://coinmarketcap.com/charts/cmc20/) [CoinMarketCap 100 Index](https://coinmarketcap.com/charts/cmc100/) ETF Flows\n[Crypto ETFs](https://coinmarketcap.com/etf/) [Bitcoin ETFs](https://coinmarketcap.com/etf/bitcoin/) [Ethereum ETFs](https://coinmarketcap.com/etf/ethereum/) Technical Analysis\n[RSI](https://coinmarketcap.com/charts/rsi/) [MACD](https://coinmarketcap.com/charts/macd/) Derivatives\n[Funding Rates](https://coinmarketcap.com/charts/funding-rates/) [DexScan](https://dex.coinmarketcap.com/token/all/) [SignalsNew](https://dex.coinmarketcap.com/signals/all/) [Trending](https://dex.coinmarketcap.com/token/all/) [New](https://dex.coinmarketcap.com/token/all/?tableRankBy=new_24h) [Gainers](https://dex.coinmarketcap.com/token/all/?tableRankBy=gainers_24h) [Meme Explorer](https://dex.coinmarketcap.com/meme/four.meme/) [Top Traders](https://dex.coinmarketcap.com/top-traders/all/) [Exchanges](https://coinmarketcap.com/rankings/exchanges/) Centralized Exchanges\n[Spot](https://coinmarketcap.com/rankings/exchanges/) [Derivatives](https://coinmarketcap.com/rankings/exchanges/derivatives/) Decentralized Exchanges\n[Spot](https://coinmarketcap.com/rankings/exchanges/dex/?type=spot) [Derivatives](https://coinmarketcap.com/rankings/exchanges/dex/?type=derivatives) [Community](https://coinmarketcap.com/community/) [Feeds](https://coinmarketcap.com/community/) [Topics](https://coinmarketcap.com/community/topics/) [Lives](https://coinmarketcap.com/community/lives/) [Articles](https://coinmarketcap.com/community/articles/) [Sentiment](https://coinmarketcap.com/sentiment/) Products Products\n[Converter](https://coinmarketcap.com/converter/) [Newsletter](https://coinmarketcap.com/newsletter/) [CMC Launch](https://coinmarketcap.com/cmclaunch/) [CMC Labs](https://coinmarketcap.com/events/cmc-labs/) [Telegram Bot](https://coinmarketcap.com/chatbot/) [Advertise](https://coinmarketcap.com/events/advertise/) [Crypto API](https://coinmarketcap.com/api/) [Site Widgets](https://coinmarketcap.com/widget/ticker/) Campaigns\n[Airdrops](https://coinmarketcap.com/airdrop/) [Diamond Rewards](https://coinmarketcap.com/account/rewards/) [Learn & Earn](https://coinmarketcap.com/earn/) Calendars\n[ICO Calendar](https://coinmarketcap.com/ico-calendar/) [Events Calendar](https://coinmarketcap.com/events/) Learn\n[News](https://coinmarketcap.com/headlines/news/) [Academy](https://coinmarketcap.com/academy/) [Research](https://coinmarketcap.com/academy/categories/cmc-research/) [Videos](https://www.youtube.com/channel/UCnhdZlwVd6ocXGhdSyV9Axg/?sub_confirmation=1) [Glossary](https://coinmarketcap.com/academy/glossary/) \n# Latest Zcash (ZEC) News Update\nBy CMC AI 06 January 2026 12:16AM (UTC+0) [See ZEC Price Chart](https://coinmarketcap.com/currencies/zcash/#cmcaiquestion=0) \n## What is the latest news on ZEC?\n\n## TLDR\n\nZcash navigates bullish technicals and whale-sized bets as privacy narratives gain steam. Here are the latest news:\n1. Bull Flag Holds Despite Weakness (6 January 2026) – ZEC’s bullish structure remains intact, but weakening momentum signals caution.\n2. Whale Bets $39M on ZEC Long (5 January 2026) – A crypto whale opened a leveraged position equivalent to 1.2% of ZEC’s circulating supply.\n3. Grayscale Zcash Trust Discount Widens (5 January 2026) – Shares trade 25% below net asset value despite rising institutional interest.\n\n## Deep Dive\n\n### 1. Bull Flag Holds Despite Weakness (6 January 2026)\n\nOverview: ZEC maintains a bullish market structure with an 85% upside target ($930+) if it holds above $404 support. However, momentum indicators like the Chaikin Money Flow (CMF) near zero suggest weakening buying pressure.\n\nWhat this means: The technical setup is bullish long-term but faces headwinds from Bitcoin’s negative correlation with ZEC and $39M in short-term short leverage. A break below $404 could trigger a deeper correction. (TokenPost)\n\n### 2. Whale Bets $39M on ZEC Long (5 January 2026)\n\nOverview: Address 0x6b26 opened a 5x leveraged long position with 79,438 ZEC ($39.24M) on Binance, risking amplified volatility.\n\nWhat this means: Large leveraged positions increase liquidation risks—$54M in shorts vs. $24M longs sit near current prices. While this signals confidence, the whale already faces a $1.88M unrealized loss, raising concerns about forced selling. (Binance News)\n\n### 3. Grayscale Zcash Trust Discount Widens (5 January 2026)\n\nOverview: Grayscale’s Zcash Trust (ZCSH) shares trade at a 25% discount to NAV despite holding $190M in ZEC, reflecting skepticism about near-term liquidity improvements.\n\nWhat this means: The widening gap between institutional and spot prices highlights ZEC’s regulatory ambiguity but could create arbitrage opportunities if ETF conversion rumors materialize. (CoinMarketCap)\n\n## Conclusion\n\nZcash balances bullish technicals against whale-driven volatility and institutional hesitancy. While its privacy tech attracts believers, the market awaits clarity: Will shielded transaction growth (now 20-25% of supply) offset Bitcoin’s gravitational pull on prices?\n\n## What are people saying about ZEC?\n\n## TLDR\n\nZcash's community oscillates between breakout euphoria and correction jitters, with privacy tech hype clashing with technical caution. Here’s what’s trending:\n1. Traders debate if ZEC’s consolidation is a bull trap or springboard\n2. Institutions bet big while retail eyes $550 prediction markets\n3. Technical charts flash conflicting signals across timeframes\n\n## Deep Dive\n\n### 1. @earlyadopterz: “Inverse Bitcoin hedge” thesis gains traction 🚀\n\n“When Bitcoin gets flushed down, Zcash will blast off... ZEC is the hedge”– @earlyadopterz (7.1K followers · 14M impressions · 2026-01-02 16:13 UTC)View original postWhat this means: Bullish for ZEC as some view it as a counter-cyclical play against Bitcoin volatility. The narrative gained traction after ZEC rose 2.8% while BTC dipped 0.4% on January 2.\n\n### 2. @VipRoseTr: Rising wedge warns of 42% drop 📉\n\n“ZEC forming bearish pattern – breakdown below support targets $289”– @VipRoseTr (63.4K followers · 8.2M impressions · 2025-12-27 13:53 UTC)View original postWhat this means: Bearish technical outlook as ZEC struggles at $519 resistance (current price $501). The pattern’s measured move aligns with the 38.2% Fibonacci retracement of its 295% 90-day rally.\n\n### 3. @MusicByVirtuals: Prediction market shows skepticism 🎯\n\n“85.8% bet ZEC stays below $550 through EOY 2025”– @MusicByVirtuals (6.1K followers · 3.1M impressions · 2025-11-28 14:56 UTC)View original postWhat this means: Neutral-bearish sentiment despite ZEC’s 47.9% 30-day gain. The crowd doubts sustainability of recent momentum, though the poll closed before January’s Grayscale Trust accumulation news.\n\n## Conclusion\n\nThe consensus on Zcash is mixed – bullish on privacy adoption narratives but wary of stretched valuations. While institutions like Grayscale’s $190M Zcash Trust signal long-term conviction, derivatives data shows $54M in vulnerable short positions that could fuel volatility. Watch the $404 support level: A hold above maintains the ascending triangle pattern targeting $630, while a breakdown might confirm the bearish wedge toward $300. With 29% of ZEC’s supply now in shielded pools, regulatory clarity remains the ultimate make-or-break factor.\n\n## What is the latest update in ZEC’s codebase?\n\n## TLDR\n\nZcash's codebase advances privacy and node infrastructure.\n1. NU6.1 Activation (Oct 2025) – Enabled shielded transaction upgrades and fee optimizations.\n2. Zcashd Deprecation (Apr 2025) – Migration to Zebra nodes and Zallet wallet underway.\n3. Zashi 2.0.3 (Apr 2025) – Streamlined shielded addresses and cross-chain swaps.\n\n## Deep Dive\n\n### 1. NU6.1 Activation (Oct 2025)\n\nOverview: Implemented ZIPs 317 and 320, refining fee structures and transparent address formats.This upgrade introduced a new transaction version (v5) as the default, reducing fees for shielded transfers by ~30% through optimized proof bundling. It also added stricter mempool rules to prevent spam transactions.\n\nWhat this means: This is bullish for ZEC because lower fees and improved spam resistance make private transactions more accessible and scalable. (Source)\n\n### 2. Zcashd Deprecation (Apr 2025)\n\nOverview: Phasing out the legacy C++ client (zcashd) in favor of Rust-based Zebra nodes and Zallet wallet.Key RPC methods like z_getbalance were deprecated, with users urged to migrate before August 2025. Zebra offers faster sync times and modular architecture.\n\nWhat this means: This is neutral for ZEC – while modernization improves long-term maintainability, migration complexities could temporarily strain ecosystem tools. (Source)\n\n### 3. Zashi 2.0.3 (Apr 2025)\n\nOverview: Wallet update defaulting to shielded addresses and integrating Maya DEX for cross-chain swaps.The redesign simplified sending private transactions and added auto-shielding of transparent balances. Over 15% more ZEC moved to shielded pools post-update.\n\nWhat this means: This is bullish for ZEC because frictionless privacy strengthens its core value proposition amid regulatory scrutiny. (Source)\n\n## Conclusion\n\nZcash’s updates prioritize privacy usability and infrastructure resilience, aligning with its role as a compliance-friendly anonymity tool. With shielded adoption rising and node modernization complete, how will ZEC balance regulatory pressures against its technological edge in 2026?\n\n## What is next on ZEC’s roadmap?\n\n## TLDR\n\nZcash's development roadmap focuses on privacy enhancements, ecosystem expansion, and governance upgrades through early 2026.\n1. Zashi Wallet 2.0 (Q1 2026) – Shielded swaps and cross-chain DeFi integration.\n2. Ztarknet Devnet Launch (Q1 2026) – Privacy-preserving smart contracts.\n3. Governance Model Overhaul (2026) – Streamlined development funding.\n\n## Deep Dive\n\n### 1. Zashi Wallet 2.0 (Q1 2026)\n\nOverview:The Zashi wallet will enable fully shielded swaps via NEAR Protocol’s Intents, allowing users to privately convert assets like BTC or ETH into shielded ZEC without intermediaries. This follows the November 2025 integration that simplified shielded-to-transparent transactions.\n\nWhat this means:Bullish for ZEC adoption, as frictionless privacy could attract users seeking compliance-friendly anonymity. Risks include potential delays in cross-chain refund privacy features.\n\n### 2. Ztarknet Devnet Launch (Q1 2026)\n\nOverview:Ztarknet, a Starknet-inspired Layer-2 rollup, will bring programmable smart contracts to Zcash using Circle-STARK proofs. This allows private computation off-chain while settling on Zcash’s base layer, maintaining shielded pool integrity (Eli5defi, Nov 2025).\n\nWhat this means:Neutral-to-bullish – while this expands Zcash’s utility beyond simple payments, adoption depends on developer uptake. Success could position ZEC as a privacy-centric smart contract platform.\n\n### 3. Governance Model Overhaul (2026)\n\nOverview:Community proposals aim to replace Zcash’s expiring development fund with a new model emphasizing transparency and faster execution. This follows June 2025 debates about sustaining ecosystem growth.\n\nWhat this means:Bullish if governance reforms reduce bureaucratic delays, but bearish risks emerge if funding disputes fragment the community.\n\n## Conclusion\n\nZcash’s 2026 trajectory hinges on balancing technical innovation (Ztarknet, Zashi) with governance maturity. While privacy upgrades could drive mainstream adoption, regulatory scrutiny remains a wildcard. How will Zcash’s optional privacy model fare as global AML rules tighten?\nCMC AI can make mistakes. Not financial advice. Read more about ZEC [What is Zcash (ZEC)?](https://coinmarketcap.com/cmc-ai/zcash/what-is/) [Latest Zcash (ZEC) Price Analysis](https://coinmarketcap.com/cmc-ai/zcash/price-analysis/) [Zcash (ZEC) Price Prediction](https://coinmarketcap.com/cmc-ai/zcash/price-prediction/) \n## Explore Similar Coins\n\n![ZEC](https://s2.coinmarketcap.com/static/img/coins/64x64/1437.png)\nZcash ZEC | $494.67 \n1.51% (1d)\n[See ZEC Price Chart](https://coinmarketcap.com/currencies/zcash/#cmcaiquestion=0) Read more about ZEC [What is Zcash (ZEC)?](https://coinmarketcap.com/cmc-ai/zcash/what-is/) [Latest Zcash (ZEC) Price Analysis](https://coinmarketcap.com/cmc-ai/zcash/price-analysis/) [Zcash (ZEC) Price Prediction](https://coinmarketcap.com/cmc-ai/zcash/price-prediction/) Cryptos: [29.55M](https://coinmarketcap.com/charts/number-of-cryptocurrencies-tracked/) Exchanges: [913](https://coinmarketcap.com/rankings/exchanges/) Market Cap: [$3.18T](https://coinmarketcap.com/charts/) 0.79% 24h Vol: [$138.65B](https://coinmarketcap.com/charts/) 11.53% Dominance: [BTC: 58.2% ETH: 12.3%](https://coinmarketcap.com/charts/bitcoin-dominance/) ** ETH Gas : 0.04 Gwei Fear & Greed: [49/100](https://coinmarketcap.com/charts/fear-and-greed-index/) [API](https://coinmarketcap.com/api/pricing/)\n</searchResult>\n\n\n<searchResult>\n[doc9]:\n**Zcash and the Altcoin Season Indicator: A Technical and Sentiment ...**\n![logo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAfQAAAA2CAYAAAAxgWuBAAAAAXNSR0IArs4c6QAAAmFJREFUeF7t1YEJACAMA0G7/9AV3MLnnMBcCpnd3eMRIECAAAECXwuMQf+6P58nQIAAAQJPwKA7BAIECBAgEBAw6IESRSBAgAABAgbdDRAgQIAAgYCAQQ+UKAIBAgQIEDDoboAAAQIECAQEDHqgRBEIECBAgIBBdwMECBAgQCAgYNADJYpAgAABAgQMuhsgQIAAAQIBAYMeKFEEAgQIECBg0N0AAQIECBAICBj0QIkiECBAgAABg+4GCBAgQIBAQMCgB0oUgQABAgQIGHQ3QIAAAQIEAgIGPVCiCAQIECBAwKC7AQIECBAgEBAw6IESRSBAgAABAgbdDRAgQIAAgYCAQQ+UKAIBAgQIEDDoboAAAQIECAQEDHqgRBEIECBAgIBBdwMECBAgQCAgYNADJYpAgAABAgQMuhsgQIAAAQIBAYMeKFEEAgQIECBg0N0AAQIECBAICBj0QIkiECBAgAABg+4GCBAgQIBAQMCgB0oUgQABAgQIGHQ3QIAAAQIEAgIGPVCiCAQIECBAwKC7AQIECBAgEBAw6IESRSBAgAABAgbdDRAgQIAAgYCAQQ+UKAIBAgQIEDDoboAAAQIECAQEDHqgRBEIECBAgIBBdwMECBAgQCAgYNADJYpAgAABAgQMuhsgQIAAAQIBAYMeKFEEAgQIECBg0N0AAQIECBAICBj0QIkiECBAgAABg+4GCBAgQIBAQMCgB0oUgQABAgQIGHQ3QIAAAQIEAgIGPVCiCAQIECBAwKC7AQIECBAgEBAw6IESRSBAgAABAgbdDRAgQIAAgYCAQQ+UKAIBAgQIELiTLNdf/jBPsAAAAABJRU5ErkJggg==)\nSymbols Symbols [Aime](https://www.ainvest.com/aime/) [Products](https://www.ainvest.com/screener/) [News](https://www.ainvest.com/news/) [Markets](https://www.ainvest.com/market/) [Watchlist](https://www.ainvest.com/watchlist/) [Brokers](https://www.ainvest.com/brokers/) \n# Zcash and the Altcoin Season Indicator: A Technical and Sentiment-Driven Analysis\nGenerated by AI Agent [12X Valeria](https://www.ainvest.com/news/author/12x-valeria) Tuesday, Oct 7, 2025 7:07 pm ET 2min read \n![Speaker 1](https://cdn.ainvest.com/articles/focusnews/coverimage/content/pictures/alexander_9990f0971755765042310.png)\n\n![Speaker 2](https://cdn.ainvest.com/articles/focusnews/coverimage/content/pictures/en_Amelia_e5b296241755764828756.png)\nAI Podcast: Your News, Now Playing [ZEC--](https://chart.ainvest.com/ZECUSDT/?exchange=BINANCE) [BTC--](https://chart.ainvest.com/BTCUSDT/?exchange=BINANCE) [XMR--](https://chart.ainvest.com/XMRUSDT/?exchange=BINANCE) [XRP--](https://chart.ainvest.com/XRPUSDT/?exchange=BINANCE) [ETH--](https://chart.ainvest.com/ETHUSDT/?exchange=BINANCE) \n![Aime Robot](https://cdn.ainvest.com/frontResources/s/ainvest-nova/news/_next/static/media/aimeRobot.ddb9bcda.png)\nAime Summary \n- Zcash (ZEC) shows mixed technical signals in late 2025, with bearish short-term pressure near $40.98 but bullish long-term momentum via rising 200-day moving averages.\n\n- Market sentiment remains cautious (Fear & Greed Index at 37) amid privacy concerns, yet institutional upgrades like Zashi App's CrossPay boost utility and investor confidence.\n\n- Historical patterns suggest ZEC acts as an altcoin season barometer, with 2025's 43% monthly gain mirroring 2017/2021 rallies and signaling capital shifts from Bitcoin to privacy coins.\n\n- Analysts project $62.21 target by September 29, 2025, but warn of risks including regulatory scrutiny, macro volatility, and retesting key support levels ($49.07–$42.98).\n\nZcash (ZEC) has long been a focal point for investors seeking exposure to privacy-centric narratives in the cryptocurrency market. As of September 2025, its price dynamics and market sentiment offer a compelling case study for understanding altcoin season dynamics. This analysis examines ZEC's technical indicators, historical performance, and sentiment shifts to assess its role as a potential barometer for broader altcoin cycles.\n\n### Technical Patterns: Mixed Signals Amid Volatility\n\nZcash's technical indicators present a nuanced picture. In late September 2025,\n[ZEC](https://chart.ainvest.com/ZECUSDT/?exchange=BINANCE) faced bearish pressure near the 38.2% Fibonacci retracement level ($40.98) and the 30-day simple moving average ($39.01), suggesting short-term weakness, according to a [CoinMarketCap analysis](https://coinmarketcap.com/cmc-ai/zcash/price-analysis/) . However, the RSI at 61.77 indicated a neutral stance, while the 50-day moving average showed upward momentum, and the 200-day moving average had risen since late August, signaling long-term strength, according to a [Coincodex prediction](https://coincodex.com/article/73695/zcash-prediction-september-24-2025/) . Analysts project an 8.5% price increase to $62.21 by September 29, 2025, though retesting support levels ($49.07–$42.98) remains a risk, according to Coincodex. \nThe 200-day moving average's upward trajectory since August 31, 2025, aligns with broader bullish trends in privacy-focused assets, as noted by Coincodex. Meanwhile, ZEC's 30-day volatility (9.30) and 17 green days in the last 30 suggest resilience amid macro-level corrections. For instance, Bitcoin's 7.2% drop from $124,480 to $115,000 in late August 2025 dragged ZEC down due to its high 30-day correlation with\n[BTC](https://chart.ainvest.com/BTCUSDT/?exchange=BINANCE) (0.87), as the CoinMarketCap analysis noted. This interdependence underscores ZEC's sensitivity to Bitcoin's dominance, a common trait during altcoin seasons. \n### Market Sentiment: Fear and Institutional Curiosity\n\nMarket sentiment for ZEC remains mixed. The Fear & Greed Index scored 37 (Fear) in late September 2025, reflecting widespread caution, as Coincodex reported. This aligns with broader crypto fear, as the index dipped to 39, reducing risk appetite, per CoinMarketCap data. However, institutional interest and network upgrades, such as the Zashi App's CrossPay enabling shielded transactions across 20+ blockchains, have injected bullish sentiment, according to a\n[Coin Republic report](https://www.thecoinrepublic.com/2025/10/07/zcash-prices-200-rally-issues-bear-flag-for-bitcoin-signals-altcoin-season/) . \nPrivacy concerns, particularly Qubic's mining attacks on Monero, have indirectly pressured ZEC, triggering panic selling and a 162% surge in 24-hour trading volume to $72.9M, as CoinMarketCap showed. Yet, ZEC's 11.72% 24-hour rally on September 24, 2025, to $58.34-following a 43.26% monthly gain-suggests growing retail and institutional confidence, Coincodex noted. Analysts draw parallels between ZEC's chart and XRP's cup-and-handle formation, projecting long-term targets of $350–$450, according to the Coin Republic piece.\n\n### Historical Performance: A Proven Altcoin Season Player\n\nZEC's historical performance during past altcoin seasons reinforces its role as a leading indicator. In 2017, ZEC surged 88.47% in March and reached an all-time high of $743.96, peaking in October before declining, according to CoinMarketCap. Similarly, in 2021, ZEC hit $367.43 before a 34% pullback in May, recovering amid a broader bull market, CoinMarketCap data shows. These patterns mirror the 2025 rally, where ZEC's 200% surge in October 2025 coincided with the TOTAL3 chart (excluding\n[Bitcoin](https://chart.ainvest.com/BTCUSDT/?exchange=BINANCE) and Ethereum) hitting $1.18 trillion, per the Coin Republic report. \nDuring these cycles, ZEC's price movements often signaled Bitcoin's waning dominance and the onset of altcoin seasons. For example, ZEC's 200% rally in October 2025 was interpreted as a bear flag for Bitcoin, indicating a shift in capital from BTC to privacy-focused assets, as the Coin Republic piece observed. This historical correlation suggests ZEC's price action can serve as a contrarian indicator for Bitcoin's lifecycle.\n\n### Zcash as an Altcoin Season Indicator: Strengths and Risks\n\nZEC's dual role as a privacy coin and a technical performer positions it as a potential altcoin season indicator. Its recent 43.26% monthly gain and 99.67% annual increase reflect strong retail and institutional demand, Coincodex noted. However, risks persist: privacy concerns, regulatory scrutiny, and macroeconomic volatility could undermine its momentum.\n\nThe Fear & Greed Index's 37 (Fear) score suggests ZEC may be undervalued, but traders must monitor key resistance levels ($55.15–$61.24) and support levels ($49.07–$42.98), per Coincodex. Institutional upgrades like CrossPay and growing shielded transaction counts on the\n[Zcash](https://chart.ainvest.com/ZECUSDT/?exchange=BINANCE) network could mitigate these risks by reinforcing ZEC's utility, as the CoinMarketCap analysis suggested. \n### Conclusion: A Cautious Bull Case\n\nZcash's technical and sentiment dynamics in 2025 mirror historical altcoin season patterns, suggesting it could act as a leading indicator for broader market rotations. While short-term bearish pressure exists, long-term fundamentals-including institutional adoption and network upgrades-support a bullish case. Investors should balance ZEC's potential with caution, using technical levels and sentiment metrics to time entries and exits.\n\n![author avatar](https://cdn.ainvest.com/social/account/portraits/12x.png)\n12X Valeria\n\nAI Writing Agent which integrates advanced technical indicators with cycle-based market models. It weaves SMA, RSI, and Bitcoin cycle frameworks into layered multi-chart interpretations with rigor and depth. Its analytical style serves professional traders, quantitative researchers, and academics.\n\n### Latest Articles\n[Bitcoin's Institutional-Driven Rally: Is a 100%+ Surge Imminent?Jan.06 2026](https://www.ainvest.com/news/bitcoin-institutional-driven-rally-100-surge-imminent-2601/) [Bitcoin's 2026 Rally: Is This the Real Start of a Sustainable Bull Cycle?Jan.06 2026](https://www.ainvest.com/news/bitcoin-2026-rally-real-start-sustainable-bull-cycle-2601/) [Ethereum's Breakout Above $3,200 and the Path to $4,000: Technical Momentum and Leverage-Driven Risk Dynamics in Early 2026Jan.06 2026](https://www.ainvest.com/news/ethereum-breakout-3-200-path-4-000-technical-momentum-leverage-driven-risk-dynamics-early-2026-2601/) [Morgan Stanley's Entry into the Bitcoin ETF Market and Its Implications for Institutional AdoptionJan.06 2026](https://www.ainvest.com/news/morgan-stanley-entry-bitcoin-etf-market-implications-institutional-adoption-2601/) [Ethereum Staking Dynamics Signal Reduced Selling Pressure and Renewed Institutional Confidence in ETHJan.06 2026](https://www.ainvest.com/news/ethereum-staking-dynamics-signal-reduced-selling-pressure-renewed-institutional-confidence-eth-2601/) \n## AInvest Newsletter\n\nDaily stocks & crypto headlines, free to your inbox\n\n### Or continue with others\n[Crypto Signal Trade Smarter: Get Crypto Signals for BTC and Gain an Edge.](https://www.ainvest.com/pricing/benefits/magic-prophet/?source=news_symbol_signalcard) \n### Comments\n\n﻿\nAdd a public comment...\n\n![No comments](https://cdn.ainvest.com/frontResources/s/ainvest-nova/news/_next/static/media/placeholder-no-comment.ed02f197.png)\n\nNo comments yet\nAinvest News articles are AI-generated using advanced large language model (LLM) technology designed to analyze and synthesize publicly available data and news. While AI tools assist in producing initial drafts and insights, all AI generated content published on Ainvest is subject to comprehensive human editorial review before publication. A designated human editor reviews, verifies, and approves each article for factual accuracy, coherence, and compliance with AInvest Fintech Inc's editorial and disclosure standards. Despite these review procedures, the information provided may still contain inaccuracies, incomplete data, or time sensitive references due to the inherent limitations of AI generated analysis and evolving changes. The material is provided strictly for informational and educational purposes and does not constitute personalized investment, legal, or financial advice. Readers should independently verify all facts, figures, and statements before making any decision based on this content. AInvest Fintech Inc. its affiliates, and partners accept no liability or responsibility for any direct or consequential losses arising from reliance on this content. All articles and analyses are subject to revision, update, or removal without prior notice to maintain accuracy and integrity in our publications.\n\n![logo](https://cdn.ainvest.com/kamisAssets/icon_menu_logo_dark.wp20iq3a1ms.png)\n[](https://www.producthunt.com/products/aime?amp%3butm_medium=badge&amp%3butm_souce=badge-aime) PRODUCTS\n[Aime](https://www.ainvest.com/chat/?comefrom=WebainvestFooter) [Newswire](https://www.ainvest.com/news/wire/) [Screener](https://www.ainvest.com/screener/) [Super Charts](https://www.ainvest.com/chart?symbol=NASDAQ-AAPL) [Magic Portfolio](https://www.ainvest.com/pricing/magic-portfolio/) ABOUT US\n[Our Story](https://www.ainvest.com/about/) [News Authors](https://www.ainvest.com/news/author/) [Privacy Policy](https://cdn.ainvest.com/agreement/Ainvest-Fintech-Inc-Privacy-Policy.pdf) [Term of Use](https://cdn.ainvest.com/agreement/Ainvest-Fintech-Terms-of-Use.pdf) [Third Party Brokerage Disclaimer](https://cdn.ainvest.com/agreement/Third-Party-Brokerage-Disclaimer.pdf) [AIME Terms of Use](https://cdn.ainvest.com/agreement/AIME-Terms-of-Use.pdf) [AInvest AI Risk Disclosures](https://cdn.ainvest.com/agreement/Ainvest-AI-Risk-Disclosures.pdf) [Careers](https://career.ainvest.com/) [CONTACT US](https://contact.ainvest.com/) [](https://discord.gg/44AMr7JMtD) [](https://www.linkedin.com/showcase/ainvest-fintech-inc/) [](https://www.youtube.com/@ainvestofficial) [](https://www.instagram.com/ainvest_fintech/) [](https://twitter.com/AInvestOfficial) [](https://www.tiktok.com/@ainvestofficial) Recommended\n\n![aime](https://cdn.ainvest.com/kamisAssets/image.g1ihevi0tt.png)\n</searchResult>\n\n\n"
  },
  {
    "ToolCallId": "call_4vcRFJ5oE9TUyGxguD8x6dYq",
    "Output": "<searchResult>\n[doc5]:\n**Zcash(ZEC) Price Today, ZEC to USD Real-Time, Latest Discussions ...**\n[](https://stocktwits.com/) - Trending\n- News\n- Earnings\n[DIA1.11%](https://stocktwits.com/symbol/DIA) [SPY0.68%](https://stocktwits.com/symbol/SPY) [QQQ1.03%](https://stocktwits.com/symbol/QQQ) Trending [CRML53.59%](https://stocktwits.com/symbol/CRML) [MSTR9.11%](https://stocktwits.com/symbol/MSTR) [RUM5.73%](https://stocktwits.com/symbol/RUM) [VKTX0.50%](https://stocktwits.com/symbol/VKTX) [SNDK32.24%](https://stocktwits.com/symbol/SNDK) [APLD1.72%](https://stocktwits.com/symbol/APLD) [JASMY22.79%](https://stocktwits.com/coins/jasmycoin) [MNTS16.95%](https://stocktwits.com/symbol/MNTS) [IMSR43.28%](https://stocktwits.com/symbol/IMSR) [SOFI8.15%](https://stocktwits.com/symbol/SOFI) [CRML53.59%](https://stocktwits.com/symbol/CRML) [MSTR9.11%](https://stocktwits.com/symbol/MSTR) [RUM5.73%](https://stocktwits.com/symbol/RUM) [VKTX0.50%](https://stocktwits.com/symbol/VKTX) [SNDK32.24%](https://stocktwits.com/symbol/SNDK) [APLD1.72%](https://stocktwits.com/symbol/APLD) [JASMY22.79%](https://stocktwits.com/coins/jasmycoin) [MNTS16.95%](https://stocktwits.com/symbol/MNTS) [IMSR43.28%](https://stocktwits.com/symbol/IMSR) [SOFI8.15%](https://stocktwits.com/symbol/SOFI) [](https://stocktwits.com/sentiment/trending) [home](https://stocktwits.com/) [Coins](https://stocktwits.com/coins) ZEC \n![ZEC logo](https://logos.stocktwits-cdn.com/ZEC-X.png)\n\n# ZECZcash\n9,992 Mkt Cap $8.22B 24H Volume $781.82M FDV $8.22B Circ Supply 16.48M Total Supply 16.48M ZEC Fundamentals Max Supply 21M 7D High $533.33 7D Low $484.40 24H High $525.08 24H Low $494.04 All-Time High $3,191.93 All-Time Low $16.08 Total Supply 16.48M ZEC Prices ZEC / USD $499.47 ZEC / EUR €426.88 ZEC / GBP £369.66 ZEC / CAD CA$690.00 ZEC / AUD A$740.17 ZEC / INR ₹45,031.00 ZEC / NGN NGN 714,475.00 ZEC / NZD NZ$863.02 ZEC / PHP ₱29,611.00 ZEC / SGD SGD 639.69 ZEC / ZAR ZAR 8,171.94 Loading... Loading... - Chart\n- News\n- Sentiment\n- Info\n- Historical Prices\nNews all press releases Arthur Hayes Says Privacy Will Be Crypto's Next Dominant Trade Privacy Coin News BitMEX co-founder Arthur Hayes disclosed a substantial Zcash position held by his family office, Maelstrom, while arguing that privacy will define cryptocurrency's next major narrative. The disclosure came in a Tuesday blog post connecting privacy-focused assets...\nAyesha Aziz · 6h ago \n![News Placeholder](https://chunks-prd.stocktwits-cdn.com/_next/static/media/news-placeholder.eb4d81c7.svg)\nMore News\n\n![News Placeholder](https://chunks-prd.stocktwits-cdn.com/_next/static/media/news-placeholder.eb4d81c7.svg)\nHere’s what happened in crypto today Need to know what happened in crypto today? Here is the latest news on daily trends and events impacting Bitcoin price, blockchain, DeFi, NFTs, Web3 and crypto regulation.\ncointelegraph · 7h ago \n![News Placeholder](https://chunks-prd.stocktwits-cdn.com/_next/static/media/news-placeholder.eb4d81c7.svg)\nMarket Focus Shifts From Polkadot and Zcash as BlockDAG’s Presale Nears January 26 Deadline With 3.5B Coins Left Learn why BlockDAG’s $441M presale is nearing its January 26 close, with 312K holders, shaping views on the next crypto to explode as Polkadot crypto and Zcash price struggle. Read original article on coincu.com\nCoincu · 1d ago \n![News Placeholder](https://chunks-prd.stocktwits-cdn.com/_next/static/media/news-placeholder.eb4d81c7.svg)\nHow Zcash (ZEC) Turned Privacy From a Risk Into a Premium For years, privacy coins were treated like a problem the market wanted to avoid. Exchanges delisted them, regulators frowned on them, and investors learned to keep their distance. That is why Grayscale’s move to file for a Zcash ETF caught so much attention. It landed at a moment...\nCaptain Altcoin · 1d ago \n![News Placeholder](https://chunks-prd.stocktwits-cdn.com/_next/static/media/news-placeholder.eb4d81c7.svg)\nGrayscale Zcash Trust Offers U.S. Investors Regulated Exposure to $ZEC Amid OTC Discount Quick Breakdown Grayscale Zcash Trust gives U.S. investors regulated access to ZEC through brokerage accounts Shares trade at $29.41, below the NAV of $39.50 Fund manages $190.7M with all assets held by third-party custodians Grayscale Investments’ Zcash Trust (Ticker: $ZCSH) pro...\nDeFi Planet · 2d ago \n![News Placeholder](https://chunks-prd.stocktwits-cdn.com/_next/static/media/news-placeholder.eb4d81c7.svg)\nWhy Is Virtuals Protocol (VIRTUAL) Price Pumping Today? Virtuals Protocol is the strongest mover in the market today. The VIRTUAL price is up more than 18% over the past day, trading around $1.03 at writing. Trading volume has also jumped by over 31%, placing the token at the top of the daily gainers list. This move did not come out o...\nCaptain Altcoin · 2d ago \n![News Placeholder](https://chunks-prd.stocktwits-cdn.com/_next/static/media/news-placeholder.eb4d81c7.svg)\nBig Altcoin Whale Falls Victim to Greed: Made $3.2 Million in Profits, But A large whale in the cryptocurrency market made a serious mistake after making a huge profit on an altcoin. Continue Reading: Big Altcoin Whale Falls Victim to Greed: Made $3.2 Million in Profits, But\nBitcoin Sistemi · 2d ago \n![News Placeholder](https://chunks-prd.stocktwits-cdn.com/_next/static/media/news-placeholder.eb4d81c7.svg)\nPrivacy coins explained: Why secrecy may shape crypto’s next era As crypto heads toward 2026, the debate over transparency versus privacy is intensifying.\ncrypto.news · 4d ago \n![News Placeholder](https://chunks-prd.stocktwits-cdn.com/_next/static/media/news-placeholder.eb4d81c7.svg)\nHere’s Where Zcash (ZEC) Price Could Go Next in January 2026 Zcash is starting 2026 in a pretty interesting spot. The price isn’t surging higher anymore, but it also isn’t giving back much of its recent gains. After a strong run into late December, ZEC has shifted into a pause mode, holding near its highs while the market digests what just...\nCaptain Altcoin · 5d ago \n![News Placeholder](https://chunks-prd.stocktwits-cdn.com/_next/static/media/news-placeholder.eb4d81c7.svg)\nBithumb Finds $202M In Dormant Crypto Assets Across 2.6 Million Inactive User Accounts Bithumb identified $202M in dormant crypto across 2.6M inactive accounts, with some holdings untouched for 12 years.\nYellow News · 5d ago <\n1\n2\n...\n>\n\nSentiment\nIndicates whether most users posting on a symbol’s stream over the last 24 hours are fearful or greedy.\n0\n25\n50\n75\n100\nExtreme\nFear\nNeutral\nGreed\nExtreme\nFear\nGreed\nN/A\nLast score\n\nN/A\n1 day ago\n\nSign Up / Log In\n1 week ago\n\nSign Up / Log In\n1 month ago\n\nSign Up / Log In\n3 months ago\n\nSign Up / Log In\n6 months ago\n\nSign Up / Log In\n1 year ago\n\nSign Up / Log In\n\nMessage Volume\nMeasures the total amount of chatter on a stream over the last 24 hours.\n0\n25\n50\n75\n100\nExtremely\nLow\nNormal\nHigh\nExtremely\nLow\nHigh\nN/A\nLast score\n\nN/A\n1 day ago\n\nSign Up / Log In\n1 week ago\n\nSign Up / Log In\n1 month ago\n\nSign Up / Log In\n3 months ago\n\nSign Up / Log In\n6 months ago\n\nSign Up / Log In\n1 year ago\n\nSign Up / Log In\n\nParticipation Ratio\nMeasures the number of unique accounts posting on a stream relative to the number of total messages on that stream.\n0\n25\n50\n75\n100\nExtremely\nLow\nNormal\nHigh\nExtremely\nLow\nHigh\nN/A\nLast score\n\nN/A\n1 day ago\n\nSign Up / Log In\n1 week ago\n\nSign Up / Log In\n1 month ago\n\nSign Up / Log In\n3 months ago\n\nSign Up / Log In\n6 months ago\n\nSign Up / Log In\n1 year ago\n\nSign Up / Log In\nAbout Zcash is a privacy-focused cryptocurrency that uses trustless zero-knowledge proofs to enable fully encrypted transactions while maintaining blockchain transparency and security. It was the first cryptocurrency to implement zero-knowledge encryption for private peer-to-peer payments, addressing the fundamental privacy gap in traditional cryptocurrencies that expose transaction details publicly. With a fixed supply of 21 million ZEC and a halving schedule similar to Bitcoin, Zcash allows users to prove transactions are valid without revealing sensitive information like wallet balances, transaction amounts, or participant identities, making it suitable for everyday payments, long-term savings, and cross-border money transfers where financial confidentiality matters. The protocol operates on its own blockchain currently using Proof-of-Work consensus, though it's evolving toward Proof-of-Stake through the planned \"Crosslink\" upgrade to enhance security, scalability, and energy efficiency. Zcash employs trustless zero-knowledge proofs (Halo) within its Orchard shielded pool to verify transactions without revealing sender, receiver, or amount information. Users can choose between transparent public transactions and shielded private transactions through Unified Addresses, which work with both types. The network is faster and cheaper than Bitcoin, with new blocks mined every 75 seconds and transaction fees typically just a fraction of a cent. Privacy adoption has surged in 2025, with over 30% of total ZEC supply now held in fully shielded pools. Zcash was created by a group of scientists in 2013 who initially proposed Zerocoin as a privacy extension to Bitcoin before building a standalone protocol. The ecosystem operates with a self-funded development model where block rewards support independent teams through the Zcash Community Grants Committee and a new Coinholder-Controlled Fund. Details Links Website Source [GitHub](https://github.com/zcash/zcash) Categories Coinbase 50 Index Layer 1 (L1) Made in USA Near Protocol Ecosystem Pantera Capital Portfolio Privacy Coins Proof of Work (PoW) Quantum-Resistant Smart Contract Platform Zero Knowledge (ZK) Date\nMarket Cap\nVolume\nClose\nJanuary 07, 2026\n$8.22B\n$781.82M\n---\nJanuary 07, 2026\n$8.28B\n$660.9M\n---\nJanuary 06, 2026\n$8.31B\n$598.39M\n$503.62\nJanuary 05, 2026\n$8.27B\n$389.89M\n$502.46\nJanuary 04, 2026\n$8.43B\n$494.48M\n$511.43\nJanuary 03, 2026\n$8.05B\n$566.7M\n$488.46\nJanuary 02, 2026\n$8.63B\n$456.97M\n$523.93\nJanuary 01, 2026\n$8.43B\n$824.39M\n$512.50\nDecember 31, 2025\n$8.69B\n$605.95M\n$527.84\nDecember 30, 2025\n$8.91B\n$969.61M\n$540.91\n\n### Poll\nWhat Role Will Crypto Play in 2026 Markets?\nMacro Hedge Against Dollar & Geopolitical Risk\nSpeculative Trade\nRange-Bound After the Big Run\nOther – Comment Below\n\n1.8k votes\n· \n6d left\n\n## Latest ZEC News\n\nAdvertisement|Remove ads.\n\nAdvertisement|Remove ads.\n[Trending](https://stocktwits.com/sentiment) [News](https://stocktwits.com/news-articles) [Community](https://stocktwits.com/) Profile\n</searchResult>\n\n\n<searchResult>\n[doc6]:\n**Will Zcash (ZEC) Price Finally Retest $500 After Nearly 8 Years?**\n# guce\n[guce](https://consent.yahoo.com/v2/&#x2F;&#x2F;uk.yahoo.com&#x2F;) \nYahoo is part of the Yahoo family of brandsThe sites and apps that we own and operate, including Yahoo and Engadget, and our digital advertising service, Yahoo Advertising.Yahoo family of brands.\nWhen you use our sites and apps, we use Cookies Cookies (including similar technologies such as web storage) allow the operators of websites and apps to store and read information from your device. Learn more in our [cookie policy](https://consent.yahoo.com/redirect?to=https%3A%2F%2Flegal.yahoo.com%2Fie%2Fen%2Fyahoo%2Fprivacy%2Fcookies%2Findex.html&brandDomain=&brandId=yahoo&tos=eu&step=&sessionId=3_cc-session_7c26e674-c44f-4b27-9e88-e7a48467eb6f&userType=NON_REG) . cookies to: - provide our sites and apps to you\n- authenticate users, apply security measures, and prevent spam and abuse, and\n- MeasurementWe count the number of visitors to our pages, the type of device they use (iOS or Android), the browser they use, and the duration of their visit to our websites and apps. This data is collected in aggregate and is not tied to specific users.measure your use of our sites and apps\nIf you click ' **Accept all** ', we and [our partners](https://consent.yahoo.com/v2/partners-list?sessionId=3_cc-session_7c26e674-c44f-4b27-9e88-e7a48467eb6f) , including 245 who are part of the IAB Transparency & Consent Framework, will also store and/or access information on a device (in other words, use cookies) and use precise geolocation data and other personal data such as IP address and browsing and search data, for analytics, personalized advertising and content, advertising and content measurement, and audience research and services development. \nIf you do not want us and our partners to use cookies and personal data for these additional purposes, click 'Reject all'.\n\nIf you would like to customise your choices, click 'Manage privacy settings'.\n\nYou can withdraw your consent or change your choices at any time by clicking on the 'Privacy & Cookie Settings' or 'Privacy Dashboard' links on our sites and apps. Find out more about how we use your personal data in our Privacy Policy and Cookie Policy.\n[Manage privacy settings](https://consent.yahoo.com/v2/partners?sessionId=3_cc-session_7c26e674-c44f-4b27-9e88-e7a48467eb6f)\n</searchResult>\n\n\n<searchResult>\n[doc4]:\n**Latest Zcash News - (ZEC) Future Outlook, Trends & Market Insights**\n[](https://coinmarketcap.com/) [Cryptocurrencies](https://coinmarketcap.com/) Cryptocurrencies\n[Ranking](https://coinmarketcap.com/) [Categories](https://coinmarketcap.com/cryptocurrency-category/) [Historical Snapshots](https://coinmarketcap.com/historical/) [Token unlocks](https://coinmarketcap.com/token-unlocks/) [Yield](https://coinmarketcap.com/yield/) [Real-World Assets](https://coinmarketcap.com/real-world-assets/) Leaderboards\n[Trending](https://coinmarketcap.com/trending-cryptocurrencies/) [Upcoming](https://coinmarketcap.com/upcoming/) [Recently Added](https://coinmarketcap.com/new/) [Gainers & Losers](https://coinmarketcap.com/gainers-losers/) [Most Visited](https://coinmarketcap.com/most-viewed-pages/) [Community Sentiment](https://coinmarketcap.com/sentiment/) [Chain Ranking](https://coinmarketcap.com/chain-ranking/) NFT\n[Overall NFT Stats](https://coinmarketcap.com/nft/) [Upcoming Sales](https://coinmarketcap.com/nft/upcoming/) [Dashboards](https://coinmarketcap.com/charts/) Markets\n[Market Overview](https://coinmarketcap.com/charts/) [Spot Market](https://coinmarketcap.com/charts/spot-market/) [Derivatives Market](https://coinmarketcap.com/charts/derivatives-market/) [No. of Cryptocurrencies](https://coinmarketcap.com/charts/number-of-cryptocurrencies-tracked/) [BNB Treasuries](https://coinmarketcap.com/charts/bnb-treasuries/) Indicators\n[Fear and Greed Index](https://coinmarketcap.com/charts/fear-and-greed-index/) [Altcoin Season Index](https://coinmarketcap.com/charts/altcoin-season-index/) [Market Cycle Indicators](https://coinmarketcap.com/charts/crypto-market-cycle-indicators/) [Bitcoin Dominance](https://coinmarketcap.com/charts/bitcoin-dominance/) [CoinMarketCap 20 Index](https://coinmarketcap.com/charts/cmc20/) [CoinMarketCap 100 Index](https://coinmarketcap.com/charts/cmc100/) ETF Flows\n[Crypto ETFs](https://coinmarketcap.com/etf/) [Bitcoin ETFs](https://coinmarketcap.com/etf/bitcoin/) [Ethereum ETFs](https://coinmarketcap.com/etf/ethereum/) Technical Analysis\n[RSI](https://coinmarketcap.com/charts/rsi/) [MACD](https://coinmarketcap.com/charts/macd/) Derivatives\n[Funding Rates](https://coinmarketcap.com/charts/funding-rates/) [DexScan](https://dex.coinmarketcap.com/token/all/) [SignalsNew](https://dex.coinmarketcap.com/signals/all/) [Trending](https://dex.coinmarketcap.com/token/all/) [New](https://dex.coinmarketcap.com/token/all/?tableRankBy=new_24h) [Gainers](https://dex.coinmarketcap.com/token/all/?tableRankBy=gainers_24h) [Meme Explorer](https://dex.coinmarketcap.com/meme/four.meme/) [Top Traders](https://dex.coinmarketcap.com/top-traders/all/) [Exchanges](https://coinmarketcap.com/rankings/exchanges/) Centralized Exchanges\n[Spot](https://coinmarketcap.com/rankings/exchanges/) [Derivatives](https://coinmarketcap.com/rankings/exchanges/derivatives/) Decentralized Exchanges\n[Spot](https://coinmarketcap.com/rankings/exchanges/dex/?type=spot) [Derivatives](https://coinmarketcap.com/rankings/exchanges/dex/?type=derivatives) [Community](https://coinmarketcap.com/community/) [Feeds](https://coinmarketcap.com/community/) [Topics](https://coinmarketcap.com/community/topics/) [Lives](https://coinmarketcap.com/community/lives/) [Articles](https://coinmarketcap.com/community/articles/) [Sentiment](https://coinmarketcap.com/sentiment/) Products Products\n[Converter](https://coinmarketcap.com/converter/) [Newsletter](https://coinmarketcap.com/newsletter/) [CMC Launch](https://coinmarketcap.com/cmclaunch/) [CMC Labs](https://coinmarketcap.com/events/cmc-labs/) [Telegram Bot](https://coinmarketcap.com/chatbot/) [Advertise](https://coinmarketcap.com/events/advertise/) [Crypto API](https://coinmarketcap.com/api/) [Site Widgets](https://coinmarketcap.com/widget/ticker/) Campaigns\n[Airdrops](https://coinmarketcap.com/airdrop/) [Diamond Rewards](https://coinmarketcap.com/account/rewards/) [Learn & Earn](https://coinmarketcap.com/earn/) Calendars\n[ICO Calendar](https://coinmarketcap.com/ico-calendar/) [Events Calendar](https://coinmarketcap.com/events/) Learn\n[News](https://coinmarketcap.com/headlines/news/) [Academy](https://coinmarketcap.com/academy/) [Research](https://coinmarketcap.com/academy/categories/cmc-research/) [Videos](https://www.youtube.com/channel/UCnhdZlwVd6ocXGhdSyV9Axg/?sub_confirmation=1) [Glossary](https://coinmarketcap.com/academy/glossary/) \n# Latest Zcash (ZEC) News Update\nBy CMC AI 06 January 2026 12:16AM (UTC+0) [See ZEC Price Chart](https://coinmarketcap.com/currencies/zcash/#cmcaiquestion=0) \n## What is the latest news on ZEC?\n\n## TLDR\n\nZcash navigates bullish technicals and whale-sized bets as privacy narratives gain steam. Here are the latest news:\n1. Bull Flag Holds Despite Weakness (6 January 2026) – ZEC’s bullish structure remains intact, but weakening momentum signals caution.\n2. Whale Bets $39M on ZEC Long (5 January 2026) – A crypto whale opened a leveraged position equivalent to 1.2% of ZEC’s circulating supply.\n3. Grayscale Zcash Trust Discount Widens (5 January 2026) – Shares trade 25% below net asset value despite rising institutional interest.\n\n## Deep Dive\n\n### 1. Bull Flag Holds Despite Weakness (6 January 2026)\n\nOverview: ZEC maintains a bullish market structure with an 85% upside target ($930+) if it holds above $404 support. However, momentum indicators like the Chaikin Money Flow (CMF) near zero suggest weakening buying pressure.\n\nWhat this means: The technical setup is bullish long-term but faces headwinds from Bitcoin’s negative correlation with ZEC and $39M in short-term short leverage. A break below $404 could trigger a deeper correction. (TokenPost)\n\n### 2. Whale Bets $39M on ZEC Long (5 January 2026)\n\nOverview: Address 0x6b26 opened a 5x leveraged long position with 79,438 ZEC ($39.24M) on Binance, risking amplified volatility.\n\nWhat this means: Large leveraged positions increase liquidation risks—$54M in shorts vs. $24M longs sit near current prices. While this signals confidence, the whale already faces a $1.88M unrealized loss, raising concerns about forced selling. (Binance News)\n\n### 3. Grayscale Zcash Trust Discount Widens (5 January 2026)\n\nOverview: Grayscale’s Zcash Trust (ZCSH) shares trade at a 25% discount to NAV despite holding $190M in ZEC, reflecting skepticism about near-term liquidity improvements.\n\nWhat this means: The widening gap between institutional and spot prices highlights ZEC’s regulatory ambiguity but could create arbitrage opportunities if ETF conversion rumors materialize. (CoinMarketCap)\n\n## Conclusion\n\nZcash balances bullish technicals against whale-driven volatility and institutional hesitancy. While its privacy tech attracts believers, the market awaits clarity: Will shielded transaction growth (now 20-25% of supply) offset Bitcoin’s gravitational pull on prices?\n\n## What are people saying about ZEC?\n\n## TLDR\n\nZcash's community oscillates between breakout euphoria and correction jitters, with privacy tech hype clashing with technical caution. Here’s what’s trending:\n1. Traders debate if ZEC’s consolidation is a bull trap or springboard\n2. Institutions bet big while retail eyes $550 prediction markets\n3. Technical charts flash conflicting signals across timeframes\n\n## Deep Dive\n\n### 1. @earlyadopterz: “Inverse Bitcoin hedge” thesis gains traction 🚀\n\n“When Bitcoin gets flushed down, Zcash will blast off... ZEC is the hedge”– @earlyadopterz (7.1K followers · 14M impressions · 2026-01-02 16:13 UTC)View original postWhat this means: Bullish for ZEC as some view it as a counter-cyclical play against Bitcoin volatility. The narrative gained traction after ZEC rose 2.8% while BTC dipped 0.4% on January 2.\n\n### 2. @VipRoseTr: Rising wedge warns of 42% drop 📉\n\n“ZEC forming bearish pattern – breakdown below support targets $289”– @VipRoseTr (63.4K followers · 8.2M impressions · 2025-12-27 13:53 UTC)View original postWhat this means: Bearish technical outlook as ZEC struggles at $519 resistance (current price $501). The pattern’s measured move aligns with the 38.2% Fibonacci retracement of its 295% 90-day rally.\n\n### 3. @MusicByVirtuals: Prediction market shows skepticism 🎯\n\n“85.8% bet ZEC stays below $550 through EOY 2025”– @MusicByVirtuals (6.1K followers · 3.1M impressions · 2025-11-28 14:56 UTC)View original postWhat this means: Neutral-bearish sentiment despite ZEC’s 47.9% 30-day gain. The crowd doubts sustainability of recent momentum, though the poll closed before January’s Grayscale Trust accumulation news.\n\n## Conclusion\n\nThe consensus on Zcash is mixed – bullish on privacy adoption narratives but wary of stretched valuations. While institutions like Grayscale’s $190M Zcash Trust signal long-term conviction, derivatives data shows $54M in vulnerable short positions that could fuel volatility. Watch the $404 support level: A hold above maintains the ascending triangle pattern targeting $630, while a breakdown might confirm the bearish wedge toward $300. With 29% of ZEC’s supply now in shielded pools, regulatory clarity remains the ultimate make-or-break factor.\n\n## What is the latest update in ZEC’s codebase?\n\n## TLDR\n\nZcash's codebase advances privacy and node infrastructure.\n1. NU6.1 Activation (Oct 2025) – Enabled shielded transaction upgrades and fee optimizations.\n2. Zcashd Deprecation (Apr 2025) – Migration to Zebra nodes and Zallet wallet underway.\n3. Zashi 2.0.3 (Apr 2025) – Streamlined shielded addresses and cross-chain swaps.\n\n## Deep Dive\n\n### 1. NU6.1 Activation (Oct 2025)\n\nOverview: Implemented ZIPs 317 and 320, refining fee structures and transparent address formats.This upgrade introduced a new transaction version (v5) as the default, reducing fees for shielded transfers by ~30% through optimized proof bundling. It also added stricter mempool rules to prevent spam transactions.\n\nWhat this means: This is bullish for ZEC because lower fees and improved spam resistance make private transactions more accessible and scalable. (Source)\n\n### 2. Zcashd Deprecation (Apr 2025)\n\nOverview: Phasing out the legacy C++ client (zcashd) in favor of Rust-based Zebra nodes and Zallet wallet.Key RPC methods like z_getbalance were deprecated, with users urged to migrate before August 2025. Zebra offers faster sync times and modular architecture.\n\nWhat this means: This is neutral for ZEC – while modernization improves long-term maintainability, migration complexities could temporarily strain ecosystem tools. (Source)\n\n### 3. Zashi 2.0.3 (Apr 2025)\n\nOverview: Wallet update defaulting to shielded addresses and integrating Maya DEX for cross-chain swaps.The redesign simplified sending private transactions and added auto-shielding of transparent balances. Over 15% more ZEC moved to shielded pools post-update.\n\nWhat this means: This is bullish for ZEC because frictionless privacy strengthens its core value proposition amid regulatory scrutiny. (Source)\n\n## Conclusion\n\nZcash’s updates prioritize privacy usability and infrastructure resilience, aligning with its role as a compliance-friendly anonymity tool. With shielded adoption rising and node modernization complete, how will ZEC balance regulatory pressures against its technological edge in 2026?\n\n## What is next on ZEC’s roadmap?\n\n## TLDR\n\nZcash's development roadmap focuses on privacy enhancements, ecosystem expansion, and governance upgrades through early 2026.\n1. Zashi Wallet 2.0 (Q1 2026) – Shielded swaps and cross-chain DeFi integration.\n2. Ztarknet Devnet Launch (Q1 2026) – Privacy-preserving smart contracts.\n3. Governance Model Overhaul (2026) – Streamlined development funding.\n\n## Deep Dive\n\n### 1. Zashi Wallet 2.0 (Q1 2026)\n\nOverview:The Zashi wallet will enable fully shielded swaps via NEAR Protocol’s Intents, allowing users to privately convert assets like BTC or ETH into shielded ZEC without intermediaries. This follows the November 2025 integration that simplified shielded-to-transparent transactions.\n\nWhat this means:Bullish for ZEC adoption, as frictionless privacy could attract users seeking compliance-friendly anonymity. Risks include potential delays in cross-chain refund privacy features.\n\n### 2. Ztarknet Devnet Launch (Q1 2026)\n\nOverview:Ztarknet, a Starknet-inspired Layer-2 rollup, will bring programmable smart contracts to Zcash using Circle-STARK proofs. This allows private computation off-chain while settling on Zcash’s base layer, maintaining shielded pool integrity (Eli5defi, Nov 2025).\n\nWhat this means:Neutral-to-bullish – while this expands Zcash’s utility beyond simple payments, adoption depends on developer uptake. Success could position ZEC as a privacy-centric smart contract platform.\n\n### 3. Governance Model Overhaul (2026)\n\nOverview:Community proposals aim to replace Zcash’s expiring development fund with a new model emphasizing transparency and faster execution. This follows June 2025 debates about sustaining ecosystem growth.\n\nWhat this means:Bullish if governance reforms reduce bureaucratic delays, but bearish risks emerge if funding disputes fragment the community.\n\n## Conclusion\n\nZcash’s 2026 trajectory hinges on balancing technical innovation (Ztarknet, Zashi) with governance maturity. While privacy upgrades could drive mainstream adoption, regulatory scrutiny remains a wildcard. How will Zcash’s optional privacy model fare as global AML rules tighten?\nCMC AI can make mistakes. Not financial advice. Read more about ZEC [What is Zcash (ZEC)?](https://coinmarketcap.com/cmc-ai/zcash/what-is/) [Latest Zcash (ZEC) Price Analysis](https://coinmarketcap.com/cmc-ai/zcash/price-analysis/) [Zcash (ZEC) Price Prediction](https://coinmarketcap.com/cmc-ai/zcash/price-prediction/) \n## Explore Similar Coins\n\n![ZEC](https://s2.coinmarketcap.com/static/img/coins/64x64/1437.png)\nZcash ZEC | $494.67 \n1.51% (1d)\n[See ZEC Price Chart](https://coinmarketcap.com/currencies/zcash/#cmcaiquestion=0) Read more about ZEC [What is Zcash (ZEC)?](https://coinmarketcap.com/cmc-ai/zcash/what-is/) [Latest Zcash (ZEC) Price Analysis](https://coinmarketcap.com/cmc-ai/zcash/price-analysis/) [Zcash (ZEC) Price Prediction](https://coinmarketcap.com/cmc-ai/zcash/price-prediction/) Cryptos: [29.55M](https://coinmarketcap.com/charts/number-of-cryptocurrencies-tracked/) Exchanges: [913](https://coinmarketcap.com/rankings/exchanges/) Market Cap: [$3.18T](https://coinmarketcap.com/charts/) 0.79% 24h Vol: [$138.65B](https://coinmarketcap.com/charts/) 11.53% Dominance: [BTC: 58.2% ETH: 12.3%](https://coinmarketcap.com/charts/bitcoin-dominance/) ** ETH Gas : 0.04 Gwei Fear & Greed: [49/100](https://coinmarketcap.com/charts/fear-and-greed-index/) [API](https://coinmarketcap.com/api/pricing/)\n</searchResult>\n\n\n"
  }
]

```

03:15:59.369 - State transitioned from  to RunStepCompleted with type RunStepUpdate

03:15:59.369 - State transitioned from RunStepCompleted to RunQueued with type RunUpdate

03:15:59.647 - State transitioned from RunQueued to RunInProgress with type RunUpdate

03:16:03.735 - State transitioned from RunInProgress to RunStepCreated with type RunStepUpdate

03:16:03.751 - State transitioned from RunStepCreated to RunStepInProgress with type RunStepUpdate

03:16:03.754 - State transitioned from RunStepInProgress to MessageCreated with type MessageStatusUpdate

03:16:03.760 - State transitioned from MessageCreated to MessageInProgress with type MessageStatusUpdate

03:16:03.766 - State transitioned from MessageInProgress to MessageUpdated with type MessageContentUpdate

03:16:13.586 - State transitioned from MessageUpdated to MessageCompleted with type MessageStatusUpdate

03:16:13.654 - State transitioned from MessageCompleted to RunStepCompleted with type RunStepUpdate

03:16:13.693 - State transitioned from RunStepCompleted to RunCompleted with type RunUpdate

03:16:13.693 - RunCompleted received from Assistants API

# Answer


### Comprehensive Sentiment Analysis for Zcash (ZEC)

#### 1. **Information Sources Summary:**
- **RSS News Feeds:** 10 articles analyzed from DL News and other sources                    .
- **Internet Search:** 8 relevant results analyzed, including CoinMarketCap, CoinBird, and MarketBeat                .
- **Twitter/X:** Multiple posts reviewed, including insights from influencers and traders                .
- **Reddit:** No specific Reddit posts detected.

---

#### 2. **Sentiment Analysis:**
- **Current Market Sentiment:** **Bullish** (Confidence Level: Medium)
- **Key Sentiment Drivers:**
  - **Positive Factors:**
    - Institutional interest from Grayscale and Winklevoss-backed Cypherpunk, with significant Zcash purchases      .
    - Increasing adoption of privacy technology, including Zcash's shielded transactions and new wallet upgrades      .
    - Positive price movement with Zcash gaining 23% in the past week  .
    - Analysts and influencers projecting potential price increases up to $800  .
    - Strong support for Zcash as a privacy-centric hedge against Bitcoin's transparency    .
  - **Negative Factors:**
    - Regulatory scrutiny in the EU and other regions, with potential bans on privacy coins    .
    - Concerns about liquidity and delisting risks from major exchanges like Binance    .
    - Whale-driven volatility, including leveraged positions that could lead to liquidation risks  .
    - Recent unshielding activity and transfers to Binance raising concerns about potential sell-offs    .

- **Sentiment Trends Over Time:**
  - The sentiment has been predominantly positive in the past week, driven by institutional investments and technological advancements. However, regulatory concerns and market volatility have introduced caution among investors.

---

#### 3. **Source-Specific Insights:**
- **News Impact Assessment:**
  - Institutional purchases and technological upgrades have been major bullish drivers      .
  - Regulatory concerns and delisting risks are key bearish factors    .
- **Social Media Sentiment Trends:**
  - Twitter influencers show mixed sentiment, with some projecting bullish price targets and others warning of potential bearish retracements  .
- **Community Perception Summary:**
  - The community sentiment is divided, with optimism about privacy adoption and institutional support, but concerns about regulatory hurdles and price volatility    .

---

#### 4. **Trading Recommendation:**
- **Recommendation:** **HOLD**
- **Confidence Level:** **Medium**
- **Rationale:**
  - Zcash has shown strong price growth and institutional interest, signaling long-term potential.
  - Privacy technology adoption is increasing, which aligns with Zcash's core value proposition.
  - However, regulatory risks and liquidity concerns pose significant challenges, making it prudent to adopt a cautious approach.
- **Key Factors Driving Recommendation:**
  - Institutional confidence (Grayscale ETF filing, Winklevoss investment).
  - Positive sentiment around privacy technology.
  - Recent price surge and bullish technical indicators.
- **Risk Factors and Opportunities:**
  - Risks: Regulatory bans on privacy coins, potential exchange delistings, and market volatility.
  - Opportunities: Continued institutional adoption, technological advancements, and potential price breakout.

---

#### 5. **Summary Table:**

| **Source Type**          | **Count Analyzed** | **Overall Sentiment** | **Key Metrics/Insights**                                                                                                                                          |
|---------------------------|--------------------|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RSS News Feeds            | 10                | Bullish                | Institutional support, privacy adoption, price surge, regulatory concerns             |
| Internet Search           | 8                 | Neutral-Bullish        | Mixed sentiment with bullish narratives and bearish risks                                                        |
| Twitter/X                 | Multiple posts    | Mixed                  | Mixed sentiment from influencers, with bullish price targets and bearish warnings                                                                      |
| Reddit                    | 0                 | N/A                    | No Reddit posts detected                                                                                                                                        |

---

### Final Note:
The market sentiment for Zcash (ZEC) over the past week has been predominantly bullish due to institutional interest and technological advancements. However, the presence of regulatory risks and liquidity concerns warrants a cautious approach. Holding ZEC is recommended, with monitoring of key support and resistance levels to manage potential risks and capitalize on future opportunities.




---



# Resources Used to Generate Answer:


### Tools:

```json

[
  {
    "LlmIterationIndex": 1,
    "Name": "InternetSearch",
    "Status": "Success",
    "Arguments": "{\"question\": \"Recent news and sentiment analysis for Zcash (ZEC) over the last 7 days\"}"
  },
  {
    "LlmIterationIndex": 1,
    "Name": "InternetSearch",
    "Status": "Success",
    "Arguments": "{\"question\": \"Recent Reddit discussions and sentiment about Zcash (ZEC)\"}"
  },
  {
    "LlmIterationIndex": 1,
    "Name": "InternetSearch",
    "Status": "Success",
    "Arguments": "{\"question\": \"Recent Twitter sentiment and trends about Zcash (ZEC)\"}"
  },
  {
    "LlmIterationIndex": 1,
    "Name": "WebSiteSearch",
    "Status": "Success",
    "Arguments": "{\"question\": \"Zcash (ZEC) news on DL News RSS feed\"}"
  },
  {
    "LlmIterationIndex": 1,
    "Name": "WebSiteSearch",
    "Status": "Success",
    "Arguments": "{\"question\": \"Recent news about Zcash (ZEC) over the last 7 days\"}"
  }
]

```


### Token Consumption: 

```json

[
  {
    "Category": "ToolFunctionDefinition",
    "CountTokens": 37,
    "Confidence": "Measured",
    "Source": "Tool Definition - Internet Search"
  },
  {
    "Category": "ToolFunctionDefinition",
    "CountTokens": 43,
    "Confidence": "Measured",
    "Source": "Tool Definition - Website Data"
  },
  {
    "Category": "SystemPrompt",
    "CountTokens": 810,
    "Confidence": "Measured",
    "Source": "System Prompt"
  },
  {
    "Category": "InternetSearch",
    "CountTokens": 16846,
    "Confidence": "Measured",
    "Source": "Internet Search"
  },
  {
    "Category": "InternetSearch",
    "CountTokens": 7346,
    "Confidence": "Measured",
    "Source": "Internet Search"
  },
  {
    "Category": "InternetSearch",
    "CountTokens": 13151,
    "Confidence": "Measured",
    "Source": "Internet Search"
  },
  {
    "Category": "InternetSearch",
    "CountTokens": 22375,
    "Confidence": "Measured",
    "Source": "Website data source"
  },
  {
    "Category": "InternetSearch",
    "CountTokens": 15834,
    "Confidence": "Measured",
    "Source": "Website data source"
  },
  {
    "Category": "Answer",
    "CountTokens": 880,
    "Confidence": "Measured",
    "Source": "Assistant Response"
  }
]

```


### Execution Logs: 

```json

[
  {
    "ExecutionLogType": "GenerateFinalAnswer",
    "ExecutionLogDetailLevel": "Verbose",
    "Message": "Sending request 0 to gpt-4o using Assistants API.",
    "CreatedAt": "2026-01-07T03:15:47.2062354+00:00",
    "IsError": false
  },
  {
    "ExecutionLogType": "GenerateFinalAnswer",
    "ExecutionLogDetailLevel": "Verbose",
    "Message": "Sending request 1 to gpt-4o using Assistants API.",
    "CreatedAt": "2026-01-07T03:15:55.18566+00:00",
    "IsError": false
  },
  {
    "ExecutionLogType": "GenerateFinalAnswer",
    "ExecutionLogDetailLevel": "Verbose",
    "Message": "There are 5 tool call(s) to make.",
    "CreatedAt": "2026-01-07T03:15:55.1874189+00:00",
    "IsError": false
  },
  {
    "ExecutionLogType": "InternetSearch",
    "ExecutionLogDetailLevel": "Verbose",
    "Message": "Searching website",
    "SimpleData": {
      "question": "Recent news about Zcash (ZEC) over the last 7 days",
      "website": "https://www.dlnews.com/"
    },
    "CreatedAt": "2026-01-07T03:15:55.1884292+00:00",
    "IsError": false
  },
  {
    "ExecutionLogType": "GenerateFinalAnswer",
    "ExecutionLogDetailLevel": "Verbose",
    "Message": "Searching the Internet",
    "SimpleData": {
      "question": "Recent news and sentiment analysis for Zcash (ZEC) over the last 7 days"
    },
    "CreatedAt": "2026-01-07T03:15:55.1916909+00:00",
    "IsError": false
  },
  {
    "ExecutionLogType": "InternetSearch",
    "ExecutionLogDetailLevel": "Verbose",
    "Message": "Searching website",
    "SimpleData": {
      "question": "Zcash (ZEC) news on DL News RSS feed",
      "website": "https://www.dlnews.com/"
    },
    "CreatedAt": "2026-01-07T03:15:55.1918804+00:00",
    "IsError": false
  },
  {
    "ExecutionLogType": "GenerateFinalAnswer",
    "ExecutionLogDetailLevel": "Verbose",
    "Message": "Searching the Internet",
    "SimpleData": {
      "question": "Recent Twitter sentiment and trends about Zcash (ZEC)"
    },
    "CreatedAt": "2026-01-07T03:15:55.1920219+00:00",
    "IsError": false
  },
  {
    "ExecutionLogType": "GenerateFinalAnswer",
    "ExecutionLogDetailLevel": "Verbose",
    "Message": "Searching the Internet",
    "SimpleData": {
      "question": "Recent Reddit discussions and sentiment about Zcash (ZEC)"
    },
    "CreatedAt": "2026-01-07T03:15:55.1921823+00:00",
    "IsError": false
  },
  {
    "ExecutionLogType": "InternetSearch",
    "ExecutionLogDetailLevel": "Verbose",
    "Message": "Finished Searching the Internet",
    "SimpleData": {
      "webPages": {
        "value": [
          {
            "name": "Zcash surges tenfold as investors bet on privacy as ban looms",
            "url": "https://www.dlnews.com/articles/markets/zcash-surges-tenfold-as-investors-bet-on-privacy-as-ban-looms/"
          },
          {
            "name": "Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% ...",
            "url": "https://www.dlnews.com/articles/people-culture/zcash-foundation-shakes-up-leadership-amidst-zec-token-price-rally/"
          },
          {
            "name": "Why Zcash price is up 700% since September, according to Galaxy Digital",
            "url": "https://www.dlnews.com/articles/markets/why-privacy-token-zcash-price-is-up-700-percent-since-september/"
          },
          {
            "name": "Zcash price primed for 45% breakout as Grayscale files for ETF",
            "url": "https://www.dlnews.com/articles/markets/zcash-price-primed-for-45-percent-breakout-as-grayscale-files-for-etf/"
          },
          {
            "name": "Zcash price surge continues despite market turmoil – DL News",
            "url": "https://www.dlnews.com/articles/markets/zcash-price-surge-continues-despite-market-turmoil/"
          },
          {
            "name": "Winklevoss twins bet on Zcash with new treasury firm targeting 5% ...",
            "url": "https://www.dlnews.com/articles/markets/winklevoss-twins-bet-on-zcash-with-new-treasury-firm/"
          },
          {
            "name": "DL News - Markets, DeFi, Regulation and top cryptocurrency news",
            "url": "https://www.dlnews.com/"
          },
          {
            "name": "RSS - DL News",
            "url": "https://www.dlnews.com/rss/"
          },
          {
            "name": "How privacy coins Firo and Zcash dodged Binance delisting ... - DL News",
            "url": "https://www.dlnews.com/articles/defi/how-privacy-coins-firo-and-zcash-dodged-binance-delisting/"
          },
          {
            "name": "Monero and Zcash’s liquidity dries up as Binance eyes ... - DL News",
            "url": "https://www.dlnews.com/articles/defi/monero-and-zcash-liquidity-runs-dry-as-binance-may-delist/"
          }
        ]
      }
    },
    "CreatedAt": "2026-01-07T03:15:56.0571424+00:00",
    "IsError": false
  },
  {
    "ExecutionLogType": "InternetSearch",
    "ExecutionLogDetailLevel": "Verbose",
    "Message": "Finished Searching the Internet",
    "SimpleData": {
      "webPages": {
        "value": [
          {
            "name": "Zcash Social Sentiment & Market Pulse Data | BitMart X Insight",
            "url": "https://www.bitmart.com/ai/xinsight/coins/detail/ZEC"
          },
          {
            "name": "Zcash News Today (ZEC) – Latest Updates & Trends",
            "url": "https://www.coinbird.com/cryptocurrencies/zcash/news"
          },
          {
            "name": "Will Zcash (ZEC) Price Finally Retest $500 After Nearly 8 Years?",
            "url": "https://finance.yahoo.com/news/zcash-zec-price-finally-retest-150000437.html"
          },
          {
            "name": "Latest Zcash News - (ZEC) Future Outlook, Trends & Market Insights",
            "url": "https://coinmarketcap.com/cmc-ai/zcash/latest-updates/"
          },
          {
            "name": "Zcash and the Altcoin Season Indicator: A Technical and Sentiment ...",
            "url": "https://www.ainvest.com/news/zcash-altcoin-season-indicator-technical-sentiment-driven-analysis-2510/"
          },
          {
            "name": "Zcash Real-Time Price Performance, Futures Metrics, Spot & Futures ...",
            "url": "https://www.coinglass.com/currencies/ZEC"
          },
          {
            "name": "Zcash(ZEC) Price Today, ZEC to USD Real-Time, Latest Discussions ...",
            "url": "https://stocktwits.com/coins/zcash"
          },
          {
            "name": "ZEC’s Record $2.27B Market Cap Signals Major Shift in Investor Sentiment",
            "url": "https://www.ethnews.com/zecs-record-2-27b-market-cap-signals-major-shift-in-investor-sentiment/"
          },
          {
            "name": "ZCash (ZEC) Latest News Articles - CoinDesk",
            "url": "https://www.coindesk.com/price/zec/news"
          },
          {
            "name": "Reasons why Zcash is surging on Thursday - FXStreet",
            "url": "https://www.fxstreet.com/cryptocurrencies/news/zcash-price-forecast-zec-extends-rally-as-demand-for-privacy-protocols-surges-202510091213"
          }
        ]
      }
    },
    "CreatedAt": "2026-01-07T03:15:56.0684646+00:00",
    "IsError": false
  },
  {
    "ExecutionLogType": "InternetSearch",
    "ExecutionLogDetailLevel": "Verbose",
    "Message": "Finished Searching the Internet",
    "SimpleData": {
      "webPages": {
        "value": [
          {
            "name": "Zcash price surge continues despite market turmoil – DL News",
            "url": "https://www.dlnews.com/articles/markets/zcash-price-surge-continues-despite-market-turmoil/"
          },
          {
            "name": "Zcash surges tenfold as investors bet on privacy as ban looms",
            "url": "https://www.dlnews.com/articles/markets/zcash-surges-tenfold-as-investors-bet-on-privacy-as-ban-looms/"
          },
          {
            "name": "Zcash price primed for 45% breakout as Grayscale files for ETF",
            "url": "https://www.dlnews.com/articles/markets/zcash-price-primed-for-45-percent-breakout-as-grayscale-files-for-etf/"
          },
          {
            "name": "Why Zcash price is up 700% since September, according to Galaxy Digital",
            "url": "https://www.dlnews.com/articles/markets/why-privacy-token-zcash-price-is-up-700-percent-since-september/"
          },
          {
            "name": "Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% ...",
            "url": "https://www.dlnews.com/articles/people-culture/zcash-foundation-shakes-up-leadership-amidst-zec-token-price-rally/"
          },
          {
            "name": "Winklevoss twins bet on Zcash with new treasury firm targeting 5% ...",
            "url": "https://www.dlnews.com/articles/markets/winklevoss-twins-bet-on-zcash-with-new-treasury-firm/"
          },
          {
            "name": "Monero and Zcash’s liquidity dries up as Binance eyes ... - DL News",
            "url": "https://www.dlnews.com/articles/defi/monero-and-zcash-liquidity-runs-dry-as-binance-may-delist/"
          },
          {
            "name": "Ika Announces EdDSA Signatures, Expanding Native Support to Solana ...",
            "url": "https://www.dlnews.com/external/ika-announces-eddsa-signatures-expanding-native-support-to-solana-zcash-cardano-and-more/"
          },
          {
            "name": "How privacy coins Firo and Zcash dodged Binance delisting ... - DL News",
            "url": "https://www.dlnews.com/articles/defi/how-privacy-coins-firo-and-zcash-dodged-binance-delisting/"
          },
          {
            "name": "ZKasino’s year-long silence on investor refunds ends in a $27m ...",
            "url": "https://www.dlnews.com/articles/defi/crypto-gambling-app-zkasino-liquidated/"
          }
        ]
      }
    },
    "CreatedAt": "2026-01-07T03:15:56.0809248+00:00",
    "IsError": false
  },
  {
    "ExecutionLogType": "InternetSearch",
    "ExecutionLogDetailLevel": "Verbose",
    "Message": "Finished Searching the Internet",
    "SimpleData": {
      "webPages": {
        "value": [
          {
            "name": "Zcash Exchange Balances Plunge 20% - Breakout To $800 Likely - BeInCrypto",
            "url": "https://beincrypto.com/zcash-accumulation-sets-stage-for-zec-price-breakout/"
          },
          {
            "name": "Zcash News Today (ZEC) – Latest Updates & Trends",
            "url": "https://www.coinbird.com/cryptocurrencies/zcash/news"
          },
          {
            "name": "Zcash Price Prediction, News, and Analysis (ZEC) - MarketBeat",
            "url": "https://www.marketbeat.com/cryptocurrencies/zcash/"
          },
          {
            "name": "Latest Zcash News - (ZEC) Future Outlook, Trends & Market Insights",
            "url": "https://coinmarketcap.com/cmc-ai/zcash/latest-updates/"
          },
          {
            "name": "ZCash (ZEC) 7-day Price Change | MEXC Crypto Pulse",
            "url": "https://www.mexc.com/en-GB/crypto-pulse/article/zcash-zec-7-day-price-change-64040"
          },
          {
            "name": "How Low Can Zcash Price Go After ZEC’s 30% Drop From ... - Cointelegraph",
            "url": "https://cointelegraph.com/news/zcash-down-30-percent-november-will-zec-price-crash-further"
          },
          {
            "name": "Crypto News: Zcash Rebounds From $300 as Expert Flags Key Levels",
            "url": "https://www.livebitcoinnews.com/expert-shares-zcash-zec-price-update-heres-his-outlook/"
          },
          {
            "name": "ZCash (ZEC) Latest News Articles - CoinDesk",
            "url": "https://www.coindesk.com/price/zec/news"
          },
          {
            "name": "Zcash Price (ZEC): Key Insights, Technical Analysis, and Market ... - OKX",
            "url": "https://www.okx.com/learn/zcash-price-zec-insights-analysis-trends"
          },
          {
            "name": "Will Zcash (ZEC) Price Finally Retest $500 After Nearly 8 Years?",
            "url": "https://finance.yahoo.com/news/zcash-zec-price-finally-retest-150000437.html"
          }
        ]
      }
    },
    "CreatedAt": "2026-01-07T03:15:56.2031662+00:00",
    "IsError": false
  },
  {
    "ExecutionLogType": "InternetSearch",
    "ExecutionLogDetailLevel": "Verbose",
    "Message": "Finished Searching the Internet",
    "SimpleData": {
      "webPages": {
        "value": [
          {
            "name": "Zcash - Reddit",
            "url": "https://www.reddit.com/r/zec/"
          },
          {
            "name": "Zcash(ZEC) Price Today, ZEC to USD Real-Time, Latest Discussions ...",
            "url": "https://stocktwits.com/coins/zcash"
          },
          {
            "name": "Will Zcash (ZEC) Price Finally Retest $500 After Nearly 8 Years?",
            "url": "https://finance.yahoo.com/news/zcash-zec-price-finally-retest-150000437.html"
          },
          {
            "name": "People Share Thoughts on ZEC (ZCash) in Forums : BlockScopeX",
            "url": "https://blockscopex.com/news/opinions-on-zec-zcash-in-forums/"
          },
          {
            "name": "Latest Zcash News - (ZEC) Future Outlook, Trends & Market Insights",
            "url": "https://coinmarketcap.com/cmc-ai/zcash/latest-updates/"
          },
          {
            "name": "Taking a Step Back: Closing the ZEC Chapter | CoinDailies",
            "url": "https://coindailies.com/news/closing-chapter-with-zec-investment/"
          },
          {
            "name": "ZEC Reddit Mentions | ChartExchange",
            "url": "https://chartexchange.com/symbol/crypto-zecrlusd/trends/reddit/"
          },
          {
            "name": "Zcash Community Forum - An open forum for Zcash users and enthusiasts ...",
            "url": "https://forum.zcashcommunity.com/"
          },
          {
            "name": "ZEC - Zcash - Reddit Mentions and Sentiments - Memeberg Terminal",
            "url": "https://www.memebergterminal.com/cryptos/zec"
          },
          {
            "name": "Zcash: Why ZEC keeps failing at $520 despite brief rebounds",
            "url": "https://ambcrypto.com/zcash-why-zec-keeps-failing-at-520-despite-brief-rebounds/"
          }
        ]
      }
    },
    "CreatedAt": "2026-01-07T03:15:56.2049347+00:00",
    "IsError": false
  }
]

```


### Timings:

```json

{
  "Operation": "root",
  "TimeMs": 27891,
  "NestedTimings": [
    {
      "Operation": "Create Assistant",
      "TimeMs": 530,
      "NestedTimings": [
        {
          "Operation": "Code Interpreter",
          "TimeMs": 0,
          "NestedTimings": [],
          "StartTicks": 639033525453183006,
          "Id": "f57c7d8e-eb06-41cd-bedb-210c32ce10ab"
        }
      ],
      "StartTicks": 639033525453182700,
      "Id": "da9f63bf-8d9c-441a-add4-2b21294e521f"
    },
    {
      "Operation": "Setup Assistant Thread",
      "TimeMs": 856,
      "NestedTimings": [],
      "StartTicks": 639033525463497433,
      "Id": "a687ab11-c23d-4621-842d-b5c376f52f77"
    },
    {
      "Operation": "LLM Response",
      "TimeMs": 26505,
      "NestedTimings": [
        {
          "Operation": "First Block Received",
          "TimeMs": 7979,
          "NestedTimings": [
            {
              "Operation": "Tool Call - WebSiteSearch",
              "TimeMs": 3476,
              "NestedTimings": [
                {
                  "Operation": "Web: Zcash price surge continues despite market turmoil – DL News",
                  "TimeMs": 1763,
                  "NestedTimings": [],
                  "StartTicks": 639033525560815079,
                  "Id": "ad472ad0-6b6e-491c-a94e-dc783f6def7c"
                },
                {
                  "Operation": "Web: Zcash surges tenfold as investors bet on privacy as ban looms",
                  "TimeMs": 2031,
                  "NestedTimings": [],
                  "StartTicks": 639033525560816468,
                  "Id": "600ef609-4c57-4c14-bdff-892791a39ae4"
                },
                {
                  "Operation": "Web: Zcash price primed for 45% breakout as Grayscale files for ETF",
                  "TimeMs": 2013,
                  "NestedTimings": [],
                  "StartTicks": 639033525560817618,
                  "Id": "3e14a401-7eb9-4ed6-bba4-dda478970877"
                },
                {
                  "Operation": "Web: Why Zcash price is up 700% since September, according to Galaxy Digital",
                  "TimeMs": 1981,
                  "NestedTimings": [],
                  "StartTicks": 639033525560818524,
                  "Id": "a96902e1-7a2e-4306-9ffc-16d2531d3a5c"
                },
                {
                  "Operation": "Web: Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% ...",
                  "TimeMs": 1954,
                  "NestedTimings": [],
                  "StartTicks": 639033525560819293,
                  "Id": "a76fdd34-e206-4739-97a7-293e14ec921a"
                },
                {
                  "Operation": "Web: Winklevoss twins bet on Zcash with new treasury firm targeting 5% ...",
                  "TimeMs": 2058,
                  "NestedTimings": [],
                  "StartTicks": 639033525560820026,
                  "Id": "1ae59f91-e7c4-4825-99a0-1bae6928b8e7"
                },
                {
                  "Operation": "Web: Monero and Zcash’s liquidity dries up as Binance eyes ... - DL News",
                  "TimeMs": 2564,
                  "NestedTimings": [],
                  "StartTicks": 639033525560820793,
                  "Id": "d85b5d24-0416-47cb-a5eb-ca2e76bf1f40"
                },
                {
                  "Operation": "Web: Ika Announces EdDSA Signatures, Expanding Native Support to Solana ...",
                  "TimeMs": 2575,
                  "NestedTimings": [],
                  "StartTicks": 639033525560822668,
                  "Id": "05e41805-82cf-4d5f-81b5-e72aeda25efc"
                },
                {
                  "Operation": "Web: How privacy coins Firo and Zcash dodged Binance delisting ... - DL News",
                  "TimeMs": 2436,
                  "NestedTimings": [],
                  "StartTicks": 639033525560824958,
                  "Id": "8d76b8d0-b522-4982-bfb2-a3ff89672401"
                },
                {
                  "Operation": "Web: ZKasino’s year-long silence on investor refunds ends in a $27m ...",
                  "TimeMs": 2489,
                  "NestedTimings": [],
                  "StartTicks": 639033525560827179,
                  "Id": "38531a75-4cdc-46db-afa0-5cee24b53c53"
                }
              ],
              "StartTicks": 639033525551874383,
              "Id": "d7268d33-5819-4d89-9164-6c61866b04f7"
            },
            {
              "Operation": "Tool Call - InternetSearch",
              "TimeMs": 2218,
              "NestedTimings": [
                {
                  "Operation": "Web: Zcash Exchange Balances Plunge 20% - Breakout To $800 Likely - BeInCrypto",
                  "TimeMs": 861,
                  "NestedTimings": [],
                  "StartTicks": 639033525562037487,
                  "Id": "9c3c9255-e796-4279-bbd0-8214b9c36590"
                },
                {
                  "Operation": "Web: Zcash News Today (ZEC) – Latest Updates & Trends",
                  "TimeMs": 1086,
                  "NestedTimings": [],
                  "StartTicks": 639033525562039110,
                  "Id": "06f826b0-65eb-40f9-9055-a4cb4834a007"
                },
                {
                  "Operation": "Web: Zcash Price Prediction, News, and Analysis (ZEC) - MarketBeat",
                  "TimeMs": 1196,
                  "NestedTimings": [],
                  "StartTicks": 639033525562040103,
                  "Id": "f0687328-e92e-47f3-9565-941cab2b647d"
                },
                {
                  "Operation": "Web: Latest Zcash News - (ZEC) Future Outlook, Trends & Market Insights",
                  "TimeMs": 987,
                  "NestedTimings": [],
                  "StartTicks": 639033525562041171,
                  "Id": "f4c1b638-2a28-4c58-b4d0-6540bd5ee4cd"
                },
                {
                  "Operation": "Web: ZCash (ZEC) 7-day Price Change | MEXC Crypto Pulse",
                  "TimeMs": 368,
                  "NestedTimings": [],
                  "StartTicks": 639033525562042753,
                  "Id": "550753cc-c7c3-4942-b2a3-4b15ebd57d02"
                }
              ],
              "StartTicks": 639033525551916595,
              "Id": "f6378ad8-5c53-4492-8a45-683b188b29e1"
            },
            {
              "Operation": "Tool Call - WebSiteSearch",
              "TimeMs": 3471,
              "NestedTimings": [
                {
                  "Operation": "Web: Zcash surges tenfold as investors bet on privacy as ban looms",
                  "TimeMs": 2019,
                  "NestedTimings": [],
                  "StartTicks": 639033525560583492,
                  "Id": "467338e6-8892-47e1-bfa2-897887a3547b"
                },
                {
                  "Operation": "Web: Zcash Foundation shakes up leadership amidst blockchain token’s 1,000% ...",
                  "TimeMs": 1564,
                  "NestedTimings": [],
                  "StartTicks": 639033525560586170,
                  "Id": "2a9d8711-7ffe-4e29-b761-a6145c1e238b"
                },
                {
                  "Operation": "Web: Why Zcash price is up 700% since September, according to Galaxy Digital",
                  "TimeMs": 1482,
                  "NestedTimings": [],
                  "StartTicks": 639033525560587500,
                  "Id": "b2d5463e-ba29-40b5-b12c-a450f171d6d0"
                },
                {
                  "Operation": "Web: Zcash price primed for 45% breakout as Grayscale files for ETF",
                  "TimeMs": 1306,
                  "NestedTimings": [],
                  "StartTicks": 639033525560588355,
                  "Id": "6206363d-c9b6-4a6b-b988-199c5c276cdd"
                },
                {
                  "Operation": "Web: Zcash price surge continues despite market turmoil – DL News",
                  "TimeMs": 1494,
                  "NestedTimings": [],
                  "StartTicks": 639033525560589286,
                  "Id": "f8c502f0-05e2-4b70-ab24-7dab72740447"
                },
                {
                  "Operation": "Web: Winklevoss twins bet on Zcash with new treasury firm targeting 5% ...",
                  "TimeMs": 1700,
                  "NestedTimings": [],
                  "StartTicks": 639033525560590295,
                  "Id": "6a76410e-f42f-4d69-9517-0680aa681c88"
                },
                {
                  "Operation": "Web: DL News - Markets, DeFi, Regulation and top cryptocurrency news",
                  "TimeMs": 2103,
                  "NestedTimings": [],
                  "StartTicks": 639033525560598380,
                  "Id": "d2efc4cf-2c78-4ddf-af6d-f47feb6d61ad"
                },
                {
                  "Operation": "Web: RSS - DL News",
                  "TimeMs": 1582,
                  "NestedTimings": [],
                  "StartTicks": 639033525560600547,
                  "Id": "e1ebda25-d31f-4965-8b62-bf1acbf572ac"
                },
                {
                  "Operation": "Web: How privacy coins Firo and Zcash dodged Binance delisting ... - DL News",
                  "TimeMs": 2457,
                  "NestedTimings": [],
                  "StartTicks": 639033525560601427,
                  "Id": "a23a63df-9a01-4926-91b2-e194d5efbc5d"
                },
                {
                  "Operation": "Web: Monero and Zcash’s liquidity dries up as Binance eyes ... - DL News",
                  "TimeMs": 2592,
                  "NestedTimings": [],
                  "StartTicks": 639033525560602700,
                  "Id": "68c48368-1066-4900-a2c1-afdf61108ec7"
                }
              ],
              "StartTicks": 639033525551918114,
              "Id": "65608a07-5585-44d7-a727-a6bb1896c708"
            },
            {
              "Operation": "Tool Call - InternetSearch",
              "TimeMs": 3118,
              "NestedTimings": [
                {
                  "Operation": "Web: Zcash Social Sentiment & Market Pulse Data | BitMart X Insight",
                  "TimeMs": 2236,
                  "NestedTimings": [],
                  "StartTicks": 639033525560690414,
                  "Id": "81d2de51-9c28-4cf4-bc86-e21d8218856d"
                },
                {
                  "Operation": "Web: Zcash News Today (ZEC) – Latest Updates & Trends",
                  "TimeMs": 1208,
                  "NestedTimings": [],
                  "StartTicks": 639033525560692227,
                  "Id": "4db1d5ae-8abd-4bf3-b6d4-f6157da0e059"
                },
                {
                  "Operation": "Web: Will Zcash (ZEC) Price Finally Retest $500 After Nearly 8 Years?",
                  "TimeMs": 893,
                  "NestedTimings": [],
                  "StartTicks": 639033525560694048,
                  "Id": "e4599c3e-0163-478c-8831-22c5b3519b3d"
                },
                {
                  "Operation": "Web: Latest Zcash News - (ZEC) Future Outlook, Trends & Market Insights",
                  "TimeMs": 1110,
                  "NestedTimings": [],
                  "StartTicks": 639033525560694982,
                  "Id": "f5c9e9b1-fe64-4b5c-b79a-15c9e9702e2a"
                },
                {
                  "Operation": "Web: Zcash and the Altcoin Season Indicator: A Technical and Sentiment ...",
                  "TimeMs": 1396,
                  "NestedTimings": [],
                  "StartTicks": 639033525560695737,
                  "Id": "a38c0e0c-0c35-4536-8314-5ff0f83a3c87"
                }
              ],
              "StartTicks": 639033525551919888,
              "Id": "33921ae1-8a5d-4143-8d83-dac773f0eaf4"
            },
            {
              "Operation": "Tool Call - InternetSearch",
              "TimeMs": 2611,
              "NestedTimings": [
                {
                  "Operation": "Web: Zcash - Reddit",
                  "TimeMs": 399,
                  "NestedTimings": [],
                  "StartTicks": 639033525562053668,
                  "Id": "251720f7-7b7b-4f96-b00e-b338d9a53270"
                },
                {
                  "Operation": "Web: Zcash(ZEC) Price Today, ZEC to USD Real-Time, Latest Discussions ...",
                  "TimeMs": 1594,
                  "NestedTimings": [],
                  "StartTicks": 639033525562054890,
                  "Id": "38dabb02-209a-4325-9a6a-0e846d2c5201"
                },
                {
                  "Operation": "Web: Will Zcash (ZEC) Price Finally Retest $500 After Nearly 8 Years?",
                  "TimeMs": 835,
                  "NestedTimings": [],
                  "StartTicks": 639033525562056084,
                  "Id": "aeb2f93d-432d-491a-8e71-c05656c5b75a"
                },
                {
                  "Operation": "Web: People Share Thoughts on ZEC (ZCash) in Forums : BlockScopeX",
                  "TimeMs": 332,
                  "NestedTimings": [],
                  "StartTicks": 639033525562057142,
                  "Id": "3939723b-ff98-4208-b557-1abed448b468"
                },
                {
                  "Operation": "Web: Latest Zcash News - (ZEC) Future Outlook, Trends & Market Insights",
                  "TimeMs": 935,
                  "NestedTimings": [],
                  "StartTicks": 639033525562057802,
                  "Id": "ab92506f-3375-4e94-9264-9a1ce7a7194c"
                }
              ],
              "StartTicks": 639033525551921641,
              "Id": "bfc63afd-2ab1-4203-9e7b-9e7402f008c3"
            }
          ],
          "StartTicks": 639033525472062296,
          "Id": "4a422bd2-e343-4c65-908c-6ce7f000ab73"
        }
      ],
      "StartTicks": 639033525472062213,
      "Id": "43b17d8c-5f7d-47ee-be9e-f65b4993e172"
    }
  ],
  "StartTicks": 639033525453182241,
  "Id": "2455281e-dcac-407c-8b2c-d51c9fb26633"
}

```

