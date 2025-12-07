# from DB.database import Base
# from sqlalchemy import Column,String,Integer,Boolean,TIMESTAMP,ForeignKey,Numeric

# class reviews(Base):
#     __tablename__="reviews"

#     review_id=Column(Integer,index=True, primary_key=True)
#     user_id=Column(Integer,ForeignKey("users.user_id"))
#     rating=Column(Integer)
#     comment=Column(String)
#     created_at=Column(TIMESTAMP)
#     vendor_id=Column(Integer,ForeignKey("vendors.vendor_id"))
