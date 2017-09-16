####################################################################################
##
##  Script: NOAA_Pacific_CPC.py
##
##      - check out second example here - http://www.programcreek.com/python/example/81585/urllib.request.urlretrieve
##      - build in error checking
##      - figure out what this data is for
##      - find the download schedule
##      - unzip and load shapefile into postgres
##
####################################################################################


import os, sys,datetime, psycopg2,urllib2,urllib
import requests
from contextlib import closing
import csv


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


outputfolder = 'C:/Work/Projects/everyday/download_data/ClimatePredictionCenter/'+formattedDate
if not os.path.exists(outputfolder):
    os.makedirs(outputfolder)



#Week 1
#Tropical Cyclone Formation
cpc_week1_tcf_shp = 'http://www.cpc.ncep.noaa.gov/products/precip/CWlink/ghazards/Shps/TC_W1_latest.zip'
urllib.urlretrieve(cpc_week1_tcf_shp, outputfolder+"/TC_W1_latest_"+formattedDate+".zip")
print('TC_W1_latest Downloaded')

#Upper Tercile Precipitation
cpc_week1_utp = 'http://www.cpc.ncep.noaa.gov/products/precip/CWlink/ghazards/Shps/WET_W1_latest.zip'
urllib.urlretrieve(cpc_week1_utp, outputfolder+"/WET_W1_latest_"+formattedDate+".zip")
print('WET_W1_latest Downloaded')

#Lower Tercile Precipitation
cpc_week1_ltp = 'http://www.cpc.ncep.noaa.gov/products/precip/CWlink/ghazards/Shps/DRY_W1_latest.zip'
urllib.urlretrieve(cpc_week1_ltp, outputfolder+"/DRY_W1_latest_"+formattedDate+".zip")
print('DRY_W1_latest Downloaded')

#Above Average Temperatures
cpc_week1_aat ='http://www.cpc.ncep.noaa.gov/products/precip/CWlink/ghazards/Shps/WARM_W1_latest.zip'
urllib.urlretrieve(cpc_week1_aat, outputfolder+"/WARM_W1_latest_"+formattedDate+".zip")
print('WARM_W1_latest Downloaded')

#Below Average Temperatures
cpc_week1_bat = 'http://www.cpc.ncep.noaa.gov/products/precip/CWlink/ghazards/Shps/COLD_W1_latest.zip'
urllib.urlretrieve(cpc_week1_bat, outputfolder+"/COLD_W1_latest_"+formattedDate+".zip")
print('COLD_W1_latest Downloaded')

#Week2
#Tropical Cyclone Formation
cpc_week2_tcf_shp='http://www.cpc.ncep.noaa.gov/products/precip/CWlink/ghazards/Shps/TC_W2_latest.zip'
urllib.urlretrieve(cpc_week2_tcf_shp, outputfolder+"/TC_W2_latest_"+formattedDate+".zip")
print('TC_W2_latest Downloaded')

#Upper Tercile Precipitation
cpc_week2_utp ='http://www.cpc.ncep.noaa.gov/products/precip/CWlink/ghazards/Shps/WET_W2_latest.zip'
urllib.urlretrieve(cpc_week2_utp, outputfolder+"/WET_W2_latest_"+formattedDate+".zip")
print('WET_W2_latest Downloaded')

#Lower Tercile Precipitation
cpc_week2_ltp ='http://www.cpc.ncep.noaa.gov/products/precip/CWlink/ghazards/Shps/DRY_W2_latest.zip'
urllib.urlretrieve(cpc_week2_ltp, outputfolder+"/DRY_W2_latest_"+formattedDate+".zip")
print('DRY_W2_latest Downloaded')

#Above Average Temperatures
cpc_week2_aat ='http://www.cpc.ncep.noaa.gov/products/precip/CWlink/ghazards/Shps/WARM_W2_latest.zip'
urllib.urlretrieve(cpc_week2_aat, outputfolder+"/WARM_W2_latest_"+formattedDate+".zip")
print('WARM_W2_latest Downloaded')

#Below Average Temperatures
cpc_week2_bat ='http://www.cpc.ncep.noaa.gov/products/precip/CWlink/ghazards/Shps/COLD_W2_latest.zip'
urllib.urlretrieve(cpc_week2_bat, outputfolder+"/COLD_W2_latest_"+formattedDate+".zip")
print('COLD_W2_latest Downloaded')








print('Script Complete')
