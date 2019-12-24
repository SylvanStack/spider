# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 16:49
# @Author  : SiYuan Han
# @Email   : 422295068@qq.com
# @File    : mysql_test.py
# @Software: PyCharm

import pymysql

db = pymysql.connect(host='localhost',user='root', password='mysql123456', port=3306)
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version:', data)
# cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
db.close()