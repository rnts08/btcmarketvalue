#!/usr/bin/env python
#
# display last price for BTC on different markets. 

import requests

def get_mtgox_price():
    btcusd = requests.get('https://mtgox.com/api/1/BTCUSD/ticker').json()
    return btcusd['return']['last']['value']

def get_btce_price():
    btcusd = requests.get('https://btc-e.com/api/2/btc_usd/ticker').json()
    return btcusd['ticker']['last']

def get_bitstamp_price():
    btcusd = requests.get('https://www.bitstamp.net/api/ticker/').json()
    return btcusd['last']

if __name__ == '__main__':
    prices = {'btce': get_btce_price(), 'mtgox': get_mtgox_price(), 'bitstamp': get_bitstamp_price()}

    for market in prices:
        print market + ': ' + str(prices[market])
