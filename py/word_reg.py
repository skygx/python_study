#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   word_reg.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/26  15:57   xguo      1.0         None

'''

import pytesseract
from PIL import Image
# from imageio import imread


def main():
    # img = imread('text1.jpg')
    img = Image.open('text1.jpg')
    img.load()
    print(img)
    text = pytesseract.image_to_string(img)
    print(text)

if __name__ == "__main__":
    main()