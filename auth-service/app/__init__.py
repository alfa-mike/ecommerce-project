from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
import os

db = SQLAlchemy()
migrate = Migrate()
# basdir = os.path.abspath(os.path.dirname(__file__))
# MIGRATION_DIR = os.path.join(basdir, 'migrations')

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
