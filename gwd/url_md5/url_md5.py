# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   url_md5.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/11/25 下午12:12   hello      1.0         None

'''
import requests
import json
def get_url_md5(url, body):
    try:
        response = requests.get(url,body=body)
        data = response.content.decode('utf-8')
        data_json = json.loads(data)
        md5 = data_json['original_md5']
        app_name = data_json['name']
        print(f"app_name:{app_name}, md5:{md5}")
        return md5
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    # url = "https://jfrog.com/api/search/checksum?a=1&b=2"
    url = "http://artifactory.dev.cmbc.cn:31344/artifactory/api/search/aql"
    body = 'item.find({"repo": {"$eq": "cccbm-docker-preprd-local"}},{"modified": {"$gt": "2021-11-20T00:00:00.00+08：00"}}).include("name","repo","path","modified","original_md5","created_by").sort({"$desc": ["modified"]}).limit(30)'
    get_url_md5(url, body)

if __name__ == '__main__':
    main()
