# -*- coding: utf-8 -*-
import json
import scrapy

from yanxuan.items import Cate, Group


class CateSaveSpider(scrapy.Spider):
    name = 'cate_save'
    allowed_domains = ['you.163.com']
    start_urls = ['http://you.163.com/xhr/globalinfo/queryTop.json']

    def parse(self, response):
        result = json.loads(response.text)
        if result['code'] == "200":
            cateList = result["data"]["cateList"]
            for cate_one in cateList:
                big_name = cate_one["name"]
                big_category_url = 'http://you.163.com/item/list?categoryId=' + str(cate_one["id"])
                big_id = cate_one["id"]
                big_superCategoryId = cate_one["superCategoryId"]
                big_showIndex = cate_one["showIndex"]
                big_frontName = cate_one["frontName"]
                big_frontNameIcon = cate_one["frontNameIcon"]
                big_frontDesc = cate_one["frontDesc"]
                big_bannerUrl = cate_one["bannerUrl"]
                big_iconUrl = cate_one["iconUrl"]
                big_level = cate_one["level"]
                big_result_item = Cate(name=big_name, category_url=big_category_url, id=big_id,
                                           superCategoryId=big_superCategoryId, showIndex=big_showIndex,
                                           frontName=big_frontName, frontNameIcon=big_frontNameIcon,
                                           bannerUrl=big_bannerUrl, iconUrl=big_iconUrl, level=big_level,
                                           groupId=None, frontDesc=big_frontDesc)
                yield big_result_item
                # url = item["category_url"]
                # yield scrapy.Request(url, callback=self.cate_parse, dont_filter=True, meta={"item": deepcopy(item)})
                subCateGroupList = cate_one['subCateGroupList']
                for subCateGroup_one in subCateGroupList:
                    group_name = subCateGroup_one['name']
                    group_id = subCateGroup_one['id']
                    yield Group(name=group_name, id=group_id)
                    categoryList = subCateGroup_one['categoryList']
                    for category_one in categoryList:
                        name = category_one["name"]
                        category_url = 'http://you.163.com/item/list?categoryId=' + str(
                            category_one["superCategoryId"]) + "&subCategoryId=" + str(category_one["id"])
                        id = category_one["id"]
                        superCategoryId = category_one["superCategoryId"]
                        showIndex = category_one["showIndex"]
                        frontName = category_one["frontName"]
                        frontNameIcon = category_one["frontNameIcon"]
                        frontDesc = category_one["frontDesc"]
                        bannerUrl = category_one["bannerUrl"]
                        iconUrl = category_one["iconUrl"]
                        level = category_one["level"]
                        yield Cate(name=name, category_url=category_url, id=id,
                                       superCategoryId=superCategoryId, showIndex=showIndex,
                                       frontName=frontName, frontNameIcon=frontNameIcon,
                                       bannerUrl=bannerUrl, iconUrl=iconUrl, level=level, groupId=None,
                                       frontDesc=frontDesc)
