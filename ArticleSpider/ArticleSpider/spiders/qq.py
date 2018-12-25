# -*- coding: utf-8 -*-
import scrapy
from ArticleSpider.items import ArticlespiderItem


class BaidutiebaSpider(scrapy.Spider):
    name = 'qq'
    allowed_domains = ['qq.com']
    start_urls = ['https://www.qq.com/']

    def parse(self, response):
        data = response.xpath('//*[@id="tab-news-01"]/ul[1]/li[1]/a').extract()
        print(data)
