import scrapy


class UrlspiderSpider(scrapy.Spider):
    name = "urlSpider"
    allowed_domains = ["www.allocine.fr"]
    start_urls = ["https://www.allocine.fr/film/meilleurs/", "https://www.allocine.fr/film/meilleurs/?page=2",
                  "https://www.allocine.fr/film/meilleurs/?page=3", "https://www.allocine.fr/film/meilleurs/?page=4"]

    def parse(self, response):
        lien = response.css('a.meta-title-link::attr(href)').extract()
        yield {
            'url': lien
        }
