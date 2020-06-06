from app.api.trial_user_api import test_namespace
from flask_restx import fields


test_model_child = test_namespace.model(
    "ActivityPeriods",
    {
        "start_time": fields.String(required=True),
        "end_time": fields.String(required=True),
    },
)

test_model = test_namespace.model(
    "User",
    {
        "id": fields.String(readOnly=True),
        "name": fields.String(required=True),
        "tz": fields.String(required=True),
        "activity_log": fields.List(fields.Nested(test_model_child)),
    },
)
