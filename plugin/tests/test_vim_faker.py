import unittest
import vim_faker as sut
import pytz


class VimFakerTests(unittest.TestCase):

    def test_provider(self):
        result = sut.vim_faker('name')
        self.assertEqual(unicode, type(result))

    def test_kwargs(self):
        result = sut.vim_faker('iso8601', tzinfo=pytz.timezone('UTC'))
        self.assertEqual('+00:00', result[-6:])

    def test_exceptions_are_returned(self):
        result = sut.vim_faker('junk')
        self.assertEqual("'Generator' object has no attribute 'junk'", result)

    def test_localization(self):
        result = sut.vim_faker('name', l10n='fa_IR')
        self.assertGreater(ord(result[0]), 1536)
