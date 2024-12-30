import unittest
from src.infixToPostfix import infixToPostfix, postfixEval, doMath


class TestInfixToPostfix(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
    
    def test_infixToPostfix(self):
        infix = "( A + B )"
        postfix = "A B +"
        self.assertEqual(infixToPostfix(infix), postfix)

        self.assertEqual(infixToPostfix("( A + B ) * ( C + D )"), "A B + C D + *")
        self.assertEqual(infixToPostfix("( A + B ) * C"), "A B + C *")
        self.assertEqual(infixToPostfix("A + B * C"), "A B C * +")

    def test_doMath(self):
        self.assertEqual(doMath('+', 1, 2), 3)
        self.assertEqual(doMath('-', 2, 1), 1)
        self.assertEqual(doMath('*', 1, 2), 2)
        self.assertEqual(doMath('/', 4, 2), 2)

    def test_postfixEval(self):
        exprs = [
            ("1 + 2", 3),
            ("2 * 2", 4),
            ("1 + 2 * 3", 7),
            ("( 1 + 2 ) * ( 3 + 4 )", 21),
        ]

        for expr, result in exprs:
            self.assertEqual(postfixEval(infixToPostfix(expr)), result)