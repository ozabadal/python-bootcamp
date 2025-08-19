from marshmallow import Schema, fields

class AvailabilitySchema(Schema):
    id = fields.Int(dump_only=True)
    doctor_id = fields.Int(required=True)
    start_time = fields.DateTime(required=True)
    end_time = fields.DateTime(required=True)

availability_schema = AvailabilitySchema()
availabilities_schema = AvailabilitySchema(many=True)