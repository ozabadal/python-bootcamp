from Clinic_backend.common.models.user import Role
from Clinic_backend.Admin.models.doctor_department import DoctorDepartment
from Clinic_backend.database import db
from Clinic_backend.Admin.repository import user_repository

def create_doctor(name, email, password):
    return user_repository.create_user(name, email, password, role=Role.DOCTOR)


# TODO - denormalize assign_doctor_to_department function
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