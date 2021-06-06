import json
import time
import numpy as np
import requests

url = "https://api.bitbay.net/rest/trading/stats/BTC-PLN"

headers = {'content-type': 'application/json'}

#{
#  "status": "Ok",
#  "stats": {
#    "m": "BTC-PLN",
#    "h": "32841.02",
#    "l": "31173.99",
#    "v": "2538.53749287",
#    "r24h": "31155.76"
#  }
#}

def get_code():
    response = requests.request("GET", url, headers=headers)
    BTC = json.loads(response.text)
    if BTC['status'] == 'Ok':
        return BTC['stats']['m']
    else:
        return print('error')

def get_highest_rate_24h():
    response = requests.request("GET", url, headers=headers)
    BTC = json.loads(response.text)
    if BTC['status'] == 'Ok':
        return float(BTC['stats']['h'])
    else:
        return print('error')

def get_lowest_rate_24h():
    response = requests.request("GET", url, headers=headers)
    BTC = json.loads(response.text)
    if BTC['status'] == 'Ok':
        return float(BTC['stats']['l'])
    else:
        return print('error')

def get_volume_24h():
    response = requests.request("GET", url, headers=headers)
    BTC = json.loads(response.text)
    if BTC['status'] == 'Ok':
        return float(BTC['stats']['v'])
    else:
        return print('error')

def get_average_24h():
    response = requests.request("GET", url, headers=headers)
    BTC = json.loads(response.text)
    if BTC['status'] == 'Ok':
        return float(BTC['stats']['r24h'])
    else:
        return print('error')