# -*- coding: utf-8 -*-
import scrapy


class BisnisComSpider(scrapy.Spider):
    name = 'bisnis_com'
    allowed_domains = ['bisnis.com']
    start_urls = ['http://search.bisnis.com/?q=jagung']

    def parse(self, response):
        pass
