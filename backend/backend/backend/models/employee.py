from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    basic_salary = Column(Float, nullable=False)
    kra_pin = Column(String, unique=True)
