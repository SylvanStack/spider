import re
import json
import requests

# f = open("test.txt", "rt", encoding='utf-8')
# data = f.read()
# f.close()
#
# content = re.findall(r'var json_Data=(.+);', data)
# result = json.loads(content[0])
# with open("good.html", 'w', encoding='utf-8') as f:
#     f.write(json.dumps(content, ensure_ascii=False, indent=2))
#
# currentCategory = result['currentCategory']  # 一级标签数据
# deliveryAreaList = result['deliveryAreaList']  # 配送地区数据
# focusList = result['focusList']  # 频道类目首焦广告
# categoryItemList = result['categoryItemList']  # 分类加商品信息
# pathList = result['pathList']  # 一级标签数据

# print(pathList)

# i = 0
# category = {}
# item = {}
# for itemList in categoryItemList:
#     itemList_json = itemList['itemList']
#     for item_one in itemList_json:
#         item["name"] = item_one['name']
#         item["id"] = item_one['id']
#         item['good_detail_url'] = 'http://you.163.com/item/detail?id=' + str(item["id"])
#         print(item)
#     i += 1
#     if i > 1: break

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
# }
# response = requests.get('http://you.163.com/item/detail?id=1021020', headers=headers)
# content_good = response.content.decode("utf-8")
# with open("goodDemo.txt", "w", encoding="utf-8") as f1:
#     f1.write(content_good)
# f1.close()

f1 = open("goodDemo.txt", "rt", encoding='utf-8')
content_good = f1.read()
f1.close()
content_good = content_good.replace("\n", "").replace("\'", "\"")
data_good = re.findall(r'var JSON_DATA_FROMFTL = (.+);.*var JSON_DATA', content_good)[0]
good = json.loads(data_good)
item=good["item"]
commentCount=good["commentCount"]
commentGoodRates=good["commentGoodRates"]
policyList=good["policyList"]
rcmdItems=good["rcmdItems"]
suitList=good["suitList"]
itemType=good["itemType"]
categoryList=good["categoryList"]

print(item)
