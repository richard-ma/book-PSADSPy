import unittest
from palchecker import palchecker


class TestPalchecker(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_palchecker(self):
        self.assertTrue(palchecker("radar"))
        self.assertFalse(palchecker("lsdkjfskf"))