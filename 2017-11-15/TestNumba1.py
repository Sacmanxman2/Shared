# Test question 1
# Jared Sackett
# 2017-11-15
# Write a Python program to determine how many lines and words the text file is

with open("Constitution.txt") as f:
    USALines = f.readlines()

USAWords = []
for line in USALines:
    LineWords = line.split()
    USAWords += LineWords

print("there are {} lines in the constitution file".format(len(USALines)))
print("there are {} words in the constitution file".format(len(USAWords)))
