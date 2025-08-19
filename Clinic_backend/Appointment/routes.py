from flask import Blueprint, request, jsonify
from Clinic_backend.Appointment.services import appointment_service
from Clinic_backend.Appointment.schemas.appointment_schema import appointment_schema, appointments_schema
from Clinic_backend.common.rbac import role_required
from Clinic_backend.common.models.user import Role


appointment_bp = Blueprint("appointment", __name__)


@appointment_bp.route("/", methods=["POST"])
@role_required(Role.MEMBER)
def book_appointment(user_id, user_role):
    data = request.get_json()
    data['member_id'] = user_id
    try:
        validated = appointment_schema.load(data)
        appointment = appointment_service.book_appointment(validated["member_id"], validated["doctor_id"],
                                                                validated["appointment_time"])
        return jsonify(appointment_schema.dump(appointment)), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@appointment_bp.route("/", methods=["GET"])
@role_required(Role.MEMBER, Role.DOCTOR, Role.ADMIN)
def list_appointments(user_id, user_role):
    try:
        appointments = appointment_service.list_appointments(user_id, user_role)
        return jsonify(appointments_schema.dump(appointments))
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
