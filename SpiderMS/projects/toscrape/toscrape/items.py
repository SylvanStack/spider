import scrapy


class ToscrapeItem(scrapy.Item):
    name = scrapy.Field()  # 书籍的名称
    price = scrapy.Field()  # 价格
    url = scrapy.Field()  # 链接地址
    content = scrapy.Field()  # 书籍简介
