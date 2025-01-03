import unittest
from pythonds.graph import *


class TestGraph(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_graph(self):
        g = Graph()
        for i in range(6):
            g.addVertex(i)

        self.assertEqual(len(g.vertList), 6)