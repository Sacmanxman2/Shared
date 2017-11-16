# Test question 4
# Jared Sackett
# 2017-11-15
# Write a program to cut out and display the Amendment passed by Congress on 12/18/1917

with open("Constitution.txt") as f:
    USA = f.read()

def StringSearch(string,term,start=0,end=-1):
    if end==-1:
        end=len(string.split())
    Yes = False
    count = start-1
    for word in string.split()[start:end]:
        count +=1
        if term in word:
            Yes = True
            break
        else:
            continue
    return count

Start = StringSearch(USA,"XXVI")
End = StringSearch(USA,"legislation",start=Start) + 1
print(" ".join(USA.split()[Start:End]))

