import unittest
import requests
from tests.config import MAIN_URL
from tests.test_api.common import signup, signin


SETTINGS_CREATE_URL = f'{MAIN_URL}/api/settings/create/'
SETTINGS_UPDATE_URL = f'{MAIN_URL}/api/settings/update/'
SETTINGS_DETAIL_URL = f'{MAIN_URL}/api/settings/details/'


class TestSettingsCreate(unittest.TestCase):
    def setUp(self) -> None:
        data = signup()
        if data == 201:
            data = signin()
            self.access_token = data['access']

    def test__when_everything_valid__should_pass(self):
        json = {
            "countries": "ae, us, cn",
            "sources": "cnn, google-news",
            "keywords": "covid, pandemic, daily"
        }
        resp = requests.post(SETTINGS_CREATE_URL, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 201)


class TestSettingsUpdate(unittest.TestCase):
    def setUp(self) -> None:
        data = signin()
        self.access_token = data['access']

    def test__when_all_data_valid__should_pass(self):
        json = {
            "countries": "us, de",
            "sources": "cnn, google-news",
            "keywords": "covid, pandemic, accident"
        }
        resp = requests.put(SETTINGS_UPDATE_URL, json=json, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)


class TestSettingsDetail(unittest.TestCase):
    def setUp(self) -> None:
        data = signin()
        self.access_token = data['access']

    def test__when_valid__should_pass(self):
        resp = requests.get(SETTINGS_DETAIL_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def test__without_access_token__should_failed(self):
        resp = requests.get(SETTINGS_DETAIL_URL)
        self.assertEqual(resp.status_code, 401)


if __name__ == '__main__':
    unittest.main()