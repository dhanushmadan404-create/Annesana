# from DB.database import Base
# from sqlalchemy import Column,String,Integer,Boolean,TIMESTAMP,ForeignKey,Numeric

# class favorites(Base):
#     __tablename__="favorites"

#     favorite_id=Column(Integer,index=True, primary_key=True)
#     user_id=Column(Integer,ForeignKey("users.user_id"))
#     food_id=Column(Integer,ForeignKey("foods.food_id"))
#     created_at=Column(TIMESTAMP)