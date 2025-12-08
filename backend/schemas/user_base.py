from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import Optional

class UserRole(str, Enum):
    admin = "admin"
    user = "user"
    vendor = "vendor"

class UserBase(BaseModel):
    email: str
    password_hash: str
    role: UserRole
    created_at: Optional[datetime] = None  # Auto-filled by DB

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    user_id: int

    class Config:
        from_attributes = True
