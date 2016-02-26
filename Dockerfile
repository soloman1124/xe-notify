FROM python:2.7.10
MAINTAINER Soloman Weng "soloman.weng@simplehq.com.au"
ENV REFRESHED_AT 2016-02-26

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

ADD . /usr/src/app
