#!/usr/bin/python
# Question 9
# Write a program to read first n lines of a file

fil = 'biglist.txt'

# Again with my personal preference for opening files.
#with open(fil) as f:
#    text = f.readlines()

f = open(fil)
realtext = f.readlines()

def readXlines(x,text=realtext): # define a function that takes X as how many lines, and text for what text to scan (I have it set by default to our other text variable)
    for line in text:
        print(line)
        x-=1 # This is a weird way to iterate through a for loop x amounts of times, but it works. A while loop would work too, but that would make iterating through the lines more annoying.
        if x<=0:
            break

readXlines(12) # We don't have to define text since the default works with our variable
