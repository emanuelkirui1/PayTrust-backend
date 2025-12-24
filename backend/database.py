from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config

connect_args = {}
if Config.DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

engine = create_engine(
    Config.DATABASE_URL,
    connect_args=connect_args
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
