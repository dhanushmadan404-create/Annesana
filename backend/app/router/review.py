from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from database import get_db
import fastapi_models
import fastapi_schemas

router = APIRouter(
    prefix="/reviews",
    tags=["Reviews"]
)

# --------------------------------------------------
# CREATE REVIEW
# --------------------------------------------------
@router.post("", response_model=fastapi_schemas.ReviewResponse)
def create_review(
    review: fastapi_schemas.ReviewCreate,
    db: Session = Depends(get_db)
):
    db_review = fastapi_models.Review(
        user_id=review.user_id,
        food_id=review.food_id,
        vendor_id=review.vendor_id,
        rating=review.rating,
        review_text=review.review_text,
        created_at=datetime.utcnow()
    )

    db.add(db_review)
    db.commit()
    db.refresh(db_review)

    return db_review


# --------------------------------------------------
# GET ALL REVIEWS
# --------------------------------------------------
@router.get("", response_model=List[fastapi_schemas.ReviewResponse])
def get_reviews(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return (
        db.query(fastapi_models.Review)
        .offset(skip)
        .limit(limit)
        .all()
    )


# --------------------------------------------------
# GET REVIEW BY ID
# --------------------------------------------------
@router.get("{review_id}", response_model=fastapi_schemas.ReviewResponse)
def get_review(review_id: int, db: Session = Depends(get_db)):
    review = (
        db.query(fastapi_models.Review)
        .filter(fastapi_models.Review.review_id == review_id)
        .first()
    )

    if not review:
        raise HTTPException(status_code=404, detail="Review not found")

    return review
