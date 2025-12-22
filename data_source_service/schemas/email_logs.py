from pydantic import BaseModel


class EmailLogOut(BaseModel):
    sender: str
    to: str
    data: str
    subject: str
    body: str

