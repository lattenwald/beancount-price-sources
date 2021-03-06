"""Fetch prices from CryptoCompare.com JSON API
"""
import time
import logging
import json
from dateutil import tz,utils
from datetime import datetime
from urllib import error
from math import log10, floor

from beancount.core.number import D
from beancount.prices import source
from beancount.utils import net_utils

class Source(source.Source):
    "CryptoCompare API price extractor."

    def get_historical_price(self, ticker, date):
        commodity, currency = ticker.split(':')
        trade_date = utils.default_tzinfo(datetime.combine(date, datetime.max.time()), tz.UTC)
        ts = int(time.mktime(trade_date.timetuple()))
        url = 'https://min-api.cryptocompare.com/data/pricehistorical?fsym={}&tsyms={}&ts={}'.format(commodity, currency, ts)
        logging.info("Fetching %s", url)
        try:
            response = net_utils.retrying_urlopen(url)
            if response is None:
                return None
            response = response.read().decode('utf-8').strip()
            response = json.loads(response)
        except error.HTTPError:
            return None

        price = D(response[commodity][currency]).quantize(D('1.000000000000000000'))
        return source.SourcePrice(D('0') if price == 0 else price, trade_date, currency)

    def get_latest_price(self, ticker):
        commodity, currency = ticker.split(':')
        url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}'.format(commodity, currency)
        logging.info("Fetching %s", url)
        try:
            response = net_utils.retrying_urlopen(url)
            if response is None:
                return None
            response = response.read().decode('utf-8').strip()
            response = json.loads(response)
        except error.HTTPError:
            return None
        price = D(response[currency]).quantize(D('1.000000000000000000'))
        trade_date = utils.default_tzinfo(datetime.now(), tz.gettz())
        return source.SourcePrice(D('0') if price == 0 else price, trade_date, currency)
