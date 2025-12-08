from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.users import UserCreate, UserResponse
from models.users import Users
from core.config import get_db

router = APIRouter()

@router.post("/", response_model=UserResponse)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):

    user = Users(
        email=payload.email,
        password_hash=payload.password_hash,
        role=payload.role,
        created_at=payload.created_at  # if None → DB will auto-fill
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user
