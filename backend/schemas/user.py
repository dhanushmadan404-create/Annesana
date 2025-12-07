from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    admin = "admin"
    user = "user"
    vendor = "vendor"

class UserBase(BaseModel):
    email: str
    created_at: datetime
    password_hash: str
    role: UserRole

class UserResponse(UserBase):
    user_id: int

    class Config:
        from_attributes = True
