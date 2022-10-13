import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        for pep in response.css('section[id=numerical-index] tbody tr')[:100]:
            item = PepParseItem()
            item['number'] = pep.css('td + td a::text').get()
            item['name'] = pep.css('td + td + td a::text').get()
            pep_link = pep.css('a::attr(href)').get()
            yield response.follow(
                pep_link,
                callback=self.parse_pep,
                cb_kwargs=dict(item=item)
            )

    def parse_pep(self, response, item):
        item['status'] = response.css('dt:contains("Status") + dd::text').get()
        yield item
