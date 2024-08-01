import os
from dotenv import load_dotenv

load_dotenv()

class DevelopmentConfig:
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URI', 'sqlite:///dev.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
