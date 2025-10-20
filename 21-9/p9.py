#!/usr/bin/python3
# p9.py
# executable file for assignment 9
# Extra credit: Graph Algorithm
# p9.py:(working/tested)


import sys
import math
from Floyd_warshall import initialize, floyd_warshall
# this file is the executable file for the assignment and implementation of
# the grph algorithm Floyd-warshall

# function to print either the distance or parent matrix
def print_matrix(label, matrix, is_distance = True):
    num_cols = len(matrix)
    c_labels =  " ".join([f"{i + 1}:" for i in range(num_cols)])
    print(f"{label} {c_labels}")
    for i, row in enumerate(matrix):
        line = f"{i + 1}:"
        for val in row:
            if is_distance:
                # use '.' if no parent, otherwise show parent node(1-indexed)
                if val == math.inf or val == 0:
                    line += " ."
                else:
                    line += f" {int(val)}"
            else:
                if val is None:
                    line += " ."
                else:
                    line += f" {val + 1}"
        print(line)

# Main function to read edges and compute shortest paths
def main():
    edges = [] # list to store u, v, w edge triples
    max_node = 0 # Track the largest node number
    for line in sys.stdin: # reads input line by line 
        line = line.strip() # removes trailing whitespace
        if not line:
            continue # continue is used since return exits the program and pass
        # causes error
        try:
            # replace commas with spaces and isolate integers
            parts = [int(p) for p in line.replace(",", " ").split()]
            if len(parts) != 3: # makes sure source destination and weight are
                # present
                continue
            u, v, w = parts # assigns integers to variables
            edges.append((u, v, w)) # adds input values to edge list as tuples
            max_node = max(max_node, u, v) # update max node seen
        except:
            continue


    # if not updated then no input
    if max_node == 0:
        print("No node.")
    else:
        # initialize distance and parent matrices instead of __init__ function
        # done to make matrices that'll match expected output
        dist, parent = initialize(max_node, edges)
        # calls and run floyd_warshall algorithm
        floyd_warshall(max_node, dist, parent)
        # print final distance matrix
        print_matrix("D", dist,  is_distance = True)
        print()
        # print final parent matrix
        print_matrix("P", parent,  is_distance = False)


if __name__ == "__main__":
    main()
