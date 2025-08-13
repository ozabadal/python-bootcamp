from functools import wraps
from flask import request, jsonify
from Clinic_backend.common.jwt_handler import decode_access_token

def role_required(*roles):
    def wrapper(fn):
        @wraps(fn)
        def decorated(*args, **kwargs):
            auth_header = request.headers.get("Authorization")
            if not auth_header or not auth_header.startswith("Bearer "):
                return jsonify({"error": "Unauthorized"}), 401
            
            token = auth_header.split(" ")[1]
            payload = decode_access_token(token)
            if not payload:
                return jsonify({"error": "Invalid or expired token"}), 401

            user_role = payload.get("role")
            if user_role not in [role.value for role in roles]:
                return jsonify({"error": "Forbidden"}), 403

            return fn(*args, **kwargs)
        return decorated
    return wrapper
