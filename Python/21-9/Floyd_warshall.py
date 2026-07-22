#!/usr/bin/python3
# Floyd_warshall.py
# graph algorithm file for assignment 9
# Extra credit: Graph Algorithm
# Floyd_warshall.py:(working/tested)

# File contains graph algorith discussed in class for APSP similar
# purpose as Bellman ford but used to make a distance and parent matrix for
# all sources-nodes using weighted edges to determine distance and using
# the direction or adjacency relations to determine parent. In this file
# generate/initialize distance and parent matices. Along with the
# implementation of the  Floyd warshall algorithm

import math # used for infinity flag instead of float("inf")


def initialize(n, edges):
    dist = [[math.inf] * n for _ in range(n)] # distance from i to j
    parent = [[None] * n for _ in range(n)] # parent pointers
    for i in range(n):
        dist[i][i] = 0 # distance to self is 0
    # load initial edge weights and parents
    for u, v, w in edges:
        dist[u-1][v-1] = w
        parent[u-1][v-1] = u - 1 # store 0 based index

    return dist, parent

# Run the FLoyd-Warshall algorith, got help from STEM for the path implementation
# to replace min(dij, dik + dkj) from psuedo easier than i made it in head.
def floyd_warshall(n, dist, parent):
    for k in range(n): # intermediate node
        for i in range(n): # source node
            for j in range(n): # destination node
                # checks if paths exist
                if dist[i][k] != math.inf and dist[k][j] != math.inf:
                    # chechs if this path is shorter
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        parent[i][j] = parent[k][j] # updates parent
