from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity

def company_filter(query):
    user = get_jwt_identity()
    return query.filter_by(company_id=user.get("company_id"))
