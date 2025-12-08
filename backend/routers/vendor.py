from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.vendor_base import VendorCreate, VendorResponse
from models.vendor import Vendor
from models.foods import Food
from models.locations import Location
from core.config import connect_db


router = APIRouter()


@router.post("/", response_model=VendorResponse)
def create_vendor(payload: VendorCreate, db: Session = Depends(connect_db)):
# 1) create Location
    Loc = Location(
    location_name=payload.location_name,
    longitude=payload.longitude,
    latitude=payload.latitude,
    )
    db.add(Loc)
    db.commit()
    db.refresh(Loc)


# 2) create Food
    food = Food(
    food_name=payload.menu_list,
    food_image=payload.cart_image,
    )
    db.add(food)
    db.commit()
    db.refresh(food)


# 3) create Vendor and link the fks
    vendor = Vendor(
    vendor_name=payload.vendor_name,
    cart_name=payload.cart_name,
    food_type=payload.food_type,
    phone_number=payload.phone_number,
    location_id=Loc.location_id,
    food_id=food.food_id,
    cart_image=payload.cart_image,
    opening_time=payload.opening_time,
    closing_time=payload.closing_time,
    )
    db.add(vendor)
    db.commit()
    db.refresh(vendor)


# Return the vendor (Pydantic will read related fields from payload and the refreshed vendor)
    return VendorResponse(
    vendor_id=vendor.vendor_id,
    vendor_name=vendor.vendor_name,
    cart_name=vendor.cart_name,
    food_type=vendor.food_type,
    phone_number=vendor.phone_number,
    location_name=Loc.location_name,
    longitude=Loc.longitude,
    latitude=Loc.latitude,
    cart_image=vendor.cart_image,
    menu_list=food.food_name,
    opening_time=vendor.opening_time,
    closing_time=vendor.closing_time,
    location_id=Loc.location_id,
    food_id=food.food_id,
    )