from marshmallow import Schema, fields

class DoctorDepartmentSchema(Schema):
    id = fields.Int(dump_only=True)
    doctor_id = fields.Int(required=True)
    department_id = fields.Int(required=True)

doctor_department_schema = DoctorDepartmentSchema()
doctor_departments_schema = DoctorDepartmentSchema(many=True)

class DoctorAssignSchema(Schema):
    doctor_id = fields.Int(required=True)
    department_id = fields.Int(required=True)

doctor_assign_schema = DoctorAssignSchema()