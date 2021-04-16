# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
from itemadapter import ItemAdapter
import pymongo
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


class ChtCrawlerPipeline:
    def __init__(self):
        self.mongo_uri = os.getenv("MONGO_HOST")
        self.db_name = "crawler"

    def open_spider(self, spider):
        self.db_client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.db_client[self.db_name]

    def process_item(self, item, spider):
        self.insert_article(item)       

    def insert_article(self, item):
        item = dict(item)
        if not item['content_text'] == '':
            self.db.article.insert_one(item)

    def close_spider(self, spider):
        self.db_client.close()

