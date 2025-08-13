from Clinic_backend.Admin.repository import department_repository

def create_department(name):
    return department_repository.create_department(name)

def list_departments():
    return department_repository.list_departments()
