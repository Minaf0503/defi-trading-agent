from enum import Enum
from typing import List, Optional, Dict
from pydantic import BaseModel


class AnalystType(str, Enum):
    TECHNICAL = "technical"
    ONCHAIN = "onchain"
    TOKENOMICS = "tokenomics"
    SENTIMENT_NEWS = "sentiment_news"
