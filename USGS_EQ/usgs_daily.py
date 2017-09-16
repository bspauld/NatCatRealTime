####################################################################################
##                                                                                  
##  Script: USGS_Daily.py
##
##  Purpose: Script to pull daily USGS eq reports
##
##
##  
##
####################################################################################


import os, sys,datetime, psycopg2
import requests
from contextlib import closing
import csv

#Set up SQL Connection
inputTable_eq = 'public.usgs_eq'


try:
    conn = psycopg2.connect("dbname='usgs_eq' user='postgres' host='localhost' port='5433' password='Spauld$4'")
    print ("CONNECTION SUCCESSFUL")
except:
    print ("I am unable to connect to the database")


cur = conn.cursor()


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

#create daily SPC files
#pathname
dailyEQpath = "C:\Work\Projects\everyday\download_data\USGS_Daily\USGS_EQ_"+formattedDate+".csv"


urlEQ = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.csv"


#EQ Download and Upload
print("Load EQ Reports")
with open(dailyEQpath,"w+") as t:
    with closing(requests.get(urlEQ, stream=True)) as r:
            reader = csv.reader(r.iter_lines(), delimiter=',', quotechar='"')
            for row in reader:
                t.write(sqlformatteDate+','+str(row[0])+','+str(row[1])+','+str(row[2])+','+str(row[3])+','+str(row[4])+','+str(row[5])+','+str(row[6])+','+str(row[7])+','+str(row[8])+','+str(row[9])+','+str(row[10])+','+str(row[11])+','+str(row[12])+','+str(row[13])+','+str(row[14])+','+str(row[15])+','+str(row[16])+','+str(row[17])+','+str(row[18])+','+str(row[19])+','+str(row[20])+','+str(row[21])+'\n')
                #print((str(row[0])+','+str(row[1])+','+str(row[2])+','+str(row[3])+','+str(row[4])+','+str(row[5])+','+str(row[6])+','+str(row[7])+'\n')  )

#cur.execute("""Copy public.NOAA_SPC_torn from %s DELIMITER ',' CSV Header""",[dailyTornpath])

