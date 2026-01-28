"""User database model."""
from sqlalchemy import Column, Integer, String, Date
from app.database import Base


class User(Base):
    """User model."""
    
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    birthdate = Column(Date, nullable=False)
    gender = Column(String, nullable=False)
