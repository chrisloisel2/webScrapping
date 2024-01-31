import scrapy


class AllospiderSpider(scrapy.Spider):
    name = "alloSpider"
    allowed_domains = ["www.allocine.fr"]
    start_urls = ["https://www.allocine.fr/", "https://www.allocine.fr/films/"]

    def parse(self, response):
        titres = response.css('h2, p').extract()
        # recuperer un a par css
        print(titres)
        pass
