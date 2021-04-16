FROM python:3.6-slim

ADD . /data
WORKDIR /data

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["scrapy"]
CMD ["crawl", "slave"]
