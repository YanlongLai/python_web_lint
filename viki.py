from urllib2 import urlopen
from urllib2 import Request
from bs4 import BeautifulSoup, NavigableString
import time
import json
import random
# import re

def RiteshKumar(l):
    return list(set([x for x in l if l.count(x) > 1]))

def hexCodeColors():
    a = hex(random.randrange(0,256))
    b = hex(random.randrange(0,256))
    c = hex(random.randrange(0,256))
    a = a[2:]
    b = b[2:]
    c = c[2:]
    if len(a)<2:
        a = "0" + a
    if len(b)<2:
        b = "0" + b
    if len(c)<2:
        c = "0" + c
    z = a + b + c
    return "#" + z.upper()

url = 'http://www.viki.com'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req)
bsObj = BeautifulSoup(html.read(), "html.parser")

# find depulcate links of homepage
links = []
for link in bsObj.findAll("a"):
    links.append(link.get('href'))

# for item in links:
#     print item


links = RiteshKumar(links)

# test depulcate output
# for item in links:
#     print item

# find all a tag link and class for mapping
response = []
for link in bsObj.findAll("a"):
    classSet = link.get('class')
    if classSet is not None:
        classSet = " ".join(str(x) for x in link.get('class'))
    else :
        classSet = ""
    response.append({'href': link.get('href'), 'class': classSet })

# highlight the depulcate links
# for a in bsObj.findAll('a'):
#     if a.get('href') in links:
#         a['style'] = "background: yellow;"
depulcateIndex = 0
for depulcateLink in links:
    color = hexCodeColors()
    depulcateIndex = depulcateIndex + 1
    for a in bsObj.findAll('a'):
        if a.get('href') is depulcateLink:
            print a.get('href')
            # a['style'] = "background: " + color + ";"
            # a.insert(0, NavigableString("(" + str(depulcateIndex) + ")"))
            a['style'] = "border-style: solid; border-width: 8px; border-color: " + color + ";"

for linkSource in bsObj.findAll("link"):
    linkSource['href'] = linkSource['href'].replace("//","http://")


html = bsObj.prettify("utf-8")
with open("output.html", "wb") as file:
    file.write(html)