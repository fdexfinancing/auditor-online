import scrapy
import os

class CollateralSpider(scrapy.Spider):
    name = 'CollateralSpider'
    start_urls = [os.environ['SITE_URL']]

    def parse(self, response):
        print('inicio')
        print(response)
        return
