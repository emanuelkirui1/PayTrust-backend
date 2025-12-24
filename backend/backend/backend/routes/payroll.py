from flask import Blueprint, jsonify

payroll_bp = Blueprint("payroll", __name__)

@payroll_bp.route("/", methods=["GET"])
def home():
    return jsonify({"message": "PayTrust backend running successfully"})
