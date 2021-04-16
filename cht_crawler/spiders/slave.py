# import os
# import logging
import re
import hashlib
import json
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisCrawlSpider
from ..items import ChtCrawlerItem
# from dotenv import load_dotenv, find_dotenv
# load_dotenv(find_dotenv())

def get_hash256(url: str):
    s = hashlib.sha256()
    s.update(url.encode('utf-8'))
    URLID = s.hexdigest()
    return URLID

class CrawlerRedis(RedisCrawlSpider):
    """
    custom setting: save data into mongo
    download_delay: get rough but fast way to finish this job
    """
    name = 'slave'
    redis_key = 'cht_slave:start_urls'

    # rules = (
    #     Rule(callback='parse',
    #          follow=False,
    #          process_links=None,
    #          ),
    # )

    def __init__(self, *args, **kwargs):
        """
        initial setting
        """
        super(CrawlerRedis, self).__init__(*args, **kwargs)

    def make_requests_from_url(self, data: str):
        """
        custom crawl rule
        """
        req_data = json.loads(data)
        target_url = req_data['url']
        
        return scrapy.Request(
            target_url,
            meta={
            'req_data': req_data,
            'dont_retry': True,
            }
        )

    def parse_start_url(self, response):

        item = ChtCrawlerItem()

        item['_id'] = get_hash256(response.url)
        item['execute_date'] = response.meta['req_data']['date']
        item['target_url'] = response.url
        item['content_text'] = re.sub(
                                ' |\t|\r|\n|\u3000|\xa0|<br>|<br/>', '。',
                                ''.join(response.xpath('//body//text()').extract())
                                ).replace('。。', '。')
        yield item

