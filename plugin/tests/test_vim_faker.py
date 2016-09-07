import unittest
import vim_faker as sut


# @unittest.skip("Don't forget to test!")
class VimFakerTests(unittest.TestCase):

    def test_example_fail(self):
        result = sut.vim_faker_example()
        self.assertEqual("Happy Hacking", result)
