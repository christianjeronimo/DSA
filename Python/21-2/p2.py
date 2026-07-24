#!/usr/bin/python3
# p2.py
# main/executable file for assignment 2
# Integer Minimum Heap and Priority Queue
# heap.py:(working/tested)
import sys
from heap import MinimumHeap

# initialized the minimum heap and the capacity in the main function
# tajes user input into the Min-heap and appends if its a positive value
# if not then 0, -1, and -2 operate in a separate way providing different
# information and calling different functions
def main():
    capacity = 2_400_000 # self._size shouldn't exceed this value
    heap = MinimumHeap() # heap initialization

    for line in sys.stdin:
        line = line.strip()
        try:
            value = int(line)
            if value > 0:
                if heap._size < capacity:
                    heap.insert(value)
                    print(f"insert: {value}")
            elif value == 0:
                print(heap)
            elif value == -1:
                print(f"extract min: {heap.extract_min()}")
            elif value == -2:
                sorted_array = heap.heap_sort()
                print("sorted array:", sorted_array) # fixed to return [] when
                # heap is empty or contain the elements within the brackets.
        except ValueError:
            pass

if __name__ == "__main__":
    main()
