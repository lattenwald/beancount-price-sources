"""Fetch prices from WavesPlatform using PyWaves
"""
import time
import traceback
import logging
from dateutil import tz,utils
from datetime import datetime
from urllib import error
from math import log10, floor

import pywaves as pw

from beancount.core.number import D
from beancount.prices import source
from beancount.utils import net_utils

class Source(source.Source):
    "Waves price extractor"

    def get_latest_price(self, ticker):
        try:
            currency, pair = asset_pair(ticker)
            ticker = pair.ticker()
            if 'status' in ticker and ticker['status'] == 'error':
                logging.error("%s", ticker['message'])
                return None
            logging.info("Ticker %s", ticker)
            price = D(ticker['24h_close']).quantize(D('1.000000000000000000'))
            ts = ticker['timestamp'] / 1000
            trade_date = utils.default_tzinfo(datetime.fromtimestamp(ts), tz.UTC)
            return source.SourcePrice(D('0') if price == 0 else price, trade_date, currency)
        except Exception as e:
            logging.error(traceback.format_exc())
            return None

    def get_historical_price(self, ticker, date):
        try:
            currency, pair = asset_pair(ticker)
            trade_date_start = utils.default_tzinfo(datetime.combine(date, datetime.min.time()), tz.UTC)
            trade_date = datetime.combine(date, datetime.max.time())
            ohlcv = pair.candles(1440, 1000*int(trade_date_start.timestamp()), 1000*int(trade_date.timestamp()))
            assert len(ohlcv) == 1
            ohlcv = ohlcv[0]
            price = D(ohlcv['close']).quantize(D('1.000000000000000000'))
            trade_date = utils.default_tzinfo(datetime.fromtimestamp(ohlcv['timestamp'] / 1000), tz.UTC)
            return source.SourcePrice(D('0') if price == 0 else price, trade_date, currency)
        except Exception as e:
            logging.error(traceback.format_exc())
            return None

def asset_pair(ticker):
    commodity, currency_id, currency_name = ticker.split(':')
    commodity_asset = pw.Asset(commodity)
    currency_asset = pw.Asset(currency_id)
    return currency_name, pw.AssetPair(commodity_asset, currency_asset)
