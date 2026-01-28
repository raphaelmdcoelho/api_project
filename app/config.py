"""Application configuration."""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""
    
    database_url: str = "sqlite:///./app.db"
    debug: bool = False
    app_title: str = "API"
    app_version: str = "0.1.0"
    
    class Config:
        env_file = ".env"


settings = Settings()
