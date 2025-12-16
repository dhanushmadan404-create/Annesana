
# ==================== routers/user.py ====================
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
import fastapi_schemas
import fastapi_models
from database import get_db


router = APIRouter(prefix="/users",tags=["users"])

@router.post("/", response_model=fastapi_schemas.UserResponse)
def create_user(user: fastapi_schemas.UserCreate, db: Session = Depends(get_db)):
    """Create a new user"""

    db_user = fastapi_models.User(
        email=user.email,
        password_hash=user.password,  # plain text password (not secure)
        role=user.role,
        created_at=datetime.utcnow()  # set created_at on server
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



@router.get("/", response_model=List[fastapi_schemas.UserResponse])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all users with pagination"""
    users = db.query(fastapi_models.User).offset(skip).limit(limit).all()
    return users

@router.get("/{user_id}", response_model=fastapi_schemas.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """Get a specific user by ID"""
    user = db.query(fastapi_models.User).filter(fastapi_models.User.user_id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
