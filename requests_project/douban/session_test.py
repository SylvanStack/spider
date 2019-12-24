import requests

session = requests.Session()

# url = 'http://192.144.149.176/Login/CheckLogin'

# 爬取豆瓣
url = 'https://accounts.douban.com/j/mobile/login/basic'
data = {
    'ck': '',
    'name': '你的名字',
    'password': '你的密码',
    'remember': 'true',
    'ticket': '',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

result = session.post(url=url, data=data, headers=headers)
print(result.text)

html = session.get("https://www.douban.com/people/196413242/notes", headers=headers)
print(html.text)
