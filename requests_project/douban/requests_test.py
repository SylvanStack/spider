import requests

# r = requests.get('https://www.baidu.com/')
# r = requests.post('http://httpbin.org/post')
# r = requests.delete('http://httpbin.org/delete')
# r = requests.head('http://httpbin.org/get')
r = requests.options('http://httpbin.org/get')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)


