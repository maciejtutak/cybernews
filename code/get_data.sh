#!/bin/bash

echo -e "\n\nDATA COLLECTION STARTED AT `date`\n\n"

# get into the scraper app
cd /code/cybernews_web/scraper

for i in $(scrapy list); do
    scrapy crawl ${i}
done

# come back to manage.py directory
cd ..

python manage.py classify
