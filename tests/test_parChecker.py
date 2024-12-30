import unittest
from pythonds.parChecker import parChecker


class TestParChecker(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_parChecker(self):
        self.assertTrue(parChecker("{{([][])}()}"))
        self.assertTrue(parChecker("[[{{(())}}]]"))
        self.assertTrue(parChecker("[][][](){}"))
                
        self.assertFalse(parChecker("([)]"))
        self.assertFalse(parChecker("((()]))"))
        self.assertFalse(parChecker("[{()]"))