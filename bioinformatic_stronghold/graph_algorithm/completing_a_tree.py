"""
Graph algorithm 2

Given a positive integer n and adjacency list corresponding to a graph on n nodes, return the minimum number of edges 
that can be added to the graph to produce a tree

Example:
IN:
10
1 2
2 8
4 10
5 9
6 10
7 9

OUT:
3
"""
# path = "example_dataset/tree.txt"

def get_required_nodes(path):
    with open(path, "r") as f:
        nodes = int(next(f))

        available_nodes = 0

        for _ in f:
            available_nodes += 1

        required_edges = (nodes - available_nodes) - 1

    return required_edges