# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImageItem(scrapy.Item):
    # 保存图片id
    image_id = scrapy.Field()
    # 保存图片下载地址
    download = scrapy.Field()
