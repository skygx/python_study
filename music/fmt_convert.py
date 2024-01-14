#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   fmt_convert.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/7/17 下午 4:37   hello      1.0         None

'''

from pydub import AudioSegment
import os
from os import path

def trans_mp3_to_other(filepath, hz):
    song = AudioSegment.from_mp3(filepath)
    song.export(filepath[:-3] + str(hz), format=str(hz))


def trans_wav_to_other(filepath, hz):
    song = AudioSegment.from_wav(filepath)
    song.export(filepath[:-3] + str(hz), format=str(hz))


def trans_ogg_to_other(filepath, hz):
    song = AudioSegment.from_ogg(filepath)
    song.export(filepath[:-3] + str(hz), format=str(hz))


def trans_flac_to_other(filepath, hz):
    song = AudioSegment.from_file(filepath)
    song.export(filepath[:-3] + str(hz), format=str(hz))


def trans_m4a_to_other(filepath, hz):
    song = AudioSegment.from_file(filepath)
    song.export(filepath[:-3] + str(hz), format=str(hz))


# 参数1：音频路径， 参数2：转换后的格式
# trans_m4a_to_other('D:\project\Pyproject\python_study\music\Word List.m4a', "MP3")
def main():
    m4a_path = "C:/Users/Administrator/Downloads/小学英语四年级下册/"  # m4a文件所在文件夹
    m4a_file = os.listdir(m4a_path)
    for m4a in m4a_file:
        if m4a[-3:] == 'm4a':
            #print(path.join(m4a_path,m4a))
            trans_m4a_to_other(path.join(m4a_path,m4a),"mp3")

if __name__ == '__main__':
    main()
