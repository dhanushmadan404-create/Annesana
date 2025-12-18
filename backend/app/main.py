from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


# Import all routers
from router import user, food, vendor, location, favorite, review


# Create FastAPI application instance
app = FastAPI()

origins = [
    "http://127.0.0.1:5501",  # your frontend origin
    "http://localhost:5501"
]

app.mount("/static", StaticFiles(directory="/"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5501"],
    allow_credentials=True,
    allow_methods=["*"],     # ← allows OPTIONS automatically
    allow_headers=["*"],
)


# Include all routers with API prefix
app.include_router(user.router)
app.include_router(food.router)
app.include_router(vendor.router)
app.include_router(location.router )
app.include_router(favorite.router)
app.include_router(review.router )
