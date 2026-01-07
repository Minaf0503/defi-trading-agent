"""
Comprehensive Evaluation Framework for Sentiment News Analyst

This framework evaluates:
1. Component-based evaluations (each step separately)
2. End-to-end evaluations (overall user experience)
3. Quantitative and qualitative metrics
4. Pattern detection (hallucinations, tone mismatch, user confusion)
"""

import json
import re
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime
from dataclasses import dataclass, asdict
from enum import Enum
import statistics


class EvaluationType(Enum):
    COMPONENT = "component"
    END_TO_END = "end_to_end"
    QUANTITATIVE = "quantitative"
    QUALITATIVE = "qualitative"


class SentimentLabel(Enum):
    BULLISH = "bullish"
    BEARISH = "bearish"
    NEUTRAL = "neutral"


@dataclass
class ComponentEvaluation:
    """Evaluation for individual components/steps"""
    component_name: str
    accuracy_score: float  # 0-1
    api_error_rate: float  # 0-1
    policy_adherence: float  # 0-1
    execution_time_ms: Optional[float] = None
    error_messages: List[str] = None
    success: bool = True
    
    def __post_init__(self):
        if self.error_messages is None:
            self.error_messages = []


@dataclass
class EndToEndEvaluation:
    """End-to-end evaluation metrics"""
    final_response_correctness: float  # 0-1
    tone_score: float  # 0-1
    satisfaction_score: float  # 0-1
    completeness_score: float  # 0-1
    coherence_score: float  # 0-1
    recommendation_quality: float  # 0-1


@dataclass
class PatternDetection:
    """Pattern detection results"""
    hallucination_count: int
    hallucination_examples: List[str]
    tone_mismatch_detected: bool
    tone_mismatch_examples: List[str]
    user_confusion_indicators: List[str]
    missing_information: List[str]
    contradictory_statements: List[str]


@dataclass
class EvaluationResult:
    """Complete evaluation result"""
    evaluation_id: str
    timestamp: str
    prompt: str
    response: str
    execution_log: Dict[str, Any]
    
    # Component evaluations
    component_evals: List[ComponentEvaluation]
    
    # End-to-end evaluation
    end_to_end_eval: EndToEndEvaluation
    
    # Pattern detection
    patterns: PatternDetection
    
    # Overall scores
    overall_score: float
    component_avg_score: float
    end_to_end_avg_score: float
    
    # Metadata
    evaluator_type: str  # "human", "llm", "automated"
    notes: str = ""


