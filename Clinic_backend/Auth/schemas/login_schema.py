from marshmallow import Schema, fields

class LoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(load_only=True, required=True)


login_schema = LoginSchema()
