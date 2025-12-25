from flask import Blueprint, request, jsonify
import pyotp
from flask_jwt_extended import jwt_required

twofa_bp = Blueprint("twofa_bp", __name__)
secret_key = pyotp.random_base32()

@twofa_bp.route("/generate-otp", methods=["GET"])
@jwt_required()
def generate_otp():
    otp = pyotp.TOTP(secret_key).now()
    return jsonify({"otp": otp})

@twofa_bp.route("/verify-otp", methods=["POST"])
def verify_otp():
    otp = request.json.get("otp")
    if pyotp.TOTP(secret_key).verify(otp):
        return jsonify({"success": True, "message": "OTP verified"})
    return jsonify({"success": False, "message": "Invalid OTP"}), 400
