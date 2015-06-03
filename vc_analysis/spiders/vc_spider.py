__author__ = 'RunzeZhao'
from scrapy import Spider
from scrapy.selector import Selector

from vc_analysis.items import VcAnalysisItem

class VCSpider(Spider):
    name = "vc"
    allowed_domains = [""]
    start_urls = [
        "http://www.entrepreneur.com/article/242702",
    ]

    def parse(self, response):
        links_names = Selector(response).xpath('//div[@class="bodycopy"]/h2/a')

        for link_name in links_names:
            item = VcAnalysisItem()
            item['title'] = link_name.xpath(
                'text()').extract()
            item['url'] = link_name.xpath(
                '@href').extract()
            print item
            yield item
