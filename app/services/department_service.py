from app.models.department import Department
from app.database import db

def create_department(name):
    if Department.query.filter_by(name=name).first():
        raise ValueError("Department already exists")
    dept = Department(name=name)
    db.session.add(dept)
    db.session.commit()
    return dept

def list_departments():
    return Department.query.all()
