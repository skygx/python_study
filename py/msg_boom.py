#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   msg_boom.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/26  12:39   xguo      1.0         None

'''
from pynput import mouse

def main():
    m_mouse=mouse.Controller()
    print(m_mouse.position)


if __name__ == "__main__":
    main()