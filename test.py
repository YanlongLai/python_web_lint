from urllib2 import urlopen
from urllib2 import Request
from bs4 import BeautifulSoup

url = 'http://www.viki.com'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req)
bsObj = BeautifulSoup(html.read(), "html.parser")
cardContents = bsObj.findAll("div", {"class": "card-content"})
for cardContent in cardContents:
    print(cardContent)
