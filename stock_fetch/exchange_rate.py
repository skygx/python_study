#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   fetch_stock.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/3/3 上午 9:22   hello      1.0         None

'''

import time
import requests
import json
from prometheus_client import start_http_server, CollectorRegistry, Gauge


reg = CollectorRegistry()
gauge = Gauge(
    'rate', '人民币汇率',
    ['money_id'], registry=reg
)


def process_request():
    url = "https://v6.exchangerate-api.com/v6/2cb0300471bff43a31352ac7/latest/CNY"

    result = requests.get(url).json()
    rates = json.dumps(result['conversion_rates'])
    rates_json = json.loads(rates)
    codes = parse_code()
    for k,v in dict(rates_json).items():
         gauge.labels(money_id=codes[k]).set(v)
    time.sleep(60)

def parse_code():
    codes={}
    with open('./rates_code.json','r',encoding='utf-8') as f:
        r = json.load(f)
    for i in r:
        code = i['code']
        name = i['name']
        codes[code] = name
    return codes

if __name__ == '__main__':
    start_http_server(8000, registry=reg)
    while True:
        process_request()
