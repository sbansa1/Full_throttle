from flask import Flask
import os

from app.api import api
from app.extensions import db


def create_app(script_info=None):
    """Creates an application instance"""

    app = Flask(__name__)
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)
    extensions(app)
    return app


def extensions(app):
    """Ties the applicaton instance to the exntesions required by the application"""
    db.init_app(app)
    api.init_app(app)
