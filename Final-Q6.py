#!/usr/bin/python
# Question 6
# Write a python program to convert a string to datetime
# Sample string: Jan 1 2014 2:43 PM
# Expected Output: 2014-01-01 14:32:00
import re

months = [['jan','january'],['feb','febuary'],['March','march'],['april'],['may'],['june'],['jul','july'],['aug','august'],['sep','sept','september'],['oct','october'],['nov','november'],['dec','december']]

dateStr = input("Please enter a date/time in the form of Month day year hours:minutes AM/PM:\n> ")
dateDiv = dateStr.split(' ')

month1 = dateDiv[0]
day1 = dateDiv[1]
year1 = dateDiv[2]

# removing special characters from the dates
month1 = (''.join(c for c in month1 if c not in ',.!:;')).lower()
day1 = (''.join(c for c in day1 if c not in ',.!:;')).lower()
year1 = (''.join(c for c in year1 if c not in ',.!:;')).lower()

if len(dateDiv)>4:
    time1 = dateDiv[3] + dateDiv[4]
else:
    time1 = dateDiv[3]
time1 = (''.join(c for c in time1 if c not in ',.!;')).lower()

mNum = 0
for x,m in enumerate(months):
    if month1 in m:
        mNum = x+1

if mNum>9:
    dateFin = '-'.join([year1,str(mNum),day1])
else:
    dateFin = '-'.join([year1,'0'+str(mNum),day1])

time2 = time1.split(':',1)
hr = time2[0]
minFin = (re.split("[a-z]+",time2[1],1))[0]
amPm = (re.split("[0-9]+",time2[1],1))[1]

if amPm == 'am':
    hrFin = hr
else:
    hrFin = int(hr)+12

timeFin = ':'.join([str(hrFin),str(minFin),'00'])

dateTimeFin = dateFin + ' ' + timeFin
print(dateTimeFin)

