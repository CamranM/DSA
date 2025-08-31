# Hashing

from collections import *

"""
1. Tests whether the letters in a string can be permuted to form a palindrome.
"""

'''
This function takes a string as input and hashes its letters into a python dictionary. Each key(letter) is mapped to 
a value, which is the number of occurrences of that letter in the word. If the amount of times a letter is present in
a word is odd is more than one, the function returns false. Otherwise, the word must be a palindrome, and the function
returns true.
'''
def canFormPalindrome(s):
    hash_table = {} # creates a dictionary

    # this for loop iterates through the string and assigns each letter in the dictionary a value of 0. This will
    # be used to increment the frequencies of each letter in the next for loop, and to do this, we must initialize each
    # value to 0 first.
    for letter in s:
        hash_table[letter] = 0 # all values are set to 0

    # this for loop iterates through the string and stores the amount of times a letter is present in the string as the
    # value in a key-value pair.
    for letter in s:
        hash_table[letter] += 1 # increments each value in a key-value pair

    # this variable will be used to count how many times a letter was present within a word an odd number of times
    occurrences_of_odd = 0

    # this for loop iterates through the hash_table, and if there is a letter that was in the string for an odd amount
    # of times, it increments the occurrences_of_odd variable
    for key in hash_table:
        if hash_table[key] % 2 != 0: # if the value(# of times the letter was present) was odd, variable is incremented
            occurrences_of_odd += 1

    # if the # of times a letter was present an odd amount of times is greater than 1, this can't be a palindrome,
    # since there can only be on middle letter(the letter that occurs once) in a palindrome. Therefore, the function
    # returns false
    if occurrences_of_odd > 1:
        return False

    # if the # of times a letter was present an odd amount of times is less than or equal to one, the string is a
    # and the function returns True
    else:
        return True

"""
2. Determines if it is possible to write an anonymous letter using a book.
"""

'''
This function takes in two strings as input, a book and a letter. The function returns True if the letter can be created
using the strings within book. Otherwise, it returns False. The function uses two hash table and maps the letters in book
and letter to the # of times they were present in both strings. The function compares the two hash tables to see if the
letter was created validly.
'''

def anonymousLetter(book, letter):
    hash_table_book = {} # creates the hash table for the book
    hash_table_letter = {} # creates the hash table for the letter
    valid = False # creates the valid variable

    # this for loop iterates through the book string and assigns each letter in the dictionary a value of 0. This will
    # be used to increment the frequencies of each letter in the next for loop, and to do this, we must initialize each
    # value to 0 first.
    for char in book:
        hash_table_book[char] = 0

    # this for loop iterates through the book string and stores the amount of times a letter is present in the string as the
    # value in a key-value pair.
    for char in book:
        hash_table_book[char] += 1

    # this for loop iterates through the letter string and assigns each letter in the dictionary a value of 0. This will
    # be used to increment the frequencies of each letter in the next for loop, and to do this, we must initialize each
    # value to 0 first.
    for char in letter:
        hash_table_letter[char] = 0

    # this for loop iterates through the letter string and stores the amount of times a letter is present in the string as the
    # value in a key-value pair.
    for char in letter:
        hash_table_letter[char] += 1
    #print(hash_table_book)
    #print(hash_table_letter)

    # if the letter string is empty, the letter hash table will also be empty. If the letter string is empty, it must
    # be present in the book, so we can create the letter using the book, and we return True.
    if hash_table_letter == {}:
        valid = True
        return valid

    # if the book string is empty and the letter string isn't empty, we can't create anything using the book string,
    # so we have to return false.
    elif hash_table_book == {} and hash_table_letter != {}:
        return False

    # this for loop iterates through the letter string, and compares the amount of times each letter occurred in the
    # letter string to the amount of times it occurred in the book string.
    for char in letter:

        # if the amount of times each character in the letter string is present less than or an equal amount of times than
        # in the book string, this means that we can use the book string to create the letter string, and we return True.
        if hash_table_letter[char] <= hash_table_book[char]:
            valid = True

        # otherwise, if the amount of times a character occurred in the letter string is greater than the amount of
        # times it occurred in the book string, we can't use the book to create the string, and we return false
        else:
            valid = False
            return valid
    return valid # if the letter string can be created using the book string we return valid
