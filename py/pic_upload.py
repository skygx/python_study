#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   pic_upload.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/12/19 下午 3:08   hello      1.0         None

'''
import requests
import json
url = "https://pics.sunbangyan.cn/application/upload.php"
files = {
    'file': open(input("输入文件名或者目录:"), 'rb')
}
if files:
    response = requests.post(url, files=files) #进行post请求并提交文件
    print(response.text,"\n\n图片链接："+json.loads(response.text)["url"])
