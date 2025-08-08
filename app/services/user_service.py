from app.models.user import User, Role
from app.models.doctor_department import DoctorDepartment
from app.database import db
from app.utils.security import hash_password

def create_doctor(name, email, password):
    if User.query.filter_by(email=email).first():
        raise ValueError("Email already registered")

    doctor = User(
        name=name,
        email=email,
        password_hash=hash_password(password),
        role=Role.DOCTOR
    )
    db.session.add(doctor)
    db.session.commit()
    return doctor

def assign_doctor_to_department(doctor_id, department_id):
    # Check if already assigned
    if DoctorDepartment.query.filter_by(doctor_id=doctor_id, department_id=department_id).first():
        raise ValueError("Doctor already assigned to this department")

    assignment = DoctorDepartment(
        doctor_id=doctor_id,
        department_id=department_id
    )
    db.session.add(assignment)
    db.session.commit()
    return assignment
