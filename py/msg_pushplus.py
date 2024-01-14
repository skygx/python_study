#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   msg_pushplus.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/10/2 下午 1:09   hello      1.0         None

'''

import requests
# Python源码资料电子书领取群 279199867

def send_wechat(msg):
    token = '269d67cc19ef467987ae3c7fc4b54c69'#前边复制到那个token
    title = 'hello world'
    content = msg
    template = 'html'
    topic='001'
    # url = f"https://www.pushplus.plus/send?token={token}&title={title}&content={content}&template={template}"
    url = f"https://www.pushplus.plus/send?token={token}&title={title}&content={content}&template={template}&topic={topic}"
    print(url)
    r = requests.get(url=url)
    print(r.text)

if __name__ == '__main__':
    msg = 'hello world'
    send_wechat(msg)
