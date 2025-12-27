from datetime import datetime
from pydantic import BaseModel, Field
from typing import Literal

class Metadata(BaseModel):
    rating: float = Field(..., description="The rating of the source, only from the reviews")
    subject: str = Field(..., description="The subject of the source, only from the emails")
    platform: str = Field(..., description="The platform of the source, only from the social medias")
    session_id: str = Field(..., description="The session id of the source, only from the chats/calls")


class CommonOutputSchema(BaseModel):
    id: str = Field(..., description="generated UUID or source-specific ID for output")
    source_type: Literal["product_review", "support_ticket", "chat_transcript", "email", "social_media", "call_center_transcript"] = Field(..., description="Source type")
    timestamp: datetime = Field(..., description="Timestamp UTC")
    customer_identifier: str = Field(..., description="Customer identifier")
    text_content: str = Field(..., description="The main body/transcript/review text, cleaned (e.g., remove HTML, normalize whitespace)")
    metadata: Metadata = Field(..., description="The metadata of the source")
    original_raw: str = Field(..., description="The original raw of the source")


