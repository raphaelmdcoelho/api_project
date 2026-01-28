"""Application entry point."""
from fastapi import FastAPI

from app.config import settings
from app.database import Base, engine
from app.api.routes import router

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title=settings.app_title,
    version=settings.app_version,
    debug=settings.debug,
)

# Include routers
app.include_router(router, prefix="/api")


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": f"Welcome to {settings.app_title}"}
