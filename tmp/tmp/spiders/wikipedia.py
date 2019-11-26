# -*- coding: utf-8 -*-
import scrapy


class WikipediaSpider(scrapy.Spider):
	name = 'wikipedia'
	allowed_domains = ['wikipedia.org']
	start_urls = ['https://id.m.wikipedia.org/wiki/Jagung']
	url_sekarang = "https://id.m.wikipedia.org/wiki/Jagung"

	def parse(self, response):
		judul = response.css("h1.firstHeading::text").extract_first()
		isi_all = response.css(".mw-parser-output > p::text").extract()
		isi=""
		for i in isi_all:
			isi += i + " "
		yield {
		"link"	: self.url_sekarang,
		"judul" : judul,
		"isi" : isi,
		}
