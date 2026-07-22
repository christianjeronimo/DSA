#!/usr/bin/python3
# bst.py
# part of Assignment #7:
# Assignment #7: Binary Search Tree
# bst.py: (tested/working)

# implementation of a Binary Search Tree (BST) data structure, supports insertion,
# search, inorder, preorder, postoder taversals, along with successor and delete
# as discussed in class.
class BST:
    # Node representation in the BST, each node contains data and references to
    # it's parent, left and right children which are used to support the functions
    # implemented
    class Node:

        def __init__(self, data):
            # initializes a new node and store the data in the node
            self.parent = None
            self.left = None
            self.right = None
            self.data = data

    def __init__(self):
        # initializes an empty BST with a Null root
        self.root = None


    def insert(self, data):
        # inserts a new node with the given data into the BST, Maintains BST
        # property by inserting data less than the node's data into the left
        #subtree and greater values into the right subtree.
        node = self.Node(data)
        prev = None
        temp = self.root
        # traverse the tree to find Appropiate insertion point
        while(temp is not None):
            prev = temp
            if (data < temp.data):
                temp = temp.left
            else:
                temp = temp.right

        node.parent =  prev
        # If the tree was empty, the new node becomes the root
        if prev is None:
            self.root = node
            return

        # Links the new node to its parent either as the left or right child
        if (data < prev.data):
            prev.left = node
        else:
            prev.right = node

    # preforms an inorder traversal of the BSTz visits node in ascending order
    # of the stored data, and returns a list containing the data of the nodes
    # in ascending order
    def inOrder(self):
        results = []
        self._inOrder(self.root, results)
        return results

    # inorder private function(recursive) used to healp with the inorder
    # traversal, private since user does't have access to data directly
    # and to avoid middling with code
    def _inOrder(self, node, results):
        if node is None:
            return
        self._inOrder(node.left, results)
        results.append(node.data)
        self._inOrder(node.right, results)

    # Searches for a node with the given key in the BST, with a value being
    # providded and outputs true or false if the value is in the tree
    def search(self, key):
        return self.__search(self.root, key) is not None

    # Recursive helper function for searching.
    # returns node if found or None if not
    def __search(self, node, key):
        if node is None:
            return None
        if node.data == key:
            return node
        if key < node.data:
            return self.__search(node.left, key)
        return self.__search(node.right, key)

    # contains function allows checking of a key in the BST using the "in"
    # operator. returns true if key exists, false otherwise. Not codded for
    # assignment but not removed since it is useful and it doesn't
    # disturb anything
    def __contains__(self, key):
        return self.search(key)

    # Iterative search for a node with the given key in the BST, not called
    # on but not removed just to have both implemented.
    def isearch(self, key):
        return self.__iseearch(self.root, key) is not None

    # Iterative helper function for searching node is the current node being
    # checked and the key is the value being searched for.
    def __isearch(self,key):
        while (node is not None and node.data is not key):
            if key < node.data:
                node = node.left
            else:
                node = node.right
        return node

    # Finds the minimum value in the BST, returns the value if tree isn't
    # empty or None otherwise
    def min(self):
        if self.root is None:
            return None
        return self.__min(self.root).data

    # Recursive private function to find the node with the minimum value
    # constanly goes down the left subtrees/node to find the leftmost node
    def __min(self, node):
        while node.left is not None:
            node = node.left
        return node

    # similar to the min function but for the maximum value in the BST
    def max(self):
        if self.root is None:
            return None
        return self.__max(self.root).data

    # Private recursive function does the same as the private min function
    # but repeatedly goes down the right to find the rightmose node
    def __max(self, node):
        while node.right is not None:
            node = node.right
        return node

    # finds the successor of a node with the given key-next largest value.
    # returns the successor value if it exists else None
    def successor(self, key):
        target = self.__search(self.root, key)
        if target is None:
            return None
        result = self.__successor(target)
        if result is None:
            return None
        return result.data

    # private function used to iterate through the tree breifly to find
    # the successor value
    def __successor(self, node):
        if (node.right is not None):
            return self.__min(node.right)
        temp = node.parent
        while (temp is not None and node == temp.right):
            node = temp
            temp = temp.parent

        return temp

    # does similar thing as the successor function but for the next
    # smaller value and returns the value if it exists
    def predecessor(self, key):
        target = self.__search(self.root, key)
        if target is None:
            return None
        result = self.__predecessor(target)
        if result is None:
            return None
        return result.data

    # Privat function used to find the predecessor of a given node by
    # breifly going through the BST using the Max function
    def __predecessor(self, node):
        if (node.left is not None):
            return self.__max(node.left)
        temp = node.parent
        while (temp is not None and node is temp.left):
            node = temp
            temp = temp.parent

        return temp

    # deletes a node with a given value from the BST and returns true
    # if the value was found and deleted, false otherwise
    def delete(self, value):
        target = self.__search(self.root, value)
        if target is None:
            return False
        self.__delete(target)
        return True

    # private delete function used to perform the deletion of a given node
    # handles cases of 0 childre, one child and 2 children
    def __delete(self, node):
        # Case 1: Node has at most one child
        if( node.left is None or node.right is None):
            target = node
        else:
            # Case 2: Node has two children, find its successor
            target = self.__successor(node)
        # ex is the child of the target or none if no children
        if target.left is not None:
            ex = target.left
        else:
            ex = target.right
        # if ex exist updates parent reference
        if ex is not None:
            ex.parent = target.parent
        # update the parent of the target to point to ex
        if target.parent is None:
            self.root = ex # target was the root
        elif target is target.parent.left:
            target.parent.left = ex
        else:
            target.parent.right = ex
        # if the node to be deleted was not the successor, copy the
        # successors data
        if node is not target:
            node.data = target.data
        # removes the target node
        del target

    # performs a pre-order traversal of the BST, Visits current nod first,
    # then left subtree, then right subtree. returns a list containing the
    # data of the nodes in pre-order sequence
    def preorder(self):
        results = []
        self.__preorder(self.root, results)
        return results

    # recursive function for preorder traversal appends data then visits
    # left then right appending the data respectivly.
    def __preorder(self, node, results):
        if node:
            results.append(node.data)
            self.__preorder(node.left, results)
            self.__preorder(node.right, results)

    # performs a postorder traversal of the BST, Visits left subtree, then
    # right subtree the the current node, returning the list containing
    # the data of the nodes in post-order sequence
    def postorder(self):
        results = []
        self.__postorder(self.root, results)
        return results

    # recursive function for post-order traversal appending the data
    # from the left then the right and fincaly the current node into the list
    def __postorder(self, node, results):
        if node:
            self.__postorder(node.left, results)
            self.__postorder(node.right, results)
            results.append(node.data)
