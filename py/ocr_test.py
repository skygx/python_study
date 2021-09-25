#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: xguo
@project: python_study
@file: ocr_test.py
@time: 2021/7/25 9:57
"""

import ddddocr

def check_charset(file_path):
    import chardet
    with open(file_path, "rb") as f:
        data = f.read()
        charset = chardet.detect(data)['encoding']

    return charset

def main():
    ocr=ddddocr.DdddOcr()
    # aa = check_charset('../jpg/111.jpg')
    # print(aa)
    with open('../jpg/text.jpg','r',encoding='GBK') as f:
        img_type = f.read()
    res = ocr.classification(img_type)
    print(res)


if __name__ == '__main__':
    main()
