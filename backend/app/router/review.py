



# ==================== routers/review.py ====================
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
import fastapi_schemas
import fastapi_models
from database import get_db

router = APIRouter(prefix="/reviews", tags=["Reviews"])

@router.post("/", response_model=fastapi_schemas.ReviewResponse)
def create_review(review: fastapi_schemas.ReviewCreate, db: Session = Depends(get_db)):
    """Create a new review"""
    db_review = fastapi_models.Review(
        review_id_serial=0,
        user_id_integer=review.user_id_integer,
        food_id_integer=review.food_id_integer,
        rating_integer=review.rating_integer,
        review_text_text=review.review_text_text,
        created_at_timestamp_with_out_time_zone=datetime.now()
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

@router.get("/", response_model=List[fastapi_schemas.ReviewResponse])
def get_reviews(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all reviews with pagination"""
    reviews = db.query(fastapi_models.Review).offset(skip).limit(limit).all()
    return reviews

@router.get("/{review_id}", response_model=fastapi_schemas.ReviewResponse)
def get_review(review_id: int, db: Session = Depends(get_db)):
    """Get a specific review by ID"""
    review = db.query(fastapi_models.Review).filter(fastapi_models.Review.review_id == review_id).first()
    if review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    return review