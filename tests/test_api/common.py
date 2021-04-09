import requests
from tests.config import USERNAME, EMAIL, PASSWORD
from tests.config_api import REGISTER_URL, SIGNIN_URL


def signup():
    signup_url = REGISTER_URL
    json = {
        'email': EMAIL,
        'username': USERNAME,
        'password': PASSWORD
    }
    resp = requests.post(signup_url, json=json)
    return resp.status_code


def signin():
    signin_url = SIGNIN_URL
    json = {
        'username': USERNAME,
        'password': PASSWORD
    }
    resp = requests.post(signin_url, json=json)
    if resp.status_code == 200:
        return resp.json()