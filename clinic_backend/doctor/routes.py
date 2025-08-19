from flask import Blueprint, request, jsonify
from clinic_backend.doctor.services import availability_service
from clinic_backend.doctor.schemas.availability_schema import availability_schema, availabilities_schema
from clinic_backend.common.rbac import role_required
from clinic_backend.common.models.user import Role

availability_bp = Blueprint("availability", __name__)


@availability_bp.route("/", methods=["POST"])
@role_required(Role.DOCTOR)
def create_availability(user_id, user_role):
    data = request.get_json()
    data['doctor_id'] = user_id
    try:
        validated = availability_schema.load(data)
        availability = availability_service.create_availability(validated["doctor_id"], validated["start_time"],
                                                                validated["end_time"])
        return jsonify(availability_schema.dump(availability)), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@availability_bp.route("/", methods=["GET"])
@role_required(Role.MEMBER, Role.DOCTOR, Role.ADMIN)
def list_availability(user_id, user_role):
    try:
        availabilities = availability_service.list_availability(doctor_id=user_id)
        return jsonify(availabilities_schema.dump(availabilities))
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
