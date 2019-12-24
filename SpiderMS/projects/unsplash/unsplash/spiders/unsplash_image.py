# -*- coding: utf-8 -*-
import json

import scrapy

from unsplash.items import ImageItem


class UnsplashImageSpider(scrapy.Spider):
    name = 'unsplash_image'
    allowed_domains = ['unsplash.com']

    # 定义起始页面
    start_urls = ['https://unsplash.com/napi/photos?page=1&per_page=12']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.page_index = 1

    def parse(self, response):
        # 解析服务器响应的JSON字符串
        photo_list = json.loads(response.text)  # ①
        # 遍历每张图片
        for photo in photo_list:
            item = ImageItem()
            item['image_id'] = photo['id']
            item['download'] = photo['links']['download']
            yield item
        self.page_index += 1
        # 获取下一页的链接
        next_link = 'https://unsplash.com/napi/photos?page=' + str(self.page_index) + '&per_page=12'
        # 继续获取下一页的图片
        yield scrapy.Request(next_link, callback=self.parse)
