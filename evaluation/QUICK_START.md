# Evaluation Framework - Quick Start Guide

## Run Evaluation on Your Output

### Step 1: Prepare Your Files

You need three files:
1. **Prompt file** - The user's input prompt
2. **Response file** - The agent's response
3. **Execution log** - The execution log (JSON or markdown)

### Step 2: Run Evaluation

```bash
python evaluation/run_evaluation.py \
    --prompt-file output/prompt.txt \
    --response-file output/response.txt \
    --log-file output/execution_log.json \
    --output-file evaluation_report.md
```

### Step 3: Review Results

The evaluation will generate:
- **Markdown report** - Human-readable evaluation report
- **JSON results** - Machine-readable scores and metrics

## Quick Example: Evaluate ZEC Output

```bash
python evaluation/run_evaluation_on_zec.py
```

This evaluates the ZEC example and shows:
- Component scores
- End-to-end scores
- Pattern detection results
- Overall assessment

## Understanding Scores

### Overall Score
- **0.9 - 1.0**: Excellent - Production ready
- **0.8 - 0.9**: Good - Minor improvements needed
- **0.7 - 0.8**: Acceptable - Some improvements needed
- **0.6 - 0.7**: Needs Work - Significant improvements needed
- **< 0.6**: Poor - Major overhaul required

### Component Scores
Each component is scored on:
- **Accuracy** (40% weight): Did it work correctly?
- **Policy Adherence** (40% weight): Was it used as required?
- **Error Rate** (20% weight): How many errors occurred?

### End-to-End Scores
- **Correctness**: Does response address prompt?
- **Tone**: Is it professional?
- **Satisfaction**: Completeness + Coherence
- **Recommendation Quality**: Is recommendation good?

## Key Metrics to Watch

1. **API Error Rate** - Should be < 20%
2. **Policy Adherence** - Should be 100% for all components
3. **Hallucination Count** - Should be 0
4. **Missing Information** - Should be 0
5. **Contradictions** - Should be 0

## Common Issues and Fixes

### Low Component Scores
**Issue:** Components not being used
**Fix:** Check agent instructions, ensure tools are available

### High Error Rate
**Issue:** API calls failing
**Fix:** Check API keys, rate limits, network connectivity

### Low Coherence Score
**Issue:** Contradictions or poor structure
**Fix:** Improve prompt instructions, add structure requirements

### Missing Information
**Issue:** Required sections not present
**Fix:** Update prompt to explicitly require all sections

## Next Steps

1. **Review Report** - Read the evaluation report
2. **Identify Issues** - Check pattern detection section
3. **Improve Prompt** - Update based on feedback
4. **Re-evaluate** - Run evaluation again
5. **Track Progress** - Compare scores over time

## Files Generated

After running evaluation, you'll get:
- `evaluation_report.md` - Full evaluation report
- `evaluation_results.json` - JSON scores and metrics
- `results/zec_evaluation_report.md` - ZEC-specific report (if using ZEC example)

## Using LLM Judge (Optional)

For more detailed evaluation, use LLM judge:

```bash
python evaluation/run_evaluation.py \
    --prompt-file output/prompt.txt \
    --response-file output/response.txt \
    --log-file output/execution_log.json \
    --output-file evaluation_report.md \
    --use-llm-judge
```

**Note:** Requires OpenAI API key and incurs API costs.

## Human Review (Optional)

For gold standard evaluation, use the human reviewer template:

1. Open `evaluation/human_reviewer_template.md`
2. Fill out the evaluation form
3. Compare with automated results
4. Use insights to improve the agent

## Integration

### Python API

```python
from evaluation.evaluation_framework import SentimentNewsAnalystEvaluator

evaluator = SentimentNewsAnalystEvaluator()
result = evaluator.evaluate(prompt, response, execution_log)
print(f"Overall Score: {result.overall_score:.2%}")
```

### CI/CD Integration

Add to your CI/CD pipeline:

```yaml
- name: Run Evaluation
  run: |
    python evaluation/run_evaluation.py \
      --prompt-file output/prompt.txt \
      --response-file output/response.txt \
      --log-file output/execution_log.json \
      --output-file evaluation_report.md
```

## Tips

1. **Run regularly** - Evaluate after each prompt change
2. **Track trends** - Compare scores over time
3. **Focus on patterns** - Address recurring issues
4. **Use multiple methods** - Combine automated + LLM judge + human review
5. **Set benchmarks** - Define target scores for production

## Support

For questions or issues:
1. Check `evaluation/README.md` for detailed documentation
2. Review `evaluation/EVALUATION_FRAMEWORK_SUMMARY.md` for framework details
3. Examine example evaluations in `evaluation/results/`

