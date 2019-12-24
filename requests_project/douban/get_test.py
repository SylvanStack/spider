import requests


r= requests.get("http://192.144.149.176/Login")
print(r.text)