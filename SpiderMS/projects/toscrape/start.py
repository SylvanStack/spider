from scrapy import cmdline

cmdline.execute("scrapy crawl toscrape -o toscrape.csv".split())