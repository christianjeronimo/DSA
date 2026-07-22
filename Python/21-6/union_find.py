#!/usr/bin/python3
# union_find.py
# part of Assignment #6: Amazing Union-Find
# Maze generation with Disjoint Sets
# union_find.py

# Implementation of Disjoint Set Union data structure. Structure used to keep
# track of the separation of a set into a number of non-overlapping subsets.
# Provides operations to find which subset an element belongs to and for joining
# two subsets into one.
class DisjointSet:

    # Used to initialize the data structure with n elements which are initialized
    # into their own disjoint set, n is the number of elements in the set. Rank
    # is used for optimization as discussed in class to allow union by rank, it
    # stores each set's root in a list. Parent is a list which contains the
    # parent of element i. Sets is used to keep track of the number of current
    # sets.
    def __init__(self, n):
        self.rank = [0] * n # rank initially set to 0
        self.parent = list(range(n))
        self.size = n
        self.sets = n

    # Find function is used to find the root of the set that the element x
    # belongs to. Also Implements path compression as discussed in class
    # x is the element whose representative set is to be found. Returns
    # the root containing x or -1 if x is out of bounds.
    def find(self, x):
        if not (0 <= x < self.size): # checks if x is a valid index.
            return -1
        if self.parent[x] != x: # if x is not the parent recursively calls
            # find to find the root of it's parent while updating x to be
            # the root
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x] # returns the root of x

    # Merges the sets containing elements u and v into a single set. calls find
    # to determine the root of the sets and uses the privat link function shown
    # in class to do the actual mergin using union by rank. Returns true if union
    # was successful; returns False if u and v were already in the same set
    def union(self, u, v):
        # checks if u and v are valid indices
        if not (0 <= u < self.size) or not (0 <= v < self.size):
            return -1 # returns -1 if out of bounds
        root_u = self.find(u) # finds root of u
        root_v = self.find(v) # finds root of v
        if root_u == root_v: # checks if u and v are in the same set.
            return False # false if they are
        self._link(root_u, root_v) # if they are in different sets, merges them
        self.sets -= 1 # decreases count os sets since two were just merged.
        return True

    # Links the set with root x to root y using union by rank.
    def _link(self, x, y):
        if x == y: # if the root s are the same does nothing
            return
        # Compares the ranks of the two sets the set with the smaller rank is
        # attached to the root of the set with the larger rank. Helps keep the
        # structure flat improving the efficiency of the find operation
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x # If rank of x is greater make x the parent of y
        else:
            # otherwise y's rank is greater or equal and is mad the parent of x
            self.parent[x] = y
            # if the ranks were equal increments the rank of y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
            
    # returns the current number of disjoint sets
    def num_sets(self):
        return self.sets
