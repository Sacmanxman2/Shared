#!/usr/bin/python
# Question 5
# Write a Python script to check if a given key already exists in a dictionary

dictionary = {'a':'yo','b':'hahaha','elephant':'unicorn','stuff':'morestuff'}

def dCheck(dictionary,term):
    if term in dictionary:
        return True 
    else:
        return False

print(dCheck(dictionary,'a'))
print(dCheck(dictionary,'unicorn'))
