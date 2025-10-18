#!/usr/bin/python3
# p8.py
# part of Assignment #8: file executable 
# Breadth-First Search
# p8.py (working/tested)

import sys
from bfs import Maze_solver

# Main function used to take in maze input line by line adding it to a list
# after having any whitspace removed afterwards it runs the maze solver program
# to find the fastest path out of the maze provided.

def main():
    maze_lines = [] # list to store teh lines of the maze

    for line in sys.stdin:
        clean = line.strip()
        if clean: # Only add non-empty lines
            maze_lines.append(clean)
    if  maze_lines: # entire block runs only if there's input
        
        try:
            solver = Maze_solver(maze_lines) # solver is created here
        except ValueError as e:
            print(f"Error initializing maze: {e}")
            sys.exit(1)
        except IndexError as e: # Catch potential index errors during initialization
            print(f"Error during maze setup: {e}")
            sys.exit(1)

    # there lines are correctly handle, then solver is defined within the scope
    # the object instance are called in
    solver.bfs()
    shortest_path = solver.get_path()
    if shortest_path:
        for x, y in shortest_path:
            print(f"({x}, {y})")

    else:
         pass
     
    # no output if maze_lines is empty, ending the program

if __name__ == "__main__":
    main()
