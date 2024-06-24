import os


class Config:
    SECRET_KEY = 'secret_key_ORDERSERVICE'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/order_db'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/ecommerce_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
