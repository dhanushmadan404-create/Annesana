from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ReviewBase(BaseModel):
    rating: int
    comment: str
    user_id: int
    vendor_id: int
    created_at: Optional[datetime] = None   # DB default

class ReviewCreate(ReviewBase):
    pass

class ReviewResponse(ReviewBase):
    review_id: int

    class Config:
        from_attributes = True
