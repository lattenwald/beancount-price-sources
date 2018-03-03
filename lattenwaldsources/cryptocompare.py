"""Fetch prices from CryptoCompare.com JSON API
"""
import re
import datetime
import time
import logging
import json
from urllib import parse
from urllib import error

from beancount.core.number import D
from beancount.prices import source
from beancount.utils import net_utils

from dateutil import tz

class Source(source.Source):
    "CryptoCompare API price extractor."

    def get_historical_price(self, ticker, date):
        commodity, currency = ticker.split(':')
        trade_date = datetime.datetime.combine(date, datetime.datetime.max.time())
        ts = int(time.mktime(trade_date.timetuple()))
        url = 'https://min-api.cryptocompare.com/data/pricehistorical?fsym={}&tsyms={}&ts={}'.format(commodity, currency, ts)
        try:
            response = net_utils.retrying_urlopen(url)
            if response is None:
                return None
            response = response.read().decode('utf-8').strip()
            response = json.loads(response)
        except error.HTTPError:
            return None

        price = D(response[commodity][currency])
        return source.SourcePrice(price, trade_date, currency)

    def get_latest_price(self, ticker):
        commodity, currency = ticker.split(':')
        url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}'.format(commodity, currency)
        try:
            response = net_utils.retrying_urlopen(url)
            if response is None:
                return None
            response = response.read().decode('utf-8').strip()
            response = json.loads(response)
        except error.HTTPError:
            return None

        price = D(response[currency])
        td = datetime.datetime.now()
        return source.SourcePrice(price, td, currency)
