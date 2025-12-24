from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from database import SessionLocal
from models.employee import Employee
from services.rbac import role_required

employees_bp = Blueprint("employees", __name__, url_prefix="/api/employees")

@employees_bp.route("/", methods=["GET"])
@jwt_required()
@role_required("superadmin", "admin", "hr")
def list_employees():
    db = SessionLocal()
    employees = db.query(Employee).all()
    db.close()

    return jsonify([{
        "id": e.id,
        "first_name": e.first_name,
        "last_name": e.last_name,
        "salary": e.salary
    } for e in employees])

@employees_bp.route("/", methods=["POST"])
@jwt_required()
@role_required("superadmin", "admin")
def create_employee():
    data = request.json
    db = SessionLocal()

    employee = Employee(
        first_name=data["first_name"],
        last_name=data["last_name"],
        salary=data["salary"]
    )
    db.add(employee)
    db.commit()
    db.close()

    return jsonify({"message": "Employee created"}), 201

from flask_jwt_extended import get_jwt_identity
from services.audit import log_action
