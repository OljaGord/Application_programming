import unittest

from task3 import money_storage


class TestMoneyStorage(unittest.TestCase):
    def setUp(self):
        money_storage.app.config['TESTING'] = True
        money_storage.storage = {2023: {8: 50, 9: 100, 12: 1000}}
        self.app = money_storage.app.test_client()

    def test__add_new_date_value__new_storage_value(self):
        self.app.get('/add/20230123/100')
        self.assertEqual(money_storage.storage[2023][1], 100)

    def test__add_value_to_exist_month__sum_for_month(self):
        self.app.get('/add/20230801/100')
        self.assertEqual(money_storage.storage[2023][8], 150)

    def test__uncorrected_date__error_message(self):
        response = self.app.get('/add/2023220923/50')
        response_text = response.data.decode()
        self.assertEqual('Введенная дата некорректна, исправьте!', response_text)

    def test__calculate__correct_year(self):
        response = self.app.get('/calculate/2023')
        response_text = response.data.decode()
        self.assertEqual(response_text, 'Расходы за 2023 год составили: 1150 руб.')

    def test__calculate__correct_year_and_month(self):
        response = self.app.get('/calculate/2023/09')
        response_text = response.data.decode()
        self.assertEqual(response_text, 'Расходы за 2023 год и 9 месяц составили: 100 руб.')

    def test__calculate__not_exist_date(self):
        money_storage.storage = {}
        response = self.app.get('/calculate/2023')
        response_text = response.data.decode()
        self.assertEqual(response_text, 'У меня пока нет данных по 2023 году')
