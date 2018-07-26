#!/bin/sh

# wait for PSQL server to start
sleep 10

cd cybernews_web

# prepare init migration
python3 manage.py makemigrations --noinput
# migrate db, so we have the latest db schema
python3 manage.py migrate
python3 manage.py collectstatic --noinput
# start development server on public ip interface, on port 8000
python3 manage.py runserver 0.0.0.0:8000