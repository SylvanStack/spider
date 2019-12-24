# -*- coding: utf-8 -*-
import json
import re
from copy import deepcopy

import scrapy


class GoodSaveSpider(scrapy.Spider):
    name = 'good_save'
    allowed_domains = ['you.163.com']
    start_urls = ['http://you.163.com/xhr/globalinfo/queryTop.json']

    def parse(self, response):  # 解析标签
        result = json.loads(response.text)
        if result['code'] == "200":
            cateList = result["data"]["cateList"]
            for cate_one in cateList:
                category_url = 'http://you.163.com/item/list?categoryId=' + str(cate_one["id"])
                print(category_url)
                yield scrapy.Request(category_url, callback=self.cate_parse, dont_filter=True)

    def cate_parse(self, response):  # 根据标签解析商品页
        content = re.findall(r'var json_Data=(.+);', response.text)
        result = json.loads(content[0])
        categoryItemList = result['categoryItemList']
        for itemList in categoryItemList:
            for item_one in itemList['itemList']:
                id = item_one["id"]
                goodDetailUrl = "http://you.163.com/item/detail?id=" + str(id)
                yield scrapy.Request(goodDetailUrl, callback=self.good_parse, dont_filter=True)

    def good_parse(self, response):  # 解析商品页
        content_good = response.text.replace("\n", "").replace("\'", "\"")
        data_good = re.findall(r'var JSON_DATA_FROMFTL = (.+);.*var JSON_DATA', content_good)[0]
        good = json.loads(data_good)
        item = good["item"]
        commentCount = good["commentCount"]
        commentGoodRates = good["commentGoodRates"]
        policyList = good["policyList"]
        rcmdItems = good["rcmdItems"]
        suitList = good["suitList"]
        itemType = good["itemType"]
        categoryList = good["categoryList"]

        # 提取商品信息
        id = item['id']
        name = item['name']
        goodDetailUrl = "http://you.163.com/item/detail?id=" + str(id)
        scenePicUrl = item['scenePicUrl']
        primaryPicUrl = item['primaryPicUrl']
        counterPrice = item['counterPrice']
        retailPrice = item['retailPrice']
        primarySkuId = item['primarySkuId']
        displaySkuId = item['displaySkuId']
        simpleDesc = item['simpleDesc']
        promId = item['promId']
        postageTip = item['postageTip']
        rank = item['rank']
        sellVolume = item['sellVolume']


    def comment_parse(self, response):  # 解析评论页
        pass
