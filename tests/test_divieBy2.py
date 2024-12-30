import unittest
from src.divideBy2 import divideBy2


class TestDivideBy2(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
    
    def test_divideBy2(self):
        decNumber = 233
        binString = "11101001"

        self.assertEqual(divideBy2(decNumber), binString)