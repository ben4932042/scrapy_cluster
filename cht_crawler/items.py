# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ChtCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    execute_date = scrapy.Field()
    target_url = scrapy.Field()
    content_text = scrapy.Field()
