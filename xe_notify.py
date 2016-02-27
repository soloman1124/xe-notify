#!/usr/bin/env python
import requests
import re
import boto3
import time
import logging

XE_URL = 'http://themoneyconverter.com'
CURRENCY_FROM = 'AUD'
CURRENCY_TO = 'JPY'
TARGET_RATE = 84.0


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event=None, context=None):
    current_rate = __get_exchange_rate()

    logging.info("current rate [%f] checked at [%s]" % \
        (current_rate, time.strftime('%c')))

    if current_rate >= TARGET_RATE:
        __notify(current_rate, TARGET_RATE)



def __notify(current_rate, target_rate):
    rate_title = "[Exchange Rate] 1 %s => %f %s" % \
        (CURRENCY_FROM, current_rate, CURRENCY_TO)
    rate_content = "Time to exchange!!! \n %f >= %f \n" % \
        (current_rate, target_rate)

    client = boto3.client('ses')
    client.send_email(
        Source='soloman1124@gmail.com',
        Destination={
            'ToAddresses': ['soloman1124@gmail.com']
        },
        Message={
            'Subject': {
                'Data': rate_title,
            },
            'Body': {
                'Text': {
                    'Data': rate_content
                }
            }
        }
    )


def __get_exchange_rate():
    r = requests.get("%s/%s/%s.aspx" % (XE_URL, CURRENCY_FROM, CURRENCY_TO))
    m = re.search('<h3>Latest Exchange Rates: 1 (.+) = ([\d\.]+) (.+)</h3>', r.text, re.MULTILINE)
    exchange_rate = float(m.group(2))

    return exchange_rate

if __name__ == '__main__':
    lambda_handler()
