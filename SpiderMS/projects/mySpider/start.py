from scrapy import cmdline

# cmdline.execute("scrapy crawl itcast".split())
# json格式，默认为Unicode编码
# cmdline.execute("scrapy crawl itcast -o teachers.json".split())
# json lines格式，默认为Unicode编码
# cmdline.execute("scrapy crawl itcast -o teachers.jsonlines".split())
# csv 逗号表达式，可用Excel打开
cmdline.execute("scrapy crawl itcast -o teachers.csv".split())
# xml格式
# cmdline.execute("scrapy crawl itcast -o teachers.xml".split())
