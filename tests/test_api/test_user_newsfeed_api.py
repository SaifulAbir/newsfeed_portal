import unittest
import requests
from django.contrib.auth.models import User
from settings.models import Settings
from tests.config import MAIN_URL, USERNAME
from tests.test_api.common import signin


NEWSFEED_URL = f'{MAIN_URL}/api/news-feed/'


class TestNewsFeed(unittest.TestCase):
    def setUp(self) -> None:
        data = signin()
        self.access_token = data['access']

    def test__when_valid_settings_data_are_given__should_pass(self):
        resp = requests.get(NEWSFEED_URL, headers={'Authorization': 'Bearer ' + self.access_token})
        self.assertEqual(resp.status_code, 200)

    def tearDown(self):
        user = User.objects.get(username=USERNAME)
        Settings.objects.get(user=user).delete()
        user.delete()


if __name__ == '__main__':
    unittest.main()