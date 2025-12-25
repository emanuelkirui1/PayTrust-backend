from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.utils.roles import role_required

admin_bp = Blueprint("admin_bp", __name__)

@admin_bp.route("/dashboard")
@jwt_required()
@role_required(["superadmin","admin"])
def admin_dashboard():
    return jsonify({"msg": "Welcome Admin"})
