# Test question 4
# Jared Sackett
# 2017-11-15
# Write out a program to cut out the contents of Article II, Section 1. Create a list, sort it, and display the contents so that each word only appears once (similar to the romeo.txt problem)

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

Start = StringSearch(USA,"Article.?II.")
Secondary = StringSearch(USA,"2.",start=Start) -1
End = StringSearch(USA,"Article.?III.",start=Secondary) 
Chunk = USA.split()[Secondary:End]

words = []

for word in Chunk:
    if word in words:
        continue
    else:
        words.append(word)

print(words)
