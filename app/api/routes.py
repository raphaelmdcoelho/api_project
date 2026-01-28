"""API routes."""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.schemas import UserResponse

router = APIRouter()


@router.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok"}


@router.get("/users", response_model=list[UserResponse])
async def get_users(db: Session = Depends(get_db)):
    """Get all users."""
    return db.query(User).all()
