import pymysql
import pymongo
from yanxuan.items import Cate, Group, CateMongo, GroupMongo
import yanxuan.settings as settings


class YanxuanPipeline(object):
    # 定义构造器，初始化要写入的文件
    def __init__(self):
        self.conn = pymysql.connect("localhost", "root", "mysql123456", "db_yanxuan")  # 连接数据库
        self.cur = self.conn.cursor()

    def close_spider(self, spider):  # 重写close_spider回调方法，用于关闭数据库资源s
        print('----------关闭数据库资源-----------')
        self.cur.close()  # 关闭游标
        self.conn.close()  # 关闭连接

    def process_item(self, item, spider):
        if spider.name == "you":
            pass
        if spider.name == "cate_save":
            if isinstance(item, Cate):
                self.insert_cate(item)
            if isinstance(item, Group):
                self.insert_group(item)
        if spider.name == "good_save":
            pass

    def insert_cate(self, item):
        self.cur.execute("INSERT INTO db_yanxuan.category VALUES(null, %s, %s, %s, %s,%s, %s, %s, \
           %s, %s, %s, %s,now(),now())",
                         (item['superCategoryId'], item['name'], item['category_url'], item['groupId'], item['level'],
                          item['showIndex'], item['iconUrl'], item['frontNameIcon'],
                          item['frontName'], item['frontDesc'], item['bannerUrl']))
        self.conn.commit()

    def insert_group(self, item):
        self.cur.execute("INSERT INTO db_yanxuan.group VALUES(null, %s,now(),now())", item['name'])
        self.conn.commit()


class MongodbPipeline(object):
    def __init__(self):
        # 链接数据库
        self.client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        # 数据库登录需要帐号密码的话
        # self.client.admin.authenticate(settings['MINGO_USER'], settings['MONGO_PSW'])
        self.db = self.client[settings['MONGO_DB']]  # 获得数据库的句柄
        # self.coll = self.db[settings['MONGO_COLL']]  # 获得collection的句柄
        self.coll = self.db["{}".format("test")]  # 获得collection的句柄

        def process_item(self, item, spider):
            if spider.name == "you":
                pass
            if spider.name == "cate_save":
                if isinstance(item, CateMongo):
                    self.insert_data(item, "category")
                if isinstance(item, GroupMongo):
                    self.insert_data(item, "group")
            if spider.name == "good_save":
                pass

    def insert_data(self, item, name):
        self.coll = self.db["{}".format(name)]  # 获得collection的句柄
        postItem = dict(item)  # 把item转化成字典形式
        self.coll.insert(postItem)  # 向数据库插入一条记录
        # return item
