from Clinic_backend.database import db

class DoctorDepartment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey("department.id"), nullable=False)
