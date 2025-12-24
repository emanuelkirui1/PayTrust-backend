from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    action = Column(String)
    endpoint = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
