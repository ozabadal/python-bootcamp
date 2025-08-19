from Clinic_backend.Appointment.models.appointment import Appointment
from Clinic_backend.Doctor.models.availability import Availability
from flask import Blueprint, request, jsonify
from Clinic_backend.database import db
from Clinic_backend.common.models.user import Role


def book_appointment(member_id, doctor_id, appointment_time):

    appointment = Appointment(
        doctor_id=doctor_id,
        member_id=member_id,
        appointment_time=appointment_time,
    )
    db.session.add(appointment)
    db.session.commit()
    return appointment


def list_appointments(user_id, user_role):
    query = Appointment.query
    if user_role == Role.MEMBER.value:
        query = query.filter_by(member_id=user_id)
    elif user_role == Role.DOCTOR.value:
        query = query.filter_by(doctor_id=user_id)

    return query.all()
