import unittest
from pythonds.recursion import *


class TestRecursion(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_listsum(self):
        numList = [1, 3, 5, 7, 9]
        self.assertEqual(listsum(numList), 25)

    def test_toStr(self):
        self.assertEqual(toStr(10, 2), "1010")