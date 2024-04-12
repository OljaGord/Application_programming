import unittest
from freezegun import freeze_time
from task1.hello_word_with_day import app


class TestHelloWorldWithDay(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    def test__correct_username_day__correct_username_with_weekday(self):
        username = 'username'
        response = self.app.get(self.base_url+username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)

    @freeze_time("2024-04-03")  #Среда
    def test_get_username_with_correct_weekday(self):
        username = 'Хорошей среды'
        expected_response = f'Привет, {username}. Хорошей среды!'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertEqual(response_text, expected_response)
