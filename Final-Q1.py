#!/usr/bin/python
# Question 1
# Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
import re

stuff = input("Please type a sentence")
if re.match("^[A-z0-9]*$", stuff):
    print("Yay! You're a conformist! Good job following the rules.")
else:
    print("You included \x1B[3mspecial\x1B[23m characters. What a rebel. Also spaces count as special characters so... sorry")

