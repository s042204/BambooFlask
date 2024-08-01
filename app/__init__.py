from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_object('config.development.DevelopmentConfig')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')

    db.init_app(app)

    from app.models import Employees

    with app.app_context():
        db.create_all()

    from app.routes import auth_bp, employees_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(employees_bp, url_prefix='/api')

    return app
