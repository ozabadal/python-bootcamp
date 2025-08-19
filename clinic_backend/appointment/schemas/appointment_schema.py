from marshmallow import Schema, fields

class AppointmentSchema(Schema):
    id = fields.Int(dump_only=True)
    doctor_id = fields.Int(required=True)
    member_id = fields.Int(required=True)
    appointment_time = fields.DateTime(required=True)

appointment_schema = AppointmentSchema()
appointments_schema = AppointmentSchema(many=True)