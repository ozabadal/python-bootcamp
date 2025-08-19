from flask import Blueprint, request, jsonify
from clinic_backend.auth.services import auth_service
from clinic_backend.auth.schemas import register_schema, login_schema
from clinic_backend.common.schemas.user_schema import user_schema


auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    try:
        validated = register_schema.load(data)
        user = auth_service.register_user(validated["name"], validated["email"], validated["password"])
        return jsonify(user_schema.dump(user)), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    try:
        validated = login_schema.load(data)
        token, user = auth_service.login_user(validated["email"], validated["password"])
        return jsonify({
            "access_token": token,
            "user": user_schema.dump(user)
        }), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 401
