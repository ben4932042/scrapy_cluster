import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

BOT_NAME = 'cht_crawler'

SPIDER_MODULES = ['cht_crawler.spiders']
NEWSPIDER_MODULE = 'cht_crawler.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = 6379

DNS_TIMEOUT = 10
STATS_CLASS = "scrapy_redis.stats.RedisStatsCollector"
FEED_EXPORT_ENCODING = 'utf-8'
DOWNLOAD_FAIL_ON_DATALOSS=False
DOWNLOAD_TIMEOUT=5
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER_PERSIST = True
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

ITEM_PIPELINES = {
    'cht_crawler.pipelines.ChtCrawlerPipeline': 300,
	#'scrapy_redis.pipelines.RedisPipeline': 400,
}


DEFAULT_REQUEST_HEADERS = {
    "Accept": "*/*",
    "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        }

# DOWNLOADER_MIDDLEWARES = {
#     'cht_crawler.middlewares.ChtCrawlerSpiderMiddleware': 543,
# }


LOG_LEVEL = 'DEBUG'
CONCURRENT_REQUESTS = 32
CONCURRENT_REQUESTS_PER_DOMAIN = 32
CONCURRENT_REQUESTS_PER_IP = 32

DOWNLOAD_DELAY = 0
COOKIES_ENABLED = False
