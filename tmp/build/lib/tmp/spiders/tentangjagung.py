# -*- coding: utf-8 -*-
import scrapy


class TentangjagungSpider(scrapy.Spider):
	name = 'tentangjagung'
	allowed_domains = ['tentangjagung.blogspot.com']
	start_urls = ['http://tentangjagung.blogspot.com/']
	url_sekarang =""

	def parse(self, response):
		urls = response.css(".entry-title > a::attr(href)").extract()
		for url in urls:
			self.url_sekarang = url
			yield scrapy.Request(
				response.urljoin(url),
				callback=self.parse_detail)

		NEXT_PAGE_SELECTOR = "a.blog-pager-older-link::attr(href)"
		next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
		if next_page:
			yield scrapy.Request ( response.urljoin(next_page),callback=self.parse)
	def parse_detail(self, response):
		judul = response.css(".entry-title::text").extract_first()
		isi_all = response.css(".post-body > div::text").extract()
		isi=""
		for i in isi_all:
			isi += i + " "
		yield {
		"link" : self.url_sekarang,
		"judul" : judul,
		"isi" : isi,
		}
