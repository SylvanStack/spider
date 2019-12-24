from scrapy import cmdline

# cmdline.execute("scrapy crawl books".split())
cmdline.execute("scrapy crawl images -o images.csv".split())