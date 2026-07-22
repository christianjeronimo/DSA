#!/usr/bin/python3
# LinkedList.py
# Part of Assignmetn #1 review.
# Linked Lists, Stacks, and Queues
# LinkedList.py: (Tested/working)

class Linked_List:
    # Used some of the Linked List programs I programed in CS20P
    # the link node that will hold the data and the Pointers are
    # initialized here in the Node class
    class Node:
        def __init__(self, data = 0):
            self.data = data
            self.next = None
            self.prev = None

    # another initialization block this one to have both head and tail
    # initialized as the beggining of the Linked list and the end of the list
    # respectfully we also have an index just to have and provide some
    # support for iteration might remove, i don't think it's needed
    def __init__(self):
        self.head = None
        self.tail = None
        self.index = None

    def __iter__(self):
        self.index = self.head
        return self

    # String dunder method used to collect data from nodes into a built-in list
    # then using the join method/function to create and return the string of
    # the information
    def __str__(self):
        result = [] # list used to contain Data from nodes
        current = self.head # begginning of Linked list
        while (current != None): # while function used to transverse through
            # the linked list
            result.append(str(current.data)) # appends node data into result list
            current = current.next # moves on to the next node
        return " ".join(result) # concatenates the information to form a string.

    # checks to see if the Linked List is empty using a boolean operand
    # will return tru if empty or self.head is none, false if self.head holds
    # data.
    def isEmpty(self):
        return self.head == None
    
    # Insert from takes data or words and adds them to the front of the list
    # then re-assigns pointers if there is already a node with data.
    def insertFront(self, word):
        # simply returns and does nothing to the list if there is no data in word
        if not word:
            return

        # makes a node in the linked list that contains the word as it's data
        node = self.Node(word)

        # this if statement takes into consideration that the Linked list is
        # empty there for the previously made node containing word would be both
        # the head and tail of the list as the first data entry.
        if self.head is None:
            self.head = node
            self.tail = node
        # else block considers there already being data in the List and sets up
        # pointers in the list to account for the changes and making the new node
        # the head of the LInked List.
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
    # pretty much does the samething as the insert front function only this time
    # inserting to the rear and adjusting pointers accordingly.
    def insertRear(self, word):
        # does nothing to the list just returns nothing if the input is nothing
        if not word:
            return
        
        # sets up node as the data entry you wwant to make to the rear this time
        node = self.Node(word)

        # the if statement also considers the linked list already being empty
        # an if this statement comes back true designates node as the head
        # and tail of the Linked List.
        if self.head is None:
            self.head = node
            self.tail = node
        # if data is already present in the list re-assigns the pointers so
        # that the new node will be tail and prev pointer points at the old
        # tail or second to last data entry
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    # function designed to remove the first node in the Linked list or head
    # get the data of the head node and removes it by changing the pointers
    # away from the node and printing the node's data
    def removeFront(self):
        # Returns None if there is nothing in the Linked list to remove
        if self.head is None:
            return None
        # data is disignated the head node's data.
        data = self.head.data
        # if there is only one node in the Linked list it is both the head
        # and the tail and to ensure it's removal we set both head and tial
        # equal to None and returning the node's data
        if (self.head is self.tail):
            self.head = self.tail = None
            return data
        # if there is more than one node we re-assign the pointers to make
        # sure the Head node isn't associated in the linked List anymore
        # therefore successfully removing the node.
        self.head = self.head.next
        self.head.prev = None
        return data

    # Does the same as the remove front function but with the removal of
    # the nodes at the rear of the Linked list or tail by re-assigning the
    # pointers and returning the node's data
    def removeRear(self):
        # returns None if there is nothing in the Linked list.
        if self.head is None:
            return None
        # Designates the Linked list tail data to the variable data.
        data = self.tail.data
        # does the same here if the function only has one node re-assigns
        # the head and tail to none and returns the data in that node.
        if (self.head is self.tail):
            self.head = self.tail = None
            return data
        # more than one node, re-assigns the pointers away from the Rear node
        # Which should dissociate the rear or tail node from the rest of the
        # linked list and returns the data of that node.
        self.tail = self.tail.prev
        self.tail.next = None
        return data
    
    
