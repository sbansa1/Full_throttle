import os


class BaseConfig(object):
    """Base class for the config"""

    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SECRET_KEY = "my_precious"


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestingConfig(BaseConfig):
    TESTING = True


class ProductionConfig(BaseConfig):
    """Not using it for now"""

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
