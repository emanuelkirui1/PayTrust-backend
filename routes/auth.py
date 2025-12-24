from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from database import SessionLocal
from models.user import User

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    db = SessionLocal()

    user = db.query(User).filter_by(email=data["email"]).first()
    if not user or not user.check_password(data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity={"id": user.id, "role": user.role})
    return jsonify({"access_token": token})

from flask_jwt_extended import jwt_required, get_jwt_identity
from services.rbac import role_required
from models.audit_log import AuditLog

@auth_bp.route("/audit", methods=["GET"])
@jwt_required()
@role_required("superadmin")
def audit_logs():
    db = SessionLocal()
    logs = db.query(AuditLog).all()
    db.close()

    return jsonify([{
        "user_id": l.user_id,
        "action": l.action,
        "timestamp": l.timestamp.isoformat()
    } for l in logs])
