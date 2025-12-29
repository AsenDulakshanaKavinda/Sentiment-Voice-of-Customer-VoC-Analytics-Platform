
from pydantic import BaseModel, Field
from typing import Literal

class Sentiment(BaseModel):
    polarity: Literal["positive", "neutral", "negative", "mixed"] = Field(..., description="Indicates the overall emotional direction of the customer feedback.")
    intensity: Literal["low", "medium", "high", "extreme"] = Field(..., description="Represents the strength or severity of the expressed sentiment.")
    confidence: float = Field(..., description="Numerical score indicating how confident the agent is in the sentiment classification.")
    is_mixed: bool = Field(..., description="Indicates whether both positive and negative sentiments are present in the same input.")


class Metadata(BaseModel):
    sarcasm_detected: bool = Field(..., description="Flags whether sarcasm or irony is used to express sentiment indirectly.")
    implicit_sentiment: bool = Field(..., description="Indicates whether sentiment is implied through context rather than explicitly stated.")
    sa_agent_message: str = Field(..., description="Diagnostic message returned only when the sentiment agent encounters an error or abnormal condition.")

class SentimentAgentOutput(BaseModel):
    sentiment: Sentiment
    emotions: Literal["joy", "satisfaction", "trust", "frustration",
    "anger", "sadness", "fear", "disappointment", "confusion", "surprise", "none"] = Field(..., description="List of specific emotions detected in the customer feedback. Multiple emotions may be present..")
    metadata: Metadata





