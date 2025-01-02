import unittest
from pythonds.tree import BinaryTree
from pythonds.tree_parser import *


class TestTreeParser(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_printexp_and_postordereval(self):
        x = BinaryTree('*')
        x.insertLeft('+')
        l = x.getLeftChild()
        l.insertLeft(4)
        l.insertRight(5)
        x.insertRight(7)
        
        self.assertEqual(
            "(((4)+(5))*(7))",
            printexp(x)
        )

        self.assertEqual(63, postordereval(x))