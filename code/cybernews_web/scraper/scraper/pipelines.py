import newspaper
import time
from scrapy.exceptions import DropItem
from collection.models import Entry, Article
from .seen_url_database import SeenURLDatabase
from django.db import IntegrityError


class NewsScraperPipeline(object):
    def process_item(self, item, spider):
        article = newspaper.Article(item['url'])
        article.download()
        # in case it fails to download immediately
        if article.download_state == 0:
            time.sleep(1)
        try:
            article.parse()
        except newspaper.ArticleException:
            raise DropItem("Article failed to download.")

        if len(article.text.split()) < 80:
            raise DropItem("Article too short.")

        item['title'] = article.title
        item['text'] = article.text
        item['length'] = len(article.text.split())
        item['image_url'] = article.top_image

        if not item['author'] and article.authors:
            item['author'] = article.authors[0]

        try:
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
            raise Exception("Item with this key already exists: {}".format(i.url))
        return item

    def open_spider(self, spider):
        spider.seen_url_db = SeenURLDatabase()

    def close_spider(self, spider):
        spider.seen_url_db.close()

