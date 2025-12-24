from sqlalchemy import Column, Integer, String, Float
from models import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    basic_salary = Column(Float, nullable=False)
    country = Column(String, default="KE")
    company_id = Column(Integer)
    kra_pin = Column(String, unique=True, nullable=False)
