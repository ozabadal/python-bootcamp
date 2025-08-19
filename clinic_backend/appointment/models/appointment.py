from datetime import datetime
from Clinic_backend.database import db

class Appointment(db.Model):
    __tablename__ = "appointments"

    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    appointment_time = db.Column(db.DateTime, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.now())

    doctor = db.relationship("User", foreign_keys=[doctor_id], backref="doctor_appointments")
    member = db.relationship("User", foreign_keys=[member_id], backref="member_appointments")

    __table_args__ = (
        db.UniqueConstraint("doctor_id", "appointment_time", name="uq_doctor_time"),
    )

    def __repr__(self):
        return f"<Appointment doctor_id={self.doctor_id}, member_id={self.member_id}, time={self.appointment_time}>"
