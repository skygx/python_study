#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   guoqing_touxiang.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/10/2 上午 11:11   hello      1.0         None

'''

from PIL import Image

# 读取图片
guoqi = Image.open('../png/m_五星红旗.png')
touxiang = Image.open('../png/m_郭欣.png').convert("RGBA")

# 获取国旗的尺寸
x,y = guoqi.size
print(x,y)
# 根据需求，设置左上角坐标和右下角坐标（截取的是正方形）
# quyu = guoqi.crop((262,100, y+62,y-100))

# 获取头像的尺寸
w,h = touxiang.size
print(w,h)
quyu = guoqi.crop((0,0, w,h))
# quyu.show()

# 将区域尺寸重置为头像的尺寸
quyu = quyu.resize((w,h))
# quyu.show()
# 透明渐变设置
for i in range(w):
    for j in range(h):
        color = quyu.getpixel((i, j))
        alpha = 255-i//3
        if alpha < 0:
            alpha=0
        color = color[:-1] + (alpha, )
        quyu.putpixel((i, j), color)

# 粘贴到头像并保存
touxiang.paste(quyu,(0,0),quyu)
# touxiang.show()
touxiang.save('../png/五星红旗半透明渐变头像.png')
