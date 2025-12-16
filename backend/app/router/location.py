


# ==================== routers/location.py ====================
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
import fastapi_schemas
import fastapi_models
from database import get_db

router = APIRouter(prefix="/locations", tags=["Locations"])

@router.post("/", response_model=fastapi_schemas.LocationResponse)
def create_location(location: fastapi_schemas.LocationCreate, db: Session = Depends(get_db)):
    """Create a new location"""
    db_location = fastapi_models.Location(
        location_id_serial=0,
        location_name_character_varying_255=location.location_name_character_varying_255,
        latitude_numeric_10_6=location.latitude_numeric_10_6,
        longitude_numeric_10_6=location.longitude_numeric_10_6,
        vendor_id=location.vendor_id,
        qr_time_input_url_character_varying_255=location.qr_time_input_url_character_varying_255,
        qr_code_time_time_without_time_zone=datetime.now(),
        qr_code_time_time_without_me_zone=datetime.now()
    )
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location

@router.get("/", response_model=List[fastapi_schemas.LocationResponse])
def get_locations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all locations with pagination"""
    locations = db.query(fastapi_models.Location).offset(skip).limit(limit).all()
    return locations

@router.get("/{location_id}", response_model=fastapi_schemas.LocationResponse)
def get_location(location_id: int, db: Session = Depends(get_db)):
    """Get a specific location by ID"""
    location = db.query(fastapi_models.Location).filter(fastapi_models.Location.location_id == location_id).first()
    if location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return location



