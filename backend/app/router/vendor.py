


# ==================== routers/vendor.py ====================
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
import fastapi_schemas
import fastapi_models
from database import get_db

router = APIRouter(prefix="/vendors", tags=["Vendors"])

@router.post("/", response_model=fastapi_schemas.VendorResponse)
def create_vendor(vendor: fastapi_schemas.VendorCreate, db: Session = Depends(get_db)):
    """Create a new vendor"""
    db_vendor = fastapi_models.Vendor(
        vendor_id_serial=0,
        vendor_name_character_varying_255=vendor.vendor_name_character_varying_255,
        qr_name_character_varying_255=vendor.qr_name_character_varying_255,
        qr_code_time_without_time_zone=datetime.now(),
        qr_code_time_time_without_me_zone=datetime.now()
    )
    db.add(db_vendor)
    db.commit()
    db.refresh(db_vendor)
    return db_vendor

@router.get("/", response_model=List[fastapi_schemas.VendorResponse])
def get_vendors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all vendors with pagination"""
    vendors = db.query(fastapi_models.Vendor).offset(skip).limit(limit).all()
    return vendors

@router.get("/{vendor_id}", response_model=fastapi_schemas.VendorResponse)
def get_vendor(vendor_id: int, db: Session = Depends(get_db)):
    """Get a specific vendor by ID"""
    vendor = db.query(fastapi_models.Vendor).filter(fastapi_models.Vendor.vendor_id == vendor_id).first()
    if vendor is None:
        raise HTTPException(status_code=404, detail="Vendor not found")
    return vendor

