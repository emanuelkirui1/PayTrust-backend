from flask import Blueprint, request, jsonify
from utils.payrollCalculator import calculate_payroll

payroll_bp = Blueprint("payroll_bp", __name__)

@payroll_bp.route("/", methods=["POST"])
def run_payroll():
    data = request.json
    result = calculate_payroll(data["basic"], data.get("allowances",0), data.get("deductions",0))
    return jsonify({"message":"Payroll calculated","result":result})
