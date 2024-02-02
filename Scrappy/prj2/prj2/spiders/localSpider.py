import scrapy
from prj2.items import Prj2Item


class LocalspiderSpider(scrapy.Spider):
    name = "localSpider"
    allowed_domains = ["127.0.0.1:5500"]
    start_urls = ["http://127.0.0.1:5500/exerice/Bourses.html"]

    def parse(self, response):
        # instance de la classe item
        item = Prj2Item()

        print(response.css('p::text').extract())
        print(response.xpath('//p/text()').getall())
