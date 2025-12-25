from flask_jwt_extended import get_jwt_identity, jwt_required
from functools import wraps
from flask import jsonify

def role_required(roles):
    def wrapper(fn):
        @wraps(fn)
        @jwt_required()
        def decorated(*args, **kwargs):
            user = get_jwt_identity()
            if user['role'] not in roles:
                return jsonify({"error": "Forbidden - insufficient role"}), 403
            return fn(*args, **kwargs)
        return decorated
    return wrapper
