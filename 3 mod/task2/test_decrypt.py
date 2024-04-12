import unittest

from task2.decrypt import decrypt


class TestDecrypt(unittest.TestCase):
    def test__no_dots__string_not_changed(self):
        self.assertEqual(decrypt('абра-кадабра'), 'абра-кадабра')

    def test__one_dot__remove_dot(self):
        self.assertEqual(decrypt('абра-кадабра.'), 'абра-кадабра')

    def test__two_dots__remove_previous_symbol(self):
        self.assertEqual(decrypt('абраа..-кадабра'), 'абра-кадабра')
        self.assertEqual(decrypt('абра--..кадабра'), 'абра-кадабра')
        self.assertEqual(decrypt('1..2.3'), '23')

    def test__some_dots__remove_previous_symbol(self):
        self.assertEqual(decrypt('абраа..-.кадабра'), 'абра-кадабра')
        self.assertEqual(decrypt('абрау...-кадабра'), 'абра-кадабра')
        self.assertEqual(decrypt('абр......а.'), 'а')

    def test__dots_more_than_symbols__empty_string(self):
        self.assertEqual(decrypt('абра........'), '')
        self.assertEqual(decrypt('1.......................'), '')
        self.assertEqual(decrypt('1...2......3..4.........'), '')

    def test__only_dot__empty_string(self):
        self.assertEqual(decrypt('.'), '')

    def test__empty_string__empty_string(self):
        self.assertEqual(decrypt(''), '')
