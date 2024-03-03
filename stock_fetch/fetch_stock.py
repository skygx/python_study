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
from prometheus_client import start_http_server, CollectorRegistry, Gauge


reg = CollectorRegistry()
gauge = Gauge(
    'rank', '人气榜排名',
    ['stock_id'], registry=reg
)


def process_request():
    url = "https://emappdata.eastmoney.com/stockrank/getAllCurrentList"
    kwargs = {
        "appId": "appId01",
        "pageNo": 1,
        "pageSize": "100",
    }
    result = requests.post(url, json=kwargs).json()
    for i in result.get("data", []):
        gauge.labels(stock_id=i["sc"]).set(i["rk"])
    time.sleep(60)


if __name__ == '__main__':
    start_http_server(8000, registry=reg)
    while True:
        process_request()
