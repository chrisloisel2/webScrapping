import scrapy


class MarmitonspiderSpider(scrapy.Spider):
    name = "marmitonSpider"
    allowed_domains = ["www.cuisineaz.com"]
    start_urls = ["https://www.cuisineaz.com/recettes/jus-de-kaki-116653.aspx"]

    def parse(self, response):
        # Recuperation par css des balises dans la page
        CSSlis = response.css("h2.borderSection_title.m-0")

        # recuperer le texte par css de la balise
        CSSlistxt = response.css("h2.borderSection_title.m-0::text").extract()

        # recuperer les attributs par css de la balise
        CSSlisclass = response.css(
            "h2.borderSection_title.m-0::attr(class)").extract()

        # Recuperer une balise par xpath
        XPATHlis = response.xpath("//h2[@class='borderSection_title m-0']")

        # Recuperer le texte d'une balise par xpath
        XPATHlistxt = response.xpath(
            "//h2[@class='borderSection_title m-0']/text()").extract()

        # Recuperer les attributs d'une balise par xpath
        XPATHlisclass = response.xpath(
            "//h2[@class='borderSection_title m-0']/@class").extract()

        yield {
            "CSSlis": CSSlis,
            "CSSlistxt": CSSlistxt,
            "CSSlisclass": CSSlisclass,
            "XPATHlis": XPATHlis,
            "XPATHlistxt": XPATHlistxt,
            "XPATHlisclass": XPATHlisclass
        }
