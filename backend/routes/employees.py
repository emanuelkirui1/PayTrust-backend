from flask import Blueprint, request, jsonify

employees_bp = Blueprint("employees_bp", __name__)

employees = []

@employees_bp.route("/", methods=["POST"])
def add_employee():
    data = request.json
    data["id"] = len(employees) + 1
    employees.append(data)
    return jsonify({"message": "Employee added", "employee": data})

@employees_bp.route("/", methods=["GET"])
def get_employees():
    return jsonify(employees)

@employees_bp.route("/<int:id>", methods=["PUT"])
def update_employee(id):
    employees[id-1].update(request.json)
    return jsonify({"message": "Employee updated", "employee": employees[id-1]})

@employees_bp.route("/<int:id>", methods=["DELETE"])
def delete_employee(id):
    employees[:] = [e for e in employees if e["id"] != id]
    return jsonify({"message": "Employee removed"})
