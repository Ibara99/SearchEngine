# -*- coding: utf-8 -*-
import scrapy


class MerdekaSpider(scrapy.Spider):
	name = 'merdeka'
	allowed_domains = ['merdeka.com']
	start_urls = ['https://www.merdeka.com/tag/pariwisata-yogyakarta/']

	def parse(self, response):
		self.log("Visited: "+ response.url)
		judul = response.xpath("//h2/a/text()").extract()
		judul += response.xpath("//h3/a/text()").extract()
		for i in judul:
			info  = {
				"judul" : i,
			}
			
			yield info