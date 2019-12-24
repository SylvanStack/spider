from scrapy import cmdline

cmdline.execute("scrapy crawl job -o web.csv".split())
