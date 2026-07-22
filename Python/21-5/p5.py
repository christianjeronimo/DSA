#!/usr/bin/python3
# p5.py
# main/executable file for assignment 5
# Hash tables
# p5.py:(working/tested)


import sys
from hashtable import HashTable

# the hashtable object file used to take interactive input to execute certain
# functions relating to the hashtable.
# lad function for input = 1, Loads records from a specified ASCII text file
# into the hash table. takes in the name of the file to read from, and the
# the hashtable to load the records into are the arguments for this function

def load_file(filename, hashtable):
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip() # remove whitespace
                if not line: # used to skip empty lines
                    pass
                parts = line.split(" ", 1) # separates linto a key and info
                if len(parts) == 2: # insures both actually exist
                    key_str, info = line.split(" ", 1)
                    if key_str.isdigit() and len(key_str) == 9: # ensures key
                        # if a number is is nine digits long as specified
                        key = int(key_str) # converts key string to integer
                        value = info if info else ''
                        hashtable.insert(HashTable.Record(key, value)) # calls
                        # hashtable insert function.
                    else:
                        pass # pass used because alternatives are verbose
                else:
                    pass
                
    except FileNotFoundError:
        print("file not found.")
    except ValueError:
        print("Invalid format in file.")

# save function used to save the contents of the hash table to a specified
# file takes in the filename and current hash table object as the arguments
def save_file(filename, hashtable):
    try: # with statement statement used to access and close the file
        with open(filename, 'w') as file:
            for chain in hashtable.table:
                for record in chain:
                    file.write(f"{record.get_id() : 09d} {record._value}\n")
                    # writes the key padded to 9 digits succeeded by the value
    except Exception as e:
        print(f"Error saving file: {e}")

# main function is the function handling the interactive portion of the program
def main():

    hashtable = HashTable(178000) # initializes the hashtable w/specific capacity
    while True: # used to repeadedly print menu until quit is hit
        menu_str = "(1)load (2)insert (3)delete (4)search "
        menu_str += "(5)clear (6)save (7)quit -- Your choice? "
        print(menu_str, end='') # print menu in one line without having code line
        # exceed 80 characters
        choice = input() # get user input for menu choice

        if choice == '1': # calls load_file function when selected
            filename = input("read hash table - filename?  ").strip()
            load_file(filename, hashtable)

        elif choice == '2': # input value to insert value into the hash table
            print("input new record: ")
            line = input().strip()
            parts  = line.split(' ', 1)
            if len(parts) == 2: # does the same as load function to add data
                key_str, value = parts
                if key_str.isdigit() and len(key_str) == 9:
                    key = int(key_str)
                    hashtable.insert(HashTable.Record(key, value))
                else: # avoids reading bad non digit key entry
                    print("invalid key format.")
            else: # skips input not containing both key and value/info inputs
                pass

        # input used to delete information provided by a specific key value
        elif choice == '3':
            key = int(input("delete record - key? ").strip()) # takes int value
            deleted_record = hashtable.delete(key) # calls hashtable delete
            # member function
            if deleted_record: # returns record contents: key value
                print(f"Delete: {deleted_record}")
            else: # used if record is not found in the function
                print(f"Delete not found: {key}")

                
        # searches for record based on key         
        elif choice == '4':
            key = int(input("search for record - key? ").strip())
            result = hashtable.search(key) # calls member function
            if result:
                print(f"Found: {result}")
            else:
                print(f"Search not found: {key}")

        # clears the current hash table.
        elif choice == '5':
            hashtable.clear()
            print("Clearing hash table.")

        # # choice called to save hashtable data to a file calls save_file
        # to accomplish this calles for a filename
        elif choice == '6':
            filename = input("Write hash table - filename? ").strip()
            save_file(filename, hashtable)

        # this is the quit function used to exit the program
        # uses break because other solotions are verbose.
        elif choice == '7':
            break


        else: # place here if another input is used.
            print("Invalid choice. Please select 1–7.")


if __name__ == "__main__":
    main()
