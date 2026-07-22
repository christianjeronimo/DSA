#!/usr/bin/python3
# bfs.py
# part of Assignment #8: Breadth-first search
# Breadth-First Search-Maze solver
# maze.py (working/tested)
# use of collections Module/Library since I've been told a self made queue
# would affect the run time not making it the expecting time complexity
from collections import deque

# bitmask constant for wall representation. values correspond to bits in the
# hexadecimal input characters. consistent with the maze generation algorithms
# like assignment 6, which used bitwise operations for the walls, which makes
# the graph building compatible with generated mazes. Quite a bit of help from
# STEM center

east = 1 # right (wall) binary representation
south = 2 # bottom (wall) binary representation
west = 4 # left (wall) binary representation
north = 8 # top (wall) binary representation

class Maze_solver:
    # solves a square maze represented by a hexadecimal string Using breadth
    # first search (N x N maze) starting at (0, 0) ends at (N-1, N-1)
    # checks cardinal direction for graph building.

    # intiializes the Maze solver with a list of string representing the maze
    # performs validation to ensure the input maze is a perfect square, might
    # not be needed since desciption of input indicates good maze input, will
    # comment out.
    def __init__(self, maze_lines):
        self.n = len(maze_lines)
        #if any(len(line) != self.n for line in maze_lines):
        #    raise ValueError("Maze is not square (N x N).")
        self.grid = self.hex_string(maze_lines) # turns hex input into a 2D
        # grid of integer bitmasks
        num_nodes = self.n * self.n #initializes BFS related data structures
        # using arrays to simplify BFS operations as indicated in class
        self.color = ["white"] * num_nodes # white = undiscovered node
        self.dist = [float('inf')] * num_nodes # distance from start node
        self.parent = [None] * num_nodes # parent in the BFS tree-used for path
        # reconstruction
        # Build adjacency list representation of the maze graph, this graph
        # stores connection between cells using checks for each direction
        self.graph = self.build_graph() # callls graph building method
        self.start = (0, 0) # start coordinates
        self.end = (self.n - 1, self.n - 1) # end coordinates
        self.start_id = self.index(self.start[0], self.start[1]) # 1D indices
        self.end_id = self.index(self.end[0], self.end[1])


    # turns a list of maze lines into a 2D list of integer bitmasks, input maze
    # is a list of strings.returns list of list of int representing the wall
    # bitmask of a cell
    def hex_string(self, maze_lines):
        grid = [[0 for _ in range(self.n)] for _ in range(self.n)]
        for r in range(self.n):
            for c in range(self.n):
                # convert each hexadecimal character(0-f) into it's integer
                # equivalent whose value should represent the presence or absence
                # of walls defined by the bitmask constants
                grid[r][c] = int(maze_lines[r][c].lower(), 16)
        return grid

    # builds the adjacency list representation of the maze graph. Checks each
    # node in the graph and checks each of the four cardinal directions for
    # connections. node corresponds to a 1d index of a maze cell. Inspired
    # by the remove wall function from the maze.py file by setting a bit to 0
    # this function checks the absence of wall by checking if the relevant bit
    # is 0 for the current cell and possible neighbor
    def build_graph(self):
        graph = [[] for _ in range(self.n * self.n)] # initialize adjacency list
        # for all V nodes
        for r in range(self.n):
            for c in range(self.n):
                idx = self.index(r, c)
                cell_value = self.grid[r][c] # get the bitmask for a current cell
                # check Right (move east)
                nr, nc = r, c + 1 # calculates neighbors coordinates
                # and ensures neighbor is within maze boundaries
                if (0 <= nr < self.n) and (0 <= nc < self.n):
                    neighbor_id = self.index(nr, nc)
                    neighbor_val = self.grid[nr][nc] # get neighbor's bitmask
                    # path = current cell does not have east wall (bit 1 = 0)
                    # and neighbor cell does not have a west wall (bit 4 = 0)
                    if (cell_value & east) == 0 and (neighbor_val & west) == 0:
                        graph[idx].append(neighbor_id) # add edge to graph
                # check left (move west)
                nr, nc = r, c - 1
                if (0 <= nr < self.n) and (0 <= nc < self.n):
                    neighbor_id = self.index(nr, nc)
                    neighbor_val = self.grid[nr][nc]
                    # path = current cell does not have west wall
                    # and neighbor cell does not have a east wall
                    if (cell_value & west) == 0 and (neighbor_val & east) == 0:
                        graph[idx].append(neighbor_id)
                # check down (move south)
                nr, nc = r + 1, c
                if (0 <= nr < self.n) and (0 <= nc < self.n):
                    neighbor_id = self.index(nr, nc)
                    neighbor_val = self.grid[nr][nc]
                    # path = current cell does not have south wall
                    # and neighbor cell does not have a north wall
                    if (cell_value & south) == 0 and (neighbor_val & north) == 0:
                        graph[idx].append(neighbor_id)
                # check up (move north)
                nr, nc = r - 1, c
                if (0 <= nr < self.n) and (0 <= nc < self.n):
                    neighbor_id = self.index(nr, nc)
                    neighbor_val = self.grid[nr][nc]
                    # path = current cell does not have north wall
                    # and neighbor cell does not have a south wall
                    if (cell_value & north) == 0 and (neighbor_val & south) == 0:
                        graph[idx].append(neighbor_id)
                    
        return graph

    # performs Breadth-First Search to fond the shortest path from the start cell
    # to the end cell this method utilizes color, dist, and parent arrays which
    # are then used by the get path function for path reconstruction.
    def bfs(self): # Time complexity O(V + E) acheivable by collections dequeue

        queue = deque() # use collections.deque for efficient O(1) enqueue
        # and dequeue
        # initialize the start node for BFS
        self.color[self.start_id] = 'gray' # mark as discovered 
        self.dist[self.start_id] = 0 # distance from source is 0
        queue.append(self.start_id) # add start node to the queue
        
        # BFS main loop: continue as long as there are node to visit in the queue
        while queue:
            u = queue.popleft() # get the next node to process from queue
            # if the end node is reached we've found the shortest path,
            # so we can stop the BFS early.
            if u == self.end_id:
                return # Exit the BFS method
            
            # explore neighbors of the current node u
            for v in self.graph[u]: # iterate through adjacent nodes from list
                if self.color[v] == 'white': # if node v is undiscovered
                    self.color[v] = 'gray' # mark v as discovered (processing)
                    self.dist[v] = self.dist[u] + 1 # distance is one more than
                    # parent's
                    self.parent[v] = u # set current node u as parrent of
                    # neighbor v
                    queue.append(v) # add neighbor to queue for future processin
            self.color[u] = 'black' # set current node as fully processed

    # converts 2D (row, col) coordinates to a 1D index for graph representation
    # simplifies array access for color, dist, and parent
    def index(self, r, c):
        if not (0 <= r < self.n and 0 <= c < self.n): # checks if out of bounds
            return
        return r * self.n + c

    # reverts what index does by turning 1D index back to 2D (row, col)
    # coordinates. makes sure the index is within the bounds of graph
    def coord(self, idx):
        if not (0 <= idx < self.n * self.n):
            return
        return idx // self.n, idx % self.n

    # reconstructs the shortest path from the start to the end cell using the
    # parent array generated by BFS, path returned in (col, row) (x, y) format
    # as required for output
    def get_path(self):
        path = [] # temporary list to store (row, col) coordinates
        current = self.end_id # start path reconstruction from the end node
        # if the end node was not reachable during BFS, its distance will still
        # be infinity. this check determines if a path was found.
        if self.dist[current] == float('inf'):
            return None # no path found

        # reconstruct path by tracing back from the end_id to the start_id using
        # the parent pointers. the path is built in reverse order
        while current is not None:
            path.append(self.coord(current)) # add current node to path
            current = self.parent[current] # Move to the parent node

        path.reverse() # reverse the path to get the correct start to end order
        # convert cordinates (row, col) to (col, row) format as required for
        # output (x,y).
        coordinates = []
        for r, c in path:
            coordinates.append((c, r)) # (x, y) corresponds to (column, row)
        return coordinates
