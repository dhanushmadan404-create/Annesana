from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from DB.database import SessionLocal, engine, Base
from schemas.user import UserBase, UserResponse
from models.user import Users

app = FastAPI()
Base.metadata.create_all(bind=engine)

def connect_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users", response_model=UserResponse)
def create_user(new_user: UserBase, dbs: Session = Depends(connect_db)):
    u = Users(
        email=new_user.email,
        created_at=new_user.created_at,
        password_hash=new_user.password_hash,
        role=new_user.role
    )
    dbs.add(u)
    dbs.commit()
    dbs.refresh(u)
    return u
