from Clinic_backend.database import db

class Department(db.Model):
    __tablename__ = "departments"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f"<Department {self.name}>"