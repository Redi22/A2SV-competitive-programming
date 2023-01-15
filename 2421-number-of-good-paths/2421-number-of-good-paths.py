from collections import defaultdict
from itertools import product
from math import comb


class Disjoint:
    def __init__(self, n) -> None:

        # Intialize lists to keep track of parent nodes and heights
        self.parents, self.heights = [-1] * n, [0] * n

    def find(self, node):
        # Find the parent node recursively

        if self.parents[node] == -1:
            return node

        return self.find(self.parents[node])

    def union(self, node1, node2):
        # Union two nodes together while keeping the tree hieght minimum

        # Find parent nodes of both nodes
        parent1, parent2 = self.find(node1), self.find(node2)

        # If both nodes belong to the same tree, return
        if parent1 == parent2:
            return

        # Else, make the first tree the shorter of the two
        if self.heights[parent1] > self.heights[parent2]:
            parent1, parent2 = parent2, parent1

        # Merge the first tree under the second tree
        self.parents[parent1] = parent2

        # Update the height of the second tree
        self.heights[parent2] += int(self.heights[parent1] == self.heights[parent2])


class Solution:
    def numberOfGoodPaths(self, vals: list[int], edges: list[list[int]]) -> int:

        # Find the number of nodes
        n = len(vals)

        # Build an adjacency list
        adj = defaultdict(list)
        for node1, node2 in edges:
            if vals[node1] <= vals[node2]:
                adj[node2].append(node1)

            if vals[node1] >= vals[node2]:
                adj[node1].append(node2)

        # Group all nodes based on their values
        nodes = defaultdict(list)
        for i, val in enumerate(vals):
            nodes[val].append(i)

        # Initialize the result and the disjoint set
        res, dis = n, Disjoint(n)

        # Iterate through all groups of nodes sorted by their values
        for val in sorted(nodes):

            # For each node in a group
            for node in nodes[val]:

                # Union such node with its neighboring nodes
                for node1, node2 in product([node], adj[node]):
                    dis.union(node1, node2)

            # Find how many nodes of the current values belong to the same tree in the disjoint set
            groups = defaultdict(int)
            for node in nodes[val]:
                groups[dis.find(node)] += 1

            # Calculate the combination of nodes in each tree
            for count in groups.values():
                res += comb(count, 2)

        return res