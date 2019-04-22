# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BitcointalkItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    status = scrapy.Field()
    activity = scrapy.Field()
    merit = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    content = scrapy.Field()
