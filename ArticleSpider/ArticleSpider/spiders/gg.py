# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
import time
from ArticleSpider.items import ArticlespiderItem


class ggSpider(scrapy.Spider):
    name = 'gg'
    allowed_domains = ['dhgate.com']
    start_urls = ['https://www.dhgate.com/product/christmas-gift-soft-tpu-silicone-case-for/428730157.html#cellpphonedcp2018-tab1-item-0']

    def parse(self, response):

        # data = response.xpath('//body/div').extract()

        browser = webdriver.Chrome()
        browser.get(response.url)
        like = browser.find_element_by_xpath('//*[@id="js-priceTips"]/span/text()')

        print("内容：", like)
        browser.close()
        return like
