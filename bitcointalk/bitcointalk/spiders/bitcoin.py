# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import re

from bitcointalk.items import BitcointalkItem


class BitcoinSpider(scrapy.Spider):
    name = 'bitcoin'
    allowed_domains = ['bitcointalk.org']
    start_urls = ['https://bitcointalk.org/index.php?topic=2669586']

    def parse(self, response):

        f = open('result.csv', 'w')
        f.write('name,status,activity,merit,time,title,context\n')
        f.close()

        # 构造url
        for i in range(100):
            link = 'https://bitcointalk.org/index.php?topic=2669586.' + str(int(20*i))
            yield scrapy.Request(link, callback=self.parse_page)

    def parse_page(self, response):

        item = BitcointalkItem()

        '''
        可找到每个回复区域（一个页面20个区域）的xpath：'//*[@id="quickModForm"]/table[1]/tr/td/table/tr/td'
        '''

        name = response.xpath('//*[@id="quickModForm"]/table[1]/tr/td/table/tr/td/table/tr[1]/td[1]/b/a')\
            .re('.?(\w{2,})</a>')
        left = response.xpath('//*[@id="quickModForm"]/table[1]/tr/td/table/tr/td/table/tr[1]/td[1]/div')\
            .extract()
        title = response.xpath('//*[@id="quickModForm"]/table[1]/tr/td/table/tr/td/'
                               'table/tr[1]/td[2]/table/tr/td[2]/div/a/text()').extract()
        time_text = response.xpath('//*[@id="quickModForm"]/table[1]/tr/td/table/tr/td/table/tr[1]/td[2]/table/tr/td[2]/div[2]')\
            .extract()
        content = response.xpath('//*[@id="quickModForm"]/table[1]/tr/td/table/tr/td/table/tr[1]/td[2]/div').extract()

        status = []
        activity = []
        merit = []
        for i in range(len(left)):
            s = re.findall(r'.*\n\t\t\t\t\t\t\t\t?([a-zA-Z.\s]{2,})<br>.*', left[i])
            status.append(s[0])
            a = re.findall(r'.*Activity: ([0-9]+)<br>.*', left[i])
            activity.append(a[0])
            m = re.findall(r'.*Merit: ([0-9]+)<br>.*', left[i])
            merit.append(m[0])

        time = []
        for i in range(len(time_text)):
            t = re.findall(r'.*((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[,:\w\s]{20,}(AM|PM)).*', time_text[i])
            time.append(list(t[0])[0])

        with open('result.csv', 'a', encoding='utf8') as f:
            # f.write(response.url)
            # f.write(str(len(name)) + ', ' + str(len(title)) + ', ' + str(len(content)) + '\n')
            for i in range(len(name)):
                f.write(str(name[i]) + ",")
                f.write(str(status[i]) + ",")
                f.write(str(activity[i]) + ",")
                f.write(str(merit[i]) + ",")
                f.write("'" + str(time[i]) + "',")
                f.write("'" + str(title[i]) + "',")
                # f.write("'" + str(content[i]) + "'\n")
                f.write("'" + str(BeautifulSoup(str(content[i])).get_text()) + "'\n")

        item['name'] = name
        item['status'] = status
        item['activity'] = activity
        item['merit'] = merit
        item['title'] = title
        item['time'] = time
        item['content'] = content

        yield item
