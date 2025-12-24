from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from database import SessionLocal
from models.employee import Employee

employees_bp = Blueprint(
    "employees",
    __name__,
    url_prefix="/api/employees"
)

@employees_bp.route("/", methods=["GET"])
@jwt_required()
def get_employees():
    db = SessionLocal()
    employees = db.query(Employee).filter(Employee.company_id == user["company_id"]).all()

    data = []
    for e in employees:
        data.append({
            "id": e.id,
            "first_name": e.first_name,
            "last_name": e.last_name,
            "salary": e.salary
        })

    db.close()
    return jsonify(data), 200


@employees_bp.route("/", methods=["POST"])
@jwt_required()
def create_employee():
    payload = request.get_json()

    db = SessionLocal()
    employee = Employee(
        first_name=payload["first_name"],
        last_name=payload["last_name"],
        salary=payload["salary"]
    )

    db.add(employee)
    db.commit()
    db.refresh(employee)
    db.close()

    return jsonify({"message": "Employee created"}), 201
