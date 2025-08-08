from marshmallow import Schema, fields

class DepartmentSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)

department_schema = DepartmentSchema()
departments_schema = DepartmentSchema(many=True)
