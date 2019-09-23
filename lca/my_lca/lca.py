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
from treeNode import TreeNode as Node


class lca:
    # Do DFS on bst
    # O(n)
    def ensure_bst(self, root):
        if not root:
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
        self.path_find(root, v, path1)
        self.path_find(root, w, path2)
        temp = [i for i, j in zip(path1, path2) if i != j]
        print(temp)

if __name__ == "__main__":
    root = Node(18)
    root.left = Node(40)
    root.right = Node(30)
    root.right.left = Node(100)
    root.right.right = Node(40)
    lca = lca()

    lca.lowest_common_ancestor(root, 100, 40)

