#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   pdf_dump.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/27  15:51   xguo      1.0         None

'''

import PyPDF2
import pdfplumber

def main():
    with pdfplumber.open(r'C:\project\python_study\pdf\Python.pdf') as p:
        page = p.pages[2]
        print(page.extract_text())

if __name__ == "__main__":
    main()