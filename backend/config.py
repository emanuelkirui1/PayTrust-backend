import os

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL")
    JWT_SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
