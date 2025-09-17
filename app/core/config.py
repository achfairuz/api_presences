import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    APP_NAME: str = os.getenv("APP_NAME", "FastAPI Application")
    DEBUG: bool = os.getenv("APP_DEBUG", "False").lower() in ("true", "1", "t")
    DATABASE_URL: str = os.getenv("DATABASE_URL")

settings = Settings()
