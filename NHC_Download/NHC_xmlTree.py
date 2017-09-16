#import xml.etree.ElementTree
#e = xml.etree.ElementTree.parse('http://www.nhc.noaa.gov/rss_examples/gis-ep.xml').getroot()

#for atype in e.findall('type'):
#    print(atype.get('foobar'))

from xml.dom import minidom
xmldoc = minidom.parse('C:\Work\Projects\everyday\download_data\NHC_Events\gis-ep.xml')
itemlist = xmldoc.getElementsByTagName('item')
print(len(itemlist))
print(itemlist[0].attributes['name'].value)
for s in itemlist:
    print(s.attributes['name'].value)
