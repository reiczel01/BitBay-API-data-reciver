import json
import time
import numpy as np
import requests
import data_get as dta
#work in progres
rate_array = np.zeros(10)
rate_bid = np.zeros(10)
rate_ask = np.zeros(10)

i = 0
for i in range(10):
    rate_array[i] = dta.get_rate()
    rate_bid[i] = dta.get_bid()
    rate_ask[i] = dta.get_ask()
    print('rate:',dta.get_rate(),' bid:',dta.get_bid(),' ask:',dta.get_ask())
    time.sleep(10)

j = 0
avg_cors = np.zeros(3)
for j in range(10):
    avg_cors[0]+= rate_array[j]
    avg_cors[1]+= rate_bid[j]
    avg_cors[2]+= rate_ask[j]

print("avg rate:",avg_cors[0]/10," avg bid:",avg_cors[1]/10," avg ask:",avg_cors[2]/10)