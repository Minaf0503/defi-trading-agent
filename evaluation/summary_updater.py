"""
Helper module to update evaluation summary files
"""

from pathlib import Path
from datetime import datetime
from typing import Dict, Any
import json


def append_to_sentiment_summary(result: Dict[str, Any], prompt: str, token: str = "Unknown"):
    """Append evaluation results to sentiment analyst summary"""
    summary_file = Path(__file__).parent / "results" / "sentiment_analyst_evaluation_summary.md"
    
    if not summary_file.exists():
        return  # Summary file doesn't exist yet
    
    # Read current summary
    content = summary_file.read_text()
    
    # Extract run number
    run_number = content.count("## Evaluation Run #") + 1
    
    # Get evaluation details - handle both dict and direct access
    auto_data = result.get("automated", {})
    if isinstance(auto_data, dict):
        eval_id = auto_data.get("evaluation_id", f"eval_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
        timestamp = auto_data.get("timestamp", datetime.now().isoformat())
        auto_score = auto_data.get("overall_score", 0)
        if isinstance(auto_score, float) and auto_score <= 1.0:
            auto_score = auto_score * 100
    else:
        eval_id = f"eval_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        timestamp = datetime.now().isoformat()
        auto_score = 0
    
    date = timestamp.split("T")[0] if "T" in timestamp else datetime.now().strftime("%Y-%m-%d")
    
    rubric_data = result.get("rubric", {})
    if isinstance(rubric_data, dict):
        rubric_score = rubric_data.get("overall_score", 0)
        if isinstance(rubric_score, float) and rubric_score <= 1.0:
            rubric_score = rubric_score * 100
    else:
        rubric_score = 0
    
    avg_score = (auto_score + rubric_score) / 2
    
    # Build new evaluation entry
    entry = f"""
## Evaluation Run #{run_number} - {token} Sentiment Analysis

**Date:** {date}  
**Evaluation ID:** {eval_id}  
**Token Analyzed:** {token}  
**Prompt:** {prompt[:100]}...

### Overall Scores

- **Automated Overall Score:** {auto_score:.2f}%
- **Rubric Overall Score:** {rubric_score:.2f}%
- **Average Score:** {avg_score:.2f}%

### Component-Based Evaluations

| Component | Accuracy | API Error Rate | Policy Adherence | Success |
|-----------|----------|----------------|------------------|---------|
"""
    
    # Add component evaluations
    comp_evals = auto_data.get("component_evals", []) if isinstance(auto_data, dict) else []
    for comp in comp_evals:
        name = comp.get("component_name", "").replace("_", " ").title()
        accuracy = comp.get("accuracy_score", 0)
        if isinstance(accuracy, float) and accuracy <= 1.0:
            accuracy = accuracy * 100
        error_rate = comp.get("api_error_rate", 0)
        if isinstance(error_rate, float) and error_rate <= 1.0:
            error_rate = error_rate * 100
        policy = comp.get("policy_adherence", 0)
        if isinstance(policy, float) and policy <= 1.0:
            policy = policy * 100
        success = "✓" if comp.get("success", False) else "✗"
        entry += f"| {name} | {accuracy:.2f}% | {error_rate:.2f}% | {policy:.2f}% | {success} |\n"
    
    # Add end-to-end evaluation
    comp_avg = auto_data.get("component_avg_score", 0) if isinstance(auto_data, dict) else 0
    if isinstance(comp_avg, float) and comp_avg <= 1.0:
        comp_avg = comp_avg * 100
    end_to_end = auto_data.get("end_to_end_avg_score", 0) if isinstance(auto_data, dict) else 0
    if isinstance(end_to_end, float) and end_to_end <= 1.0:
        end_to_end = end_to_end * 100
    
    # Get pattern data
    patterns = auto_data.get("patterns", {}) if isinstance(auto_data, dict) else {}
    
    entry += f"""
**Component Average Score:** {comp_avg:.2f}%

### End-to-End Evaluation

| Metric | Score |
|--------|-------|
| End-to-End Average | {end_to_end:.2f}% |

**Note:** Detailed end-to-end metrics are available in the full evaluation report.

### Pattern Detection

- **Hallucinations Detected:** {patterns.get("hallucination_count", 0)}
- **Tone Mismatch:** {'Yes' if patterns.get("tone_mismatch_detected", False) else 'No'}
- **User Confusion Indicators:** {len(patterns.get("user_confusion_indicators", []))}
- **Missing Information:** {len(patterns.get("missing_information", []))}
- **Contradictions:** {len(patterns.get("contradictory_statements", []))}

### Rubric-Based Evaluation

| Category | Score | Weight |
|----------|-------|--------|
"""
    
    # Add rubric scores
    rubric_categories = rubric_data.get("category_scores", {}) if isinstance(rubric_data, dict) else {}
    for category, data in rubric_categories.items():
        score = data.get("score", 0) if isinstance(data, dict) else 0
        if isinstance(score, float) and score <= 1.0:
            score = score * 100
        weight = data.get("weight", 0) if isinstance(data, dict) else 0
        if isinstance(weight, float) and weight <= 1.0:
            weight = weight * 100
        entry += f"| {category.replace('_', ' ').title()} | {score:.2f}% | {weight:.0f}% |\n"
    
    entry += f"""
**Overall Rubric Score:** {rubric_score:.2f}%

---

"""
    
    # Insert before "## Evaluation History"
    if "## Evaluation History" in content:
        parts = content.split("## Evaluation History")
        new_content = parts[0] + entry + "## Evaluation History" + parts[1]
    else:
        # Append at the end before last updated
        if "*Last Updated:" in content:
            parts = content.split("*Last Updated:")
            new_content = parts[0] + entry + "*Last Updated:" + parts[1]
        else:
            new_content = content + entry
    
    # Update last updated timestamp
    new_content = new_content.replace(
        "*Last Updated: 2026-01-06",
        f"*Last Updated: {datetime.now().strftime('%Y-%m-%d')}"
    )
    
    summary_file.write_text(new_content)


def append_to_onchain_summary(result: Dict[str, Any], prompt: str, token: str = "Unknown", network: str = "Unknown"):
    """Append evaluation results to onchain analyst summary"""
    summary_file = Path(__file__).parent / "results" / "onchain_analyst_evaluation_summary.md"
    
    if not summary_file.exists():
        return  # Summary file doesn't exist yet
    
    # Read current summary
    content = summary_file.read_text()
    
    # Extract run number
    run_number = content.count("## Evaluation Run #") + 1
    
    # Get evaluation details - handle both dict and direct access
    auto_data = result.get("automated", {})
    if isinstance(auto_data, dict):
        eval_id = auto_data.get("evaluation_id", f"eval_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
        timestamp = auto_data.get("timestamp", datetime.now().isoformat())
        auto_score = auto_data.get("overall_score", 0)
        if isinstance(auto_score, float) and auto_score <= 1.0:
            auto_score = auto_score * 100
    else:
        eval_id = f"eval_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        timestamp = datetime.now().isoformat()
        auto_score = 0
    
    date = timestamp.split("T")[0] if "T" in timestamp else datetime.now().strftime("%Y-%m-%d")
    
    # Build new evaluation entry
    entry = f"""
## Evaluation Run #{run_number} - {token} Onchain Analysis

**Date:** {date}  
**Evaluation ID:** {eval_id}  
**Token Analyzed:** {token}  
**Network:** {network}  
**Prompt:** {prompt[:100]}...

### Overall Scores

- **Automated Overall Score:** {auto_score:.2f}%

### Component-Based Evaluations

| Component | Accuracy | API Error Rate | Policy Adherence | Success |
|-----------|----------|----------------|------------------|---------|
"""
    
    # Add component evaluations
    comp_evals = auto_data.get("component_evals", []) if isinstance(auto_data, dict) else []
    for comp in comp_evals:
        name = comp.get("component_name", "").replace("_", " ").title()
        accuracy = comp.get("accuracy_score", 0)
        if isinstance(accuracy, float) and accuracy <= 1.0:
            accuracy = accuracy * 100
        error_rate = comp.get("api_error_rate", 0)
        if isinstance(error_rate, float) and error_rate <= 1.0:
            error_rate = error_rate * 100
        policy = comp.get("policy_adherence", 0)
        if isinstance(policy, float) and policy <= 1.0:
            policy = policy * 100
        success = "✓" if comp.get("success", False) else "✗"
        entry += f"| {name} | {accuracy:.2f}% | {error_rate:.2f}% | {policy:.2f}% | {success} |\n"
    
    # Add end-to-end evaluation
    comp_avg = auto_data.get("component_avg_score", 0) if isinstance(auto_data, dict) else 0
    if isinstance(comp_avg, float) and comp_avg <= 1.0:
        comp_avg = comp_avg * 100
    end_to_end = auto_data.get("end_to_end_avg_score", 0) if isinstance(auto_data, dict) else 0
    if isinstance(end_to_end, float) and end_to_end <= 1.0:
        end_to_end = end_to_end * 100
    
    # Get pattern data
    patterns = auto_data.get("patterns", {}) if isinstance(auto_data, dict) else {}
    
    entry += f"""
**Component Average Score:** {comp_avg:.2f}%

### End-to-End Evaluation

| Metric | Score |
|--------|-------|
| End-to-End Average | {end_to_end:.2f}% |

**Note:** Detailed end-to-end metrics are available in the full evaluation report.

### Pattern Detection

- **Hallucinations Detected:** {patterns.get("hallucination_count", 0)}
- **Tone Mismatch:** {'Yes' if patterns.get("tone_mismatch_detected", False) else 'No'}
- **User Confusion Indicators:** {len(patterns.get("user_confusion_indicators", []))}
- **Missing Information:** {len(patterns.get("missing_information", []))}
- **Contradictions:** {len(patterns.get("contradictory_statements", []))}

---

"""
    
    # Insert before "## Evaluation History"
    if "## Evaluation History" in content:
        parts = content.split("## Evaluation History")
        new_content = parts[0] + entry + "## Evaluation History" + parts[1]
    else:
        # Append at the end before last updated
        if "*Last Updated:" in content:
            parts = content.split("*Last Updated:")
            new_content = parts[0] + entry + "*Last Updated:" + parts[1]
        else:
            new_content = content + entry
    
    # Update last updated timestamp
    new_content = new_content.replace(
        "*Last Updated: 2026-01-06",
        f"*Last Updated: {datetime.now().strftime('%Y-%m-%d')}"
    )
    
    summary_file.write_text(new_content)
