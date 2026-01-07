"""
Onchain Analyst Evaluator

Evaluates onchain analyst outputs with component-based and end-to-end metrics.
"""

import json
import re
from typing import Dict, List, Optional, Any
from datetime import datetime
from dataclasses import dataclass

from evaluation.evaluation_framework import (
    ComponentEvaluation,
    EndToEndEvaluation,
    PatternDetection,
    EvaluationResult
)


class OnchainAnalystEvaluator:
    """Comprehensive evaluator for Onchain Analyst"""
    
    def __init__(self):
        self.required_components = [
            "liquidity_data_fetch",
            "holder_data_fetch",
            "transaction_data_fetch",
            "supply_data_fetch",
            "mempool_analysis",
            "recommendation_generation"
        ]
        
        self.required_output_sections = [
            "Onchain Data Summary",
            "Key Onchain Signals",
            "Holder Behavior Analysis",
            "Liquidity Analysis",
            "Trading Recommendation",
            "Summary Table"
        ]
    
    def evaluate(self, prompt: str, response: str, execution_log: Dict[str, Any]) -> EvaluationResult:
        """Run complete evaluation"""
        
        # Component-based evaluations
        component_evals = self._evaluate_components(execution_log, response)
        
        # End-to-end evaluation
        end_to_end_eval = self._evaluate_end_to_end(prompt, response, execution_log)
        
        # Pattern detection
        patterns = self._detect_patterns(response, execution_log)
        
        # Calculate overall scores
        component_avg = self._calculate_component_average(component_evals)
        end_to_end_avg = self._calculate_end_to_end_average(end_to_end_eval)
        overall_score = (component_avg * 0.4) + (end_to_end_avg * 0.6)
        
        return EvaluationResult(
            evaluation_id=f"eval_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            timestamp=datetime.now().isoformat(),
            prompt=prompt,
            response=response,
            execution_log=execution_log,
            component_evals=component_evals,
            end_to_end_eval=end_to_end_eval,
            patterns=patterns,
            overall_score=overall_score,
            component_avg_score=component_avg,
            end_to_end_avg_score=end_to_end_avg,
            evaluator_type="automated",
            notes=""
        )
    
    def _evaluate_components(self, execution_log: Dict, response: str) -> List[ComponentEvaluation]:
        """Evaluate each component separately"""
        evals = []
        
        # Extract tool calls from execution log
        tool_calls = self._extract_tool_calls(execution_log)
        
        # Evaluate liquidity data fetch
        liquidity_eval = self._evaluate_liquidity_data(tool_calls, response)
        evals.append(liquidity_eval)
        
        # Evaluate holder data fetch
        holder_eval = self._evaluate_holder_data(tool_calls, response)
        evals.append(holder_eval)
        
        # Evaluate transaction data fetch
        transaction_eval = self._evaluate_transaction_data(tool_calls, response)
        evals.append(transaction_eval)
        
        # Evaluate supply data fetch
        supply_eval = self._evaluate_supply_data(tool_calls, response)
        evals.append(supply_eval)
        
        # Evaluate mempool analysis
        mempool_eval = self._evaluate_mempool_analysis(tool_calls, response)
        evals.append(mempool_eval)
        
        # Evaluate recommendation generation
        recommendation_eval = self._evaluate_recommendation(response)
        evals.append(recommendation_eval)
        
        return evals
    
    def _extract_tool_calls(self, execution_log: Dict) -> List[Dict]:
        """Extract tool calls from execution log"""
        tool_calls = []
        raw_log = execution_log.get("raw_log", "")
        
        # Extract InternetSearch calls
        if "InternetSearch" in raw_log:
            # Count tool calls
            search_calls = raw_log.count("## Tool Call: InternetSearch")
            for i in range(search_calls):
                tool_calls.append({"type": "InternetSearch", "index": i})
        
        return tool_calls
    
    def _evaluate_liquidity_data(self, tool_calls: List[Dict], response: str) -> ComponentEvaluation:
        """Evaluate liquidity data fetching component"""
        # Check if liquidity-related searches were made
        liquidity_calls = [tc for tc in tool_calls if "liquidity" in str(tc).lower()]
        
        # Check for errors
        errors = self._extract_errors("liquidity")
        error_rate = len(errors) / max(len(liquidity_calls), 1) if liquidity_calls else 0.0
        
        # Check if liquidity data appears in response
        liquidity_mentioned = (
            "liquidity" in response.lower() or 
            "pool" in response.lower() or
            "DEX" in response or
            "shielded supply" in response.lower()
        )
        accuracy = 1.0 if liquidity_mentioned else 0.5
        
        # Policy adherence: Should gather liquidity data
        policy_adherence = 1.0 if liquidity_mentioned else 0.0
        
        return ComponentEvaluation(
            component_name="liquidity_data_fetch",
            accuracy_score=accuracy,
            api_error_rate=min(error_rate, 1.0),
            policy_adherence=policy_adherence,
            error_messages=errors,
            success=liquidity_mentioned and error_rate < 0.5
        )
    
    def _evaluate_holder_data(self, tool_calls: List[Dict], response: str) -> ComponentEvaluation:
        """Evaluate holder data fetching component"""
        holder_calls = [tc for tc in tool_calls if "holder" in str(tc).lower() or "whale" in str(tc).lower()]
        
        errors = self._extract_errors("holder")
        error_rate = len(errors) / max(len(holder_calls), 1) if holder_calls else 0.0
        
        # Check if holder data appears in response
        holder_mentioned = (
            "holder" in response.lower() or 
            "whale" in response.lower() or
            "wallet" in response.lower() or
            "accumulation" in response.lower()
        )
        accuracy = 1.0 if holder_mentioned else 0.5
        
        policy_adherence = 1.0 if holder_mentioned else 0.0
        
        return ComponentEvaluation(
            component_name="holder_data_fetch",
            accuracy_score=accuracy,
            api_error_rate=min(error_rate, 1.0),
            policy_adherence=policy_adherence,
            error_messages=errors,
            success=holder_mentioned and error_rate < 0.5
        )
    
    def _evaluate_transaction_data(self, tool_calls: List[Dict], response: str) -> ComponentEvaluation:
        """Evaluate transaction data fetching component"""
        transaction_calls = [tc for tc in tool_calls if "transaction" in str(tc).lower() or "network" in str(tc).lower()]
        
        errors = self._extract_errors("transaction")
        error_rate = len(errors) / max(len(transaction_calls), 1) if transaction_calls else 0.0
        
        # Check if transaction data appears in response
        transaction_mentioned = (
            "transaction" in response.lower() or 
            "volume" in response.lower() or
            "network activity" in response.lower() or
            "block" in response.lower()
        )
        accuracy = 1.0 if transaction_mentioned else 0.5
        
        policy_adherence = 1.0 if transaction_mentioned else 0.0
        
        return ComponentEvaluation(
            component_name="transaction_data_fetch",
            accuracy_score=accuracy,
            api_error_rate=min(error_rate, 1.0),
            policy_adherence=policy_adherence,
            error_messages=errors,
            success=transaction_mentioned and error_rate < 0.5
        )
    
    def _evaluate_supply_data(self, tool_calls: List[Dict], response: str) -> ComponentEvaluation:
        """Evaluate supply data fetching component"""
        supply_calls = [tc for tc in tool_calls if "supply" in str(tc).lower() or "distribution" in str(tc).lower()]
        
        errors = self._extract_errors("supply")
        error_rate = len(errors) / max(len(supply_calls), 1) if supply_calls else 0.0
        
        # Check if supply data appears in response
        supply_mentioned = (
            "supply" in response.lower() or 
            "circulating" in response.lower() or
            "total supply" in response.lower() or
            "distribution" in response.lower()
        )
        accuracy = 1.0 if supply_mentioned else 0.5
        
        policy_adherence = 1.0 if supply_mentioned else 0.0
        
        return ComponentEvaluation(
            component_name="supply_data_fetch",
            accuracy_score=accuracy,
            api_error_rate=min(error_rate, 1.0),
            policy_adherence=policy_adherence,
            error_messages=errors,
            success=supply_mentioned and error_rate < 0.5
        )
    
    def _evaluate_mempool_analysis(self, tool_calls: List[Dict], response: str) -> ComponentEvaluation:
        """Evaluate mempool analysis component"""
        mempool_calls = [tc for tc in tool_calls if "mempool" in str(tc).lower()]
        
        errors = self._extract_errors("mempool")
        error_rate = len(errors) / max(len(mempool_calls), 1) if mempool_calls else 0.0
        
        # Check if mempool data appears in response
        mempool_mentioned = "mempool" in response.lower() or "pending" in response.lower()
        accuracy = 1.0 if mempool_mentioned else 0.5
        
        policy_adherence = 1.0 if mempool_mentioned else 0.0
        
        return ComponentEvaluation(
            component_name="mempool_analysis",
            accuracy_score=accuracy,
            api_error_rate=min(error_rate, 1.0),
            policy_adherence=policy_adherence,
            error_messages=errors,
            success=mempool_mentioned and error_rate < 0.5
        )
    
    def _evaluate_recommendation(self, response: str) -> ComponentEvaluation:
        """Evaluate recommendation generation quality"""
        # Check for recommendation
        has_recommendation = bool(re.search(r'\b(BUY|HOLD|SELL)\b', response, re.IGNORECASE))
        
        # Check for confidence level
        has_confidence = bool(re.search(r'\b(high|medium|low)\s+confidence\b', response, re.IGNORECASE))
        
        # Check for rationale
        has_rationale = "rationale" in response.lower() or "reason" in response.lower() or "factors" in response.lower()
        
        accuracy = (has_recommendation + has_confidence + has_rationale) / 3.0
        
        policy_adherence = 1.0 if has_recommendation else 0.0
        
        return ComponentEvaluation(
            component_name="recommendation_generation",
            accuracy_score=accuracy,
            api_error_rate=0.0,
            policy_adherence=policy_adherence,
            error_messages=[],
            success=has_recommendation
        )
    
    def _extract_errors(self, component: str) -> List[str]:
        """Extract errors from execution log for a component"""
        # This would parse the execution log for errors
        # For now, return empty list
        return []
    
    def _evaluate_end_to_end(self, prompt: str, response: str, execution_log: Dict) -> EndToEndEvaluation:
        """Evaluate end-to-end metrics"""
        
        # Final response correctness
        correctness = self._evaluate_correctness(prompt, response)
        
        # Tone score
        tone = self._evaluate_tone(response)
        
        # Completeness
        completeness = self._evaluate_completeness(response)
        
        # Coherence
        coherence = self._evaluate_coherence(response)
        
        # Satisfaction (average of completeness and coherence)
        satisfaction = (completeness + coherence) / 2.0
        
        # Recommendation quality
        rec_quality = self._evaluate_recommendation_quality(response)
        
        return EndToEndEvaluation(
            final_response_correctness=correctness,
            tone_score=tone,
            satisfaction_score=satisfaction,
            completeness_score=completeness,
            coherence_score=coherence,
            recommendation_quality=rec_quality
        )
    
    def _evaluate_correctness(self, prompt: str, response: str) -> float:
        """Evaluate if response addresses the prompt correctly"""
        score = 0.0
        
        # Check for required sections
        required_sections = [
            "Onchain Data Summary",
            "Key Onchain Signals",
            "Holder Behavior Analysis",
            "Liquidity Analysis",
            "Trading Recommendation",
            "Summary Table"
        ]
        
        sections_found = sum(1 for section in required_sections if section in response)
        score += (sections_found / len(required_sections)) * 0.5
        
        # Check if token is mentioned
        if "ZEC" in response or "Zcash" in response:
            score += 0.3
        
        # Check if recommendation is present
        if re.search(r'\b(BUY|HOLD|SELL)\b', response, re.IGNORECASE):
            score += 0.2
        
        return min(score, 1.0)
    
    def _evaluate_tone(self, response: str) -> float:
        """Evaluate tone appropriateness"""
        # Base score
        score = 0.7
        
        # Check for professional language
        professional_indicators = [
            "analysis", "metrics", "data", "indicators", "signals",
            "recommendation", "rationale", "factors"
        ]
        professional_count = sum(1 for word in professional_indicators if word in response.lower())
        score += min(professional_count / 5.0, 0.2)
        
        # Check for inappropriate language (subtract if found)
        inappropriate = ["stupid", "dumb", "sucks", "terrible"]
        if any(word in response.lower() for word in inappropriate):
            score -= 0.3
        
        return max(0.0, min(score, 1.0))
    
    def _evaluate_completeness(self, response: str) -> float:
        """Evaluate completeness of response"""
        required_sections = [
            "Onchain Data Summary",
            "Key Onchain Signals",
            "Holder Behavior Analysis",
            "Liquidity Analysis",
            "Trading Recommendation",
            "Summary Table"
        ]
        
        sections_found = sum(1 for section in required_sections if section in response)
        return sections_found / len(required_sections)
    
    def _evaluate_coherence(self, response: str) -> float:
        """Evaluate coherence of response"""
        score = 0.5  # Base score
        
        # Check for logical flow indicators
        flow_indicators = ["summary", "analysis", "recommendation", "conclusion"]
        flow_count = sum(1 for word in flow_indicators if word in response.lower())
        score += min(flow_count / 4.0, 0.3)
        
        # Check for contradictions (subtract if found)
        # Simple heuristic: check for conflicting recommendations
        buy_count = len(re.findall(r'\bBUY\b', response, re.IGNORECASE))
        sell_count = len(re.findall(r'\bSELL\b', response, re.IGNORECASE))
        if buy_count > 0 and sell_count > 0:
            score -= 0.2
        
        return max(0.0, min(score, 1.0))
    
    def _evaluate_recommendation_quality(self, response: str) -> float:
        """Evaluate quality of trading recommendation"""
        score = 0.0
        
        # Check for recommendation
        if re.search(r'\b(BUY|HOLD|SELL)\b', response, re.IGNORECASE):
            score += 0.3
        
        # Check for confidence level
        if re.search(r'\b(high|medium|low)\s+confidence\b', response, re.IGNORECASE):
            score += 0.2
        
        # Check for rationale
        if "rationale" in response.lower() or "reason" in response.lower():
            score += 0.2
        
        # Check for risk factors
        if "risk" in response.lower() or "risk factors" in response.lower():
            score += 0.15
        
        # Check for key factors
        if "key" in response.lower() and "factors" in response.lower():
            score += 0.15
        
        return min(score, 1.0)
    
    def _detect_patterns(self, response: str, execution_log: Dict) -> PatternDetection:
        """Detect patterns in response"""
        
        # Hallucination detection
        hallucination_count = 0
        hallucination_examples = []
        
        # Check for unsupported claims (simple heuristic)
        # Look for specific numbers without citations
        numbers_without_cites = re.findall(r'\$[\d,]+[MBK]?', response)
        if len(numbers_without_cites) > 5:  # Many numbers might indicate hallucination
            # Check if they have doc references
            if "[doc" not in response:
                hallucination_count += 1
                hallucination_examples.append("Multiple numbers without citations")
        
        # Tone mismatch
        tone_mismatch_detected = False
        tone_mismatch_examples = []
        casual_words = ["awesome", "cool", "dude", "lol", "omg"]
        if any(word in response.lower() for word in casual_words):
            tone_mismatch_detected = True
            tone_mismatch_examples.append("Casual language detected")
        
        # User confusion indicators
        confusion_indicators = []
        vague_phrases = ["maybe", "perhaps", "might be", "could be", "unclear"]
        for phrase in vague_phrases:
            if phrase in response.lower():
                confusion_indicators.append(f"Vague phrase: {phrase}")
        
        # Missing information
        missing_info = []
        required_sections = [
            "Onchain Data Summary",
            "Key Onchain Signals",
            "Holder Behavior Analysis",
            "Liquidity Analysis",
            "Trading Recommendation"
        ]
        for section in required_sections:
            if section not in response:
                missing_info.append(f"Missing section: {section}")
        
        # Contradictory statements
        contradictions = []
        buy_count = len(re.findall(r'\bBUY\b', response, re.IGNORECASE))
        sell_count = len(re.findall(r'\bSELL\b', response, re.IGNORECASE))
        if buy_count > 0 and sell_count > 0:
            contradictions.append("Bullish and bearish statements in close proximity")
        
        return PatternDetection(
            hallucination_count=hallucination_count,
            hallucination_examples=hallucination_examples,
            tone_mismatch_detected=tone_mismatch_detected,
            tone_mismatch_examples=tone_mismatch_examples,
            user_confusion_indicators=confusion_indicators,
            missing_information=missing_info,
            contradictory_statements=contradictions
        )
    
    def _calculate_component_average(self, component_evals: List[ComponentEvaluation]) -> float:
        """Calculate average component score"""
        if not component_evals:
            return 0.0
        
        scores = []
        for eval in component_evals:
            # Component score = (Accuracy × 0.4) + (Policy Adherence × 0.4) + ((1 - Error Rate) × 0.2)
            score = (
                eval.accuracy_score * 0.4 +
                eval.policy_adherence * 0.4 +
                (1 - eval.api_error_rate) * 0.2
            )
            scores.append(score)
        
        return sum(scores) / len(scores)
    
    def _calculate_end_to_end_average(self, end_to_end_eval: EndToEndEvaluation) -> float:
        """Calculate average end-to-end score"""
        return (
            end_to_end_eval.final_response_correctness * 0.2 +
            end_to_end_eval.tone_score * 0.15 +
            end_to_end_eval.satisfaction_score * 0.2 +
            end_to_end_eval.completeness_score * 0.15 +
            end_to_end_eval.coherence_score * 0.15 +
            end_to_end_eval.recommendation_quality * 0.15
        )
    
    def generate_report(self, result: EvaluationResult) -> str:
        """Generate evaluation report"""
        report = f"""# Evaluation Report
**Evaluation ID:** {result.evaluation_id}
**Timestamp:** {result.timestamp}
**Overall Score:** {result.overall_score:.2%}

## Component-Based Evaluations

"""
        
        for eval in result.component_evals:
            status = "✓" if eval.success else "✗"
            report += f"""
### {eval.component_name.replace('_', ' ').title()}
- **Accuracy:** {eval.accuracy_score:.2%}
- **API Error Rate:** {eval.api_error_rate:.2%}
- **Policy Adherence:** {eval.policy_adherence:.2%}
- **Success:** {status}

"""
        
        report += f"""
## End-to-End Evaluation

- **Response Correctness:** {result.end_to_end_eval.final_response_correctness:.2%}
- **Tone Score:** {result.end_to_end_eval.tone_score:.2%}
- **Satisfaction Score:** {result.end_to_end_eval.satisfaction_score:.2%}
- **Completeness:** {result.end_to_end_eval.completeness_score:.2%}
- **Coherence:** {result.end_to_end_eval.coherence_score:.2%}
- **Recommendation Quality:** {result.end_to_end_eval.recommendation_quality:.2%}

## Pattern Detection

- **Hallucinations Detected:** {result.patterns.hallucination_count}
- **Tone Mismatch:** {'Yes' if result.patterns.tone_mismatch_detected else 'No'}
- **User Confusion Indicators:** {len(result.patterns.user_confusion_indicators)}
- **Missing Information:** {len(result.patterns.missing_information)}
- **Contradictions:** {len(result.patterns.contradictory_statements)}

"""
        
        if result.patterns.contradictory_statements:
            report += "\n### Contradictions:\n"
            for contradiction in result.patterns.contradictory_statements:
                report += f"- {contradiction}\n"
        
        return report