class SentimentNewsAnalystEvaluator:
    """Comprehensive evaluator for Sentiment News Analyst"""
    
    def __init__(self):
        self.required_components = [
            "rss_feed_fetch",
            "internet_search",
            "twitter_search",
            "reddit_search",
            "sentiment_analysis",
            "recommendation_generation"
        ]
        
        self.required_output_sections = [
            "Information Sources Summary",
            "Sentiment Analysis",
            "Source-Specific Insights",
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
        
        # Evaluate RSS feed fetch
        rss_eval = self._evaluate_rss_feed(tool_calls, response)
        evals.append(rss_eval)
        
        # Evaluate Internet search
        internet_eval = self._evaluate_internet_search(tool_calls, response)
        evals.append(internet_eval)
        
        # Evaluate Twitter search
        twitter_eval = self._evaluate_twitter_search(tool_calls, response)
        evals.append(twitter_eval)
        
        # Evaluate Reddit search
        reddit_eval = self._evaluate_reddit_search(tool_calls, response)
        evals.append(reddit_eval)
        
        # Evaluate sentiment analysis
        sentiment_eval = self._evaluate_sentiment_analysis(response)
        evals.append(sentiment_eval)
        
        # Evaluate recommendation generation
        recommendation_eval = self._evaluate_recommendation(response)
        evals.append(recommendation_eval)
        
        return evals
    
    def _extract_tool_calls(self, execution_log: Dict) -> List[Dict]:
        """Extract tool calls from execution log"""
        tool_calls = []
        
        # Parse execution log structure
        if "Timings" in execution_log:
            for timing in execution_log["Timings"]:
                if "Operation" in timing and "Tool Call" in timing["Operation"]:
                    tool_calls.append(timing)
        
        return tool_calls
    
    def _evaluate_rss_feed(self, tool_calls: List[Dict], response: str) -> ComponentEvaluation:
        """Evaluate RSS feed fetching component"""
        # Check if RSS feed was attempted
        rss_calls = [tc for tc in tool_calls if "WebSiteSearch" in str(tc) and "DL News" in str(tc)]
        
        # Check for errors
        errors = self._extract_errors(tool_calls, "rss")
        error_rate = len(errors) / max(len(rss_calls), 1)
        
        # Check if RSS data appears in response
        rss_mentioned = "RSS" in response or "DL News" in response
        accuracy = 1.0 if rss_mentioned and len(rss_calls) > 0 else 0.5
        
        # Policy adherence: Should use RSS feed
        policy_adherence = 1.0 if len(rss_calls) > 0 else 0.0
        
        return ComponentEvaluation(
            component_name="rss_feed_fetch",
            accuracy_score=accuracy,
            api_error_rate=error_rate,
            policy_adherence=policy_adherence,
            error_messages=errors,
            success=len(rss_calls) > 0 and error_rate < 0.5
        )
    
    def _evaluate_internet_search(self, tool_calls: List[Dict], response: str) -> ComponentEvaluation:
        """Evaluate internet search component"""
        internet_calls = [tc for tc in tool_calls if "InternetSearch" in str(tc)]
        
        errors = self._extract_errors(tool_calls, "internet")
        error_rate = len(errors) / max(len(internet_calls), 1)
        
        # Check if internet search results appear in response
        internet_mentioned = "internet" in response.lower() or "web" in response.lower() or "search" in response.lower()
        accuracy = 1.0 if internet_mentioned and len(internet_calls) > 0 else 0.5
        
        policy_adherence = 1.0 if len(internet_calls) > 0 else 0.0
        
        return ComponentEvaluation(
            component_name="internet_search",
            accuracy_score=accuracy,
            api_error_rate=error_rate,
            policy_adherence=policy_adherence,
            error_messages=errors,
            success=len(internet_calls) > 0 and error_rate < 0.5
        )
    
    def _evaluate_twitter_search(self, tool_calls: List[Dict], response: str) -> ComponentEvaluation:
        """Evaluate Twitter search component"""
        twitter_calls = [tc for tc in tool_calls if "Twitter" in str(tc) or "twitter" in str(tc).lower()]
        
        errors = self._extract_errors(tool_calls, "twitter")
        error_rate = len(errors) / max(len(twitter_calls), 1)
        
        twitter_mentioned = "twitter" in response.lower() or "x.com" in response.lower()
        accuracy = 1.0 if twitter_mentioned else 0.5
        
        policy_adherence = 1.0 if len(twitter_calls) > 0 else 0.0
        
        return ComponentEvaluation(
            component_name="twitter_search",
            accuracy_score=accuracy,
            api_error_rate=error_rate,
            policy_adherence=policy_adherence,
            error_messages=errors,
            success=len(twitter_calls) > 0
        )
    
    def _evaluate_reddit_search(self, tool_calls: List[Dict], response: str) -> ComponentEvaluation:
        """Evaluate Reddit search component"""
        reddit_calls = [tc for tc in tool_calls if "Reddit" in str(tc) or "reddit" in str(tc).lower()]
        
        errors = self._extract_errors(tool_calls, "reddit")
        error_rate = len(errors) / max(len(reddit_calls), 1)
        
        reddit_mentioned = "reddit" in response.lower()
        accuracy = 1.0 if reddit_mentioned else 0.5
        
        policy_adherence = 1.0 if len(reddit_calls) > 0 else 0.0
        
        return ComponentEvaluation(
            component_name="reddit_search",
            accuracy_score=accuracy,
            api_error_rate=error_rate,
            policy_adherence=policy_adherence,
            error_messages=errors,
            success=len(reddit_calls) > 0
        )
    
    def _evaluate_sentiment_analysis(self, response: str) -> ComponentEvaluation:
        """Evaluate sentiment analysis quality"""
        # Check for sentiment labels
        has_sentiment = any(label in response.lower() for label in ["bullish", "bearish", "neutral"])
        
        # Check for sentiment drivers
        has_drivers = "drivers" in response.lower() or "factors" in response.lower()
        
        # Check for FUD/FOMO detection
        has_fud_fomo = "FUD" in response or "FOMO" in response
        
        accuracy = (has_sentiment + has_drivers + has_fud_fomo) / 3.0
        
        return ComponentEvaluation(
            component_name="sentiment_analysis",
            accuracy_score=accuracy,
            api_error_rate=0.0,
            policy_adherence=1.0 if has_sentiment else 0.0,
            success=has_sentiment
        )
    
    def _evaluate_recommendation(self, response: str) -> ComponentEvaluation:
        """Evaluate trading recommendation quality"""
        # Check for recommendation
        has_recommendation = any(rec in response.upper() for rec in ["BUY", "HOLD", "SELL"])
        
        # Check for confidence level
        has_confidence = any(conf in response.lower() for conf in ["confidence", "high", "medium", "low"])
        
        # Check for rationale
        has_rationale = "rationale" in response.lower() or "reasoning" in response.lower()
        
        accuracy = (has_recommendation + has_confidence + has_rationale) / 3.0
        
        return ComponentEvaluation(
            component_name="recommendation_generation",
            accuracy_score=accuracy,
            api_error_rate=0.0,
            policy_adherence=1.0 if has_recommendation else 0.0,
            success=has_recommendation
        )
    
    def _evaluate_end_to_end(self, prompt: str, response: str, execution_log: Dict) -> EndToEndEvaluation:
        """Evaluate end-to-end user experience"""
        
        # Final response correctness
        correctness = self._evaluate_correctness(prompt, response)
        
        # Tone evaluation
        tone_score = self._evaluate_tone(response)
        
        # Satisfaction (completeness + coherence)
        completeness = self._evaluate_completeness(prompt, response)
        coherence = self._evaluate_coherence(response)
        satisfaction = (completeness + coherence) / 2.0
        
        # Recommendation quality
        recommendation_quality = self._evaluate_recommendation_quality(response)
        
        return EndToEndEvaluation(
            final_response_correctness=correctness,
            tone_score=tone_score,
            satisfaction_score=satisfaction,
            completeness_score=completeness,
            coherence_score=coherence,
            recommendation_quality=recommendation_quality
        )
    
    def _evaluate_correctness(self, prompt: str, response: str) -> float:
        """Evaluate if response correctly addresses the prompt"""
        score = 0.0
        
        # Check if all required sections are present
        required_sections = [
            "Information Sources Summary",
            "Sentiment Analysis",
            "Trading Recommendation"
        ]
        
        sections_present = sum(1 for section in required_sections if section in response)
        score += (sections_present / len(required_sections)) * 0.5
        
        # Check if token is mentioned
        # Extract token from prompt (simple heuristic)
        token_match = re.search(r'\b([A-Z]{2,5})\b', prompt)
        if token_match:
            token = token_match.group(1)
            if token in response:
                score += 0.3
        
        # Check if recommendation is present
        if any(rec in response.upper() for rec in ["BUY", "HOLD", "SELL"]):
            score += 0.2
        
        return min(score, 1.0)
    
    def _evaluate_tone(self, response: str) -> float:
        """Evaluate tone appropriateness"""
        # Professional tone indicators
        professional_indicators = [
            "analysis", "assessment", "evaluation", "recommendation",
            "rationale", "factors", "indicators", "metrics"
        ]
        
        # Unprofessional tone indicators
        unprofessional_indicators = [
            "lol", "omg", "wtf", "haha", "!!!", "???"
        ]
        
        professional_count = sum(1 for ind in professional_indicators if ind in response.lower())
        unprofessional_count = sum(1 for ind in unprofessional_indicators if ind in response.lower())
        
        # Base score
        score = 0.7
        
        # Adjust based on indicators
        if professional_count > 5:
            score += 0.2
        if unprofessional_count > 0:
            score -= 0.3
        
        return max(0.0, min(1.0, score))
    
    def _evaluate_completeness(self, prompt: str, response: str) -> float:
        """Evaluate response completeness"""
        score = 0.0
        
        # Check required sections
        required_sections = self.required_output_sections
        sections_present = sum(1 for section in required_sections if section in response)
        score += (sections_present / len(required_sections)) * 0.6
        
        # Check for sources mentioned
        sources_mentioned = sum(1 for source in ["RSS", "Twitter", "Reddit", "Internet"] if source in response)
        score += (sources_mentioned / 4.0) * 0.4
        
        return min(score, 1.0)
    
    def _evaluate_coherence(self, response: str) -> float:
        """Evaluate response coherence"""
        # Check for logical flow
        has_intro = "summary" in response.lower()[:500] or "analysis" in response.lower()[:500]
        has_body = len(response) > 1000
        has_conclusion = "recommendation" in response.lower()[-1000:] or "conclusion" in response.lower()[-1000:]
        
        coherence_score = (has_intro + has_body + has_conclusion) / 3.0
        
        # Check for contradictions (simple heuristic)
        contradictions = self._detect_contradictions(response)
        if contradictions:
            coherence_score *= 0.7
        
        return coherence_score
    
    def _evaluate_recommendation_quality(self, response: str) -> float:
        """Evaluate quality of trading recommendation"""
        score = 0.0
        
        # Has recommendation
        has_rec = any(rec in response.upper() for rec in ["BUY", "HOLD", "SELL"])
        if has_rec:
            score += 0.3
        
        # Has confidence level
        has_confidence = any(conf in response.lower() for conf in ["confidence", "high", "medium", "low"])
        if has_confidence:
            score += 0.2
        
        # Has rationale
        has_rationale = "rationale" in response.lower() or "reasoning" in response.lower()
        if has_rationale:
            score += 0.3
        
        # Has risk factors
        has_risks = "risk" in response.lower()
        if has_risks:
            score += 0.2
        
        return score
    
    def _detect_patterns(self, response: str, execution_log: Dict) -> PatternDetection:
        """Detect patterns: hallucinations, tone mismatch, user confusion"""
        
        # Detect hallucinations
        hallucinations = self._detect_hallucinations(response, execution_log)
        
        # Detect tone mismatch
        tone_mismatch = self._detect_tone_mismatch(response)
        
        # Detect user confusion indicators
        confusion_indicators = self._detect_user_confusion(response)
        
        # Detect missing information
        missing_info = self._detect_missing_information(response)
        
        # Detect contradictions
        contradictions = self._detect_contradictions(response)
        
        return PatternDetection(
            hallucination_count=len(hallucinations),
            hallucination_examples=hallucinations,
            tone_mismatch_detected=tone_mismatch[0],
            tone_mismatch_examples=tone_mismatch[1],
            user_confusion_indicators=confusion_indicators,
            missing_information=missing_info,
            contradictory_statements=contradictions
        )
    
    def _detect_hallucinations(self, response: str, execution_log: Dict) -> List[str]:
        """Detect potential hallucinations"""
        hallucinations = []
        
        # Check for specific claims that might be unsupported
        # Look for specific numbers/statements that might not be in sources
        specific_claims = re.findall(r'\d+%', response)
        
        # Check if sources support these claims
        # This is a simplified check - in practice, you'd cross-reference with actual sources
        if len(specific_claims) > 5:
            hallucinations.append("Multiple specific percentage claims that may not be fully supported")
        
        # Check for made-up sources
        fake_sources = ["According to CryptoNews", "As reported by FakeNews"]
        for fake in fake_sources:
            if fake in response:
                hallucinations.append(f"Potentially fabricated source: {fake}")
        
        return hallucinations
    
    def _detect_tone_mismatch(self, response: str) -> Tuple[bool, List[str]]:
        """Detect tone mismatch"""
        mismatches = []
        
        # Check for casual language in professional context
        casual_phrases = ["lol", "omg", "wtf", "haha", "dude", "bro"]
        found_casual = [phrase for phrase in casual_phrases if phrase in response.lower()]
        
        if found_casual:
            mismatches.extend(found_casual)
        
        # Check for overly technical language that might confuse users
        overly_technical = ["quantum", "blockchain consensus mechanism", "cryptographic hash"]
        if sum(1 for term in overly_technical if term in response) > 2:
            mismatches.append("Overly technical language may confuse users")
        
        return (len(mismatches) > 0, mismatches)
    
    def _detect_user_confusion(self, response: str) -> List[str]:
        """Detect indicators that might confuse users"""
        confusion_indicators = []
        
        # Vague statements
        vague_phrases = ["some sources", "various reports", "it is said", "people think"]
        if sum(1 for phrase in vague_phrases if phrase in response.lower()) > 3:
            confusion_indicators.append("Too many vague statements without specific sources")
        
        # Contradictory information
        if "bullish" in response.lower() and "bearish" in response.lower():
            if response.lower().count("bullish") > 2 and response.lower().count("bearish") > 2:
                confusion_indicators.append("Mixed bullish/bearish signals without clear explanation")
        
        # Missing context
        if "recommendation" in response.lower() and "HOLD" in response.upper():
            if "why" not in response.lower()[-500:]:
                confusion_indicators.append("HOLD recommendation without clear explanation")
        
        return confusion_indicators
    
    def _detect_missing_information(self, response: str) -> List[str]:
        """Detect missing required information"""
        missing = []
        
        required_sections = self.required_output_sections
        for section in required_sections:
            if section not in response:
                missing.append(f"Missing section: {section}")
        
        # Check for sources
        if "RSS" not in response and "DL News" not in response:
            missing.append("Missing RSS feed information")
        
        if "Twitter" not in response and "X" not in response:
            missing.append("Missing Twitter/X information")
        
        if "Reddit" not in response:
            missing.append("Missing Reddit information")
        
        return missing
    
    def _detect_contradictions(self, response: str) -> List[str]:
        """Detect contradictory statements"""
        contradictions = []
        
        # Check for sentiment contradictions
        if "bullish" in response.lower() and "bearish" in response.lower():
            # Count occurrences
            bullish_count = response.lower().count("bullish")
            bearish_count = response.lower().count("bearish")
            
            if bullish_count > 2 and bearish_count > 2:
                # Check if they're in close proximity (might indicate contradiction)
                sentences = response.split('.')
                for i, sentence in enumerate(sentences):
                    if "bullish" in sentence.lower():
                        # Check nearby sentences
                        nearby = ' '.join(sentences[max(0, i-2):min(len(sentences), i+3)])
                        if "bearish" in nearby.lower():
                            contradictions.append("Bullish and bearish statements in close proximity")
                            break
        
        # Check for recommendation contradictions
        if "BUY" in response.upper() and "SELL" in response.upper():
            contradictions.append("Both BUY and SELL recommendations present")
        
        return contradictions
    
    def _extract_errors(self, tool_calls: List[Dict], component: str) -> List[str]:
        """Extract error messages for a component"""
        errors = []
        
        # Look for error patterns in execution log
        # This is simplified - in practice, you'd parse the actual error messages
        for call in tool_calls:
            if component in str(call).lower():
                if "error" in str(call).lower() or "failed" in str(call).lower():
                    errors.append(str(call)[:200])  # Truncate for brevity
        
        return errors
    
    def _calculate_component_average(self, component_evals: List[ComponentEvaluation]) -> float:
        """Calculate average component score"""
        if not component_evals:
            return 0.0
        
        scores = []
        for eval in component_evals:
            # Weighted average: accuracy (40%), policy adherence (40%), error rate (20%, inverted)
            component_score = (
                eval.accuracy_score * 0.4 +
                eval.policy_adherence * 0.4 +
                (1 - eval.api_error_rate) * 0.2
            )
            scores.append(component_score)
        
        return statistics.mean(scores)
    
    def _calculate_end_to_end_average(self, end_to_end_eval: EndToEndEvaluation) -> float:
        """Calculate average end-to-end score"""
        return (
            end_to_end_eval.final_response_correctness * 0.3 +
            end_to_end_eval.tone_score * 0.2 +
            end_to_end_eval.satisfaction_score * 0.2 +
            end_to_end_eval.completeness_score * 0.15 +
            end_to_end_eval.coherence_score * 0.15
        )
    
    def generate_report(self, result: EvaluationResult) -> str:
        """Generate human-readable evaluation report"""
        report = f"""
# Evaluation Report
**Evaluation ID:** {result.evaluation_id}
**Timestamp:** {result.timestamp}
**Overall Score:** {result.overall_score:.2%}

## Component-Based Evaluations

"""
        for component in result.component_evals:
            report += f"""
### {component.component_name.replace('_', ' ').title()}
- **Accuracy:** {component.accuracy_score:.2%}
- **API Error Rate:** {component.api_error_rate:.2%}
- **Policy Adherence:** {component.policy_adherence:.2%}
- **Success:** {'✓' if component.success else '✗'}
"""
            if component.error_messages:
                report += f"- **Errors:** {len(component.error_messages)} errors detected\n"
        
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
        
        if result.patterns.hallucination_examples:
            report += "### Hallucination Examples:\n"
            for example in result.patterns.hallucination_examples:
                report += f"- {example}\n"
        
        if result.patterns.missing_information:
            report += "\n### Missing Information:\n"
            for missing in result.patterns.missing_information:
                report += f"- {missing}\n"
        
        if result.patterns.contradictory_statements:
            report += "\n### Contradictions:\n"
            for contradiction in result.patterns.contradictory_statements:
                report += f"- {contradiction}\n"
        
        return report

