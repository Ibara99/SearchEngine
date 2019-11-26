# -*- coding: utf-8 -*-
import scrapy
class MerdekaSpider(scrapy.Spider):
	name = 'merdeka'
	allowed_domains = ['liputan6.com']
	start_urls = ['https://www.liputan6.com/tag/jagung',]
	link_sekarang = 'https://www.liputan6.com/tag/jagung'

	def parse(self, response):
		#urls = response.css(".meta-content > .desc > h2 > a::attr(href)").extract()
		urls = response.css("header > h4 > a::attr(href)").extract()
		for url in urls:
			self.link_sekarang = url
			yield scrapy.Request(
				response.urljoin(url),
				callback=self.parse_detail)

		NEXT_PAGE_SELECTOR = "a.simple-pagination__next-link::attr(href)"
		next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
		if next_page:
			yield scrapy.Request(
				response.urljoin(next_page),
				callback=self.parse)
	def parse_detail(self, response):
		judul = response.css("h1.entry-title::text").extract_first()
		isi_all = response.css(".article-content-body__item-content > p::text").extract()
		isi=""
		for i in isi_all:
			isi += i + " "
		yield {
			"link"  : self.link_sekarang,
			"judul" : judul,
			"isi" : isi,
		}
