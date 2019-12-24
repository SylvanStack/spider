import requests
from lxml import etree
import re
import MySQLdb

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"}

db_conn=None
db_cursor = None

def initMySQL():
    global db_cursor
    global db_conn
    #1.连接Mysql数据库
    host = "localhost"
    user = "root"
    psd = "mysql123456"
    db = "douban"
    db_conn = MySQLdb.connect(host=host,user=user,password=psd,db=db,charset="utf8")

    #获取游标
    db_cursor = db_conn.cursor()



def parse(url):
    global db_cursor
    #得到HMTL文档
    html = requests.get(url,headers=header)

    #解析文档
    #获取豆瓣top250中页面的标题
    selector = etree.HTML(html.text)

    movies_list = selector.xpath("//ol[@class='grid_view']/li")
    for movie_selector in movies_list:
        name = movie_selector.xpath(".//div[@class='hd']/a/span[1]/text()")[0]#名称
        star = movie_selector.xpath(".//div[@class='star']/span[@class='rating_num']/text()")[0]#评分
        nums = movie_selector.xpath(".//div[@class='star']/span[last()]/text()")[0]#人数
        nums = re.sub("\D","",nums)
        director_and_act = movie_selector.xpath(".//div[@class='bd']/p[1]/text()")[0].strip("\n").strip(" ")
        director = re.findall("导演: (.*?) ",director_and_act)[0]
        act = re.findall("主演: (.*?) ",director_and_act)
        if not act:
            act = ["未知"]

        sql = "insert into movies(name,star)values('%s','%s')"%(name,star)
        #values = (name,star)
        db_cursor.execute(sql)

        url = movie_selector.xpath(".//div[@class='hd']/a/@href")[0]

    next_url = selector.xpath("//span[@class='next']/a/@href")
    if next_url:
        next_url = "https://movie.douban.com/top250"+next_url[0]
        parse(next_url)

if __name__ == "__main__":
    initMySQL()
    parse("https://movie.douban.com/top250")
    db_conn.commit()

    db_cursor.close()
    db_conn.close()








