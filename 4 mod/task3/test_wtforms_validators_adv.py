import unittest

from task2.wtforms_validators_adv import app


class TestWtformsValidatorsAdv(unittest.TestCase):
    valid_data = {
        'email': 'valid_email@example.com',
        'phone': '1234567890',
        'name': 'Test Name',
        'address': 'Test Address',
        'index': '123456',
        'comment': 'Test Comment'
    }
    invalid_data = {
        'email': 'invalid_email',
        'phone': '12345678909331',
        'name': '',
        'address': '',
        'index': '123456WDWDD',
        'comment': 'Test Comment'
    }

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        self.base_url = '/registration'
        self.data = self.valid_data.copy()

    def test__valid_email__success(self):
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(response.status_code, 200)

    def test__invalid_email__error(self):
        self.data['email'] = self.invalid_data['email']
        response = self.app.post(self.base_url, data=self.data)
        response_text = response.data.decode()
        self.assertEqual(response.status_code, 400)
        self.assertTrue('email' in response_text)

    def test__valid_phone__success(self):
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(response.status_code, 200)

    def test__invalid_phone__error(self):
        self.data['phone'] = self.invalid_data['phone']
        response = self.app.post(self.base_url, data=self.data)
        response_text = response.data.decode()
        self.assertEqual(response.status_code, 400)
        self.assertTrue('phone' in response_text)

    def test__valid_name__success(self):
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(response.status_code, 200)

    def test__invalid_name__error(self):
        self.data['name'] = self.invalid_data['name']
        response = self.app.post(self.base_url, data=self.data)
        response_text = response.data.decode()
        self.assertEqual(response.status_code, 400)
        self.assertTrue('name' in response_text)

    def test__valid_address__success(self):
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(response.status_code, 200)

    def test__invalid_address__error(self):
        self.data['address'] = self.invalid_data['address']
        response = self.app.post(self.base_url, data=self.data)
        response_text = response.data.decode()
        self.assertEqual(response.status_code, 400)
        self.assertTrue('address' in response_text)

    def test__valid_index__success(self):
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(response.status_code, 200)

    def test__invalid_index__error(self):
        self.data['index'] = self.invalid_data['index']
        response = self.app.post(self.base_url, data=self.data)
        response_text = response.data.decode()
        self.assertEqual(response.status_code, 400)
        self.assertTrue('index' in response_text)


if __name__ == '__main__':
    unittest.main()
