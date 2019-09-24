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

    def test_bst_invalid_number(self):
        lca_test = lca()

        root = Node(8) 
        root.left = Node(3) 
        root.right = Node(10)  
        root.left.left = Node(1)
        root.left.right = Node(float('-inf'))
        root.left.right.right = Node(7)
        root.left.right.left = Node(4)
        root.right.right = Node(14)
        root.right.right.left = Node(13)


        self.assertFalse(lca_test.ensure_bst(root))

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


    def test_lca_no_path(self):
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

        v = 14
        w = 86

        self.assertEqual(lca_test.lowest_common_ancestor(root, v, w), -1)

    def test_lca(self):
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

        v = 14
        w = 13

        self.assertEqual(lca_test.lowest_common_ancestor(root, v, w), 14)

        v = 6
        w = 14

        self.assertEqual(lca_test.lowest_common_ancestor(root, v, w), 8)




if __name__ == '__main__':
    unittest.main()
