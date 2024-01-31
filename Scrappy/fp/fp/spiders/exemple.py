import scrapy


class ExempleSpider(scrapy.Spider):
    name = "exemple"
    allowed_domains = ["fr.wikipedia.org"]
    start_urls = ["http://fr.wikipedia.org/"]

    def parse(self, response):
        # Extract data using css selectors
        title = response.css("h1::text").extract()
        # Extract data using xpath selectors
        links = response.xpath("//a/text()").extract()
        # Extract data using regex
        body = response.css("p").extract_first()
        # Extract data using xpath selectors
        url = response.xpath("//a/@href")

        print("title:", title)
        print("links:", links)
        print("body:", body)
        print("url:", url)
