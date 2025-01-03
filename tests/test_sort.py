import unittest
from pythonds.sort import *


class TestSort(unittest.TestCase):
    def setUp(self):
        self.alist = [3, 4, 2, 1, 7, 9, 5]
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_bubbleSort(self):
        sorted_alist = bubbleSort(self.alist)
        self.alist.sort()
        self.assertEqual(sorted_alist, self.alist)
    
    def test_shortBubbleSort(self):
        sorted_alist = shortBubbleSort(self.alist)
        self.alist.sort()
        self.assertEqual(sorted_alist, self.alist)
    
    def test_selectionSort(self):
        sorted_alist = selectionSort(self.alist)
        self.alist.sort()
        self.assertEqual(sorted_alist, self.alist)
    
    def test_insertionSort(self):
        sorted_alist = insertionSort(self.alist)
        self.alist.sort()
        self.assertEqual(sorted_alist, self.alist)
    
    def test_shellSort(self):
        sorted_alist = shellSort(self.alist)
        self.alist.sort()
        self.assertEqual(sorted_alist, self.alist)
    
    def test_mergeSort(self):
        sorted_alist = mergeSort(self.alist)
        self.alist.sort()
        self.assertEqual(sorted_alist, self.alist)
    
    def test_quickSort(self):
        sorted_alist = quickSort(self.alist)
        self.alist.sort()
        self.assertEqual(sorted_alist, self.alist)