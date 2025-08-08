from sqlalchemy.orm import Mapped, mapped_column
from app.database import db

class DoctorDepartment(db.Model):
    __tablename__ = "doctor_departments"

    id: Mapped[int] = mapped_column(primary_key=True)
    doctor_id: Mapped[int] = mapped_column(db.ForeignKey("users.id"), nullable=False)
    department_id: Mapped[int] = mapped_column(db.ForeignKey("departments.id"), nullable=False)
