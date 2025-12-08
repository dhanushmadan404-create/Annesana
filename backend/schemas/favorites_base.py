from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class FavoriteBase(BaseModel):
    user_id: int
    food_id: int
    created_at: Optional[datetime] = None  # DB default

class FavoriteCreate(FavoriteBase):
    pass

class FavoriteResponse(FavoriteBase):
    favorite_id: int

    class Config:
        orm_mode = True
