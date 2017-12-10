#!/usr/bin/python
# Question 10
# write a python program to find all words that are twelve characters long in biglist.txt

with open('biglist.txt') as f:
    bigList = f.readlines()

for line in bigList:
    if len(line.rstrip()) == 12:
        print(line)
