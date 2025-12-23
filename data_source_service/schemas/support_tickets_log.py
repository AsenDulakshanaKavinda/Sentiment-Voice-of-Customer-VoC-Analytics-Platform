
from pydantic import BaseModel


class SupportTicketsLogOut(BaseModel):
    ticket_id: str
    customer: str
    submitted: str
    subject: str
    description: str

