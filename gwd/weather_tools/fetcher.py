# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   fetcher.py.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/9/18 上午9:32   hello      1.0         None

'''
import requests
api_key = 'ebad83e3cdaa450a95771336241809'
def get_weather(city):
    """Fetch weather data from an external API."""
    url = f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'
    response = requests.get(url)
    # print(response)
    return response.json()
