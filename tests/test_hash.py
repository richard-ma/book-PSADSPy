import unittest
from pythonds.hash import *


class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable()
        self.ht[54] = "cat"
        self.ht[26] = "dog"
        self.ht[93] = "lion"
        self.ht[17] = "tiger"
        self.ht[77] = "bird"
        self.ht[31] = "cow"
        self.ht[44] = "goat"
        self.ht[55] = "pig"
        self.ht[20] = "chicken"
        
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_hashTable_put(self):
        self.assertEqual([77, 44, 55, 20, 26, 93, 17, None, None, 31, 54], self.ht.slots)
        self.assertEqual(['bird', 'goat', 'pig', 'chicken', 'dog', 'lion', 'tiger', None, None, 'cow', 'cat'], self.ht.data)

    def test_hashTable_get(self):
        self.assertEqual(self.ht[20], 'chicken')
        self.assertEqual(self.ht[17], 'tiger')

    def test_hashTable_update(self):
        self.ht[20] = 'duck'
        self.assertEqual(self.ht[20], 'duck')

    def test_hashTable_None(self):
        self.assertEqual(self.ht[99], None)