# Sentiment News Analyst - Evaluation Results Summary

This document tracks all evaluation runs for the Sentiment News Analyst agent.

---

## Evaluation Run #1 - ZEC Sentiment Analysis

**Date:** 2026-01-06  
**Evaluation ID:** eval_20260106_231712  
**Token Analyzed:** ZEC (Zcash)  
**Prompt:** Analyze the market sentiment for ZEC (Zcash) over the last 7 days

### Overall Scores

- **Automated Overall Score:** 76.58%
- **Rubric Overall Score:** 91.10%
- **Average Score:** 83.84%

### Component-Based Evaluations

| Component | Accuracy | API Error Rate | Policy Adherence | Success |
|-----------|----------|----------------|------------------|---------|
| RSS Feed Fetch | 50.00% | 0.00% | 0.00% | ✗ |
| Internet Search | 50.00% | 0.00% | 0.00% | ✗ |
| Twitter Search | 100.00% | 0.00% | 0.00% | ✗ |
| Reddit Search | 100.00% | 0.00% | 0.00% | ✗ |
| Sentiment Analysis | 66.67% | 0.00% | 100.00% | ✓ |
| Recommendation Generation | 100.00% | 0.00% | 100.00% | ✓ |

**Component Average Score:** 64.44%

### End-to-End Evaluation

| Metric | Score |
|--------|-------|
| Response Correctness | 100.00% |
| Tone Score | 90.00% |
| Satisfaction Score | 73.33% |
| Completeness | 100.00% |
| Coherence | 46.67% |
| Recommendation Quality | 100.00% |

**End-to-End Average Score:** 84.67%

### Pattern Detection

- **Hallucinations Detected:** 0
- **Tone Mismatch:** No
- **User Confusion Indicators:** 2
  - Mixed bullish/bearish signals without clear explanation
  - HOLD recommendation without clear explanation
- **Missing Information:** 0
- **Contradictions:** 1
  - Bullish and bearish statements in close proximity

### Rubric-Based Evaluation

| Category | Score | Weight |
|----------|-------|--------|
| Information Gathering | 100.00% | 25% |
| Sentiment Analysis | 70.00% | 25% |
| Recommendation | 100.00% | 30% |
| Presentation | 93.00% | 20% |

**Overall Rubric Score:** 91.10%

### Key Findings

**Strengths:**
- ✓ Response correctness: 100%
- ✓ Recommendation quality: 100%
- ✓ Tone score: 90%
- ✓ Completeness: 100%
- ✓ No hallucinations detected
- ✓ No tone mismatch

**Areas for Improvement:**
- ✗ RSS Feed Fetch: Policy adherence 0% (RSS feed not used)
- ✗ Internet Search: Policy adherence 0% (Internet search not used)
- ✗ Coherence: 46.67% (contradictions detected)
- ✗ User confusion indicators: 2
- ✗ Contradictions: 1 (bullish and bearish statements in close proximity)

### Recommendations

1. **Improve Data Source Usage:**
   - Ensure RSS feed from DL News is actively used
   - Ensure internet search is performed for comprehensive coverage

2. **Improve Coherence:**
   - Resolve contradictory statements
   - Provide clearer explanations for mixed signals

3. **Enhance Clarity:**
   - Provide clearer explanations for HOLD recommendations
   - Better explain mixed bullish/bearish signals

---

## Evaluation History

| Run # | Date | Token | Automated Score | Rubric Score | Status |
|-------|------|-------|----------------|--------------|--------|
| 1 | 2026-01-06 | ZEC | 76.58% | 91.10% | Completed |

---

## Summary Statistics

**Total Evaluations:** 1  
**Average Automated Score:** 76.58%  
**Average Rubric Score:** 91.10%  
**Average Combined Score:** 83.84%

**Component Success Rate:**
- RSS Feed Fetch: 0% (0/1)
- Internet Search: 0% (0/1)
- Twitter Search: 0% (0/1)
- Reddit Search: 0% (0/1)
- Sentiment Analysis: 100% (1/1)
- Recommendation Generation: 100% (1/1)

**Pattern Detection Averages:**
- Hallucinations per run: 0.0
- Tone mismatches per run: 0.0
- User confusion indicators per run: 2.0
- Missing information per run: 0.0
- Contradictions per run: 1.0

---

*Last Updated: 2026-01-06*

