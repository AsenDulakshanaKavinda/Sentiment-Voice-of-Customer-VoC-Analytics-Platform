from pydantic import BaseModel


class ChatLogOut(BaseModel):
    session_id: str
    participants: str
    timestamp: str
    transcript: str


