import unittest
from pythonds.tree_function import *


class TestTreeFunction(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_tree_create(self):
        r = BinaryTree(3)
        self.assertEqual([3, [], []], r)

    def test_insertLeft(self):
        r = BinaryTree(3)
        insertLeft(r, 4)
        self.assertEqual([3, [4, [], []], []], r)

    def test_insertRight(self):
        r = BinaryTree(3)
        insertRight(r, 4)
        self.assertEqual([3, [], [4, [], []]], r)

    def test_getLeftChild(self):
        r = BinaryTree(3)
        insertLeft(r, 4)
        node = getLeftChild(r)
        self.assertEqual([4, [], []], node)

    def test_getRightChild(self):
        r = BinaryTree(3)
        insertRight(r, 4)
        node = getRightChild(r)
        self.assertEqual([4, [], []], node)

    def test_get_and_set_rootval(self):
        r = BinaryTree(3)
        rootval = getRootVal(r)
        self.assertEqual(3, rootval)

        setRootVal(r, 5)
        rootval = getRootVal(r)
        self.assertEqual(5, rootval)
        