from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from extensions import db
from Admin.models.user import User, Role
from Admin.schemas.user_schema import UserRegisterSchema, UserLoginSchema, UserOutSchema
from common.utils import hash_password, verify_password
from functools import wraps


auth_bp = Blueprint("auth", __name__)

# --- RBAC decorator ---

def roles_required(*roles):
    def decorator(fn):
        @wraps(fn)
        @jwt_required()
        def wrapper(*args, **kwargs):
            claims = get_jwt()
            role = claims.get("role")
            if role not in roles:
                return jsonify({"msg": "Forbidden: insufficient role"}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator


# --- Auth routes ---
@auth_bp.post("/register")
def register():
    schema = UserRegisterSchema()
    data = schema.load(request.get_json() or {})

    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"msg": "Email already registered"}), 409

    user = User(
        email=data["email"],
        password_hash=hash_password(data["password"]),
        role=data["role"],
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
        is_active=True,
    )
    db.session.add(user)
    db.session.commit()

    return UserOutSchema().jsonify(user), 201


@auth_bp.post("/login")
def login():
    schema = UserLoginSchema()
    data = schema.load(request.get_json() or {})

    user = User.query.filter_by(email=data["email"]).first()
    if not user or not verify_password(user.password_hash, data["password"]):
        return jsonify({"msg": "Invalid credentials"}), 401

    additional_claims = {"role": user.role.value, "user_id": user.id}
    token = create_access_token(identity=str(user.id), additional_claims=additional_claims)
    return jsonify({"access_token": token})