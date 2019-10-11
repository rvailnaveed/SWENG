'''

The lowest common ancestor of 2 nodes v,w in a Directed Acyclic Graph is the lowest node with both v and w as descendants.
A node can be a descendant of itself.

Solution:

    -> Enter 2 nodes v,w to find the lca of
    -> Find all ancestors of v
    -> Find all ancestors of w
    -> The lca will be the max of the intersection of both ancestor lists

'''
#from treeNode import TreeNode as Node
from networkx import DiGraph

class lca:
    
    def ensure_acyclic(self, dag):
        pass

    def lowest_common_ancestor(self, dag, v, w):
        pass

