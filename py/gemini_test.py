#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   gemini_test.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/9  21:47   xguo      1.0         None

'''


########## GEMINI行情接口 ##########
## https://api.gemini.com/v1/pubticker/:symbol

import json
import requests



def main():
    gemini_ticker = 'https://api.gemini.com/v1/pubticker/{}'
    symbol = 'btcusd'
    btc_data = requests.get(gemini_ticker.format(symbol)).json()
    print(json.dumps(btc_data, indent=4))

if __name__ == "__main__":
    main()