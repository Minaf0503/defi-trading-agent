# Evaluation Framework for Sentiment News Analyst

Comprehensive evaluation framework covering component-based evals, end-to-end evals, quantitative and qualitative metrics, and pattern detection.

## Overview

This evaluation framework provides:

1. **Component-Based Evaluations** - Measure each step separately
   - Accuracy
   - API error rate
   - Policy adherence

2. **End-to-End Evaluations** - Score overall user experience
   - Final response correctness
   - Tone
   - Satisfaction
   - Completeness
   - Coherence
   - Recommendation quality

3. **Pattern Detection**
   - Hallucinations
   - Tone mismatch
   - User confusion indicators
   - Missing information
   - Contradictory statements

4. **Evaluation Methods**
   - Automated evaluation
   - LLM-as-Judge
   - Rubric-based evaluation
   - Human reviewer (manual)

## Quick Start

### Run Evaluation

```bash
python evaluation/run_evaluation.py \
    --prompt-file output/prompt.txt \
    --response-file "output/Analyze the market sentiment for ZEC (Zcash) over .txt" \
    --log-file output/Execution\ Log.md \
    --output-file evaluation_report.md \
    --use-llm-judge \
    --use-rubric
```

### Python API

```python
from evaluation.evaluation_framework import SentimentNewsAnalystEvaluator
from evaluation.llm_judge import LLMJudge, RubricBasedEvaluator

# Load your data
prompt = "Analyze sentiment for BTC..."
response = "### Comprehensive Sentiment Analysis..."
execution_log = {...}  # Your execution log

# Automated evaluation
evaluator = SentimentNewsAnalystEvaluator()
result = evaluator.evaluate(prompt, response, execution_log)
report = evaluator.generate_report(result)
print(report)

# LLM Judge evaluation
llm_judge = LLMJudge()
llm_result = llm_judge.evaluate(prompt, response)

# Rubric-based evaluation
rubric_evaluator = RubricBasedEvaluator()
rubric_result = rubric_evaluator.evaluate(prompt, response, execution_log)
```

## Evaluation Components

### 1. Component-Based Evaluations

Evaluates each component separately:

- **RSS Feed Fetch**
  - Accuracy: Did RSS feed data appear in response?
  - API Error Rate: Percentage of failed API calls
  - Policy Adherence: Was RSS feed used as required?

- **Internet Search**
  - Accuracy: Did internet search results appear?
  - API Error Rate: Failed search calls
  - Policy Adherence: Was internet search used?

- **Twitter Search**
  - Accuracy: Did Twitter data appear?
  - API Error Rate: Failed Twitter calls
  - Policy Adherence: Was Twitter searched?

- **Reddit Search**
  - Accuracy: Did Reddit data appear?
  - API Error Rate: Failed Reddit calls
  - Policy Adherence: Was Reddit searched?

- **Sentiment Analysis**
  - Accuracy: Quality of sentiment analysis
  - Policy Adherence: Were sentiment labels provided?

- **Recommendation Generation**
  - Accuracy: Quality of recommendation
  - Policy Adherence: Was recommendation provided?

### 2. End-to-End Evaluations

- **Final Response Correctness (0-1)**
  - Does response address the prompt?
  - Are required sections present?
  - Is token mentioned correctly?

- **Tone Score (0-1)**
  - Professional language
  - Appropriate for financial analysis
  - Clear and concise

- **Satisfaction Score (0-1)**
  - Completeness + Coherence average

- **Completeness Score (0-1)**
  - All required sections present
  - All sources mentioned

- **Coherence Score (0-1)**
  - Logical flow
  - No contradictions
  - Well-structured

- **Recommendation Quality (0-1)**
  - Recommendation present
  - Confidence level provided
  - Rationale included
  - Risk factors mentioned

### 3. Pattern Detection

- **Hallucinations**
  - Unsupported claims
  - Fabricated sources
  - Inconsistent data

- **Tone Mismatch**
  - Casual language in professional context
  - Overly technical language
  - Inappropriate tone

- **User Confusion Indicators**
  - Vague statements
  - Contradictory information
  - Missing context

- **Missing Information**
  - Required sections missing
  - Sources not mentioned
  - Incomplete analysis

- **Contradictory Statements**
  - Bullish and bearish in close proximity
  - Conflicting recommendations
  - Inconsistent sentiment

