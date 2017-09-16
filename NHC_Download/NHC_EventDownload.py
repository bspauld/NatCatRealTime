####################################################################################
##                                                                                  
##  Script: NHC_EventDownload.py
##
##  Purpose: Script to download NHC shapefiles
##
##
##  
##
####################################################################################


import os, sys,datetime, psycopg2
import requests
import zipfile, StringIO
from contextlib import closing
import csv
import BeautifulSoup


#Create Date Part  YYMMDD
print(datetime.datetime.today())

#YEAR
year = str(datetime.datetime.today().year)
formattedYear = (year[-2:])

#MONTH
month = datetime.datetime.today().month

if len(str(month)) == 1:
    formattedMonth = '0'+str(month)
    print(formattedMonth)
elif len(str(month)) == 2:
    formattedMonth = str(month)

#DAY - get previous day
day = datetime.datetime.today().day
print(len(str(day)))

if len(str(day)) == 1:
    formattedDay = '0'+str(day)
else:
    formattedDay = str(day)
    
formattedDate = formattedYear+formattedMonth+formattedDay
sqlformatteDate = formattedMonth+formattedDay+year


print 'Year:',str(formattedYear)
print 'Month:',str(formattedMonth)
print 'Day:',str(formattedDay)
print 'Date:',str(formattedDate)

#Get a list of events

EventName = 'Tropical%20Storm%20ARLENE'

#need to build look up for file names

#al - atlantic
#ep - eastern pacific
# ## - event number
# YYYY - four digit year value
# 5day - forecast type
# 001 - release identifier


urlEvent = 'http://www.nhc.noaa.gov/gis/forecast/archive/'

soup = BeautifulSoup(urlEvent, 'html.parser')

print(soup.prettify())




for link in soup.find_all('a'):
    print(link.get('href'))

	
#r = requests.get(zip_file_url, stream=True)
#z = zipfile.ZipFile(StringIO.StringIO(r.content))
#z.extractall()

