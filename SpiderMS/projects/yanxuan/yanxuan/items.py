import scrapy


class ImageItem(scrapy.Item):  # 图片类
    id = scrapy.Field()  # iD
    images = scrapy.Field()  # 必要,不可自定义
    image_urls = scrapy.Field()  # 必要,不可自定义
    image_results = scrapy.Field()  # 必要,不可自定义
    image_name = scrapy.Field()  # 非必要，可自定义,用于传递每个item的名称(用于文件夹命名)
    image_paths = scrapy.Field()  # 非必要,可自定义,在pipeline中的item_completed方法使用


class Cate(scrapy.Item):  # 标签类
    id = scrapy.Field()
    superCategoryId = scrapy.Field()
    name = scrapy.Field()
    level = scrapy.Field()
    showIndex = scrapy.Field()
    iconUrl = scrapy.Field()
    frontNameIcon = scrapy.Field()
    frontName = scrapy.Field()
    frontDesc = scrapy.Field()
    bannerUrl = scrapy.Field()
    category_url = scrapy.Field()
    groupId = scrapy.Field()
    createTime = scrapy.Field()
    updateTime = scrapy.Field()


class Group(scrapy.Item):  # 分组类
    name = scrapy.Field()
    id = scrapy.Field()
    createTime = scrapy.Field()
    updateTime = scrapy.Field()


class Good(scrapy.Item):  # 商品类
    id = scrapy.Field()
    name = scrapy.Field()
    goodDetailUrl = scrapy.Field()
    scenePicUrl = scrapy.Field()
    primaryPicUrl = scrapy.Field()
    counterPrice = scrapy.Field()
    retailPrice = scrapy.Field()
    primarySkuId = scrapy.Field()
    displaySkuId = scrapy.Field()
    simpleDesc = scrapy.Field()
    promId = scrapy.Field()
    postageTip = scrapy.Field()
    rank = scrapy.Field()
    sellVolume = scrapy.Field()


class Comment(scrapy.Item):
    pass


class CateMongo(scrapy.Item):
    pass


class GroupMongo(scrapy.Item):
    pass
