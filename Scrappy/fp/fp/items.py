# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FpItem(scrapy.Item):
    titles = scrapy.Field()
    paragraphs = scrapy.Field()
    list_items = scrapy.Field()
    images = scrapy.Field()
    links = scrapy.Field()
    pass
