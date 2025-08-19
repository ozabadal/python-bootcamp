from clinic_backend.database import db
from clinic_backend.doctor.models.availability import Availability

def create_availability(doctor_id, start_time, end_time):

    availability = Availability(
        doctor_id=doctor_id,
        start_time=start_time,
        end_time=end_time
    )
    db.session.add(availability)
    db.session.commit()
    return availability


def list_availability(doctor_id):
    query = Availability.query
    if doctor_id:
        query = query.filter_by(doctor_id=doctor_id)
    return query.all()