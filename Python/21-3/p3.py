#!/usr/bin/python3
# p3.py
# part of Assignment #2: executable
# Assignment #3: Quicksort
# p3.py: (tested/working)

import sys
from quicksort import QuickSort

# main function used to take/read input from standard input. Uses quicksort
# to sort the input and prints the sorted output
def main():
    # reads input form standard in, uses list comprehension to add it to
    # an array/list, doesn't take empty input.
    arr = [int(line.strip()) for line in sys.stdin if line.strip()]
    mo3_value = 35 # sets median of three value
    arrange = QuickSort(arr, mo3_value) # creates quicksort obje
    arrange.sort()

    for num in arrange.arr:
        print(f"{num:09d}")

if __name__ == "__main__":
    main()
