#!/usr/bin/python
# Question 5
# Write a Python script to check if a given key already exists in a dictionary

dictionary = {'a':'yo','b':'hahaha','elephant':'unicorn','stuff':'morestuff'} # Trash dictionary to do stuff on lol

def dCheck(dictionary,term): # Made a function 'cause that's always nice for reusability
    if term in dictionary:
        return True
    else:
        return False

print(dCheck(dictionary,'a')) # This prints "True" since 'a' is a key in dictionary
print(dCheck(dictionary,'unicorn')) # This prints "False" because 'unicorn' isn't a key in dictionary (even though it is a value of key 'elephant')

# Dictionaries are like lists, except not sequential (instead of indexes they use keys)
