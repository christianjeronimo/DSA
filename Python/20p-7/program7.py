#!/usr/bin/python3
# program7.py
# Solitaire Encryption (Assignment #7: tested/working)

# This is a program used to encrypt and decrypt messages, the program ignores non 
# alphabetacle characters in the users input then the program using a deck file
# creates an encrypted version of the input. Does the same when decrypting but
# instead it taked the encrypted string and decrypts it as long as the same
# deck file is used


import sys

# The clean function filters out all characters in the message the user would
# like to encrypt, that aren't letters. This then proceeds to capitalize the
# message and adds padding-"X"- to the message if its length isn't a multiple
# of five.

def clean(message):
    clean_message = ''.join(char for char in message if char.isalpha())
    clean_message = clean_message.upper()
    padding = (5 - len(clean_message) % 5) % 5 # calculate the padding needed
    clean_message += 'X' * padding
    return clean_message # returns clean message

# function used to open the deck file provided by the user
# using the with portion handles the opening and closing of the file
# returns the deck as a list of integers instead of a list of the values
# in the text.
def read_deck(file_name):
    with open(file_name, 'r') as file:
        return [int(card) for card in file.readline().split()]

# The move card function is the one used to move the jokers according to 
# how it is descibed in the assignment, steps is used to ensure the cards
# are being moved the right amount of times beforehand whenever a joker
# was second to last in the deck the joker would move three indexes down
def move_card(deck, card, steps = 0):
    for _ in range(steps):
        index = deck.index(card) # location of card
        if index == len(deck) - 1: # check if the card is at the end of list
             deck[index], deck[0] = deck[0], deck[index] # swaps first and last
        else:
            deck[index], deck[index + 1] = deck[index + 1], deck[index]
            index += 1
    
# This function is used as the triple cut of the assignment just slicing the
# portion above and below the jokes-not the cards in-between-and swaps them
# either infront of the seconf joker or behind the first joker
def triple_cut(deck):
    first_j = min(deck.index(27), deck.index(28))
    second_j = max(deck.index(27), deck.index(28))
    deck[:] = deck[second_j + 1:] + deck[first_j: second_j + 1:] + deck[:first_j]

# This function executes the bottom cut, or rather the slicing of the first
# values in the deck according to the number value of the last card, so if the
# last card is four it slices the first four cards and moves them in front
# of the last card.
def bottom_cut(deck):
    bottom_value = deck[-1] if deck[-1] < 27 else 27
    deck[:] = deck[bottom_value:-1] + deck[:bottom_value] + [deck[-1]]

# The key stream funciton is used to generate the values used to encrypt and
# decrypt the message the user chooses by shuffleing throught the deck to
# provide these value
def keystream_value(deck):
    while True:
        move_card(deck, 27, steps = 1) # moves first joker
        move_card(deck, 28, steps = 1) # moves second joker two times
        move_card(deck, 28,  steps = 1)
        triple_cut(deck) # executes the shuffling described
        bottom_cut(deck)
        top_value = deck[0] if deck[0] < 27 else 27 # finds the top value
        # as long as the value is less than 27 else 27 is assigned to top value
        keystream_card = deck[top_value] # finds the card at the top value index
        if keystream_card < 27:
            return keystream_card

# turn text to numbers using list comprehension by filtering for alphabetical
# values or letters, in the list comprehension the beginning looks uses the 
# unicode code point of the letters and fincing the difference between those
# and the unicode value of A, If the char is A the difference would be 0 plus
# one makes the numbering start from one to 26 giving them numerical values
# ranging from 1 to 26.
def text_to_num(text):
    return [ord(char) - ord('A') + 1 for char in text if char.isalpha()]

# This does the opposite and turns the numbers to letters finds the unicode
# for the letters adds the num and subtracts one for 1-based indexing the chr
# casting is used to turn the integer into letters.
def num_to_text(numbers):
    return ''.join(chr(num + ord('A') - 1) for num in numbers)

# Used for encryption by turning the letters in the text into numbers
# cycles through the numbers from the message and generates values for them
# then the numbers created from the message and the ones generated minus one
# to make up for the 0-based indexing, modulus 26 used to wrap around the aphabet
# and adds one to shift the result up by one to match the maping of letters to
# numbers then provides the new letters in the final line.
def encrypt (deck, preprocess):
    message_numbers = text_to_num(preprocess.upper())
    keystream = [keystream_value(deck) for _ in message_numbers]
    encrypted_numbers = [(m + k -1) % 26 + 1 for m,k in zip(message_numbers, keystream)]
    return num_to_text(encrypted_numbers)

# This function is made to do the opposit of the encrypt function## just in a
# reversed method and the decrypted numbers uses subtracts the keystream values
# from the message nubers with the addition of indexing and mapping adjustments
# returns decrypted message
def decrypt (deck, message):
    message_numbers = text_to_num(message.upper())
    keystream = [keystream_value(deck) for _ in message_numbers]
    decrypted_numbers = [(m - k - 1) % 26 + 1 for m,k in zip(message_numbers, keystream)]
    return num_to_text(decrypted_numbers)

# main function used to handle the input and the mode of the program 
def main():
    if len(sys.argv) < 3: # checks the legnth of the line used to run progran
        print("Usage: ./program7.py e/d deck-.txt")
        return

    mode = sys.argv[1].lower() # gets the users choice of encrypt and decrypt
    deck_file = sys.argv[2] # get the name of the file
    try:
        deck = read_deck(deck_file)
    except FileNotFoundError: # asks for file name if none is provided
        print(f"Error: File {deck_file} not found.")
        return

    if mode == "e": # runs the program through the encrypt function
        message = input("Enter message to be encrypted(non-letters ignored): ")
        preprocess = clean(message) # removes whitespace and punctuation
        print("Plaintext message is:", preprocess)
        encrypted_message = encrypt(deck, preprocess) # encrypts input
        print("The encrypted message is:", encrypted_message)
    elif mode == "d": # runs the program through the decrypt function
        message = input("Enter message to be decrypted: ")
        decrypted_message = decrypt(deck, message) # decrypts message
        print("The decrypted message is:", decrypted_message)
    else: # used if no mode is provided.
        print("Invalid mode. Use 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()
