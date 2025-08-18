from Clinic_backend.Auth.repository import user_repository
from Clinic_backend.common.models.user import Role
from Clinic_backend.common.utils import verify_password
from Clinic_backend.common.jwt_handler import create_access_token

def register_user(name, email, password):
    return user_repository.create_user(name, email, password, role=Role.MEMBER)

def login_user(email, password):
    user = user_repository.get_user_by_email(email=email)
    if not user or not verify_password(password, user.password_hash):
        raise ValueError("Invalid credentials")
    
    token = create_access_token(data={"user_id": user.id, "role": user.role.value})
    return token, user
