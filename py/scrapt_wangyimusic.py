#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   scrapt_wangyimusic.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/9/12  20:24   xguo      1.0         None

'''
# 导入框架
import requests
from lxml import etree
import os

def main():
    # 1.确定url地址
    # url = 'https://m10.music.126.net/20200912205559/9c1fcc124e6b206c3008e50285c9aa3d/yyaac/obj/wonDkMOGw6XDiTHCmMOi/3921951005/7342/705d/8921/615d1ed6f074db3b3373531906a9ad94.m4a'
    # #2.请求 (request)  content(图片，音频，视频) text
    # mp4 = requests.get(url).content
    # #3.删选数据 (xpath,正则)
    # //a[contains(@href,"song?")]/@href
    # //a[contains(@href,"song?")]/@text()
    #
    #
    # #4.保存数据
    # with open('../music/yinp.m4a','wb') as file:
    #     file.write(mp4)

    # url = 'https://link.hhtjim.com/163/1477365923.mp3'

    url = 'https://music.163.com/#/playlist?id=3212113629'
    base_url = 'https://music.163.com/#/playlist?id='
    result = requests.get(url).text
    # print(result)

    dom = etree.HTML(result)
    ids_names = dom.xpath('//a[contains(@href,"song?")]/text()')
    ids_songs = dom.xpath('//a[contains(@href,"song?")]/@href')

    print(ids_names)
    print(ids_songs)

    for ids_name,ids_song in zip(ids_names,ids_songs):
    # for ids_song in ids_songs:
        # print(ids_name)
        # print(ids_song)
        count_id = ids_song.strip('/song?id=')
        # print(count_id)

        if('$' in count_id) == False:
            song_url = base_url + count_id + '.mp3'
            print(song_url)
            mp3 = requests.get(song_url).content

            path = '../music'
            if not os.path.exists(path):
                os.makedirs(path)

            with open(f'{path}/{ids_name}.mp3','wb') as file:
                file.write(mp3)


if __name__ == "__main__":
    main()