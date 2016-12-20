#from scrapy.contrib.spiders import CrawlSpider, Rule
# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from vikiSpider.items import VikispiderItem
from scrapy.linkextractors.sgml import SgmlLinkExtractor
#from scrapy import log
import collections
import json

import xml.etree.ElementTree as ET
# tree = ET.parse('country_data.xml')
# root = tree.getroot()

class ArticleSpider(CrawlSpider):
	#log.start(logfile='log.txt', loglevel=log.CRITICAL)
	name="article"
	allowed_domains = ["www.viki.com"]
	start_urls = ["https://www.viki.com"]
	# rules = [ Rule(SgmlLinkExtractor(allow=('.*'),), callback="parse", follow=True) ]

	def RiteshKumar(self, l):
		return list(set([x for x in l if l.count(x) > 1]))
	def parse(self, response):
		links = []
		classNames = []
		datas = []
		item = VikispiderItem()
		for info in response.xpath('//a'):
			# print(info.extract())
			root = ET.fromstring(info.extract())
			if "href" in root.attrib:
				href = root.attrib["href"].encode("utf-8")
			else:
				href = ''
			if "class" in root.attrib:
				className =  root.attrib["class"].encode("utf-8")
			else:
				className = ''
			# data = {
			# 	"link": root.attrib["href"].encode("utf-8"),
			# 	"className": root.attrib["root.attrib["href"]"].encode("utf-8")
			# }
			data = {
				"link": href,
				"className": className
			}
			print(data)
			datas.append(data)

		# item["container"] = json.dumps(data)
			# if "class" in root.attrib:
			# 	print(root.attrib["class"])
		# for link in response.xpath('//a/text()'):
		# for link in response.xpath('//a/@href'):
		# 	# title = response.xpath('//h1/text()')[0].extract()
		# 	# print("Link is: "+link.extract())
		# 	links.append(link.extract())
		# for className in response.xpath('//a/@class'):
		# 	classNames.append(className.extract())
		# item["link"] = self.RiteshKumar(links)
		# item["className"] = self.RiteshKumar(classNames)
		return item

