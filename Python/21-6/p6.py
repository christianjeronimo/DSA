#!/usr/bin/python3
# p6.py - executable file
# part of Assignment #6: Amazing Union-Find
# Maze generation with Disjoint Sets
# p6.py

import sys
from maze import Maze

# main function of the script, takes the maze size as a command line argument
# generates a maze of that size and then prints the maze
def main():
    # Check if the number of command-line arguments is exactly 2
    if len(sys.argv) != 2:
        print("Use: ./p6.py <int>")
        return 
    try:
        # convert command line argument to int which will be the size of maze
        n = int(sys.argv[1])
        # ensure size of maze is at least 3
        if n < 3:
            return
    except ValueError: # error message if no int input as command line argument
        return

    maze = Maze(n) # instance of Maze class With specified size
    maze.generate() # generate maze
    maze.print_maze() # Prints the generated maze

if __name__ == "__main__":
    main()
