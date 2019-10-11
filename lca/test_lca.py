import unittest
import networkx as nx
from my_lca.lca import lca

class TestLca(unittest.TestCase):

    def test_valid_dag(self):
        lca_test = lca()

        G = nx.DiGraph()
        map(G.add_node, range(8))
        G.add_edge(1, 4)
        G.add_edge(2, 4)
        G.add_edge(3, 4)
        G.add_edge(4, 5)
        G.add_edge(4, 6)
        G.add_edge(4, 7)
        G.add_edge(5, 8)
        G.add_edge(6, 8)
        G.add_edge(7, 8)

        self.assertTrue(lca_test.ensure_acyclic(G))

    def test_lca(self):
        lca_test = lca()

        G = nx.DiGraph()
        map(G.add_node, range(8))
        G.add_edge(1, 4)
        G.add_edge(2, 4)
        G.add_edge(3, 4)
        G.add_edge(4, 5)
        G.add_edge(4, 6)
        G.add_edge(4, 7)
        G.add_edge(5, 8)
        G.add_edge(6, 8)
        G.add_edge(7, 8)

        self.assertEqual(lca_test.lowest_common_ancestor(G, 4, 5), 3)
        


if __name__ == '__main__':
    unittest.main()
