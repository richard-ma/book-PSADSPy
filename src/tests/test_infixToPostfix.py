import unittest
from infixToPostfix import infixToPostfix


class TestInfixToPostfix(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
    
    def test_baseConverter(self):
        infix = "( A + B )"
        postfix = "A B +"
        self.assertEqual(infixToPostfix(infix), postfix)