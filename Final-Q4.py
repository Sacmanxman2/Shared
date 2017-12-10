#!/usr/bin/python
# Question 4
# Write a python script to concatenate following dictionaries to create a new one:
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50,6:60}
#Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

out = {} # Blank dictionary to start with

def cycle(d,out=out): # I just put all this code in a function that I'll 'cycle' through so I don't have to repeat it
    for i in d: # For every key in dictionary d
        out.update({i:d[i]}) # Update (or append if nonexistent) the key:value pairs to the 'out' dictionary

cycle(dic1)
cycle(dic2)
cycle(dic3)

print(out)
