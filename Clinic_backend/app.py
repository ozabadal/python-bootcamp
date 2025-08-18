import os
import yaml
from flask import Flask
from flasgger import Swagger
from Clinic_backend.config import Config
from Clinic_backend.database import db
from Auth.routes import auth_bp
from Admin.routes import admin_bp


def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(admin_bp, url_prefix="/admin")

    # Load and register Swagger docs
    swagger_path = os.path.join(os.path.dirname(__file__), "swagger.yml")
    if os.path.exists(swagger_path):
        with open(swagger_path, "r") as f:
            swagger_template = yaml.safe_load(f)
        Swagger(app, template=swagger_template)
    else:
        Swagger(app)  # fallback to default

    # Initialize DB tables (only for dev/demo; use migrations in prod)
    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)