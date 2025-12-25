from flask import Blueprint, request, jsonify
from app.services.paye import calculate_paye

payroll_bp = Blueprint("payroll_bp", __name__)

@payroll_bp.route("/calculate", methods=["POST"])
def calc():
    data = request.get_json()
    tax = calculate_paye(data["country"], data["salary"])
    return jsonify({"salary": data["salary"], "tax": tax})
