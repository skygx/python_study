# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   img_base64.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/12 下午5:54   hello      1.0         None

'''
from PIL import Image
import io
import base64
def convert_image_to_webp_base64(input_image_path):
    try:
        with Image.open(input_image_path) as img:
            byte_arr = io.BytesIO()
            img.save(byte_arr, format='webp')
            byte_arr = byte_arr.getvalue()
            base64_str = base64.b64encode(byte_arr).decode('utf-8')
            return base64_str
    except IOError:
        print(f"Error: Unable to open or convert the image {input_image_path}")
        return None

input_image_path= '../image.jpg'

base64_image=convert_image_to_webp_base64(input_image_path)
print(base64_image)
