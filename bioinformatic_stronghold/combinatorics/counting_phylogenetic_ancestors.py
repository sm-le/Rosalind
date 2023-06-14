"""
Combinatorics 6

Given A positiive integer n, return the number of internal ndoes of unrooted binary tree having n leaves

Example,
In: 4
Out: 2
"""

def internal_node_unrooted(n_leaves:int) -> int:
    """Internal node counter given unrooted tree 
    (upper bifurcation does not count as 1)

    Args:
        n_leaves: number of leaves in a tree
    Returns:
        int(internal node count)
    """
    inodes = 0
    while n_leaves > 2:
        inodes += (n_leaves // 2)
        n_leaves = (n_leaves // 2) + (n_leaves % 2)

    return inodes