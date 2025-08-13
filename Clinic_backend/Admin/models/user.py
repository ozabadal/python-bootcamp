from datetime import datetime
from enum import Enum
from Clinic_backend.database import db
from Clinic_backend.common.utils import generate_password_hash, check_password_hash

class Role(Enum):
    ADMIN = "ADMIN"
    DOCTOR = "DOCTOR"
    MEMBER = "MEMBER"

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum(Role), nullable=False, default=Role.MEMBER)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f"<User {self.email} ({self.role.value})>"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
