import requests
from lxml import etree

#得到HMTL文档
html = requests.get("https://movie.douban.com/top250")

#解析文档
#获取豆瓣top250中页面的标题
selector = etree.HTML(html.text)

all_movies = []

movies_list = selector.xpath("//ol[@class='grid_view']/li")
for movie_selector in movies_list:
    name = movie_selector.xpath(".//div[@class='hd']/a/span[1]/text()")[0]#名称
    star = movie_selector.xpath(".//div[@class='star']/span[@class='rating_num']/text()")[0]#评分
    nums = movie_selector.xpath(".//div[@class='star']/span[last()]/text()")[0]#人数
    nums = nums.split("人评价")[0]
    url = selector.xpath(".//div[@class='hd']/a/@href")[0]
    one_movie = [name,star,nums,url]

    all_movies.append(one_movie)

print(all_movies)

for movie in all_movies:
    one_str = movie[0]+","+movie[1]+","+movie[2]+","+movie[3]+"\n"
    with open("movies.txt","a",encoding="utf-8") as f:
        f.write(one_str)






