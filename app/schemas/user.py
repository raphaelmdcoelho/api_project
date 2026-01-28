"""User Pydantic schemas."""
from datetime import date
from pydantic import BaseModel


class UserBase(BaseModel):
    """Base user schema."""
    
    name: str
    birthdate: date
    gender: str


class UserCreate(UserBase):
    """User creation schema."""
    
    pass


class UserResponse(UserBase):
    """User response schema."""
    
    id: int

    class Config:
        from_attributes = True
