from database import SessionLocal
from models.audit_log import AuditLog

def log_action(user_id, action):
    db = SessionLocal()
    log = AuditLog(user_id=user_id, action=action)
    db.add(log)
    db.commit()
    db.close()
