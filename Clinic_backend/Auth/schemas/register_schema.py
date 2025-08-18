from marshmallow import Schema, fields

class RegisterSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(load_only=True, required=True)

register_schema = RegisterSchema()
