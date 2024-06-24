import os

class Config:
    SECRET_KEY = 'secret_key_AUTHSERVICE'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/auth_db'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    