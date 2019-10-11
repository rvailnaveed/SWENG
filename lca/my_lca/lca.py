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
from my_lca.treeNode import TreeNode


class lca:
    # Do DFS on bst
    # O(n)
    def ensure_bst(self, root):
        if root == None:
            return True

        stack = [(root, float('-inf'), float('inf'))]

        while stack:
            root, mini, maxi = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= mini or val >= maxi:
                return False

            stack.append((root.right, val, maxi))
            stack.append((root.left, mini, val))

        return True

    # O(n)
    def path_find(self, root, x, path):
        if root is None:
            return False

        path.append(root.val)

        if root.val == x:
            return True

        if((root.left != None and self.path_find(root.left, x, path))) or ((root.right != None and self.path_find(root.right, x, path))):
            return True

        # x was not found in the bst
        path.pop()
        return False


    def lowest_common_ancestor(self, root, v, w):
        path1 = [] # path from root to v
        path2 = [] # path from root to w
        if (not self.path_find(root, v, path1) or not self.path_find(root, w, path2)):
            return -1

        i = 0
        while(i < len(path1) and i < len(path2)):
            if path1[i] != path2[i]:
                break
            i += 1

        return path1[i-1]
