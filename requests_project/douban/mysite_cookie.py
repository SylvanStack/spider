import requests

cookies = requests.Session()

url = 'http://192.144.149.176/Home/Index'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

with open('my_cookie.txt', 'r', encoding='utf-8') as f:
    cookies_str = f.readline()

cookies_list=str(cookies_str).split(";")
cookies_dict={}

for cookie in cookies_list:
        key = cookie.split("=")[0].replace(" ", "")
        value = cookie.split("=")[1]
        cookies_dict[key] = value

html = requests.get("http://192.144.149.176/User/Index", headers=headers, cookies=cookies_dict)
# print(html.text)


html1 =requests.get('http://192.144.149.176:8005/')
print(html1.text)