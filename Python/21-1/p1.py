#!/usr/bin/python3
# p1.py
# executable file for Assignment #1: Review (Tested/working)
# Linked Lists, Stacks, and queues

from stack import Stack
import sys

# This is the main function used to take lines of input pushing the information
# into the stack structure and poping the lines as long as the Stack is not empty
# the function stops running as soon as the isEmpty function returns True.
def main():
    stack = Stack() # Implementation of Stack Data Structure
    for line in sys.stdin: # takes line from STDIN
        stack.push(line) # takes line and adds it to the Stack
    while not stack.isEmpty(): # checks to see if the Stack is empty.
        print(stack.pop(), end="") # prints out the first line in the stack and
# a newline after it or rather starts a new line to print the following line onto 

if __name__ == "__main__":
    main()
