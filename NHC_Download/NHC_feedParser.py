#http://stackoverflow.com/questions/14256745/how-to-check-if-an-rss-feed-has-been-updated-in-python
#http://www.pythonforbeginners.com/feedparser/using-feedparser-in-python

import feedparser

exp = feedparser.parse('http://www.nhc.noaa.gov/rss_examples/gis-ep.xml')
atl = feedparser.parse('http://www.nhc.noaa.gov/gis-at.xml')
pfc = feedparser.parse('http://www.nhc.noaa.gov/gis-ep.xml')


#for item in atl.entries:
#    print(item.title)
#print len(pfc[entries])
print (pfc.feed.subtitle)
#for item in pfc.entries:
 #   print(item.feed)


