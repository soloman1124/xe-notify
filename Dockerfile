FROM python:2.7.10
MAINTAINER Soloman Weng "soloman.weng@simplehq.com.au"
ENV REFRESHED_AT 2016-02-26

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN pip install lambda-uploader>=0.5.1
RUN pip install boto3>=1.2.2

ADD requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

ADD . /usr/src/app
