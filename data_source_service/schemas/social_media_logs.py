from pydantic import BaseModel


class SocialMediaLogOut(BaseModel):
    platform: str
    user: str
    post_id: str
    date: str
    text: str

