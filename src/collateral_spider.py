import scrapy
import os
import datetime

class CollateralSpider(scrapy.Spider):
    name = 'CollateralSpider'
    start_urls = ['https://www.vivareal.com.br/venda/']

    def parse(self, response):
        print(response.url)
        print("----------")
        site_name = self.get_site_name(response.url)
        cur_date = str(datetime.datetime.now().year) + '_' + str(datetime.datetime.now().month)
        path = 'site/' + site_name + '/' + cur_date + '/'
        page = 1;

        for next_page in response.css('a.js-paginate-next'):
            link = next_page.xpath('@href').extract()[0]
            link = link[link.find('?'):]
            page += 1

            if page <= 2:
                yield response.follow(response.url + link, self.parse)
            else:
                print('foi')
        # file = open("../site/index.html","w")
        # file.write(response.body.decode("utf-8"))
        # file.close()
        return

    def get_site_name(self, url):
        site_url = url
        init = site_url.find('www.')
        site_name = site_url[init + 4:-1]
        end = site_name.find('.')
        return site_name[0:end]