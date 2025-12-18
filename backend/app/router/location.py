


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
        location_name=location.location_name,
        latitude=location.latitude,
        longitude=location.longitude,
        vendor_id=location.vendor_id,
    )
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location

@router.get("", response_model=List[fastapi_schemas.LocationResponse])
def get_locations( db: Session = Depends(get_db)):
    """Get all locations with pagination"""
    locations = db.query(fastapi_models.Location).all()
    return locations

@router.get("/{location_id}", response_model=fastapi_schemas.LocationResponse)
def get_location(location_id: int, db: Session = Depends(get_db)):
    """Get a specific location by ID"""
    location = db.query(fastapi_models.Location).filter(fastapi_models.Location.location_id == location_id).first()
    if location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return location



