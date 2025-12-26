from flask import Blueprint, request, jsonify
import pyotp
from flask_jwt_extended import jwt_required, get_jwt_identity

twofa_bp = Blueprint("twofa_bp", __name__)

@twofa_bp.route("/2fa/setup", methods=["GET"])
@jwt_required()
def setup():
    user = get_jwt_identity()
    secret = pyotp.random_base32()
    otp_uri = pyotp.totp.TOTP(secret).provisioning_uri(user["email"], issuer_name="PayTrust Payroll")
    return jsonify({"secret": secret, "otp_uri": otp_uri})

@twofa_bp.route("/2fa/verify", methods=["POST"])
@jwt_required()
def verify():
    data = request.json
    secret = data.get("secret")
    token = data.get("token")
    if pyotp.TOTP(secret).verify(token):
        return jsonify({"verified": True, "message": "2FA passed"})
    return jsonify({"verified": False, "message": "Invalid code"}), 400
