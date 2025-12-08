from DB.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Food(Base):
    __tablename__ = "foods"
    food_id = Column(Integer, primary_key=True, index=True)
    food_name = Column(String, nullable=False)
    food_image = Column(String, nullable=True)
    vendors = relationship("Vendor", back_populates="food")