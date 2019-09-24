import unittest
from my_lca.lca import lca
from my_lca.treeNode import TreeNode as Node

class TestLca(unittest.TestCase):

    def test_bst(self):
        lca_test = lca()

        root = Node(8) 
        root.left = Node(3) 
        root.right = Node(10)  

        self.assertTrue(lca_test.ensure_bst(root))
        


if __name__ == '__main__':
    unittest.main()
