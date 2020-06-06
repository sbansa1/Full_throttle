from app.api.utils.db_utils import ResourceMixin
from app.api.utils.utils_func import get_current_timezone_by_ip
from app.extensions import db
from datetime import datetime


class User(db.Model, ResourceMixin):
    """This creates a User Model"""

    id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    tz = db.Column(db.String(20), nullable=False)
    activity_log = db.relationship("ActivityPeriods", backref="user", lazy="dynamic")

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    @staticmethod
    def get_user_by_id(user_id):
        result = (
            db.session.query(User)
            .join(ActivityPeriods)
            .filter(ActivityPeriods.user_id == user_id)
            .all()
        )
        return result


class ActivityPeriods(db.Model, ResourceMixin):
    """Model class for activity Periods"""

    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.String(100), nullable=False)
    end_time = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.String(10), db.ForeignKey("user.id"))

    def __init__(self, *args, **kwargs):
        super(ActivityPeriods, self).__init__(*args, **kwargs)
