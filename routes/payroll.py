from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from database import SessionLocal
from models.employee import Employee
from services.paye import kra_paye, ura_paye
from services.rbac import role_required

payroll_bp = Blueprint("payroll", __name__, url_prefix="/api/payroll")

@payroll_bp.route("/", methods=["GET"])
@jwt_required()
@role_required("superadmin", "admin")
def payroll():
    db = SessionLocal()
    employees = db.query(Employee).all()
    db.close()

    return jsonify([{
        "employee": f"{e.first_name} {e.last_name}",
        "gross": e.salary,
        "kra_paye": kra_paye(e.salary),
        "ura_paye": ura_paye(e.salary),
        "net": e.salary - kra_paye(e.salary) - ura_paye(e.salary)
    } for e in employees])

from flask import send_file
from services.pdf.payslip import generate_payslip

@payroll_bp.route("/<int:employee_id>/payslip", methods=["GET"])
@jwt_required()
@role_required("superadmin", "admin", "hr")
def payslip(employee_id):
    db = SessionLocal()
    employee = db.query(Employee).get(employee_id)
    db.close()

    payroll = {
        "gross": employee.salary,
        "kra_paye": kra_paye(employee.salary),
        "ura_paye": ura_paye(employee.salary),
        "net": employee.salary - kra_paye(employee.salary) - ura_paye(employee.salary)
    }

    pdf = generate_payslip(employee, payroll)
    return send_file(pdf, download_name="payslip.pdf", as_attachment=True)
