# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 导入访问MySQL的模块
import pymysql


class ZhipinPipeline(object):
    # 定义构造器，初始化要写入的文件
    def __init__(self):
        self.conn = pymysql.connect("localhost", "root", "mysql123456", "db_boss")  # 连接数据库
        self.cur = self.conn.cursor()

    # 重写close_spider回调方法，用于关闭数据库资源
    def close_spider(self, spider):
        print('----------关闭数据库资源-----------')
        # 关闭游标
        self.cur.close()
        # 关闭连接
        self.conn.close()

    def process_item(self, item, spider):
        self.cur.execute("INSERT INTO db_boss.job_info VALUES(null, %s, %s, %s, %s, %s, \
               %s, %s, %s, %s)", (item['title'], item['salary'], item['company'],
                                  item['url'], item['work_addr'], item['industry'],
                                  item.get('company_size'), item['recruiter'], item['publish_date']))
        self.conn.commit()
