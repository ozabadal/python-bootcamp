from datetime import datetime
from Clinic_backend.database import db

class Availability(db.Model):
    __tablename__ = "availabilities"

    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.now())

    doctor = db.relationship("User", backref="availabilities")

    def __repr__(self):
        return f"<Availability doctor_id={self.doctor_id}, {self.start_time} - {self.end_time}>"
