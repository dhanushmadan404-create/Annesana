from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, TIMESTAMP
from sqlalchemy.orm import relationship
from database import Base
import enum

class UserRole(str, enum.Enum):
    user = "user"
    vendor = "vendor"

class User(Base):
    __tablename__ = "users"
    
    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False, default=UserRole.user)

    favorites = relationship("Favorite", back_populates="user")
    reviews = relationship("Review", back_populates="user")

class Favorite(Base):
    __tablename__ = "favorites"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    food_id = Column(Integer, ForeignKey("foods.food_id"), nullable=False)
    created_at = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="favorites")
    food = relationship("Food", back_populates="favorites")

class Review(Base):
    __tablename__ = "reviews"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    food_id = Column(Integer, ForeignKey("foods.food_id"), nullable=False)
    rating = Column(Integer, nullable=False)
    text = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="reviews")
    food = relationship("Food", back_populates="reviews")

class Food(Base):
    __tablename__ = "foods"
    
    food_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    vendor_id = Column(Integer, ForeignKey("vendors.vendor_id"), nullable=False)
    name = Column(String(255), nullable=False)
    image_url = Column(String(255))
    food_type = Column(String(100))
    phone_number = Column(String(15))

    favorites = relationship("Favorite", back_populates="food")
    reviews = relationship("Review", back_populates="food")
    vendor = relationship("Vendor", back_populates="foods")

class Vendor(Base):
    __tablename__ = "vendors"
    
    vendor_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)

    foods = relationship("Food", back_populates="vendor")
    locations = relationship("Location", back_populates="vendor")

class Location(Base):
    __tablename__ = "locations"
    
    location_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    latitude = Column(String(20))
    longitude = Column(String(20))
    vendor_id = Column(Integer, ForeignKey("vendors.vendor_id"), nullable=False)

    vendor = relationship("Vendor", back_populates="locations")
