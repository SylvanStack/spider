import requests

cookies = requests.Session()

url = 'https://accounts.douban.com/j/mobile/login/basic'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

with open('cookie.txt', 'r', encoding='utf-8') as f:
    cookies_str = f.readline()


cookies_list=cookies_str.split(";")
cookies_dict={}

for cookie in cookies_list:
        key = cookie.split("=")[0].replace(" ", "")
        value = cookie.split("=")[1]
        cookies_dict[key] = value

html = requests.get("https://www.douban.com/people/168443006/notes", headers=headers, cookies=cookies_dict)
print(html.text)