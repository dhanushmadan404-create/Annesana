from DB.database import Base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship


class Location(Base):
    __tablename__ = "locations"
    location_id = Column(Integer, primary_key=True, index=True)
    location_name = Column(String, nullable=False)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    vendors = relationship("Vendor", back_populates="location", cascade="all, delete-orphan")