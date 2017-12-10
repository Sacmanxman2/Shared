#!/usr/bin/python
# Question 3
# Write a Python program to extract year, month, and date from a url (use cnn.com or something similar to find a page with a date)
import bs4 as bs # bs = beautiful soup, a web parsing tool
import urllib.request # A tool that lets us download the contents of urls

url = "http://www.bbc.com/news/world-us-canada-42297370"

source = urllib.request.urlopen(url).read() # This opens the url and reads the contents of the webpage

stuff = bs.BeautifulSoup(source,'html.parser') # This parses the webpage so we can do stuff with it (like filter by html tags and attributes)

for par in stuff.find_all('div',attrs={'data-datetime':True,'class':'date date--v2'}): # For every tag in our site that's a <div> tag and has the attributes 'data-datetime', and the class is set to 'date date--v2' (This is what worked with my site, but you'll have to look in your site to see how it has the date. Regular expressions might be necessary, but this is handy)
    print(par['data-datetime']) # Print the contents of the data-datetime attribute in the selected tag
    break # End the loop after the first result
