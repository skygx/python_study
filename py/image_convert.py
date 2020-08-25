#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   image_convert.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/18  19:16   xguo      1.0         None

'''

from PIL import Image
import pytesseract


def main():
    # 上面都是导包，只需要下面这一行就能实现图片文字识别
    # text=Image.open('../jpg/te.jpg')
    text = pytesseract.image_to_string(Image.open('../jpg/yjs.jpg'), lang='chi_sim')  # 设置为中文文字的识别
    print(text)
    with open('../txt/yjs.txt', 'w') as f:
        f.write(text)

if __name__ == "__main__":
    main()