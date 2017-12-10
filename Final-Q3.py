#!/usr/bin/python
# Question 3
# Write a Python program to extract year, month, and date from a url (use cnn.com or something similar to find a page with a date)
import bs4 as bs
import urllib.request

url = "http://www.bbc.com/news/world-us-canada-42297370"

source = urllib.request.urlopen(url).read()

stuff = bs.BeautifulSoup(source,'html.parser')

for par in stuff.find_all('div',attrs={'data-datetime':True,'class':'date date--v2'}):
    print(par['data-datetime'])
    break
