"""
Run comprehensive evaluation on agent output

Usage:
    python evaluation/run_evaluation.py --prompt-file output/prompt.txt --response-file output/response.txt --log-file output/execution_log.json
"""

import json
import argparse
from pathlib import Path
from typing import Dict, Any
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from evaluation.evaluation_framework import SentimentNewsAnalystEvaluator
from evaluation.llm_judge import LLMJudge, RubricBasedEvaluator


def load_files(prompt_file: str, response_file: str, log_file: str) -> tuple:
    """Load prompt, response, and execution log files"""
    prompt = Path(prompt_file).read_text()
    response = Path(response_file).read_text()
    
    # Try to load JSON log, fallback to text
    try:
        log = json.loads(Path(log_file).read_text())
    except (json.JSONDecodeError, FileNotFoundError):
        # If it's a markdown file, create a simple structure
        log_text = Path(log_file).read_text() if Path(log_file).exists() else "{}"
        log = {"raw_log": log_text, "Timings": []}
    
    return prompt, response, log


def run_evaluation(prompt: str, response: str, execution_log: Dict[str, Any], 
                   use_llm_judge: bool = False, use_rubric: bool = True) -> Dict[str, Any]:
    """Run comprehensive evaluation"""
    
    results = {}
    
    # Automated evaluation
    print("Running automated evaluation...")
    evaluator = SentimentNewsAnalystEvaluator()
    auto_result = evaluator.evaluate(prompt, response, execution_log)
    results["automated"] = auto_result
    
    # LLM Judge evaluation (optional)
    if use_llm_judge:
        print("Running LLM judge evaluation...")
        try:
            llm_judge = LLMJudge()
            llm_result = llm_judge.evaluate(prompt, response)
            results["llm_judge"] = llm_result
        except Exception as e:
            print(f"LLM judge evaluation failed: {e}")
            results["llm_judge"] = None
    
    # Rubric-based evaluation
    if use_rubric:
        print("Running rubric-based evaluation...")
        rubric_evaluator = RubricBasedEvaluator()
        rubric_result = rubric_evaluator.evaluate(prompt, response, execution_log)
        results["rubric"] = rubric_result
    
    return results


def generate_comprehensive_report(results: Dict[str, Any]) -> str:
    """Generate comprehensive evaluation report"""
    
    report = "# Comprehensive Evaluation Report\n\n"
    
    # Automated evaluation
    if "automated" in results:
        auto_result = results["automated"]
        evaluator = SentimentNewsAnalystEvaluator()
        report += evaluator.generate_report(auto_result)
        report += "\n\n"
    
    # LLM Judge
    if "llm_judge" in results and results["llm_judge"]:
        llm_result = results["llm_judge"]
        report += "## LLM Judge Evaluation\n\n"
        report += f"**Overall Score:** {llm_result.overall_score:.2%}\n\n"
        report += f"- **Correctness:** {llm_result.correctness_score:.2%}\n"
        report += f"- **Tone:** {llm_result.tone_score:.2%}\n"
        report += f"- **Completeness:** {llm_result.completeness_score:.2%}\n"
        report += f"- **Recommendation Quality:** {llm_result.recommendation_quality:.2%}\n\n"
        report += f"**Feedback:**\n{llm_result.feedback}\n\n"
        
        if llm_result.strengths:
            report += "**Strengths:**\n"
            for strength in llm_result.strengths:
                report += f"- {strength}\n"
            report += "\n"
        
        if llm_result.weaknesses:
            report += "**Weaknesses:**\n"
            for weakness in llm_result.weaknesses:
                report += f"- {weakness}\n"
            report += "\n"
        
        if llm_result.suggestions:
            report += "**Suggestions:**\n"
            for suggestion in llm_result.suggestions:
                report += f"- {suggestion}\n"
            report += "\n"
    
    # Rubric evaluation
    if "rubric" in results:
        rubric_result = results["rubric"]
        report += "## Rubric-Based Evaluation\n\n"
        report += f"**Overall Score:** {rubric_result['overall_score']:.2%}\n\n"
        
        report += "**Category Scores:**\n"
        for category, data in rubric_result["category_scores"].items():
            report += f"- **{category.replace('_', ' ').title()}:** {data['score']:.2%} (weight: {data['weight']:.0%})\n"
        report += "\n"
    
    # Summary
    report += "## Summary\n\n"
    
    scores = []
    if "automated" in results:
        scores.append(("Automated", results["automated"].overall_score))
    if "llm_judge" in results and results["llm_judge"]:
        scores.append(("LLM Judge", results["llm_judge"].overall_score))
    if "rubric" in results:
        scores.append(("Rubric", results["rubric"]["overall_score"]))
    
    if scores:
        avg_score = sum(score for _, score in scores) / len(scores)
        report += f"**Average Score Across All Evaluators:** {avg_score:.2%}\n\n"
        
        report += "**Individual Scores:**\n"
        for name, score in scores:
            report += f"- {name}: {score:.2%}\n"
    
    return report


def main():
    parser = argparse.ArgumentParser(description="Evaluate sentiment news analyst output")
    parser.add_argument("--prompt-file", required=True, help="Path to prompt file")
    parser.add_argument("--response-file", required=True, help="Path to response file")
    parser.add_argument("--log-file", required=True, help="Path to execution log file")
    parser.add_argument("--output-file", help="Path to output report file")
    parser.add_argument("--use-llm-judge", action="store_true", help="Use LLM judge evaluation")
    parser.add_argument("--use-rubric", action="store_true", default=True, help="Use rubric-based evaluation")
    
    args = parser.parse_args()
    
    # Load files
    print(f"Loading files...")
    prompt, response, execution_log = load_files(
        args.prompt_file,
        args.response_file,
        args.log_file
    )
    
    # Run evaluation
    results = run_evaluation(
        prompt,
        response,
        execution_log,
        use_llm_judge=args.use_llm_judge,
        use_rubric=args.use_rubric
    )
    
    # Generate report
    report = generate_comprehensive_report(results)
    
    # Output
    if args.output_file:
        Path(args.output_file).write_text(report)
        print(f"\nReport saved to: {args.output_file}")
    else:
        print("\n" + "="*80)
        print(report)
        print("="*80)
    
    # Save JSON results
    json_output = args.output_file.replace(".md", ".json") if args.output_file else "evaluation_results.json"
    
    # Convert results to JSON-serializable format
    json_results = {}
    if "automated" in results:
        auto_result = results["automated"]
        json_results["automated"] = {
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
                "missing_information": auto_result.patterns.missing_information
            }
        }
    
    if "llm_judge" in results and results["llm_judge"]:
        llm_result = results["llm_judge"]
        json_results["llm_judge"] = {
            "overall_score": llm_result.overall_score,
            "correctness_score": llm_result.correctness_score,
            "tone_score": llm_result.tone_score,
            "completeness_score": llm_result.completeness_score,
            "recommendation_quality": llm_result.recommendation_quality,
            "strengths": llm_result.strengths,
            "weaknesses": llm_result.weaknesses,
            "suggestions": llm_result.suggestions
        }
    
    if "rubric" in results:
        json_results["rubric"] = results["rubric"]
    
    Path(json_output).write_text(json.dumps(json_results, indent=2))
    print(f"JSON results saved to: {json_output}")


if __name__ == "__main__":
    main()

