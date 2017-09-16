import urllib2
import re
from bs4 import BeautifulSoup
url = 'http://www.nhc.noaa.gov/gis/forecast/archive/'

conn = urllib2.urlopen(url)
html = conn.read()

soup = BeautifulSoup(html)
links = soup.find_all('a')

for tag in links:
    link = tag.get('href',None)
    if link is not None:
        
        print link[2:]
#formattedYear = (year[-2:])


#step 1 -go to ftp://nhc.noaa.gov/gis/forecast/archive/?C=M;O=D sort on last modified date

#step 2 - only select links that are today's date

#Step 3 - if the link starts with al or ep - download it

#other options - run daily RSS feed check against http://www.nhc.noaa.gov/gis-ep.xml and http://www.nhc.noaa.gov/gis-at.xml 
