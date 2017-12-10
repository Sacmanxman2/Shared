#!/usr/bin/python
# Question 6
# Write a python program to convert a string to datetime
# Sample string: Jan 1 2014 2:43 PM
# Expected Output: 2014-01-01 14:32:00
import re # We will be using regular expressions to parse the am/pm later if they aren't separated by a space

# List of possible months, so that each month's index is the month number (-1 of course, which we'll add back later)
months = [['jan','january'],['feb','febuary'],['March','march'],['april'],['may'],['june'],['jul','july'],['aug','august'],['sep','sept','september'],['oct','october'],['nov','november'],['dec','december']]

dateStr = input("Please enter a date/time in the form of Month day year hours:minutes AM/PM:\n> ")
dateDiv = dateStr.split(' ') # Split the date string by spaces. This creates a list

month1 = dateDiv[0]
day1 = dateDiv[1]
year1 = dateDiv[2]

# Find the month number
mNum = 0
for x,m in enumerate(months): # Enumerate gives us both the contents of the thing and the index of the thing, where x is the index and m is the thing (in this case, a list containing month strings)
    if month1 in m:
        mNum = x+1 # Add one to the index to get the month number (so that the month with "march" in it is 3 for example)

# Create a date string by combining numbers
if mNum>9:
    dateFin = '-'.join([year1,str(mNum),day1])
else: # This is to put a zero in front of the month if it's a single digit
    dateFin = '-'.join([year1,'0'+str(mNum),day1])

## Logic for time (so pretentious sounding... lol)

time1 = dateDiv[3].split(':') # Split the time by the colon. This will either return ['hh','mm'] or ['hh','mmPM'] depending on if they spaced it out

# If the am/pm isn't spaced out, separate it
if len(dateDiv)>4: # The length of the datestring's list will be longer if there's a space between the time and the AM/PM, since it separates the words by spaces.
    hr = time1[0]
    minFin = time1[1]
    amPm = dateDiv[4]
else:
    hr = time1[0]
    minFin = (re.split("[a-z]+",time1[1]))[0] # Use the regular expression split function to split the string wherever there are letters, thereby removing them leaving us with just the numbers. We want the first item in this list, hence the [0]
    amPm = (re.split("[0-9]+",time1[1]))[1] # Ditto, but for numbers (leaving just the letters). We want just the second item in this list (the first will be an empty string), hence the [1]

# Pretty self explanatory checking of the am/pm
if amPm == 'am':
    hrFin = hr
else:
    hrFin = int(hr)+12 # If it's not am, it must be pm, so we'll add 12 to the time for 24 hour time

timeFin = ':'.join([str(hrFin),str(minFin),'00']) # Join the time values with a : in between. The '00' is for seconds, since that's never specefied in the datestring

## Put them together

dateTimeFin = dateFin + ' ' + timeFin # Could use join for this too, but this is simpler for something with only a few items
print(dateTimeFin)

