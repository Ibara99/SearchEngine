# -*- coding: utf-8 -*-
import scrapy


class MerdekaSpider(scrapy.Spider):

	name = 'merdeka'
	allowed_domains = ['merdeka.com']
	start_urls = ['https://www.merdeka.com/tag/pariwisata-yogyakarta/',
				  'https://www.merdeka.com/tag/objek-wisata-yogyakarta/',]

	def parse(self, response):
		url1 = response.css(".meta-content > .desc > h2 > a::attr(href)").extract()
		url2 = response.css(".meta-content > .desc > h3 > a::attr(href)").extract()
		for url in url1:
			yield scrapy.Request(
				response.urljoin(url),
				callback=self.parse_detail)

		'''
		self.log("Visited: "+ response.url)
		judul = response.xpath("//h2/a/text()").extract()
		judul += response.xpath("//h3/a/text()").extract()
		for i in judul:
			info  = {
				"judul" : i,
			}
			
			yield info
		'''
		NEXT_PAGE_SELECTOR = ".link_next::attr(href)"
		next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
		if next_page:
			yield scrapy.Request(
				response.urljoin(next_page),
				callback=self.parse)
	def parse_detail(self, response):
		judul = response.css(".mdk-dt-headline > h1::text").extract_first()
		isi_all = response.css(".mdk-body-paragraph > p::text").extract()
		isi=""
		for i in isi_all:
			isi += i + " "
		yield {
		"judul" : judul,
		"isi" : isi,
		}
