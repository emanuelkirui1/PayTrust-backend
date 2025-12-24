from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime

class PayrollRun(Base):
    __tablename__ = "payroll_runs"

    id = Column(Integer, primary_key=True)
    month = Column(String)
    status = Column(String, default="DRAFT")  # DRAFT | APPROVED
    created_at = Column(DateTime, default=datetime.utcnow)
