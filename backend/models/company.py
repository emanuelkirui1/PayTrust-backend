from database import Base
from sqlalchemy import Column, Integer, String

class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
