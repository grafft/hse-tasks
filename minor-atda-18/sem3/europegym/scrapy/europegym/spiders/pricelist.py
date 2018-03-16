# -*- coding: utf-8 -*-
import scrapy
import urllib.parse

def cell_text(td):
    sel = 'div::text' if len(td.css('div')) else '::text'
    return td.css(sel).extract_first().strip()

class PricelistSpider(scrapy.Spider):
    name = 'pricelist'
    allowed_domains = ['europegym.ru']
    start_urls = ['https://www.europegym.ru/centers/prices/1.html']

    def parse(self, response):
        for link in response.css('.side_info:last-child a'):
            href = link.css('::attr(href)').extract_first()
            # yield { 'href': href }
            abs_url = urllib.parse.urljoin('https://www.europegym.ru/', href)
            yield scrapy.Request(url=abs_url, callback=self.parse_center)

    def parse_center(self, response):
        rows = response.xpath('//h2[contains(text(), "Персональные тренировки")]/following-sibling::table[1]/tr')
        res = [[cell_text(td) for td in row.xpath('td')] for row in rows]
        yield { 'title': response.css('h1::text').extract_first(), 'table': res }
