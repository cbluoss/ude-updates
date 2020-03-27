
import scrapy

URL = 'https://www.uni-due.de/med/corona'


class UpdateSpider(scrapy.Spider):
    name = "udeUpdate_spider"
    start_urls = [URL]

    def parse(self, response):
        jumbos = response.css('.jumbotron')
        return {'content':jumbos.getall() }

