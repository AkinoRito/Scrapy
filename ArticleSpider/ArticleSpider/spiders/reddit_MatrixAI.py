import scrapy
from scrapy_splash import SplashRequest
from bs4 import BeautifulSoup
import re
import time
from selenium import webdriver

from ArticleSpider.items import ArticlespiderItem


class BaidutiebaSpider(scrapy.Spider):
    name = 'reddit-MatrixAI'
    allowed_domains = ['reddit.com']
    start_urls = ['https://www.reddit.com/r/THEMATRIXAI/']

    def __init__(self):
        self.browser = webdriver.Chrome()
        time.sleep(100)

        # 模拟鼠标下滑，加载页面
        self.browser.get('https://www.reddit.com/r/THEMATRIXAI/')
        time.sleep(60)
        for i in range(10):
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)

    def __del__(self):
        self.browser.close()


    def parse(self, response):

        f = open('result.csv', 'w', encoding='utf8')
        f.write('name*time*likes*data\n')

        # self.browser.get(response.url)

        # like = self.browser.find_elements_by_xpath('//body/div/div/div/div/div/div/div/div[2]/div[3]/div[1]/div[1]/div/div/div/div[2]/div[4]/div[1]/div')#.extract()
        # pub_time = self.browser.find_elements_by_xpath('//body/div/div/div/div/div/div/div/div[2]/div[3]/div[1]/div[1]/div/div/div/div[2]/div[1]/div/div[1]/a')#.extract()
        # # data = self.browser.find_elements_by_xpath('//div[@class="ser2k5-0 fiwlJt"]')
        # data = self.browser.find_elements_by_xpath('//body/div/div/div/div/div/div/div/div[2]/div[3]/div[1]/div[1]/div/div/div/div[2]/div[3]/div/div')
        # name = self.browser.find_elements_by_xpath('//body/div/div/div/div/div/div/div/div[2]/div[3]/div[1]/div[1]/div/div/div/div[2]/div[1]/div/div[1]/div/a')#.re('.*?(\w{2,})')

        name = response.xpath('//body/div/div/div/div/div/div/div/div[2]/div[3]/div[1]/div[1]/div/div/div/div[2]/div[1]/div/div[1]/div/a/text()').re('.*?(\w{2,})')
        like = response.xpath('//body/div/div/div/div/div/div/div/div[2]/div[3]/div[1]/div[1]/div/div/div/div[2]/div[4]/div[1]/div/text()').extract()
        pub_time = response.xpath('//body/div/div/div/div/div/div/div/div[2]/div[3]/div[1]/div[1]/div/div/div/div[2]/div[1]/div/div[1]/a/text()').extract()
        data = response.xpath('//body/div/div/div/div/div/div/div/div[2]/div[3]/div[1]/div[1]/div/div/div/div[2]/div[3]/div/div').extract()

        # 写入result.csv，字段之间以 * 分隔
        for n, t, l, d in zip(name, pub_time, like, data):
            soup = BeautifulSoup(d, "lxml")
            f.write(n+'*'+t+'*'+l+'*'+re.sub(r'\n|\xa0|\\xa0', '', soup.get_text())+'\n')
            print(n, t)
        f.close()

        item = ArticlespiderItem()
        item['name'] = name
        item['time'] = time
        item['data'] = data
        item['like'] = like

        return item
