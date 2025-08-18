from Clinic_backend.Admin.repository import department_repository

def create_department(name: str):
    normalized_name = name.strip().lower()
    return department_repository.create_department(normalized_name)

def list_departments():
    return department_repository.list_departments()
