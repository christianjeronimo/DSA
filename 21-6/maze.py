#!/usr/bin/pyhthon3
# maze.py
# part of Assignment #6: Amazing Union-Find
# Maze generation with Disjoint Sets
# maze.py

import random
from union_find import DisjointSet


# represents a maze and provides functions to generate and print the maze. Uses
# the Disjoint set data structure ti remove the walls between cell untill all
# cells are connected. makes grid initially set all to F or then sets (0,0) to
# B to where the left wall is open and (n-1,n-1) to E to have the right wall
# open as shown in handout. Grid is a 2d list representaion
import random

class Maze:

    def __init__(self, n):
        self.n = n
        self.grid = [[15 for _ in range(n)] for _ in range(n)]
        if n >= 1:
            entry = random.choice([8, 4])
            exit_bit = random.choice([2, 1])
            self.grid[0][0] = 15 & ~entry
            self.grid[n-1][n-1] = 15 & ~exit_bit 
        # sets is an instance of the disjoint set class used to track connected
        # components Each cell in the maze is initially it's own set
        self.sets = DisjointSet(n * n)

    # Converts 2D grid coordinates  into a 1D index
    # for the DisjointSet data structure
    def index (self, r, c):
        # checks to see if row and column indices are in range
        if not (0 <= r < self.n and 0 <= c < self.n):
            raise IndexError(f"index({r}, {c}) out of bounds")
            return
        return r * self.n + c # calculate 1D index

    # Removes the wall between two adjacent cells at (r1, c1) and (r2, c2)
    # by updating the corresponding bits in the grid got help from the
    # stem center to remove the walls using bitwise operations
    def remove_wall(self, r1, c1, r2, c2):
        # Calculate the difference in row and column indices to determine
        # the direction of the second cell relative to the first.
        dr, dc = abs(r2 - r1), abs(c2 - c1)
        # Ensure that the two cells are indeed adjacent (differ by exactly 1
        # in either row or column). If not, return without removing a wall.
        if not ((dr == 1 and dc == 0) or (dr == 0 and dc == 1)):
            return
        # Determine the direction and update the wall bits for both cells.
        dr, dc = r2 - r1, c2 - c1
        if dr == 1: # moving south
            self.grid[r1][c1] &= ~2 # Remove South wall of (r1, c1) (bit 1)
            self.grid[r2][c2] &= ~8 # Remove North wall of (r2, c2) (bit 3)
        elif dr == -1: # moving North
            self.grid[r1][c1] &= ~8 # Remove North wall of (r1, c1) (bit 3)
            self.grid[r2][c2] &= ~2 # Remove South wall of (r2, c2) (bit 1)
        elif dc == 1: # moving east
            self.grid[r1][c1] &= ~1 # Remove West wall of (r1, c1) (bit 0)
            self.grid[r2][c2] &= ~4 # Remove East wall of (r2, c2) (bit 2)
        elif dc == -1: # moving west 
            self.grid[r1][c1] &= ~4 # Remove East wall of (r1, c1) (bit 2)
            self.grid[r2][c2] &= ~1  # Remove West wall of (r2, c2) (bit 0)


    # Generates a random maze using Kruskal's algorithm approach with the
    # Disjoint Set Union data structure. It starts with all walls present
    # and randomly removes walls between adjacent cells that belong to
    # different connected components until all cells are in the same component.
    # also received help from the STEM center for this part
    def generate(self):
        walls = [] # list that sotres the potential walls in the maze
        # for statment used to iterate through each cell in the grid
        for r in range(self.n):
            for c in range(self.n):
                if r < self.n - 1: # Add potential wall to the south if
                    # currne cell is not in the last row
                    walls.append(((r, c), (r + 1, c)))
                if c < self.n - 1: # adds wall to east if not in the last column
                    walls.append(((r, c), (r, c + 1)))
        random.shuffle(walls) # randomly shuffle the list of walls to ensure
        # randomness

        # Iterate through the shuffled list of walls.
        for (r1, c1), (r2, c2) in walls:
            idx1 = self.index(r1, c1) # 1D index of adjacent cells
            idx2 = self.index(r2, c2)
            # Tries to perform a union of the sets containing the two cells
            # if successful it removes the wall between two previously
            # disconnected parts of the maze
            union_result = self.sets.union(idx1, idx2)
            if union_result is True:
                self.remove_wall(r1, c1, r2, c2)
            # returns -1 if the indices wre out of bounds
            elif union_result == -1:
                print("Error")

    # Prints the maze to the console using hexadecimal representation of the
    # wall bits for each cell.
    def print_maze(self):
        # iterates throught the maze grid
        for row in self.grid:
            # for each cell in the row formates the integer value as a
            # hex String and join them together to print the row
            print(''.join(f"{cell:x}" for cell in row))
