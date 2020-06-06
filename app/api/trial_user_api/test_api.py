from flask_restx import Resource
from app.api.trial_user_api.model import User
from app.api.trial_user_api import test_namespace
from app.api.trial_user_api.schema.model_parser import test_model, test_model_child
from app.api.utils.utils_func import get_current_timezone_by_ip, format_time_stamp
import json
from flask_restx import marshal
from datetime import datetime


class TestApi(Resource):
    @test_namespace.marshal_with(test_model, as_list=True)
    def get(self, user_id):
        user = User.get_user_by_id(user_id=user_id)
        if not user:
            test_namespace.abort(404, f"User {user_id} does not exist")
        return user, 200


test_namespace.add_resource(TestApi, "/user/<user_id>")
