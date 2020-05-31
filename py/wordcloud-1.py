#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   wordcloud-1.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/26  10:13   xguo      1.0         None

'''

from wordcloud import WordCloud
import jieba
from imageio import imread

def main():
    mk=imread('C:\project\python_study\china.jpg')
    wc=WordCloud(width=800,height=600,background_color="white",font_path="C:\Windows\Fonts\simfang.ttf",mask=mk)
    # wc.generate('Do not go gentle into that good night')
    with open('C:\project\python_study\现代日本.txt',encoding='utf-8') as f:
        t=f.read()
    txt=" ".join(jieba.lcut(t))
    wc.generate(txt)
    wc.to_file('wchy.jpg')


if __name__ == "__main__":
    main()