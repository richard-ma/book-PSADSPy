import unittest
from pythonds.tree import *


class TestTree(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()

    def test_getLeftChild(self):
        r = BinaryTree(3)
        r.insertLeft(4)
        node = r.getLeftChild()
        self.assertEqual(4, node.getRootVal())

    def test_getRightChild(self):
        r = BinaryTree(3)
        r.insertRight(4)
        node = r.getRightChild()
        self.assertEqual(4, node.getRootVal())

    def test_get_and_set_rootval(self):
        r = BinaryTree('a')
        rootval = r.getRootVal()
        self.assertEqual('a', rootval)

        r.setRootVal('b')
        rootval = r.getRootVal()
        self.assertEqual('b', rootval)
        