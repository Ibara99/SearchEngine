# -*- coding: utf-8 -*-
import scrapy


class DetikSpider(scrapy.Spider):
	name = 'detik'
	allowed_domains = ['detik.com']
	start_urls = ['http://detik.com/tag/jagung']
	link_sekarang = "http://detik.com/tag/jagung"
	first = True

	def parse(self, response):
		#urls = response.css(".meta-content > .desc > h2 > a::attr(href)").extract()
		urls = response.css("article > a::attr(href)").extract()
		for url in urls:
			self.link_sekarang = url
			yield scrapy.Request(
				response.urljoin(url),
				callback=self.parse_detail)

		NEXT_PAGE_SELECTOR = "a.last::attr(href)"
		next_page = response.css(NEXT_PAGE_SELECTOR).extract()
		if (first and len(next_page) > 0) or len(next_page) > 1:
			first = False
			yield scrapy.Request(
				response.urljoin(next_page[-1]),
				callback=self.parse)

	def parse_detail(self, response):
		judul = response.css(".jdl > h1::text").extract_first()
		isi_all = response.css(".itp_bodycontent::text").extract()
		isi=""
		for i in isi_all:
			if (not "\n" in i):
				isi += i + " "
		yield {
		"link" : self.link_sekarang,
		"judul" : judul,
		"isi" : isi,
		}


