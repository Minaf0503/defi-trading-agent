"""
LLM-as-Judge Evaluation

Uses an LLM to evaluate the agent's response quality, tone, and correctness.
"""

import json
from typing import Dict, Any, Optional
from dataclasses import dataclass
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


@dataclass
class LLMJudgeResult:
    """Result from LLM judge evaluation"""
    correctness_score: float  # 0-1
    tone_score: float  # 0-1
    completeness_score: float  # 0-1
    recommendation_quality: float  # 0-1
    overall_score: float  # 0-1
    feedback: str
    strengths: list
    weaknesses: list
    suggestions: list


class LLMJudge:
    """LLM-based judge for evaluating agent responses"""
    
    def __init__(self, llm_model: str = "gpt-4o", api_key: Optional[str] = None):
        self.llm = ChatOpenAI(model=llm_model, temperature=0)
        self.evaluation_prompt = self._create_evaluation_prompt()
    
    def _create_evaluation_prompt(self) -> ChatPromptTemplate:
        """Create the evaluation prompt template"""
        template = """You are an expert evaluator for a cryptocurrency sentiment analysis agent. Your task is to evaluate the agent's response quality.

**User Prompt:**
{prompt}

**Agent Response:**
{response}

**Evaluation Criteria:**

1. **Correctness (0-1):** Does the response correctly address the prompt? Are the facts accurate?
2. **Tone (0-1):** Is the tone professional, clear, and appropriate for financial analysis?
3. **Completeness (0-1):** Does the response include all required sections and information?
4. **Recommendation Quality (0-1):** Is the trading recommendation well-reasoned, with clear rationale and confidence level?

**Required Sections:**
- Information Sources Summary
- Sentiment Analysis
- Source-Specific Insights
- Trading Recommendation (BUY/HOLD/SELL)
- Summary Table

**Evaluation Instructions:**
- Score each criterion from 0.0 to 1.0
- Provide specific feedback
- Identify strengths and weaknesses
- Suggest improvements

**Output Format (JSON):**
{{
    "correctness_score": 0.0-1.0,
    "tone_score": 0.0-1.0,
    "completeness_score": 0.0-1.0,
    "recommendation_quality": 0.0-1.0,
    "overall_score": 0.0-1.0,
    "feedback": "Detailed feedback text",
    "strengths": ["strength1", "strength2"],
    "weaknesses": ["weakness1", "weakness2"],
    "suggestions": ["suggestion1", "suggestion2"]
}}

Evaluate the response now:"""
        
        return ChatPromptTemplate.from_template(template)
    
    def evaluate(self, prompt: str, response: str) -> LLMJudgeResult:
        """Evaluate response using LLM judge"""
        
        chain = self.evaluation_prompt | self.llm
        
        result = chain.invoke({
            "prompt": prompt,
            "response": response
        })
        
        # Parse JSON response
        try:
            # Extract JSON from response
            content = result.content
            # Try to find JSON in the response
            json_start = content.find('{')
            json_end = content.rfind('}') + 1
            
            if json_start >= 0 and json_end > json_start:
                json_str = content[json_start:json_end]
                eval_data = json.loads(json_str)
            else:
                # Fallback: try to parse entire content
                eval_data = json.loads(content)
        except json.JSONDecodeError:
            # Fallback evaluation if JSON parsing fails
            eval_data = {
                "correctness_score": 0.5,
                "tone_score": 0.5,
                "completeness_score": 0.5,
                "recommendation_quality": 0.5,
                "overall_score": 0.5,
                "feedback": "Could not parse evaluation. Original response: " + content[:500],
                "strengths": [],
                "weaknesses": ["JSON parsing failed"],
                "suggestions": ["Improve response format"]
            }
        
        return LLMJudgeResult(
            correctness_score=eval_data.get("correctness_score", 0.5),
            tone_score=eval_data.get("tone_score", 0.5),
            completeness_score=eval_data.get("completeness_score", 0.5),
            recommendation_quality=eval_data.get("recommendation_quality", 0.5),
            overall_score=eval_data.get("overall_score", 0.5),
            feedback=eval_data.get("feedback", ""),
            strengths=eval_data.get("strengths", []),
            weaknesses=eval_data.get("weaknesses", []),
            suggestions=eval_data.get("suggestions", [])
        )


