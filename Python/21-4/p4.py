#!/usr/bin/python3
# p4.py
# part of Assignment #4: executable
# Assignment #4: Radix-bucket sort hybrid
# p4.py: (tested/working)
# copied from quicksort function with minor changes
import sys
from radix_bucket import RadixBucketSort

# main function used to take/read input from standard input. Uses radixbucketsort
# to sort the input and prints the sorted output
def main():
    # reads input form standard in, uses list comprehension to add it to
    # an array/list, doesn't take empty input.
    numbers = [int(line.strip()) for line in sys.stdin if line.strip()]
    arrange = RadixBucketSort() # creates radixbucketsort object
    sorted_numbers = arrange.sort(numbers) # calls the sort function on numbers

    for num in sorted_numbers: # prints numbers formatted to 9 digits
        print(f"{num:09d}")

if __name__ == "__main__":
    main()
