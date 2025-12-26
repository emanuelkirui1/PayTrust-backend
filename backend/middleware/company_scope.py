from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from functools import wraps

def company_required(fn):
    @wraps(fn)
    @jwt_required()
    def wrapper(*args, **kwargs):
        user = get_jwt_identity()
        company_id = request.headers.get("X-Company-ID")

        if not company_id:
            return jsonify({"error":"Missing company header"}), 400
            
        if str(user.get("company_id")) != str(company_id):
            return jsonify({"error":"Access denied: wrong company"}), 403

        return fn(*args, company_id=company_id, **kwargs)
    return wrapper
