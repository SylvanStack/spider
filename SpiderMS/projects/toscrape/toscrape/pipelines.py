import pymongo


class ToscrapePipeline(object):
    def open_spider(self, item, spider):
        # 连接MongoDb数据库服务器
        self.db_client = pymongo.MongoClient()
        if spider.name == "toscrape":
            # 指定操作的数据库
            self.db = self.db_client["toscrape"]
            # 指定集合（类似MYSQL中的表）
            self.db_collection = self.db["books"]
        return item

    def process_item(self, item, spider):
        self.db_collection.insert_one(dict(item))
        return item

    # 爬虫全部完成后执行一次（收尾工作）
    def close_spider(self, spider):
        self.db_client.close()