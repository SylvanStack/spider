# -*- coding: utf-8 -*-
import scrapy
import json


class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/user-agent']

    def parse(self, response):
        user_agent = json.loads(response.text)["user-agent"]
        print("-" * 30)
        print(user_agent)
        print("-" * 30)
        yield scrapy.Request(self.start_urls[0], callback=self.parse, dont_filter=True)
