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
        
    def test_binaryheap(self):
        bh = BinaryHeap()
        bh.insert(5)
        bh.insert(7)
        bh.insert(3)
        bh.insert(11)
        result = bh.delMin()
        self.assertEqual(result, 3)
        result = bh.delMin()
        self.assertEqual(result, 5)
        result = bh.delMin()
        self.assertEqual(result, 7)
        result = bh.delMin()
        self.assertEqual(result, 11)