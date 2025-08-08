from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from app.database import db

class Department(db.Model):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(120), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())
