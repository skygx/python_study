#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   gemini-market.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/10  14:23   xguo      1.0         None

'''

import requests
import json
import base64
import hmac
import hashlib
import datetime
import time


def main():
    base_url = "https://api.sandbox.gemini.com"
    endpoint = "/v1/order/new"
    url = base_url + endpoint

    gemini_api_key = "account-zmidXEwP72yLSSybXVvn"
    gemini_api_secret = "375b97HfE7E4tL8YaP3SJ239Pky9".encode()

    t = datetime.datetime.now()
    payload_nonce = str(int(time.mktime(t.timetuple()) * 1000))

    payload = {
        "request": "/v1/order/new",
        "nonce": payload_nonce,
        "symbol": "btcusd",
        "amount": "5",
        "price": "3633.00",
        "side": "buy",
        "type": "exchange limit",
        "options": ["maker-or-cancel"]
    }

    encoded_payload = json.dumps(payload).encode()
    b64 = base64.b64encode(encoded_payload)
    signature = hmac.new(gemini_api_secret, b64, hashlib.sha384).hexdigest()

    request_headers = {
        'Content-Type': "text/plain",
        'Content-Length': "0",
        'X-GEMINI-APIKEY': gemini_api_key,
        'X-GEMINI-PAYLOAD': b64,
        'X-GEMINI-SIGNATURE': signature,
        'Cache-Control': "no-cache"
    }

    response = requests.post(url,
                             data=None,
                             headers=request_headers)

    new_order = response.json()
    print(new_order)

if __name__ == "__main__":
    main()