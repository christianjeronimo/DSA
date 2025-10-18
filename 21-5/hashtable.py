#!/usr/bin/python3
# hashtable.py
# Part of Assignmetn #5 Hash Table class object.
# hashtable.py: (Tested/working)

import math

# class object hashtable-data structure based on a list of lists
# runs functions such as insert, delete, and search all meant to run O(1)
# Ran into issue with self._key previously had as self.__key caused
# problems for a while.
class HashTable:

    # Record class made ro be a data interface for the hashtable class
    # object contains key and value information,along with a function
    # meant to provide string representation of the records as inputed
    class Record:
        def __init__(self, key: int, value: str):
            self._key = key # 9 digit integer
            self._value = value # information/data to be inserted

        def get_id(self):
            return self._key

        def clone(self): # used to make duplicate of information
            # or rather a copy of the object, ran valgrind (correctly i hope)
            # no leaks were reported or raised, <- might be inaccurate if run
            # by someone more knowledgeable.
            return HashTable.Record(self._key, self._value)

        def __repr__(self): # provides string representation of Record
            return f"{self._key} {self._value}"

    # init function used to initialize parts of the hash table such as the
    # such as the constant c set to  the inverse of phi. capacity is set to
    # the default of zero but can be overriden if larger size is needed in th
    # main file. table is set to be a list of lists- line copied from
    # RadixBucketsort assignment.
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]
        self.C = 0.618034

    # returns the numbers stored int the hash table.
    # not used but present
    def __len__(self):
        count = 0
        for chain in self.table:
            count += len(chain)
        return count

    # used to provide a string representation of the table
    # not used but, habit to code the function.
    # uses a list to collect the data and a for loof to iterate through the table
    def __str__(self):
        result = []
        for i, chain in enumerate(self.table):
            if chain:
                result.append(f"{i}: {chain}")
        return "\n".join(result)

    # hash function as described in class to generate an index within the table
    # assumption based on notes since other functions are reliant on this no
    # bounds check are neede since it is indirectly handled, multiplication
    # method implemented returning values between 0 and capacity - 1.
    def _hash(self, key: int) -> int:
        return int(self.capacity * (key * self.C - (int(key * self.C))))

    # find function used as a helper function for the insert function
    # and delete function looks for index based on the key provided and the hash
    # value determined by the hash funcction returns index of the bucket, index
    # of the record and the records object.
    def _find(self, key: int):
        index = self._hash(key) # hash call
        for i, record in enumerate(self.table[index]):
            if record._key == key: # makes sure the keys are the same since the
                # data following should be the information looked for.
                return index, i, record # index of bucket, location of item in
            # bucket, record object.
        return -1, None, None # none values if not found

    # simple insert function since we are using the chaining method,
    # we simply append the items into the list found at the index determined
    # by the hash function and the input key.
    def insert(self, record):
        index = self._hash(record.get_id())
        self.table[index].append(record.clone())

    # search function, searches for a record with the given key in the hash
    # table provide or returns a clone of the found Record object or None
    # if not found.
    def search(self, key: int):
        index = self._hash(key)
        for i, record in enumerate(self.table[index]): # used for iteration
            if record.get_id() == key: # matches the inputed key to the key
                # stored with the Record object in the index
                return record.clone()
        return None

    # Deles a record with the given key from the hash table and the user
    # if found returns a copy of the Record object else returns false
    # uses find function to fince record in the table.
    def delete(self, key: int):
        index, i, record = self._find(key)
        if i is not None:
            del self.table[index][i]
            return record.clone()
        return False

    # called to clear the hash table, reinitializes the table to the same
    # capacity but essentially reassigns the table to a new table, old
    # table isn't reference in any way so it simply seizes to exist
    # because of pythons garbage collection and lack of reference.
    def clear(self):
        self.table = [[] for _ in range(self.capacity)]

