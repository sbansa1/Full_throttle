from flask_restx import Namespace

test_namespace = Namespace("test")

from app.api.trial_user_api import test_api
