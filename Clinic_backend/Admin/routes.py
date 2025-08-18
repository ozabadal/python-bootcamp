from flask import Blueprint, request, jsonify
from Clinic_backend.common.rbac import role_required
from Clinic_backend.Admin.services import department_service, user_service
from Clinic_backend.Admin.schemas import (
    department_schema,
    departments_schema,
    doctor_assign_schema,
    doctor_department_schema,
    user_schema,
)
from Clinic_backend.common.models.user import Role

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/departments", methods=["POST"])
@role_required(Role.ADMIN)
def create_department():
    data = request.get_json()
    try:
        validated = department_schema.load(data)
        dept = department_service.create_department(validated["name"])
        return jsonify(department_schema.dump(dept)), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@admin_bp.route("/departments", methods=["GET"])
@role_required(Role.ADMIN)
def list_departments():
    departments = department_service.list_departments()
    return jsonify(departments_schema.dump(departments))


# --- Doctor Onboarding ---
@admin_bp.route("/doctors", methods=["POST"])
@role_required(Role.ADMIN)
def onboard_doctor():
    data = request.get_json()
    try:
        validated = user_schema.load(data)
        doctor = user_service.create_doctor(validated["name"], validated["email"], validated["password"])
        return jsonify(user_schema.dump(doctor)), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


# --- Assign Doctor to Department ---
@admin_bp.route("/doctors/assign", methods=["POST"])
@role_required(Role.ADMIN)
def assign_doctor():
    data = request.get_json()
    try:
        validated = doctor_assign_schema.load(data)  # marshmallow validation
        assignment = user_service.assign_doctor_to_department(
            validated["doctor_id"], validated["department_id"]
        )
        return jsonify(doctor_department_schema.dump(assignment)), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400
