#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   emotion_reg.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/26  11:13   xguo      1.0         None

'''

import paddlehub as hub

def main():
    senta=hub.Module(name='senta_lstm')
    sentence = ['你真美','你真丑','我好难过','我不开心','这个游戏好好玩','什么垃圾游戏','我喜欢你','世界真大','天堂还是地狱']
    results = senta.sentiment_classify(data={"text":sentence})
    for result in results:
        print(result)


if __name__ == "__main__":
    main()