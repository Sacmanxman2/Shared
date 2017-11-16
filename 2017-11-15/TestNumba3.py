# Test question 3
# Jared Sackett
# 2017-11-15
# Write a python program to cut out and display just the Preamble (We the People...). 

with open("Constitution.txt") as f: #Open the file, read it into a string variable called USA
    USA = f.read()

def StringSearch(string,term): #Define a function to search for a word, which returns the number of words in something is
    Yes = False
    count = -1
    for word in string.split(): #Iterate through each word in the string
        count +=1
        if word == term:
            Yes = True
            break
        else:
            continue
    return count

Start = StringSearch(USA,"We")
End = StringSearch(USA,"America.") + 1
print(" ".join(USA.split()[Start:End])) # Prints out the words joined together with spaces
