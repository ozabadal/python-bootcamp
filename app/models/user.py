from datetime import datetime
import enum
from sqlalchemy.orm import Mapped, mapped_column
from app.database import db

class Role(enum.Enum):
    ADMIN = "ADMIN"
    DOCTOR = "DOCTOR"
    MEMBER = "MEMBER"

class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(120), nullable=False)
    email: Mapped[str] = mapped_column(db.String(120), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(db.String(255), nullable=False)
    role: Mapped[Role] = mapped_column(db.Enum(Role), nullable=False, default=Role.MEMBER)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())
