import requests
from lxml import etree
import re

# 得到HMTL文档
# html = requests.get("https://movie.douban.com/top250")

# 解析文档
# 获取豆瓣top250中页面的标题
# selector = etree.HTML(html.text)
# title = selector.xpath("/html/head/title/text()")
# name = selector.xpath("//div[@class='hd']/a/span[1]/text()")
# score = selector.xpath("//div[@class='star']/span[2]/text()")
# evaluate = selector.xpath("//div[@class='star']/span[4]/text()")
# performer = selector.xpath("//div[@class='bd']/p[1]/text()")

# for i in performer:
#     print(i.strip())

movies_list = []
def get_data(url):
    html = requests.get(url)
    selector = etree.HTML(html.text)
    all_movies = selector.xpath("//ol[@class='grid_view']/li")
    for movioes in all_movies:
        print(movioes)
        name = movioes.xpath(".//div[@class='hd']/a/span[@class='title']/text()")[0]
        print(name)
        score = movioes.xpath(".//div[@class='star']/span[2]/text()")[0]
        evaluate = movioes.xpath(".//div[@class='star']/span[4]/text()")[0][:-3]
        print(evaluate)
        performer = movioes.xpath(".//div[@class='bd']/p[1]/text()")[0].strip("\n").strip(" ")
        print(performer)
        aa=re.findall("导演: (.*?) ",performer)[0]
        print(aa)
        next_url = selector.xpath("//span[@class='next']/a/@href")
        movies_list.append(name + "      " + score + "      " + evaluate + "      " + aa+ "\n")
        if next_url:
            next_url = url + next_url[0]
            get_data(next_url)


if __name__=='__main__':
    get_data("https://movie.douban.com/top250")

# for i in movioes_list:
#     with open('douban.txt', 'a', encoding='utf-8') as f:
#         f.write(i)
