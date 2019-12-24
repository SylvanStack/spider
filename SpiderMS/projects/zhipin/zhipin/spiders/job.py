# -*- coding: utf-8 -*-
import scrapy
from zhipin.items import ZhipinItem
from zhipin.settings import JOB_NAME,JOB_CITY
import copy

class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['zhipin.com']
    query_url='https://www.zhipin.com/job_detail/?query='+JOB_NAME+'+&city='+JOB_CITY+'&industry=&position='
    start_urls = [query_url]

    def parse(self, response):
        for job_primary in response.xpath('//div[@class="job-primary"]'):
            item={}
            # 匹配工作信息
            info_primary = job_primary.xpath('./div[@class="info-primary"]')
            item["job_title"]=info_primary.xpath('./h3/a/div[@class="job-title"]/text()').extract_first()
            item["job_salary"]=info_primary.xpath('./h3/a/span/text()').extract_first()
            item["job_detail"]=info_primary.xpath('./h3/a/div[@class="info_detail"]/text()').extract_first()
            item["job_detail_url"]='https://www.zhipin.com'+info_primary.xpath('./h3/a/@href').extract_first()
            item["job_address"]=info_primary.xpath('./p/text()').extract_first()
            item["job_years"]=info_primary.xpath('./p/text()').extract()[1]
            item["job_edu"]=info_primary.xpath('./p/text()').extract()[2]
            # 职位信息下一页
            yield scrapy.Request(
                url=item["job_detail_url"],
                callback=self.parse_job_detail,
                meta={"item":copy.deepcopy(item)}
            )

            # 匹配公司信息
            info_company=job_primary.xpath('./div[@class="info-company"]')
            item["company_name"]=info_company.xpath("div/h3/a/text()").extract_first()
            item["company_url"]='https://www.zhipin.com'+info_company.xpath("div/h3/a/@href").extract_first()
            item["company_intro"]=info_company.xpath("div/p/text()").extract_first()
            item["company_intro_all"]=info_company.xpath("div/p/text()").extract()
            # 企业信息下一页
            yield scrapy.Request(
                url=item["company_url"],
                callback=self.parse_job_detail,
                meta={"item": copy.deepcopy(item)}
            )



    def parse_job_detail(self,response):
        item=response.meta["item"]
        detail_content=response.xpath("//div[@class='detail-content']/div[@class='job-sec']")[0]
        item["job_description"]=detail_content.xpath('./div/text').extract()

    def parse_company_detail(self, response):
        item=response.meta["item"]
        item["location-address"]=response.xpath("//div[@class='location-address']/a/href()")
        print(item)

    # def parse(self, response):
    #     # 遍历页面上所有//div[@class="job-primary"]节点
    #     for job_primary in response.xpath('//div[@class="job-primary"]'):
    #         item = ZhipinItem()
    #         # 匹配//div[@class="job-primary"]节点下/div[@class="info-primary"]节点
    #         # 也就是匹配到包含工作信息的<div.../>元素
    #         info_primary = job_primary.xpath('./div[@class="info-primary"]')
    #         item['title'] = info_primary.xpath('./h3/a/div[@class="job-title"]/text()').extract_first()
    #         item['salary'] = info_primary.xpath('./h3/a/span[@class="red"]/text()').extract_first()
    #         item['work_addr'] = info_primary.xpath('./p/text()').extract_first()
    #         item['url'] = info_primary.xpath('./h3/a/@href').extract_first()
    #         # 匹配//div[@class="job-primary"]节点下./div[@class="info-company"]节点下
    #         # 的/div[@class="company-text"]的节点
    #         # 也就是匹配到包含公司信息的<div.../>元素
    #         company_text = job_primary.xpath('./div[@class="info-company"]' +
    #                                          '/div[@class="company-text"]')
    #         item['company'] = company_text.xpath('./h3/a/text()').extract_first()
    #         company_info = company_text.xpath('./p/text()').extract()
    #         if company_info and len(company_info) > 0:
    #             item['industry'] = company_info[0]
    #         if company_info and len(company_info) > 2:
    #             item['company_size'] = company_info[2]
    #         # 匹配//div[@class="job-primary"]节点下./div[@class="info-publis"]节点下
    #         # 也就是匹配到包含发布人信息的<div.../>元素
    #         info_publis = job_primary.xpath('./div[@class="info-publis"]')
    #         item['recruiter'] = info_publis.xpath('./h3/text()').extract_first()
    #         item['publish_date'] = info_publis.xpath('./p/text()').extract_first()
    #         print(item)
    #         yield item
    #     # 解析下一页的链接
    #     new_links = response.xpath('//div[@class="page"]/a[@class="next"]/@href').extract()
    #     if new_links and len(new_links) > 0:
    #         # 获取下一页的链接
    #         new_link = new_links[0]
    #         # 再次发送请求获取下一页数据
    #         yield scrapy.Request("https://www.zhipin.com" + new_link, callback=self.parse)