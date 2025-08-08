from flask import Flask, request, jsonify
from flasgger import Swagger
from app.config import Config
from app.database import db
from app.services.auth_service import register_user, login_user
from app.services.department_service import create_department, list_departments
from app.services.user_service import create_doctor, assign_doctor_to_department
from app.schemas.department_schema import department_schema, departments_schema
from app.schemas.user_schema import user_schema
from app.schemas.doctor_department_schema import doctor_department_schema, doctor_assign_schema

from app.utils.rbac import role_required
from app.models.user import Role

import os
import yaml

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize DB
db.init_app(app)

# Load and register Swagger docs from YAML
swagger_path = os.path.join(os.path.dirname(__file__), "swagger.yml")
with open(swagger_path, "r") as f:
    swagger_template = yaml.safe_load(f)
Swagger(app, template=swagger_template)


# Routes
@app.route("/auth/register", methods=["POST"])
def register():
    data = request.get_json()
    if not all(k in data for k in ("name", "email", "password")):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        user = register_user(data["name"], data["email"], data["password"])
        return jsonify(user_schema.dump(user)), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route("/auth/login", methods=["POST"])
def login():
    data = request.get_json()
    if not all(k in data for k in ("email", "password")):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        token, user = login_user(data["email"], data["password"])
        return jsonify({
            "access_token": token,
            "user": user_schema.dump(user)
        }), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 401


@app.route("/admin/departments", methods=["POST"])
@role_required(Role.ADMIN)
def add_department():
    data = request.get_json()
    if "name" not in data:
        return jsonify({"error": "Missing 'name' field"}), 400

    try:
        dept = create_department(data["name"])
        return jsonify(department_schema.dump(dept)), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route("/admin/departments", methods=["GET"])
@role_required(Role.ADMIN)
def get_departments():
    depts = list_departments()
    return jsonify(departments_schema.dump(depts)), 200


@app.route("/admin/doctors", methods=["POST"])
@role_required(Role.ADMIN)
def add_doctor():
    data = request.get_json()
    try:
        doctor = create_doctor(data["name"], data["email"], data["password"])
        return jsonify(user_schema.dump(doctor)), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route("/admin/doctors/assign", methods=["POST"])
@role_required(Role.ADMIN)
def assign_doctor():
    data = request.get_json()
    try:
        validated = doctor_assign_schema.load(data) 
        assignment = assign_doctor_to_department(
            validated["doctor_id"], validated["department_id"]
        )
        return jsonify(doctor_department_schema.dump(assignment)), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Initialize DB tables
with app.app_context():
    db.create_all()

# Run server
if __name__ == "__main__":
    app.run(debug=True)
