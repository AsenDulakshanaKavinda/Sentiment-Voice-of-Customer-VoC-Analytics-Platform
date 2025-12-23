from pydantic import BaseModel


class ProductReviewLogOut(BaseModel):
    reviewer: str
    date: str
    rating: int
    text: str


