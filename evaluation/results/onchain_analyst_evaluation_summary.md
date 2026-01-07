# Onchain Analyst - Evaluation Results Summary

This document tracks all evaluation runs for the Onchain Analyst agent.

---

## Evaluation Run #1 - ZEC Onchain Analysis

**Date:** 2026-01-06  
**Evaluation ID:** eval_20260106_234338  
**Token Analyzed:** ZEC (Zcash)  
**Network:** ZEC network  
**Prompt:** Analyze the onchain data for ZEC (Zcash) on ZEC network

### Overall Scores

- **Automated Overall Score:** 93.41%
- **Rubric Overall Score:** 60.10% (Note: Using sentiment analyst rubric - not applicable)
- **Average Score:** 76.76% (Note: Rubric not applicable for onchain analysis)

### Component-Based Evaluations

| Component | Accuracy | API Error Rate | Policy Adherence | Success |
|-----------|----------|----------------|------------------|---------|
| Liquidity Data Fetch | 100.00% | 0.00% | 100.00% | ✓ |
| Holder Data Fetch | 100.00% | 0.00% | 100.00% | ✓ |
| Transaction Data Fetch | 100.00% | 0.00% | 100.00% | ✓ |
| Supply Data Fetch | 100.00% | 0.00% | 100.00% | ✓ |
| Mempool Analysis | 100.00% | 0.00% | 100.00% | ✓ |
| Recommendation Generation | 66.67% | 0.00% | 100.00% | ✓ |

**Component Average Score:** 97.78%

### End-to-End Evaluation

| Metric | Score |
|--------|-------|
| Response Correctness | 100.00% |
| Tone Score | 90.00% |
| Satisfaction Score | 90.00% |
| Completeness | 100.00% |
| Coherence | 80.00% |
| Recommendation Quality | 80.00% |

**End-to-End Average Score:** 90.50%

### Pattern Detection

- **Hallucinations Detected:** 0
- **Tone Mismatch:** No
- **User Confusion Indicators:** 0
- **Missing Information:** 0
- **Contradictions:** 0

### Rubric-Based Evaluation

**Note:** The rubric-based evaluation uses the sentiment news analyst rubric, which is not applicable for onchain analysis. The rubric looks for RSS feeds, Twitter, and Reddit, which are not relevant for onchain data analysis.

| Category | Score | Weight | Note |
|----------|-------|--------|------|
| Information Gathering | 0.00% | 25% | Not applicable (looks for RSS/Twitter/Reddit) |
| Sentiment Analysis | 70.00% | 25% | Not applicable for onchain analysis |
| Recommendation | 100.00% | 30% | ✓ Applicable |
| Presentation | 63.00% | 20% | ✓ Applicable |

**Overall Rubric Score:** 60.10% (Not applicable - rubric designed for sentiment analysis)

### Key Findings

**Strengths:**
- ✓ All onchain data sources analyzed (liquidity, holders, transactions, supply, mempool)
- ✓ All required output sections present (100% completeness)
- ✓ Clear trading recommendation (BUY) with confidence level
- ✓ Professional tone and structure (90% tone score)
- ✓ No hallucinations or contradictions detected
- ✓ All component evaluations passed (100% success rate for data gathering)
- ✓ Response correctness: 100%

**Areas for Improvement:**
- ⚠️ Recommendation Generation Accuracy: 66.67%
  - Recommendation present: ✓
  - Confidence level: ✓
  - Rationale detail: Could be more comprehensive
- ⚠️ Coherence: 80% (Could improve logical flow between sections)
- ⚠️ Recommendation Quality: 80% (Could expand on risk factors and key drivers)

### Detailed Component Analysis

#### 1. Liquidity Data Fetch: ✓ Excellent
- **Status:** Success
- **Accuracy:** 100%
- **Policy Adherence:** 100%
- **Findings:** Successfully analyzed liquidity pools, shielded supply (29.66%), and DEX liquidity metrics

#### 2. Holder Data Fetch: ✓ Excellent
- **Status:** Success
- **Accuracy:** 100%
- **Policy Adherence:** 100%
- **Findings:** Successfully identified whale movements ($93M withdrawn from Binance), holder distribution changes, and accumulation patterns

