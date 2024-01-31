import scrapy
from fp.items import FpItem


class LocalSpiderSpider(scrapy.Spider):
    name = "local_spider"
    allowed_domains = ["127.0.0.1:5500"]
    start_urls = ['http://127.0.0.1:5500/test.html']

    def parse(self, response):
        item = FpItem()
        item['titles'] = response.css('h1::text, h2::text, h3::text').getall()
        item['paragraphs'] = response.css('p::text').getall()
        item['list_items'] = response.css('li::text').getall()
        item['images'] = response.css('img::attr(src)').getall()
        item['links'] = response.css('a::attr(href)').getall()

        print(item['titles'])
        print(item['paragraphs'])
        print(item['list_items'])
        print(item['images'])
        print(item['links'])
        yield item
