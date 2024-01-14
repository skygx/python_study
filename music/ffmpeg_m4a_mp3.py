#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   ffmpeg_m4a_mp3.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/7/17 下午 4:50   hello      1.0         None

'''

import os

m4a_path = "C:/Users/Administrator/Downloads/小学英语四年级下册/"  #m4a文件所在文件夹

m4a_file = os.listdir(m4a_path)
print(m4a_path)
print('D:/Program Files (x86)/ffmpeg/bin/ffmpeg -i ')
for i, m4a in enumerate(m4a_file):
    # print(m4a[:-4])
    if m4a[-3:] == 'm4a':
        print(m4a[:-4]+".mp3")
        os.system('D:/Program Files (x86)/ffmpeg/bin/ffmpeg -i ' + m4a_path + m4a + " " + m4a_path + str(m4a[:-4]) + ".mp3" )
