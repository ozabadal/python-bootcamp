from Clinic_backend.Doctor.repository import availability_repository

def create_availability(doctor_id, start_time, end_time):
    return availability_repository.create_availability(doctor_id, start_time, end_time)


def list_availability(doctor_id):
    return availability_repository.list_availability(doctor_id)