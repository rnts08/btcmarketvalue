#!/usr/bin/env python
#
# display last price for LTC from BTC-e

import requests

def get_btce_price():
    try:
        ltcusd = requests.get('https://btc-e.com/api/2/ltc_usd/ticker').json()
        return {'last': ltcusd['ticker']['last'], 'high': ltcusd['ticker']['high'], 'low': ltcusd['ticker']['low'], 'avg': ltcusd['ticker']['avg']}
    except:
        return 0.0

if __name__ == '__main__':
    ltc = get_btce_price()
    print 'USD/LTC: ${} (${}) high/low: ${}/${}'.format(ltc['last'], ltc['avg'], ltc['high'],ltc['low'])
