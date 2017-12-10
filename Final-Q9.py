#!/usr/bin/python
# Question 9
# Write a program to read first n lines of a file

fil = 'biglist.txt'

with open(fil) as f:
    text = f.readlines()

def readXlines(x,text=text):
    for line in text:
        print(line)
        x-=1
        if x<=0:
            break

readXlines(12)
