from DB.database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship


class Vendor(Base):
    __tablename__ = "vendors"


    vendor_id = Column(Integer, primary_key=True, index=True)
    vendor_name = Column(String, nullable=False)
    cart_name = Column(String, nullable=True)
    food_type = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    location_id = Column(Integer, ForeignKey("locations.location_id"), nullable=False)
    food_id = Column(Integer, ForeignKey("foods.food_id"), nullable=True)
    cart_image = Column(String, nullable=True)
    opening_time = Column(TIMESTAMP, nullable=True)
    closing_time = Column(TIMESTAMP, nullable=True)


    location = relationship("Location", back_populates="vendors")
    food = relationship("Food", back_populates="vendors")