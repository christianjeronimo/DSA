#!/usr/bin/python3
# p7.py
# part of Assignment #7: executable
# Assignment #7: Binary Search Tree
# p7.py: (tested/working)

from bst import BST
import sys

# executable file for assignment 7 and used to run
# a command line interface for the BST. reads lines from standard input and
# performs the corresponding BST operations
def main():
    bst = BST() # Binary Search Tree Instance created
    # reads command from standard input line by line
    for line in sys.stdin:
        # remove leading/trailing whitespace from input line
        line = line.strip()
        # Skip empty lines or lines starting with "#" comments in text file
        if not line or line.startswith("#"):
            continue # had to use continue, return would exit the program
        # and pass would read the string following the # in input.

        # split line into parts based on whitespace
        parts =line.split()
        # first part of line is the command
        command = parts[0]
        # if theres a seconf part turns it into an integer (key value)
        key = int(parts[1]) if len(parts) > 1 else None
        # process the command 
        if command == "insert":
            # insert the key into the BST and prints confirmation
            bst.insert(key)
            print(f"inserted {key}.")
        elif command == "search":
            # Search for the key in the BST and prints if it was found
            if bst.search(key):
                print(f"{key} found.")
            else:
                print(f"{key} not found.")
        elif command == "delete":
            # Delete the key from the BST and print confirmation or not found
            if bst.delete(key):
                print(f"deleted {key}.")
            else:
                print(f"delete {key} - not found.")
        elif command == "min":
            # find and print the minimum value in the BST
            result = bst.min()
            print(f"min is {result}." if result is not None else "tree empty.")
        elif command == "max":
            # finds and prints the maximum  value in the BST
            result = bst.max()
            print(f"max is {result}." if result is not None else "tree empty.")
        elif command == "predecessor":
            # find and pring the predecessor of the given key prints predecessor
            # of value if present or message if no predecessor for value
            if not bst.search(key):
                print(f"{key} not in tree.")
            else:
                pred = bst.predecessor(key)
                if pred is None:
                    print(f"no predecessor for {key}.")
                else:
                    print(f"{key} predecessor is {pred}.")
        elif command == "successor":
            # find and print the successor of the given key and prints the value
            # if no value is successor to key
            if not bst.search(key):
                print(f"{key} not in tree")
            else:
                succ = bst.successor(key)
                if succ is None:
                    print(f"no successor for {key}.")
                else:
                    print(f"{key} successor is {succ}.")
        elif command == "inorder":
            # perfom and print the in-order traversal of the BST
            print("inorder traversal:")
            print(" ".join(map(str, bst.inOrder())))
        elif command == "preorder":
            # perform and print the pre-order traversal of the BST
            print("preorder traversal:")
            print(" ".join(map(str, bst.preorder())))
        elif command == "postorder":
            # perform and print the post-order traveersal of the BST
            print("postorder traversal:")
            print(" ".join(map(str, bst.postorder())))
        else:
            # handles unknown input commands
            print(f"unknown input: {line}")

# Ensure the main function is called when executed directly
if __name__ == "__main__":
    main()
