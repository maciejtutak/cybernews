import time

import newspaper
from collection.models import Article, Entry
from django.db import IntegrityError
from scrapy.exceptions import DropItem
import logging

from .seen_url_database import SeenURLDatabase


logger = logging.getLogger(__file__)

class NewsScraperPipeline(object):
    def process_item(self, item, spider):
        article = newspaper.Article(item['url'])
        logger.info("article %s is about to be downloaded", item['url'])
        article.download()
        # in case it fails to download immediately
        if article.download_state == 0:
            time.sleep(1)
        try:
            article.parse()
        except newspaper.ArticleException:
            raise DropItem("Article failed to download.")

        if len(article.text.split()) < 80:
            logging.debug("article too short")
            raise DropItem("Article too short.")

        item['title'] = article.title
        item['text'] = article.text
        item['length'] = len(article.text.split())
        item['image_url'] = article.top_image

        if not item['author'] and article.authors:
            item['author'] = article.authors[0]

        try:
            logging.debug("article creation in the db")
            i = Article(
                title=item['title'],
                text=item['text'],
                source=item['source'],
                url=item['url'],
                pub_date=item['pub_date'],
                length=item['length'],
                author=item['author'],
                image_url=item['image_url'],
            )
            i.save()
            e = Entry(
                article=i,
            )
            e.save()
        except IntegrityError:
            logging.debug("article with this key already exists: %s", i.url)
            raise Exception("Item with this key already exists: {}".format(i.url))
        return item

    def open_spider(self, spider):
        logging.debug("spider seen_url_db opened")
        spider.seen_url_db = SeenURLDatabase()

    def close_spider(self, spider):
        logging.debug("spider seen_url_db closed")
        spider.seen_url_db.close()

