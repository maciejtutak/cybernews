FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade -y && apt-get install -y cron
RUN crontab -l > temp; env >> temp; echo "12 */1 * * * /code/get_data.sh >> /code/get_data.log 2>&1" >> temp; crontab temp; rm temp

RUN mkdir /config
ADD requirements.txt /config/
RUN pip3 install --upgrade pip && pip3 install -r /config/requirements.txt
RUN python -m nltk.downloader punkt wordnet stopwords averaged_perceptron_tagger

RUN mkdir /code
WORKDIR /code