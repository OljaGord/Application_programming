import unittest

from task4.person import Person


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person('Olga', 2000, 'Perm')

    def test__get_age__correct_age(self):
        self.assertEqual(self.person.get_age(), 24)

    def test__get_name__correct_name(self):
        self.assertEqual(self.person.get_name(), 'Olga')

    def test__set_name__name_changed(self):
        new_name = 'Anna'
        self.person.set_name(new_name)
        self.assertEqual(self.person.name, new_name)

    def test__get_address__correct_address(self):
        self.assertEqual(self.person.get_address(), 'Perm')

    def test__set_address__address_changed(self):
        self.person.set_address('Moscow')
        self.assertEqual(self.person.address, 'Moscow')

    def test__is_homeless__False(self):
        self.assertEqual(self.person.is_homeless(), False)

    def test__is_homeless__True(self):
        self.person.address = None
        self.assertEqual(self.person.is_homeless(), True)
