# -*- coding: utf-8 -*-
import scrapy
import json

# from yanxuan.items import CateListItem
import logging
import re
from copy import deepcopy

logger = logging.getLogger(__name__)


class YouSpider(scrapy.Spider):
    name = 'you'
    allowed_domains = ['you.163.com/']
    start_urls = ['http://you.163.com/xhr/globalinfo/queryTop.json']

    def parse(self, response):
        result = json.loads(response.text)
        item = {}
        item2 = {}
        item3 = {}
        if result['code'] == "200":
            cateList = result["data"]["cateList"]
            for cate_one in cateList:
                item["cate"] = "一级菜单"
                item["name"] = cate_one["name"]
                item["category_url"] = 'http://you.163.com/item/list?categoryId=' + str(cate_one["id"])
                item["id"] = cate_one["id"]
                item["superCategoryId"] = cate_one["superCategoryId"]
                item["showIndex"] = cate_one["showIndex"]
                item["frontName"] = cate_one["frontName"]
                item["frontNameIcon"] = cate_one["frontDesc"]
                item["bannerUrl"] = cate_one["bannerUrl"]
                item["iconUrl"] = cate_one["iconUrl"]
                item["level"] = cate_one["level"]
                url = item["category_url"]
                # yield scrapy.Request(url, callback=self.cate_parse, dont_filter=True, meta={"item": deepcopy(item)})
                subCateGroupList = cate_one['subCateGroupList']
                for subCateGroup_one in subCateGroupList:
                    item2["cate"] = "二级菜单"
                    item2["name"] = subCateGroup_one['name']
                    item2["id"] = subCateGroup_one['id']
                    categoryList = subCateGroup_one['categoryList']
                    for category_one in categoryList:
                        item3["cate"] = "三级菜单"
                        item3["name"] = category_one["name"]
                        item3["category_url"] = 'http://you.163.com/item/list?categoryId=' + str(
                            category_one["superCategoryId"]) + "&subCategoryId=" + str(category_one["id"])
                        item3["id"] = category_one["id"]
                        item3["superCategoryId"] = category_one["superCategoryId"]
                        item3["showIndex"] = category_one["showIndex"]
                        item3["frontName"] = category_one["frontName"]
                        item3["frontNameIcon"] = category_one["frontNameIcon"]
                        item3["frontDesc"] = category_one["frontDesc"]
                        item3["bannerUrl"] = category_one["bannerUrl"]
                        item3["iconUrl"] = category_one["iconUrl"]
                        item3["level"] = category_one["level"]

    def cate_parse(self, response):
        item = response.meta['item']
        content = re.findall(r'var json_Data=(.+);', response.text)
        result = json.loads(content[0])
        currentCategory = result['currentCategory']
        deliveryAreaList = result['deliveryAreaList']
        focusList = result['focusList']
        categoryItemList = result['categoryItemList']
        pathList = result['pathList']
        category = {}
        good = {}
        cate_str=""
        big_cate_str=item["name"]
        with open('good.txt', 'a', encoding='utf-8') as f:
            for itemList in categoryItemList:
                # 获取分类名
                category_json = itemList['category']
                category['name'] = category_json['name']
                cate_str=category['name']
                f.write('-' * 30 + big_cate_str+ ":" + cate_str + "\n")
                # 获取项目信息
                itemList_json = itemList['itemList']
                for item_one in itemList_json:
                    good["name"] = item_one['name']
                    good["id"] = item_one['id']
                    good['good_detail_url'] = 'http://you.163.com/item/detail?id=' + str(good["id"])
                    print(good)
                    f.write(str(good) + "\n")
                f.write('-' * 30 + big_cate_str + ":" + cate_str + "\n")
        f.close()
