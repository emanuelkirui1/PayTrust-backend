from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from database import SessionLocal
from models.company import Company
from services.rbac import role_required

companies_bp = Blueprint("companies", __name__)

@companies_bp.route("/", methods=["POST"])
@jwt_required()
@role_required("superadmin")
def create_company():
    db = SessionLocal()
    data = request.json

    company = Company(name=data["name"])
    db.add(company)
    db.commit()

    return {"message": "Company created", "id": company.id}
