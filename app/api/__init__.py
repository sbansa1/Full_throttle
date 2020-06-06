from flask_restx import Api
from app.api.trial_user_api import test_namespace


api = Api(version=1.0, description="A Test Api for Full-Throttle Labs", doc="/doc")

api.add_namespace(test_namespace)
