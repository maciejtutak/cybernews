FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y
RUN mkdir /config
ADD requirements.txt /config/
RUN pip3 install --upgrade pip && pip3 install -r /config/requirements.txt
RUN python -m nltk.downloader punkt wordnet stopwords averaged_perceptron_tagger

RUN mkdir /code
WORKDIR /code