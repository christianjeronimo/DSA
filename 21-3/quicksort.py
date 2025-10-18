#!/usr/bin/python3
# quicksort.py
# part of Assignment #2: quicksort class object
# Assignment #3: Quicksort
# quicksort.py: (tested/working)

# quicksort class object used to sort input in ascending order
# used for big and small files. This specific sorting method uses lomuto
# partitioning to sort the input. it uses a pivot so that when sorting the
# elements it rearranges the array leading to the smaller elements on the left
# of the pivot and the greater elements to the right of the pivot.
# recursively applies this pivot method to the left and right subarrays created
# by the pivot
class QuickSort:
    # initialized the list or array and the mean of three value in this init
    # function.
    def __init__(self, arr, mo3_value):
        self.arr = arr
        self.mo3_value = mo3_value

    # median of three function used to calculate the median of three elements
    # taking the leftmost and rightmost index of the subarray. adds them
    # together and calculates the index of the median element.
    # compares the values at the index and returns the one most in the middle?
    # rather compares the values to ensure what is returned is between the
    # values at the other two indexes.
    def median_of_three(self, left, right):
        middle = (left + right) // 2 # middle index
        a, b, c = self.arr[left], self.arr[middle], self.arr[right]
        if (a < b < c) or (c < b < a): # comparisons making sure the value is
            # between the two other values
            return middle
        elif (b < a < c) or (c < a < b):
            return left
        else:
            return right
    # lomuto partitioning used to partition the subarray using the Lomuto
    # partition algorithm.  first check to see if the subarray is large enough
    # if not it goes straight to the rightmost element and  uses that as the
    # pivot. then swaps the elements accordingly i.e the element is less than
    # the pivot.
    def lomuto_partition(self, left, right):
        # checks to see if the subarray is long enough to use median of three.
        if right - left + 1 > self.mo3_value:
            mid = self.median_of_three(left, right) # calls mo3 function on the
            # arrays and uses the returned index.
            self.arr[mid], self.arr[right] = self.arr[right], self.arr[mid]
            # swaps the values at the right and mid index
            pivot = self.arr[right] # then makes the new right value the pivot
        else:
            pivot = self.arr[right] # uses rightmost element as pivot

        i = left - 1 # index of smaller element as shown in notes.

        # goes through the array and swaps values when needed
        for j in range(left, right):
            if self.arr[j] < pivot: # checks if value is less than pivot
                i += 1 # increments the i value by 1 since it is first
                # set out of bounds as shown in class
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                # if element at j is smaller then pivot, element at j and i swap
        self.arr[i + 1], self.arr[right] = self.arr[right], self.arr[i + 1]
        # once done with array places pivot its correct position
        return i + 1

    # recursive function to perform quick sort on the subarray then on the left
    # and right subarrays to completely sort the subarray. made private to
    # indicate not to touch.
    def _quicksort(self, left, right):
        if left < right:
            pivot_index = self.lomuto_partition(left, right)
            # partitions subarray
            self._quicksort(left, pivot_index - 1) # recursively sort the left
            self._quicksort(pivot_index + 1, right) # recursively sort the right

    # used to initiate the quicksort process.
    def sort(self):
        self._quicksort(0, len(self.arr) -1) # calls the recursive quicksort
        # function.
