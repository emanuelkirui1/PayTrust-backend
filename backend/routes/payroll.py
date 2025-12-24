from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

payroll_bp = Blueprint("payroll", __name__)

@payroll_bp.route("/", methods=["GET"])
@jwt_required()
def payroll_home():
    return jsonify({"status": "Payroll service running"})

from flask import send_file
from services.payslip import generate_payslip
from models.employee import Employee

@payroll_bp.route("/payslip/<int:employee_id>", methods=["GET"])
@jwt_required()
@role_required("superadmin", "admin")
def download_payslip(employee_id):
    db = SessionLocal()
    employee = db.query(Employee).get(employee_id)

    payroll = {
        "gross": employee.salary,
        "paye": calculate_paye(employee.salary, employee.country),
        "net": employee.salary - payroll["paye"]
    }

    path = generate_payslip(employee, payroll)
    return send_file(path, as_attachment=True)

from services.tax_engine import calculate_paye

@payroll_bp.route("/calculate/<int:employee_id>", methods=["GET"])
@jwt_required()
@role_required("superadmin", "admin")
def calculate_payroll(employee_id):
    db = SessionLocal()
    employee = db.query(Employee).get(employee_id)

    paye = calculate_paye(employee.salary, employee.country)
    net = employee.salary - paye

    return {
        "employee": employee.name,
        "country": employee.country,
        "gross": employee.salary,
        "paye": paye,
        "net": net
    }

from services.statutory import calculate_statutory

@payroll_bp.route("/full/<int:employee_id>", methods=["GET"])
@jwt_required()
@role_required("superadmin", "admin")
def full_payroll(employee_id):
    db = SessionLocal()
    employee = db.query(Employee).get(employee_id)

    paye = calculate_paye(employee.salary, employee.country)
    statutory = calculate_statutory(employee.salary, employee.country)

    deductions = paye + statutory["nssf"] + statutory["nhif"]
    net = employee.salary - deductions

    return {
        "employee": employee.name,
        "country": employee.country,
        "gross": employee.salary,
        "paye": paye,
        "nssf": statutory["nssf"],
        "nhif": statutory["nhif"],
        "net": net
    }

from models.payroll_run import PayrollRun

@payroll_bp.route("/run/<string:month>", methods=["POST"])
@jwt_required()
@role_required("hr", "admin", "superadmin")
def create_payroll_run(month):
    db = SessionLocal()
    run = PayrollRun(month=month)
    db.add(run)
    db.commit()
    return {"message": f"Payroll run {month} created", "status": run.status}


@payroll_bp.route("/run/<int:run_id>/approve", methods=["POST"])
@jwt_required()
@role_required("admin", "superadmin")
def approve_payroll(run_id):
    db = SessionLocal()
    run = db.query(PayrollRun).get(run_id)
    run.status = "APPROVED"
    db.commit()
    return {"message": "Payroll approved"}

@payroll_bp.route("/run/<int:run_id>/calculate", methods=["GET"])
@jwt_required()
@role_required("admin", "superadmin")
def bulk_payroll(run_id):
    db = SessionLocal()
    employees = db.query(Employee).all()

    results = []
    for e in employees:
        paye = calculate_paye(e.salary, e.country)
        statutory = calculate_statutory(e.salary, e.country)
        net = e.salary - (paye + statutory["nssf"] + statutory["nhif"])

        results.append({
            "employee": e.name,
            "gross": e.salary,
            "net": net
        })

    return {"run_id": run_id, "results": results}

from models.payroll_run import PayrollRun

@payroll_bp.route("/run/<string:month>", methods=["POST"])
@jwt_required()
@role_required("hr", "admin", "superadmin")
def create_payroll_run(month):
    db = SessionLocal()
    run = PayrollRun(month=month)
    db.add(run)
    db.commit()
    return {"message": f"Payroll run {month} created", "status": run.status}


@payroll_bp.route("/run/<int:run_id>/approve", methods=["POST"])
@jwt_required()
@role_required("admin", "superadmin")
def approve_payroll(run_id):
    db = SessionLocal()
    run = db.query(PayrollRun).get(run_id)
    run.status = "APPROVED"
    db.commit()
    return {"message": "Payroll approved"}

@payroll_bp.route("/run/<int:run_id>/calculate", methods=["GET"])
@jwt_required()
@role_required("admin", "superadmin")
def bulk_payroll(run_id):
    db = SessionLocal()
    employees = db.query(Employee).all()

    results = []
    for e in employees:
        paye = calculate_paye(e.salary, e.country)
        statutory = calculate_statutory(e.salary, e.country)
        net = e.salary - (paye + statutory["nssf"] + statutory["nhif"])

        results.append({
            "employee": e.name,
            "gross": e.salary,
            "net": net
        })

    return {"run_id": run_id, "results": results}

from services.bank_export import generate_bank_csv
from flask import send_file

@payroll_bp.route("/run/<int:run_id>/bank-file", methods=["GET"])
@jwt_required()
@role_required("admin", "superadmin")
def bank_export(run_id):
    db = SessionLocal()
    employees = db.query(Employee).all()

    data = []
    for e in employees:
        paye = calculate_paye(e.salary, e.country)
        statutory = calculate_statutory(e.salary, e.country)
        net = e.salary - (paye + statutory["nssf"] + statutory["nhif"])
        data.append({"employee": e.name, "net": net})

    path = generate_bank_csv(data)
    return send_file(path, as_attachment=True)

from services.email_service import send_email

@payroll_bp.route("/payslip/<int:employee_id>/email", methods=["POST"])
@jwt_required()
@role_required("admin", "superadmin")
def email_payslip(employee_id):
    db = SessionLocal()
    employee = db.query(Employee).get(employee_id)

    paye = calculate_paye(employee.salary, employee.country)
    statutory = calculate_statutory(employee.salary, employee.country)

    payroll = {
        "gross": employee.salary,
        "paye": paye,
        "nssf": statutory["nssf"],
        "nhif": statutory["nhif"],
        "net": employee.salary - (paye + statutory["nssf"] + statutory["nhif"])
    }

    path = generate_payslip(employee, payroll)

    send_email(
        to=employee.email,
        subject="Your Payslip",
        body="Attached is your payslip from PayTrust.",
        attachment=path
    )

    return {"message": "Payslip emailed successfully"}
