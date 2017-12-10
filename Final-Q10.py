#!/usr/bin/python
# Question 10
# write a python program to find all words that are twelve characters long in biglist.txt

# This is how I like to open files, but our prof has taught us a different way.
#with open('biglist.txt') as f: # The with statement closes the file when we're done with it, that's why I like it. Not a big deal at this time.
#    bigList = f.readlines()
    
# The different way that you should use
f = open('biglist.txt')
bigList = f.readlines()
    
for line in bigList:
    if len(line.rstrip()) == 12: #rstrip removes those annoying newline (\n) characters from the calculation. Otherwise we'd get 10 character words
        print(line)