#### 3. Transaction Data Fetch: ✓ Excellent
- **Status:** Success
- **Accuracy:** 100%
- **Policy Adherence:** 100%
- **Findings:** Successfully analyzed transaction volume ($787M), transaction patterns, and network activity

#### 4. Supply Data Fetch: ✓ Excellent
- **Status:** Success
- **Accuracy:** 100%
- **Policy Adherence:** 100%
- **Findings:** Successfully analyzed circulating supply (16,482,350 ZEC), total supply (21,000,000 ZEC), and supply distribution

#### 5. Mempool Analysis: ✓ Excellent
- **Status:** Success
- **Accuracy:** 100%
- **Policy Adherence:** 100%
- **Findings:** Successfully analyzed mempool activity (3 pending transactions, no congestion)

#### 6. Recommendation Generation: ⚠️ Good (Needs Improvement)
- **Status:** Success
- **Accuracy:** 66.67%
- **Policy Adherence:** 100%
- **Findings:** 
  - ✓ Recommendation present (BUY)
  - ✓ Confidence level stated (High)
  - ⚠️ Rationale could be more detailed
  - ⚠️ Risk factors could be expanded

### Recommendations

1. **Enhance Recommendation Rationale:**
   - Provide more detailed explanation of how onchain metrics support the recommendation
   - Expand on the connection between whale movements and price implications
   - Include more quantitative analysis of liquidity shifts

2. **Improve Coherence:**
   - Better connect sections with transitional statements
   - Ensure logical flow from data analysis to signals to recommendation

3. **Expand Risk Analysis:**
   - Provide more detailed risk factors based on onchain data
   - Include potential downside scenarios
   - Discuss liquidity risks in more detail

4. **Create Onchain-Specific Rubric:**
   - Develop a rubric specifically for onchain analysis
   - Include criteria for liquidity analysis, holder analysis, transaction analysis, etc.
   - Replace sentiment-focused rubric with onchain-focused evaluation

---

## Evaluation History

| Run # | Date | Token | Network | Automated Score | Status |
|-------|------|-------|---------|----------------|--------|
| 1 | 2026-01-06 | ZEC | ZEC network | 93.41% | Completed |

---

## Summary Statistics

**Total Evaluations:** 1  
**Average Automated Score:** 93.41%  
**Average Component Score:** 97.78%  
**Average End-to-End Score:** 90.50%

**Component Success Rate:**
- Liquidity Data Fetch: 100% (1/1)
- Holder Data Fetch: 100% (1/1)
- Transaction Data Fetch: 100% (1/1)
- Supply Data Fetch: 100% (1/1)
- Mempool Analysis: 100% (1/1)
- Recommendation Generation: 100% (1/1)

**Pattern Detection Averages:**
- Hallucinations per run: 0.0
- Tone mismatches per run: 0.0
- User confusion indicators per run: 0.0
- Missing information per run: 0.0
- Contradictions per run: 0.0

**End-to-End Metrics Averages:**
- Response Correctness: 100.00%
- Tone Score: 90.00%
- Satisfaction Score: 90.00%
- Completeness: 100.00%
- Coherence: 80.00%
- Recommendation Quality: 80.00%

---

## Performance Trends

### Component Performance Over Time

| Component | Run 1 | Average |
|-----------|-------|---------|
| Liquidity Data Fetch | 100% | 100% |
| Holder Data Fetch | 100% | 100% |
| Transaction Data Fetch | 100% | 100% |
| Supply Data Fetch | 100% | 100% |
| Mempool Analysis | 100% | 100% |
| Recommendation Generation | 66.67% | 66.67% |

### End-to-End Metrics Over Time

| Metric | Run 1 | Average |
|--------|-------|---------|
| Response Correctness | 100% | 100% |
| Tone Score | 90% | 90% |
| Satisfaction Score | 90% | 90% |
| Completeness | 100% | 100% |
| Coherence | 80% | 80% |
| Recommendation Quality | 80% | 80% |

---

*Last Updated: 2026-01-06*

