#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   msg_boom-1.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/26  12:40   xguo      1.0         None

'''

import time
from pynput import mouse, keyboard

def main():
    time.sleep(5)
    m_mouse=mouse.Controller()
    m_keyboard=keyboard.Controller()
    m_mouse.position=(850, 670)
    m_mouse.click(mouse.Button.left)

    while(True):
        m_keyboard.type('臭屁老婆！！')
        m_keyboard.press(keyboard.Key.enter)
        m_keyboard.release(keyboard.Key.enter)
        time.sleep(0.5)


if __name__ == "__main__":
    main()