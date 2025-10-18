#!/usr/bin/python3
# stack.py
# part of Assignment #1: Review (Tested/Working)
# Linked List, Stacks, and Queues

# imports the Linked_List class object from the LinkedList.py file
from LinkedList import Linked_List

# Creates Stack object which will Utilize the methods defined in the
# LinkedList.py file but only a select few since the Stack structure
# only adds and remove items from the front.
class Stack:
    # initializes itself as a Linked list object.
    def __init__(self):
        self._list = Linked_List()

    # Dunder string function calls the linked list function which should
    # help return the added items as strings.
    def __str__(self):
        return self._list.__str__()

    # the Push function is like an append function which is why it calls
    # the insertFront function from the linked list
    def push(self, word):
        return self._list.insertFront(word)

    # pop function here removes the head of the Linked list and returns the
    # data in string form
    def pop(self):
        return self._list.removeFront()

    # the isEmpty function just checks to see if the stack is empty or not.
    def isEmpty(self):
        return self._list.isEmpty()
