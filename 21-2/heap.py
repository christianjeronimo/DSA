#!/usr/bin/python3
# heap.py
# heap/priority queue implementation for assignment 2
# Integer Minimum Heap and Priority Queue
# heap.py: (working/tested)

# Class object MinHeap is initialized as an empty list--root=0-- and is used to
# append into and store data along with doing a incomplete sort of the values 
# input into the MinHeap, which implements a priority queue to acheive this
class MinimumHeap:
    
    def __init__(self):
        self._heap = [] # empty list
        self._size = 0 # length or size of the data structure

    # using the len dunder method to call the length of the minheap.
    # uncertain if it's needed but it works when called.
    def __len__(self):
        return self._size

    # str dunder method used to convert the minheaps data into a string
    # it check to see if the heap is empty if it isn't it'll make a string with
    # the heaps size and element separated by commas. if it's empty it prints
    # heap size: 0-written a bit weird to meat 80 characters per line rule.
    def __str__(self):
        if self._size >= 0:
            return (
                f"heap size {self._size}: "
                f"{', '.join(map(str, self._heap[:self._size]))}"
            ) # added space after the comma in join prefix to match syntax.
        return "heap size: 0"

    # from my understanding this is the parent node index using the small
    # equation below to calculate it. Nothing further is Known by me
    def _parent(self, i):
        return ((i - 1) //2)

    # similar situation here, calculates the left child index
    def _left(self, i):
        return ((2 * i) + 1)

    # Calculates the right child's index
    def _right(self, i):
        return ((2 * i) + 2)

    # The min of three function is used to compare the parent node value to
    # that of the left and right chile. It looks to find an value that could be
    # smaller and if one is foun it updates the minimum to the smaller value
    # returns the index of the minimum value. Has boundry check to make sure the
    # index of the left and right child's are within the valid range of indices
    # in the heap list.
    def _min_of_3(self, i, left, right):
        minimum = i # minimum = parent node
        # checls the values at the indices of left and min
        if left < self._size and self._heap[left] < self._heap[minimum]:
            minimum = left # minimum becomes left if left value is smaller
        # same here but with right and indices
        if right < self._size and self._heap[right] < self._heap[minimum]:
            minimum = right # values change if right value is smaller
        return minimum

    # Used to maintain the min heap peroperty starting with the given i node
    # index calls min of 3 function to get the minimum valu, if that value is
    # not at index of i it swaps the values at index i and minimum.
    # recursively calles heapify to on the swaped/minimum child to ensure
    # the min-heap property is maintained on the tree.
    def _heapify(self, i):
        minimum = self._min_of_3(i, self._left(i), self._right(i))
        if minimum != i:
            self._swap(i, minimum)
            self._heapify(minimum)

    # Swap function used to swap values at indices i and j in the heap list
    def _swap(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    # convert an array or a portion of an array into a min-heap. used for loop
    # to iterate through the non-leaf nodes in the heap starting with the last
    # non-leaf node and decrements by 1 in each iteration until it reaches the
    # root. runs heapify for the non-leaf nodes to ensure the nodes satisfy the
    # min-heap property.
    def __build_heap(self):
        for i in range(self._size // 2 - 1, -1, -1):
            self._heapify(i)

    # used when inserting a new value or decreasing the value along with this
    # it's used to restore the min-heap property after the value is intoduced

    # revision: added bounds and value checks which were not added previously.
    def decrease_key(self, i, key):
        if i < 0 or i >= self._size:
            return

        if key > self._heap[i]:
            return
        
        self._heap[i] = key # value at index i is the key
        # compare values of heap[i] and parent(i) if parent is greater they swap
        while i > 0 and self._heap[self._parent(i)] > self._heap[i]:
            self._swap(i, self._parent(i))
            i = self._parent(i)
        
    # appends a value into the initialized _heap list  and increases the size
    # of the heap by one for the item introduced. called the decrease key
    # function with the hopes of maintaining the min-heap property for the
    # newly added value.
    def insert(self, data):
        self._heap.append(data)
        self._size += 1
        self.decrease_key(self._size - 1, data)
        return True

    # removes and returns the minimum element from the heap. if the heap if empty
    # returns 0 else it store the min vlaue at index 0 and replaces the root with
    # the last element. decreases _size by one and removes the last element
    # calls heapify to restore the min-heap property.
    def extract_min(self):
        if self._size == 0:
            return  0

        min_value = self._heap[0] # min value should be the root 
        self._heap[0] = self._heap[self._size - 1] # makes min value the last
        # element in the list pop without argument pops that value
        self._size -= 1
        self._heap.pop()
        self._heapify(0) # removed size check, replaced with heapify call

        return min_value

    # Returns a sorteed array of the heaps elements. creates a duplicate heap and
    # repeatedly extracts the minimum element from the copy and appends it to the
    # sorted_array, reverses the array and returns it as shown in the sample
    # output.

    # redid heap sort function commented out old code incase of reference point
    # will remove it once done, from there based on the provided psuedo code
    # along with the java code you provided during class I rebuilt it to this
    # sorted arr is a list replication of the heap while original heap is
    # used to preserve the heap itself thoughout the function and make sure
    # it isn't chance since this is only supposed to be affecting the list
    # copy then i return the sorted array.
    # for reference a student asked in class if he could copy or write down the
    # java code you were showing, you agreed and i figured might as well do the
    # same.
    def heap_sort(self):

        sorted_arr = list(self._heap[:self._size]) # list copy of array
        temp_size = self._size # ensuring the size of the list is == to heap size

        original_heap = self._heap # separate copy simply to preserve the heap
        # copied from java example, hope that's okay.
        original_size = self._size # same here

        self._heap = sorted_arr # used as a type of pointer or a helper so that
        # the heap functions heapify and swap work on the copy and doesn't affect
        # the original heap
        self._size = temp_size # same here but for the size of the copy.

        # for satement similar to the pseudocode provided used to call heap
        # functions to execute the sorting
        for i in range(self._size - 1, 0, -1):
            self._swap(0, i)
            self._size -= 1
            self._heapify(0)

        self._heap = original_heap # restore the heap structure
        self._size = original_size # restore the heap size,

        return sorted_arr # returns the sorted list

    
    
