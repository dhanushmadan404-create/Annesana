



# ==================== routers/food.py ====================
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import fastapi_schemas
import fastapi_models
from database import get_db

router = APIRouter(prefix="/foods", tags=["Foods"])

@router.post("/", response_model=fastapi_schemas.FoodResponse)
def create_food(food: fastapi_schemas.FoodCreate, db: Session = Depends(get_db)):
    """Create a new food item"""
    db_food = fastapi_models.Food(
        food_id_serial=0,
        food_name_character_varying_255=food.food_name_character_varying_255,
        food_image_url_character_varying_255=food.food_image_url_character_varying_255,
        food_type_character_varying_100=food.food_type_character_varying_100,
        phone_number_character_varying_15=food.phone_number_character_varying_15,
        vendor_id_integer=food.vendor_id_integer
    )
    db.add(db_food)
    db.commit()
    db.refresh(db_food)
    return db_food

@router.get("/", response_model=List[fastapi_schemas.FoodResponse])
def get_foods(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all foods with pagination"""
    foods = db.query(fastapi_models.Food).offset(skip).limit(limit).all()
    return foods

@router.get("/{food_id}", response_model=fastapi_schemas.FoodResponse)
def get_food(food_id: int, db: Session = Depends(get_db)):
    """Get a specific food by ID"""
    food = db.query(fastapi_models.Food).filter(fastapi_models.Food.food_id == food_id).first()
    if food is None:
        raise HTTPException(status_code=404, detail="Food not found")
    return food

