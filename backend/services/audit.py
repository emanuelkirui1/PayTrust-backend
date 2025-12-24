from database import SessionLocal
from models.audit_log import AuditLog

def log_action(user_id, action, endpoint):
    db = SessionLocal()
    db.add(AuditLog(
        user_id=user_id,
        action=action,
        endpoint=endpoint
    ))
    db.commit()
