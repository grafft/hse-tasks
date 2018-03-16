# -*- coding: utf-8 -*-
import scrapy


class PricelistSpider(scrapy.Spider):
    name = 'pricelist'
    allowed_domains = ['europegym.ru']
    start_urls = ['https://www.europegym.ru/centers/prices/1.html']

    def parse(self, response):
        pass
