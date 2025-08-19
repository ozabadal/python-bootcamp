from clinic_backend.common.models.user import Role
from clinic_backend.admin.models.doctor_department import DoctorDepartment
from clinic_backend.database import db
from clinic_backend.admin.repository import user_repository

def create_doctor(name, email, password):
    normalized_name = name.strip().lower()
    normalized_email = email.strip().lower()
    return user_repository.create_user(normalized_name, normalized_email, password, role=Role.DOCTOR)


# TODO - denormalize assign_doctor_to_department function
def assign_doctor_to_department(doctor_id, department_id):
    # Check if already assigned
    if DoctorDepartment.query.filter_by(doctor_id=doctor_id, department_id=department_id).first():
        raise ValueError("doctor already assigned to this department")

    assignment = DoctorDepartment(
        doctor_id=doctor_id,
        department_id=department_id
    )
    db.session.add(assignment)
    db.session.commit()
    return assignment