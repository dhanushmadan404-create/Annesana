from DB.database import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP, Enum
from enum import Enum as PyEnum

class UserRole(PyEnum):
    admin = "admin"
    user = "user"
    vendor = "vendor"

class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(Enum(UserRole, name="user_role"), nullable=False)
