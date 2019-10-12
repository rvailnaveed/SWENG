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
        
    def test_empty_dag(self):
        lca_test = lca()

        G = nx.DiGraph()

        self.assertEqual(lca_test.lowest_common_ancestor(G, 4, 5), -1)


    def test_invalid_input(self):
        lca_test = lca()

        G = nx.DiGraph()

        map(G.add_node, range(5))
        G.add_edge(1, 2)
        G.add_edge(1, 3)
        G.add_edge(2, 4)
        G.add_edge(2, 5)

        self.assertEqual(lca_test.lowest_common_ancestor(G, 2, 'a'), -1)



    def test_value_not_present(self):
        lca_test = lca()

        G = nx.DiGraph()

        map(G.add_node, range(5))
        G.add_edge(1, 2)
        G.add_edge(1, 3)
        G.add_edge(2, 4)
        G.add_edge(2, 5)

        self.assertEqual(lca_test.lowest_common_ancestor(G, 7, 10), -1)

    def test_no_ancestors(self):
        lca_test = lca()

        G = nx.DiGraph()

    def test_single_node_dag(self):
        lca_test = lca()

        G = nx.DiGraph()

    def test_cyclic_dag(self):
        lca_test = lca()

        G = nx.DiGraph()

        map(G.add_node, range(3))
        G.add_edge(1, 2)
        G.add_edge(2, 3)
        G.add_edge(3, 1)

        self.assertEqual(lca_test.lowest_common_ancestor(G, 2, 3), -1)



if __name__ == '__main__':
    unittest.main()
