import unittest
from src.baseConverter import baseConverter


class TestBaseConverter(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
    
    def test_baseConverter(self):
        decNumber = 233
        binString = "11101001"
        octString = "351"
        hexString = "E9"

        self.assertEqual(baseConverter(decNumber, 2), binString)
        self.assertEqual(baseConverter(decNumber, 8), octString)
        self.assertEqual(baseConverter(decNumber, 16), hexString)