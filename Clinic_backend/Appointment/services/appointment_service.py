from Clinic_backend.Appointment.repository import appointment_repository

def book_appointment(member_id, doctor_id, appointment_time):
    appointment = appointment_repository.book_appointment(member_id, doctor_id, appointment_time)
    return appointment


def list_appointments(user_id, user_role):
    appointments = appointment_repository.list_appointments(user_id, user_role)
    return appointments