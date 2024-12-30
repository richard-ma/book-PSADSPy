import unittest
from hotPotato import hotPotato


class TestHotPotato(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_hotPotato(self):
        self.assertEqual(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7), "Susan")