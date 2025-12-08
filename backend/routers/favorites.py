from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.favorites_base import FavoriteCreate, FavoriteResponse
from models.favorites import Favorites
from core.config import connect_db

router = APIRouter()

@router.post("/", response_model=FavoriteResponse)
def create_favorite(payload: FavoriteCreate, db: Session = Depends(connect_db)):

    fav = Favorites(
        user_id=payload.user_id,
        food_id=payload.food_id,
        created_at=payload.created_at    # if None, DB uses NOW()
    )

    db.add(fav)
    db.commit()
    db.refresh(fav)

    return fav
