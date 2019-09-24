import unittest
from my_lca.lca import lca
from my_lca.treeNode import TreeNode as Node

class TestLca(unittest.TestCase):

    def test_bst(self):
        lca_test = lca()

        root = Node(8) 
        root.left = Node(3) 
        root.right = Node(10)  
        root.left.left = Node(1)
        root.left.right = Node(6)
        root.left.right.right = Node(7)
        root.left.right.left = Node(4)
        root.right.right = Node(14)
        root.right.right.left = Node(13)


        self.assertTrue(lca_test.ensure_bst(root))
        
        
    def test_empty_bst(self):
        lca_test = lca()
        root = None

        self.assertTrue(lca_test.ensure_bst(root))


    def test_path_find_empty_bst(self):
        lca_test = lca()

        root = None
        path = []
        x = 4
        self.assertFalse(lca_test.path_find(root, x, path))


    def test_path_find(self):
        lca_test = lca()

        root = Node(8) 
        root.left = Node(3) 
        root.right = Node(10)  
        root.left.left = Node(1)
        root.left.right = Node(6)
        root.left.right.right = Node(7)
        root.left.right.left = Node(4)
        root.right.right = Node(14)
        root.right.right.left = Node(13)

        path = []
        x = 4

        self.assertTrue(lca_test.path_find(root, x, path))


    def test_path_find_no_x(self):
        lca_test = lca()

        root = Node(8) 
        root.left = Node(3) 
        root.right = Node(10)  
        root.left.left = Node(1)
        root.left.right = Node(6)
        root.left.right.right = Node(7)
        root.left.right.left = Node(4)
        root.right.right = Node(14)
        root.right.right.left = Node(13)

        path = []
        x = 26

        self.assertFalse(lca_test.path_find(root, x, path))

if __name__ == '__main__':
    unittest.main()