## Evaluation Methods

### Automated Evaluation

Uses rule-based heuristics to evaluate:
- Component success/failure
- API error rates
- Pattern detection
- Completeness checks

**Pros:**
- Fast and consistent
- No API costs
- Reproducible

**Cons:**
- May miss nuanced issues
- Limited understanding of context

### LLM-as-Judge

Uses GPT-4o to evaluate response quality.

**Pros:**
- Understands context
- Can identify subtle issues
- Provides detailed feedback

**Cons:**
- Requires API access
- May have bias
- Slower than automated

### Rubric-Based Evaluation

Uses detailed rubric with weighted criteria.

**Pros:**
- Transparent scoring
- Consistent evaluation
- Easy to adjust weights

**Cons:**
- Requires manual rubric definition
- May not capture all nuances

### Human Reviewer

Manual evaluation by human experts.

**Pros:**
- Best understanding of quality
- Can identify subtle issues
- Domain expertise

**Cons:**
- Time-consuming
- Subjective
- Not scalable

## Scoring

### Overall Score Calculation

```
Overall Score = (Component Average × 0.4) + (End-to-End Average × 0.6)
```

### Component Average

```
Component Score = (Accuracy × 0.4) + (Policy Adherence × 0.4) + ((1 - Error Rate) × 0.2)
```

### End-to-End Average

```
End-to-End Score = (Correctness × 0.3) + (Tone × 0.2) + (Satisfaction × 0.2) + 
                   (Completeness × 0.15) + (Coherence × 0.15)
```

## Output Format

### Evaluation Report

The framework generates a comprehensive markdown report including:

1. **Overall Score**
2. **Component Evaluations** - Individual scores for each component
3. **End-to-End Evaluation** - User experience metrics
4. **Pattern Detection** - Issues found
5. **Recommendations** - Suggestions for improvement

### JSON Output

Structured JSON with all scores and metadata for programmatic analysis.

## Example Output

```
# Evaluation Report
**Overall Score:** 78.5%

## Component-Based Evaluations

### Rss Feed Fetch
- **Accuracy:** 100.00%
- **API Error Rate:** 0.00%
- **Policy Adherence:** 100.00%
- **Success:** ✓

### Internet Search
- **Accuracy:** 100.00%
- **API Error Rate:** 20.00%
- **Policy Adherence:** 100.00%
- **Success:** ✓

## Pattern Detection

- **Hallucinations Detected:** 0
- **Tone Mismatch:** No
- **User Confusion Indicators:** 1
- **Missing Information:** 0
- **Contradictions:** 0
```

## Customization

### Adjusting Weights

Edit `evaluation_framework.py` to adjust scoring weights:

```python
# Component scoring weights
component_score = (
    eval.accuracy_score * 0.4 +
    eval.policy_adherence * 0.4 +
    (1 - eval.api_error_rate) * 0.2
)

# End-to-end scoring weights
end_to_end_score = (
    correctness * 0.3 +
    tone * 0.2 +
    satisfaction * 0.2 +
    completeness * 0.15 +
    coherence * 0.15
)
```

### Adding New Criteria

Extend the rubric in `llm_judge.py`:

```python
def _create_rubric(self) -> Dict[str, Dict[str, Any]]:
    return {
        "new_category": {
            "weight": 0.1,
            "criteria": {
                "new_criterion": {"weight": 1.0, "max_score": 1.0}
            }
        }
    }
```

## Best Practices

1. **Run Multiple Evaluations** - Use automated + LLM judge + rubric for comprehensive view
2. **Track Over Time** - Compare scores across multiple runs
3. **Focus on Patterns** - Look for recurring issues in pattern detection
4. **Iterate on Prompts** - Use evaluation feedback to improve prompts
5. **Monitor Error Rates** - Track API error rates to identify infrastructure issues

## Troubleshooting

### LLM Judge Fails

- Check API key is set
- Verify model is available
- Check response format (may need to adjust JSON parsing)

### Execution Log Parsing Issues

- Ensure log file is accessible
- Check log format matches expected structure
- May need to adjust parsing logic for different log formats

### Low Scores

- Review pattern detection for specific issues
- Check component evaluations for failed steps
- Use LLM judge feedback for detailed suggestions

