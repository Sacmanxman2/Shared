#!/usr/bin/python
# Question 4
# Write a python script to concatenate following dictionaries to create a new one:
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50,6:60}
#Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

out = {}

def cycle(d,out=out):
    for i in d:
        print(i)
        print(d[i])
        out.update({i:d[i]})

cycle(dic1)
cycle(dic2)
cycle(dic3)

print(out)
