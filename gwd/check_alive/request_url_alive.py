# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   request_url_alive.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/6/21 下午4:49   hello      1.0         None

'''
import requests
def check_url_alive(url,search_string):
    try:
        response = requests.get(url, timeout=3)
        # print(response.text)
        if response.status_code in [200,301] :
            # return True
            return search_string in response.text
        else:
            return False
    except requests.exceptions.RequestException:
        return False

if __name__ == '__main__':
    with open('url.txt','r') as f:
        for line in f.readlines():
            name,ip,port,uri,key = line.split()
            url = 'http://'+ip+':'+port+'/'+uri
            print(url)
            print(name,check_url_alive(url,key))
    # url = 'http://192.168.226.20:88/bk_svr'
    # print(check_url_alive(url,'hello'))
