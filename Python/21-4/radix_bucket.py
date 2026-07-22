#!/usr/bin/python3
# radix_bucket.py
# part of Assignment #4: executable
# Assignment #4: Radix/Bucket Sort Hybrid
# radix_bucket.py: (tested/working)

# Class objectt RadixBucketSort used as implementation of the sorting algorithm
# set as class object for reuseability. 
class RadixBucketSort:

    # digits is initialized here since the input is definitively exactly 9
    # digits in length as defined in the assignment however could be set
    # to something different for different size of input
    def __init__(self, digits = 9):
        self.digits = digits # stores as attribute

    # digit_value extracts the degit at a specific position(index) from
    # the given value. index defined in another function goes from 0 to 9
    # and is used for the floor division part then after that it uses
    # modulo to get the end value or remainder.
    def digit_value(self, number, index):
        # 10 ** index index ranges from 0-9 effectively allowing to view
        # the rightmose integer which is brought out by % 10, effectively
        # extracting the digit at the specifies position later used to sort
        return (int(number) // (10 ** index)) % 10

    # Radix bucket sort hybrid function as described in class and pseudo-code
    # iterates through each digit position (index) as mentioned above to capture
    # the least significat digit (index 0) to the most significant (index 9)
    # creates buckets to hold the numbers with the same digit value, then goes
    # through the numbers in the input list numbers to begin the sorting.
    # size, digits, and range already handles and not needed as arguments for
    # function
    def _rbsort(self, numbers):
        # finds the digit value of the rightmost number then uses that as an
        # index for which bucket the value shoul be put into.
        for index in range(self.digits):
            # creates 10 empty buckets to hold numbers 
            buckets = [[] for _ in range(10)]
            # iterates through the numbers input list.
            for number in numbers:
                # value gets rightmost integer of the input number
                value = self.digit_value(number, index)
                # value used as bucket index for the number which is added there
                buckets[value].append(number)
            # numbers used to collect the values in the buckets back into the
            # numbers list after the numbers had been sorted based on the
            # current digits and iterating through all the buckets and the then
            # the values in each bucket. once the for loop is done, the sorted
            # elements are store in numbers and returned
            numbers = [num for bucket in buckets for num in bucket]

        return numbers

    # Calls the _rbsort method to perform the sorting
    def sort(self, numbers):
        return self._rbsort(numbers)
    
