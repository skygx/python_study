# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   img_convert.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/12/8 上午10:11   hello      1.0         None

'''
from PIL import Image
import os


def webp_to_jpg(input_path, output_path):
    image = Image.open(input_path)
    rgb_image = image.convert("RGB")
    rgb_image.save(output_path, "JPEG")
    print(f"Converted {input_path} to {output_path}")

def jpg_to_webp(input_path, output_path):
    image = Image.open(input_path)
    webp_image = image.convert("RGBA")
    webp_image.save(output_path, "WEBP")
    print(f"Converted {input_path} to {output_path}")

if __name__ == '__main__':
    for file in os.listdir():
        if file.endswith(".webp"):
            input_path = file
            output_path = file.replace(".webp", ".jpg")
            webp_to_jpg(input_path, output_path)
        elif file.endswith(".jpg"):
            input_path = file
            output_path = file.replace(".jpg", ".webp")
            jpg_to_webp(input_path, output_path)
        else:
            continue
            print("文件类型错误")
