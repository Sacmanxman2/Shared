#!/usr/bin/python
# Question 7
# Write a program to calculate the sum of a list of numbers

numberList = [33,1,3,1,3,5,12,3,1,5,31,3,1,5,3,3,1,2,3,1,23,3,3]
out = 0

for number in numberList:
    print("{} + {}".format(out,number))
    out += number

print(out)




