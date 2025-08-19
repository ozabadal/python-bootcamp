from clinic_backend.common.models.user import User
from clinic_backend.database import db

def create_user(name, email, password, role):
    if User.query.filter_by(email=email).first():
        raise ValueError("Email already registered")

    user = User(
        name=name,
        email=email,
        role=role
    )
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return user

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()
