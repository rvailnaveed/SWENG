'''

The lowest common ancestor of 2 nodes v,w in a Directed Acyclic Graph is the lowest node with both v and w as descendants.
A node can be a descendant of itself.

Solution:

    -> Enter 2 nodes v,w to find the lca of
    -> Find all ancestors of v
    -> Find all ancestors of w
    -> The lca will be the max of the intersection of both ancestor lists

'''

import networkx as nx

class lca:
    
    def ensure_acyclic(self, dag):
        if nx.is_directed_acyclic_graph(dag):
            return True

        return False

    def lowest_common_ancestor(self, dag, v, w):
        if dag:
            if v != None and w != None:
                if isinstance(v, int) and isinstance(w, int):
                    v_ancestors = nx.algorithms.dag.ancestors(dag, v)
                    w_ancestors = nx.algorithms.dag.ancestors(dag, w)

                    intersection = [val for val in v_ancestors if val in w_ancestors]

                    return max(intersection)

        return -1
