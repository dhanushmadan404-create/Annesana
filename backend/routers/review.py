from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.review_base import ReviewCreate, ReviewResponse
from models.reviews import Reviews
from core.config import connect_db

router = APIRouter()

@router.post("/", response_model=ReviewResponse)
def create_review(payload: ReviewCreate, db: Session = Depends(connect_db)):

    review = Reviews(
        rating=payload.rating,
        comment=payload.comment,
        user_id=payload.user_id,
        vendor_id=payload.vendor_id,
        created_at=payload.created_at
    )

    db.add(review)
    db.commit()
    db.refresh(review)

    return review
