# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 14:50
# @Author  : SiYuan Han
# @Email   : 422295068@qq.com
# @File    : tieba.py
# @Software: PyCharm
import requests


class TiebaSpider:
    def __init__(self, name):
        self.name = name
        self.start_url = 'http://tieba.baidu.com/f?ie=utf-8&kw=' + name + '&ie=utf-8&pn={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
        }

    def get_url_list(self):  # 1. 构造url列表
        url_list = []
        for i in range(100):
            url_list.append(self.start_url.format(i * 50))
        return url_list

    def parse_url(self, url):  # 发送请求
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def save_html(self, html_str, page_number):  # 保存
        page_number = '{}-第{}页.html'.format(self.name, page_number)
        with open('html/' + page_number, 'w', encoding='utf-8') as f:
            f.write(html_str)

    def run(self):  # 实现主要的业务逻辑
        # 1. 构造url列表
        url_list = self.get_url_list()
        # 2. 遍历，发送请求，获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            page_number = url_list.index(url) + 1
            # 保存
            self.save_html(html_str, page_number)


if __name__ == '__main__':
    tieba = TiebaSpider('李易峰')
    tieba.run()

