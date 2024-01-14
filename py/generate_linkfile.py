#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   generate_linkfile.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/7/27 上午 9:24   hello      1.0         None

'''
import os

def generate_linkfile(file,num):


    f=open(file,"w+")
    for i in range(1,num):
        line=f"https://psv119-2.crazycloud.ru/videos/-203043145/456245628/360/seg-{i}-v1-a1.ts?extra=rVWceBLNtGXJnVvwsA2wSQ&extra_info=cAlN4PIgl5tWhuUBiQA8XV-\n"
        f.write(line)
    f.close()
    print("linkfile generate done!")

if __name__ == '__main__':
    num=5+1
    dirpath=u"D:\\迅雷下载\\aaa\\download\\111\\"
    file=dirpath+"111.txt"

    if os.path.isfile(file):
        os.remove(file)
        generate_linkfile(file,num)
    else:
        generate_linkfile(file,num)
