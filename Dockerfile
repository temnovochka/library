FROM python:3.7

COPY . /srv/www/library
WORKDIR /srv/www/library

RUN pip install -r requirements.txt