from fastapi import FastAPI
from DB.database import engine, Base


# import vendor routers
from routers.vendor import router as vendors_router

# import favorites routers
from routers.favorites import router as favorites_router

# import review routers
from routers.review import router as review_router

from routers.user import router as users_router

app = FastAPI(title="Annesana API")


# create tables (only for development; in production use migrations)
Base.metadata.create_all(bind=engine)


app.include_router(vendors_router, prefix="/vendors", tags=["vendors"])

app.include_router(favorites_router, prefix="/favorites", tags=["Favorites"])


app.include_router(review_router, prefix="/reviews", tags=["Reviews"])


# Routers
app.include_router(users_router, prefix="/users", tags=["Users"])