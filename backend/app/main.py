from fastapi import FastAPI


# Import all routers
from router import user, food, vendor, location, favorite, review

# Create FastAPI application instance
app = FastAPI()


# Include all routers with API prefix
app.include_router(user.router)
app.include_router(food.router)
app.include_router(vendor.router)
app.include_router(location.router )
app.include_router(favorite.router)
app.include_router(review.router )
