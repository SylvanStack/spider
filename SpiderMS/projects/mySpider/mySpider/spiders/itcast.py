# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # 存放老师的集合
        items = []
        li_all = response.xpath("//div[@class='li_txt']")
        for li_one in li_all:
            item = ItcastItem()

            name = li_one.xpath("h3/text()").extract_first()
            level = li_one.xpath("h4/text()").extract_first()
            info = li_one.xpath("p/text()").extract_first()

            item["name"] = name
            item["level"] = level
            item["info"] = info
            items.append(item )
            # 将获取的数据交给pipelines
            yield item

        # 返回数据，不经过pipeline
        # return items
