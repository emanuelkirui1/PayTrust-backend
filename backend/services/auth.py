from flask import jsonify, request, Blueprint
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from database import SessionLocal
from models.user import User
from functools import wraps

auth_bp = Blueprint("auth", __name__)

def role_required(*roles):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            user = get_jwt_identity()
            if user["role"] not in roles:
                return jsonify({"error": "Permission denied"}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator


@auth_bp.route("/login", methods=["POST"])
def login():
    db = SessionLocal()
    data = request.get_json()
    user = db.query(User).filter_by(email=data["email"]).first()

    if not user or not user.check_password(data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity={"id": user.id, "role": user.role})
    return jsonify({"access_token": token})