class RubricBasedEvaluator:
    """Rubric-based evaluation with detailed scoring"""
    
    def __init__(self):
        self.rubric = self._create_rubric()
    
    def _create_rubric(self) -> Dict[str, Dict[str, Any]]:
        """Create evaluation rubric"""
        return {
            "information_gathering": {
                "weight": 0.25,
                "criteria": {
                    "rss_feed_used": {"weight": 0.3, "max_score": 1.0},
                    "internet_search_used": {"weight": 0.3, "max_score": 1.0},
                    "twitter_search_used": {"weight": 0.2, "max_score": 1.0},
                    "reddit_search_used": {"weight": 0.2, "max_score": 1.0}
                }
            },
            "sentiment_analysis": {
                "weight": 0.25,
                "criteria": {
                    "sentiment_labeled": {"weight": 0.3, "max_score": 1.0},
                    "drivers_identified": {"weight": 0.3, "max_score": 1.0},
                    "fud_fomo_detected": {"weight": 0.2, "max_score": 1.0},
                    "trends_analyzed": {"weight": 0.2, "max_score": 1.0}
                }
            },
            "recommendation": {
                "weight": 0.30,
                "criteria": {
                    "recommendation_present": {"weight": 0.25, "max_score": 1.0},
                    "confidence_level": {"weight": 0.25, "max_score": 1.0},
                    "rationale_provided": {"weight": 0.30, "max_score": 1.0},
                    "risk_factors": {"weight": 0.20, "max_score": 1.0}
                }
            },
            "presentation": {
                "weight": 0.20,
                "criteria": {
                    "structure": {"weight": 0.3, "max_score": 1.0},
                    "tone": {"weight": 0.3, "max_score": 1.0},
                    "completeness": {"weight": 0.2, "max_score": 1.0},
                    "clarity": {"weight": 0.2, "max_score": 1.0}
                }
            }
        }
    
    def evaluate(self, prompt: str, response: str, execution_log: Dict) -> Dict[str, Any]:
        """Evaluate using rubric"""
        scores = {}
        
        for category, config in self.rubric.items():
            category_score = 0.0
            category_max = 0.0
            
            for criterion, criterion_config in config["criteria"].items():
                score = self._score_criterion(criterion, response, execution_log)
                weight = criterion_config["weight"]
                max_score = criterion_config["max_score"]
                
                category_score += score * weight * max_score
                category_max += max_score * weight
            
            scores[category] = {
                "score": category_score / category_max if category_max > 0 else 0.0,
                "weight": config["weight"]
            }
        
        # Calculate overall score
        overall = sum(scores[cat]["score"] * scores[cat]["weight"] for cat in scores)
        
        return {
            "category_scores": scores,
            "overall_score": overall,
            "rubric": self.rubric
        }
    
    def _score_criterion(self, criterion: str, response: str, execution_log: Dict) -> float:
        """Score individual criterion"""
        criterion_lower = criterion.lower()
        
        if "rss" in criterion_lower:
            return 1.0 if "RSS" in response or "DL News" in response else 0.0
        elif "internet" in criterion_lower:
            return 1.0 if "internet" in response.lower() or "web" in response.lower() else 0.0
        elif "twitter" in criterion_lower:
            return 1.0 if "twitter" in response.lower() or "x.com" in response.lower() else 0.0
        elif "reddit" in criterion_lower:
            return 1.0 if "reddit" in response.lower() else 0.0
        elif "sentiment_labeled" in criterion_lower:
            return 1.0 if any(s in response.lower() for s in ["bullish", "bearish", "neutral"]) else 0.0
        elif "drivers_identified" in criterion_lower:
            return 1.0 if "drivers" in response.lower() or "factors" in response.lower() else 0.0
        elif "fud_fomo" in criterion_lower:
            return 1.0 if "FUD" in response or "FOMO" in response else 0.0
        elif "recommendation_present" in criterion_lower:
            return 1.0 if any(r in response.upper() for r in ["BUY", "HOLD", "SELL"]) else 0.0
        elif "confidence_level" in criterion_lower:
            return 1.0 if any(c in response.lower() for c in ["confidence", "high", "medium", "low"]) else 0.0
        elif "rationale_provided" in criterion_lower:
            return 1.0 if "rationale" in response.lower() or "reasoning" in response.lower() else 0.0
        elif "risk_factors" in criterion_lower:
            return 1.0 if "risk" in response.lower() else 0.0
        elif "structure" in criterion_lower:
            required_sections = ["Information Sources Summary", "Sentiment Analysis", "Trading Recommendation"]
            present = sum(1 for section in required_sections if section in response)
            return present / len(required_sections)
        elif "tone" in criterion_lower:
            # Professional tone check
            unprofessional = ["lol", "omg", "wtf"]
            if any(up in response.lower() for up in unprofessional):
                return 0.3
            return 0.9  # Assume professional if no unprofessional terms
        elif "completeness" in criterion_lower:
            required = ["Information Sources Summary", "Sentiment Analysis", "Trading Recommendation", "Summary Table"]
            present = sum(1 for req in required if req in response)
            return present / len(required)
        elif "clarity" in criterion_lower:
            # Simple clarity check: length and structure
            if len(response) > 500 and "." in response:
                return 0.8
            return 0.5
        
        return 0.5  # Default score

