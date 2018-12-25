# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
import time
from ArticleSpider.items import ArticlespiderItem



class BaidutiebaSpider(scrapy.Spider):
    name = 'baidutieba'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/']

    def parse(self, response):

        data = response.xpath('//body/div').extract()

        browser = webdriver.Chrome()
        browser.get(response.url)
        time.sleep(100)
        like = browser.find_elements_by_xpath('//*[type="text/javascript"]')
        print("内容：", like)
        browser.close()
        return data
