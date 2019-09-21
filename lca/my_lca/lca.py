'''
There are 2 possible ways: Iterative and Recursive
Both can offer runtimes of O(n)

The lowest common ancestor of 2 nodes v,w in a binary tree is the lowest node in the bst with both v and w as descendants.
A node can be a descendant of itself

Solution:

    -> Enter 2 nodes v,w to find the lca of
    -> Find a path from root to v
    -> Find a path from root to w
    -> The lca will be the node before the first mismatch between paths

'''
import my_lca.treeNode as Node


class lca:

    def ensure_bst(self, root):
        pass

    def path_find(self, root, x, path):
        if root is None:
            return False

        path.append(root.val)

        if root.val == x:
            return True

        if((root.left != None and self.path_find(self, root.left, x, path))) or ((root.right != None and self.path_find(self, root.right, x, path))):
            return True

        # x was not found in the bst
        path.pop()
        return False
