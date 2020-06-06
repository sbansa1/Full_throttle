from flask.cli import FlaskGroup
from app import create_app
from app.extensions import db
from app.api.trial_user_api.model import User,ActivityPeriods

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command("create_db")
def create_db():
    """This creates the database"""
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    """seeds the database"""
    user_data = dict(id="W012A3CDE",name="Egon Spengler",tz="America/Los_Angeles")
    user1 = User(**user_data)
    db.session.add(user1)

    activity_log_data1_user1 = dict(start_time="Feb 1 2020  1:33PM",end_time="Feb 1 2020 1:54PM",user_id="W012A3CDE")
    activity1 = ActivityPeriods(**activity_log_data1_user1)
    db.session.add(activity1)
    activity_log_data2_user1 = dict(start_time="Mar 1 2020  11:11AM",end_time="Mar 1 2020 2:00PM",user_id="W012A3CDE")
    activity2 = ActivityPeriods(**activity_log_data2_user1)
    db.session.add(activity2)

    activity_log_data3_user1 = dict(start_time="Mar 16 2020  5:33PM",end_time="Mar 16 2020 8:02PM",user_id="W012A3CDE")
    activity3 = ActivityPeriods(**activity_log_data3_user1)
    db.session.add(activity3)

    user_data = dict(id="W07QCRPA4", name="Glinda Southgood",tz="Asia/Kolkata")
    user2 = User(**user_data)
    db.session.add(user2)

    activity_log_data1_user2 = dict(start_time="Feb 1 2020  1:33PM", end_time="Feb 1 2020 1:54PM", user_id="W07QCRPA4")
    activity1 = ActivityPeriods(**activity_log_data1_user2)
    db.session.add(activity1)
    activity_log_data2_user2 = dict(start_time="Mar 1 2020  11:11AM", end_time="Mar 1 2020 2:00PM", user_id="W07QCRPA4")
    activity2 = ActivityPeriods(**activity_log_data2_user2)
    db.session.add(activity2)

    activity_log_data3_user2 = dict(start_time="Mar 16 2020  5:33PM", end_time="Mar 16 2020 8:02PM",
                                    user_id="W07QCRPA4")
    activity3 = ActivityPeriods(**activity_log_data3_user2)
    db.session.add(activity3)

    db.session.commit()




if __name__=="__main__":
    cli()