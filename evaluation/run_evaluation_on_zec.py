"""
Run evaluation on the ZEC example

This script demonstrates how to evaluate the ZEC sentiment analysis example.
"""

import json
import sys
import os
from pathlib import Path

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from evaluation.evaluation_framework import SentimentNewsAnalystEvaluator
from evaluation.llm_judge import LLMJudge, RubricBasedEvaluator
from evaluation.summary_updater import append_to_sentiment_summary


def load_zec_example():
    """Load the ZEC example files"""
    base_dir = Path(__file__).parent.parent / "output"
    
    # Load prompt
    prompt_file = base_dir / "Analyze the market sentiment for ZEC (Zcash) over .txt"
    prompt = prompt_file.read_text().split("Response:")[0].split("[01/07/2026")[1].split("]")[1].strip()
    
    # Load response
    response_file = base_dir / "Analyze the market sentiment for ZEC (Zcash) over .txt"
    response = response_file.read_text().split("Response:")[1].strip()
    
    # Load execution log (simplified structure)
    log_file = base_dir / "Execution Log.md"
    log_text = log_file.read_text()
    
    # Create simplified log structure
    execution_log = {
        "raw_log": log_text,
        "Timings": [],
        "tool_calls": []
    }
    
    # Extract tool calls from log
    if "Tool Call:" in log_text:
        # Simple extraction - in practice, you'd parse more carefully
        execution_log["has_tool_calls"] = True
        execution_log["tool_call_count"] = log_text.count("Tool Call:")
    
    # Extract errors
    errors = []
    if "Failed to download" in log_text:
        error_lines = [line for line in log_text.split("\n") if "Failed" in line]
        errors.extend(error_lines[:10])  # Limit to first 10
    
    execution_log["errors"] = errors
    
    return prompt, response, execution_log


def main():
    print("=" * 80)
    print("Evaluating ZEC Sentiment Analysis Example")
    print("=" * 80)
    print()
    
    # Load data
    print("Loading ZEC example data...")
    prompt, response, execution_log = load_zec_example()
    
    print(f"Prompt length: {len(prompt)} characters")
    print(f"Response length: {len(response)} characters")
    print(f"Execution log length: {len(execution_log.get('raw_log', ''))} characters")
    print()
    
    # Run automated evaluation
    print("Running automated evaluation...")
    evaluator = SentimentNewsAnalystEvaluator()
    auto_result = evaluator.evaluate(prompt, response, execution_log)
    
    # Generate report
    report = evaluator.generate_report(auto_result)
    
    # Save report
    output_dir = Path(__file__).parent / "results"
    output_dir.mkdir(exist_ok=True)
    
    report_file = output_dir / "zec_evaluation_report.md"
    report_file.write_text(report)
    
    print("=" * 80)
    print(report)
    print("=" * 80)
    print()
    print(f"Report saved to: {report_file}")
    
    # Run rubric evaluation
    print("\nRunning rubric-based evaluation...")
    rubric_evaluator = RubricBasedEvaluator()
    rubric_result = rubric_evaluator.evaluate(prompt, response, execution_log)
    
    print("\nRubric Results:")
    print(f"Overall Score: {rubric_result['overall_score']:.2%}")
    print("\nCategory Scores:")
    for category, data in rubric_result["category_scores"].items():
        print(f"  {category.replace('_', ' ').title()}: {data['score']:.2%} (weight: {data['weight']:.0%})")
    
    # Save JSON results
    json_results = {
        "automated": {
            "overall_score": auto_result.overall_score,
            "component_avg_score": auto_result.component_avg_score,
            "end_to_end_avg_score": auto_result.end_to_end_avg_score,
            "component_evals": [
                {
                    "component_name": ce.component_name,
                    "accuracy_score": ce.accuracy_score,
                    "api_error_rate": ce.api_error_rate,
                    "policy_adherence": ce.policy_adherence,
                    "success": ce.success
                }
                for ce in auto_result.component_evals
            ],
            "patterns": {
                "hallucination_count": auto_result.patterns.hallucination_count,
                "tone_mismatch_detected": auto_result.patterns.tone_mismatch_detected,
                "user_confusion_indicators": auto_result.patterns.user_confusion_indicators,
                "missing_information": auto_result.patterns.missing_information,
                "contradictory_statements": auto_result.patterns.contradictory_statements
            }
        },
        "rubric": rubric_result
    }
    
    json_file = output_dir / "zec_evaluation_results.json"
    json_file.write_text(json.dumps(json_results, indent=2))
    print(f"\nJSON results saved to: {json_file}")
    
    # Update summary file
    try:
        # Extract token from prompt
        token = "ZEC" if "ZEC" in prompt or "Zcash" in prompt else "Unknown"
        append_to_sentiment_summary(json_results, prompt, token)
        print(f"Summary updated: {output_dir / 'sentiment_analyst_evaluation_summary.md'}")
    except Exception as e:
        print(f"Warning: Could not update summary file: {e}")
    
    # Summary
    print("\n" + "=" * 80)
    print("EVALUATION SUMMARY")
    print("=" * 80)
    print(f"Automated Overall Score: {auto_result.overall_score:.2%}")
    print(f"Rubric Overall Score: {rubric_result['overall_score']:.2%}")
    print(f"Average Score: {(auto_result.overall_score + rubric_result['overall_score']) / 2:.2%}")
    print()
    print("Key Findings:")
    print(f"- Hallucinations: {auto_result.patterns.hallucination_count}")
    print(f"- Tone Mismatch: {'Yes' if auto_result.patterns.tone_mismatch_detected else 'No'}")
    print(f"- Missing Information: {len(auto_result.patterns.missing_information)} items")
    print(f"- Contradictions: {len(auto_result.patterns.contradictory_statements)}")
    print("=" * 80)


if __name__ == "__main__":
    main()

