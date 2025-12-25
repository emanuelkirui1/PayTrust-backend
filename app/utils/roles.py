from flask_jwt_extended import get_jwt
from flask import jsonify

def role_required(roles):
    def wrapper(fn):
        def decorated(*args, **kwargs):
            claims = get_jwt()
            if claims.get("role") not in roles:
                return jsonify({"error":"Access denied"}), 403
            return fn(*args, **kwargs)
        return decorated
    return wrapper
