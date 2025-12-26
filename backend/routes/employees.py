from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from middleware.company_scope import company_required

employees_bp = Blueprint("employees_bp", __name__)

@employees_bp.route("/", methods=["GET"])
@jwt_required()
@company_required
def get_employees(company_id):
    return jsonify({"message": f"Employees for company {company_id}"}), 200

