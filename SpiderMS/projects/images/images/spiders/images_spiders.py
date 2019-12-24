from scrapy.spiders import Spider
from scrapy import Request
from images.items import ImagesItem


class ImagesSpider(Spider):
    name = 'images'

    start_urls = ['http://699pic.com/photo/']  # 摄图网“照片”主题页

    # 初始的Request
    def start_requests(self):
        url = 'http://699pic.com/photo/'
        yield Request(url)

    # 解析函数-“照片”的主题页
    def parse(self, response):
        url_list = response.xpath(".//div[@class='pl-list']/a[1]/@href").extract()
        for url in url_list:
            yield Request(url, callback=self.parse_images)

    # 解析函数-详细页的照片
    def parse_images(self, response):
        item = ImagesItem()
        url_list = response.xpath(".//li[@class='list']/a/img/@data-original").extract()
        item["image_urls"] = url_list
        yield item

        # 下一页
        next_url = response.xpath(".//a[@class='downPage']/@href").extract()
        if next_url:
            next_url = response.urljoin(next_url[0])
            yield Request(next_url)
