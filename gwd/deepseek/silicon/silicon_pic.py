# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   silicon_pic.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/11 下午4:49   hello      1.0         None

'''
import requests
import json
from PIL import Image
import io

# 创建一个POST请求
def get_image():
    url = "https://api.siliconflow.cn/v1/images/generations"

    payload = {
        "model": "Kwai-Kolors/Kolors",
        "prompt": "an island near sea, with seagulls, moon shining over the sea, light house, boats int he background, fish flying over the sea",
        "negative_prompt": "<string>",
        "image_size": "1024x1024",
        "batch_size": 1,
        "seed": 4999999999,
        "num_inference_steps": 20,
        "guidance_scale": 7.5,
    #    "image": "data:image/webp;base64, XXX"
    }
    headers = {
        "Authorization": "Bearer sk-ujnjhovknhggmlsbhkfwcpjavkzpiubjlkdqsdtxtnvqwvgj",
        "Content-Type": "application/json"
    }

    response = json.loads(requests.request("POST", url, json=payload, headers=headers).text)
    url = response["images"][0]["url"]
    print(url)
    return url


def save_image_from_url(url, save_path):
    try:
        # 发送HTTP请求获取图片内容
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功

        # 使用PIL库打开图片
        image = Image.open(io.BytesIO(response.content))

        # 保存图片到指定路径
        image.save(save_path)
        print(f"图片已成功保存到 {save_path}")

    except requests.exceptions.RequestException as e:
        print(f"请求错误: {e}")
    except IOError as e:
        print(f"IO错误: {e}")

# 示例URL和保存路径
url = get_image()
save_path = "../image.jpg"
