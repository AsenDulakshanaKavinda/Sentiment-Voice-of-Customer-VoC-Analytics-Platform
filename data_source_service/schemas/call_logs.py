from pydantic import BaseModel
from datetime import datetime

class CallLogOut(BaseModel):
    call_id: str
    caller: str
    agent: str
    date: datetime
    transcript: str








