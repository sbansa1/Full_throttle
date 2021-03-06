from datetime import datetime
import requests


def format_time_stamp(date_time):
    """This method gets me the hours in AM and PM"""
    timestamp = datetime.strptime(
        str((date_time)), "%Y-%m-%d %H:%M:%S.%f").strftime("%b %d %Y %I%p")
    return timestamp


def get_current_timezone_by_ip():
    req = requests.get("http://ipinfo.io/json")
    data = req.json()
    return data["timezone"]
