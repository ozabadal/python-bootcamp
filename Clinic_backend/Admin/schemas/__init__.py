from .department_schema import department_schema, departments_schema
from .doctor_department_schema import (
    doctor_department_schema,
    doctor_assign_schema,
)
from .user_schema import user_schema, users_schema

__all__ = [
    "department_schema",
    "departments_schema",
    "doctor_department_schema",
    "doctor_assign_schema",
    "user_schema",
    "users_schema",
]
