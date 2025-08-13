from Clinic_backend.Admin.models.user import User, Role
from Clinic_backend.database import db
from Clinic_backend.common.utils import hash_password, verify_password
from Clinic_backend.common.jwt_handler import create_access_token

def register_user(name, email, password, role=Role.MEMBER):
    if User.query.filter_by(email=email).first():
        raise ValueError("Email already registered")

    user = User(
        name=name,
        email=email,
        password_hash=hash_password(password),
        role=role
    )
    db.session.add(user)
    db.session.commit()
    return user

def login_user(email, password):
    user = User.query.filter_by(email=email).first()
    if not user or not verify_password(password, user.password_hash):
        raise ValueError("Invalid credentials")
    
    token = create_access_token(data={"user_id": user.id, "role": user.role.value})
    return token, user
