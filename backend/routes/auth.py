from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from database import SessionLocal
from models.user import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    db = SessionLocal()

    user = db.query(User).filter(User.email == data["email"]).first()

    if not user or not user.check_password(data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(
        identity={"id": user.id, "role": user.role}
    )
    return jsonify(access_token=token)
