import json
import time
import numpy as np
import requests

url = "https://api.bitbay.net/rest/trading/ticker/BTC-PLN"

headers = {'content-type': 'application/json'}

#{
#  "status": "Ok",
#  "ticker": {
#    "market": {
#      "code": "BTC-PLN",
#      "first": {
#        "currency": "BTC",
#        "minOffer": "0.00003",
#        "scale": 8
#      },
#      "second": {
#        "currency": "PLN",
#        "minOffer": "5",
#        "scale": 2
#      }
#    },
#    "time": "1576148607293",
#    "highestBid": "27738.98",
#    "lowestAsk": "27739",
#    "rate": "27739",
#    "previousRate": "27738.98"
#  }
#}
def get_time():
    response = requests.request("GET", url, headers=headers)
    BTC = json.loads(response.text)
    if BTC['status'] == 'Ok':
        return int(BTC['ticker']['time'])
    else:
        return print('error')

def get_rate():
    response = requests.request("GET", url, headers=headers)
    BTC = json.loads(response.text)
    if BTC['status'] == 'Ok':
        return float(BTC['ticker']['rate'])
    else:
        return print('error')

def get_bid():
    response = requests.request("GET", url, headers=headers)
    BTC = json.loads(response.text)
    if BTC['status'] == 'Ok':
        return float(BTC['ticker']['highestBid'])
    else:
        return print('error')

def get_ask():
    response = requests.request("GET", url, headers=headers)
    BTC = json.loads(response.text)
    if BTC['status'] == 'Ok':
        return float(BTC['ticker']['lowestAsk'])
    else:
        return print('error')

def get_previous_rate():
    response = requests.request("GET", url, headers=headers)
    BTC = json.loads(response.text)
    if BTC['status'] == 'Ok':
        return float(BTC['ticker']['previousRate'])
    else:
        return print('error')

def get_code():
    response = requests.request("GET", url, headers=headers)
    BTC = json.loads(response.text)
    if BTC['status'] == 'Ok':
        return (BTC['ticker']['market']['code'])
    else:
        return print('error')

def get_currency_first():
    response = requests.request("GET", url, headers=headers)
    BTC = json.loads(response.text)
    if BTC['status'] == 'Ok':
        return BTC['ticker']['first']['currency']
    else:
        return print('error')

def get_min_offer_first():
    response = requests.request("GET", url, headers=headers)
    BTC = json.loads(response.text)
    if BTC['status'] == 'Ok':
        return float(BTC['ticker']['first']['minOffer'])
    else:
        return print('error')

def get_min_offer_first():
    response = requests.request("GET", url, headers=headers)
    BTC = json.loads(response.text)
    if BTC['status'] == 'Ok':
        return int(BTC['ticker']['first']['scale'])
    else:
        return print('error')

def get_currency_second():
    response = requests.request("GET", url, headers=headers)
    BTC = json.loads(response.text)
    if BTC['status'] == 'Ok':
        return BTC['ticker']['second']['currency']
    else:
        return print('error')

def get_min_offer_second():
    response = requests.request("GET", url, headers=headers)
    BTC = json.loads(response.text)
    if BTC['status'] == 'Ok':
        return float(BTC['ticker']['second']['minOffer'])
    else:
        return print('error')

def get_min_offer_second():
    response = requests.request("GET", url, headers=headers)
    BTC = json.loads(response.text)
    if BTC['status'] == 'Ok':
        return int(BTC['ticker']['second']['scale'])
    else:
        return print('error')