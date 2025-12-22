from pydantic import BaseModel

class CallLogOut(BaseModel):
    call_id: str
    caller: str
    agent: str
    date: str
    transcript: str








