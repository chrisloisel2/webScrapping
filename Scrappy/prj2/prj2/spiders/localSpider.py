import scrapy
from prj2.items import Prj2Item


class LocalspiderSpider(scrapy.Spider):
    name = "localSpider"
    allowed_domains = ["127.0.0.1:5500"]
    start_urls = ["http://127.0.0.1:5500/exerice/films.html"]

    def parse(self, response):
        # instance de la classe item
        item = Prj2Item()

        noms = response.css('h2::text').extract()
        commentaires = response.css('p::text').extract()

        for i in range(len(noms)):
            item['nom'] = noms[i]
            item['commentaire'] = commentaires[i]
            yield item
