from pydantic import BaseModel, Field,ConfigDict
from datetime import datetime
from typing import Optional
from enum import Enum

# Define Role Enum for Pydantic
class UserRole(str, Enum):
    user = "user"
    vendor = "vendor"

# ==================== USER SCHEMAS ====================

class UserBase(BaseModel):
    email: str
    role: UserRole

class UserCreate(UserBase):
    password: str
    # created_at should be handled by server, not client
    # so we generally don't include it here

class UserResponse(UserBase):
    user_id: int
    created_at: datetime  # response includes created_at
    # DO NOT include password here

    model_config = ConfigDict(from_attributes=True)


# ==================== FAVORITE SCHEMAS ====================
class FavoriteBase(BaseModel):
    user_id_integer: int
    food_id_integer: int

class FavoriteCreate(FavoriteBase):
    pass

class FavoriteResponse(FavoriteBase):
    id: int
    favorite_id_serial: int
    created_at_timestamp_with_out_time_zone: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True)


# ==================== REVIEW SCHEMAS ====================
class ReviewBase(BaseModel):
    user_id: int
    food_id: int
    vendor_id: int  
    rating: int
    review_text: str

class ReviewCreate(ReviewBase):
    pass

class ReviewResponse(ReviewBase):
    review_id: int
    created_at: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True)


# ==================== FOOD SCHEMAS ====================
class FoodBase(BaseModel):
    food_name_character_varying_255: str
    food_image_url_character_varying_255: str
    food_type_character_varying_100: str
    phone_number_character_varying_15: str
    vendor_id_integer: int

class FoodCreate(FoodBase):
    pass

class FoodResponse(FoodBase):
    food_id: int
    food_id_serial: int
    
    model_config = ConfigDict(from_attributes=True)


# ==================== VENDOR SCHEMAS ====================
class VendorBase(BaseModel):
    vendor_name_character_varying_255: str
    qr_name_character_varying_255: str

class VendorCreate(VendorBase):
    pass

class VendorResponse(VendorBase):
    vendor_id: int
    vendor_id_serial: int
    qr_code_time_without_time_zone: Optional[datetime] = None
    qr_code_time_time_without_me_zone: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True)


# ==================== LOCATION SCHEMAS ====================

class LocationBase(BaseModel):
    location_name: str
    latitude: float
    longitude: float
    # Change this to Optional so it can handle None/NULL values
    vendor_id: Optional[int] = None

class LocationCreate(LocationBase):
    pass

class LocationResponse(LocationBase):
    location_id: int
   
    
    model_config = ConfigDict(from_attributes=True)