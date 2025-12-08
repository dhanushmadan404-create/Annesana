from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
    


class VendorBase(BaseModel):
    vendor_name: str
    cart_name: Optional[str]
    food_type: Optional[str]
    phone_number: Optional[str]
    location_name: str
    longitude: float
    latitude: float
    cart_image: Optional[str]
    menu_list: str
    opening_time: Optional[datetime]
    closing_time: Optional[datetime]


class VendorCreate(VendorBase):
    pass


class VendorResponse(VendorBase):
    vendor_id: int
    location_id: int
    food_id: Optional[int]


class Config:
    orm_mode = True 


class VendorBase(BaseModel):
    vendor_name: str
    cart_name: Optional[str]
    food_type: Optional[str]
    phone_number: Optional[str]
    location_name: str
    longitude: float
    latitude: float
    cart_image: Optional[str]
    menu_list: str
    opening_time: Optional[datetime]
    closing_time: Optional[datetime]


class VendorCreate(VendorBase):
    pass


class VendorResponse(VendorBase):
    vendor_id: int
    location_id: int
    food_id: Optional[int]


class Config:
    orm_mode = True