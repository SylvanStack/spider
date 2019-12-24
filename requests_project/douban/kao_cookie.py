import requests

cookies = requests.Session()

url = 'https://www.kaochong.com/mycourse/listLesson/2284.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

with open('kao_cookies.txt', 'r', encoding='utf-8') as f:
    cookies_str = f.readline()

cookies_list=str(cookies_str).split(";")
cookies_dict={}

for cookie in cookies_list:
        key = cookie.split("=")[0].replace(" ", "")
        value = cookie.split("=")[1]
        cookies_dict[key] = value

html = requests.get("http://www.kaochong.com/live/new/80869.html?uld=1", headers=headers, cookies=cookies_dict)
print(html.text)