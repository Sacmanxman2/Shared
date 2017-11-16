# Test question 3
# Jared Sackett
# 2017-11-15
# Write a python program to cut out and display just the Preamble (We the People...). 

with open("Constitution.txt") as f:
    USA = f.read()

def StringSearch(string,term):
    Yes = False
    count = -1
    for word in string.split():
        count +=1
        if word == term:
            Yes = True
            break
        else:
            continue
    return count

Start = StringSearch(USA,"We")
End = StringSearch(USA,"America.") + 1
print(" ".join(USA.split()[Start:End]))
