
# ==================== routers/favorite.py ====================
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
import fastapi_schemas
import fastapi_models
from database import get_db

router = APIRouter(prefix="/favorites", tags=["Favorites"])

@router.post("/", response_model=fastapi_schemas.FavoriteResponse)
def create_favorite(favorite: fastapi_schemas.FavoriteCreate, db: Session = Depends(get_db)):
    """Create a new favorite"""
    db_favorite = fastapi_models.Favorite(
        favorite_id_serial=0,
        user_id_integer=favorite.user_id_integer,
        food_id_integer=favorite.food_id_integer,
        created_at_timestamp_with_out_time_zone=datetime.now()
    )
    db.add(db_favorite)
    db.commit()
    db.refresh(db_favorite)
    return db_favorite

@router.get("/", response_model=List[fastapi_schemas.FavoriteResponse])
def get_favorites(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all favorites with pagination"""
    favorites = db.query(fastapi_models.Favorite).offset(skip).limit(limit).all()
    return favorites

@router.get("/{favorite_id}", response_model=fastapi_schemas.FavoriteResponse)
def get_favorite(favorite_id: int, db: Session = Depends(get_db)):
    """Get a specific favorite by ID"""
    favorite = db.query(fastapi_models.Favorite).filter(fastapi_models.Favorite.id == favorite_id).first()
    if favorite is None:
        raise HTTPException(status_code=404, detail="Favorite not found")
    return favorite