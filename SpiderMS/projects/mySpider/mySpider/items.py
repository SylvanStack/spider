# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItcastItem(scrapy.Item):
    name = scrapy.Field()  # 姓名
    level = scrapy.Field()  # 职称
    info = scrapy.Field()  # 个人信息
