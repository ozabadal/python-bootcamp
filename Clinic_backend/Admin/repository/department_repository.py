from Clinic_backend.Admin.models.department import Department
from Clinic_backend.database import db

def create_department(name):
    if Department.query.filter_by(name=name).first():
        raise ValueError("Department already exists")
    department = Department(name=name)
    db.session.add(department)
    db.session.commit()
    return department

def list_departments():
    return Department.query.all()
