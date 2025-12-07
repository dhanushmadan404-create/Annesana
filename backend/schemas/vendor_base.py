from pydantic import BaseModel

class vendor_base(BaseModel):
    vendor_name: str
    cart_name: str
    food_type: str
    phone_number: str
    langitude: float
    latitude: float
    cart_image: str
    menu_list: str
    opening_time: str
    closing_time: str

class vendor_create(vendor_base):
    pass

class vendor_response(vendor_base):
    vendor_id: int
    location_id: int

    class Config:
        orm_mode = True
