# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   silicon_voice.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/13 上午10:56   hello      1.0         None

'''
import requests
import json

url = "https://api.siliconflow.cn/v1/uploads/audio/voice"
headers = {
    "Authorization": "Bearer sk-ujnjhovknhggmlsbhkfwcpjavkzpiubjlkdqsdtxtnvqwvgj", # 从 https://cloud.siliconflow.cn/account/ak 获取
    "Content-Type": "application/json"
}
data = {
    "model": "FunAudioLLM/CosyVoice2-0.5B", # 模型名称
    "customName": "your-voice-name", # 用户自定义的音频名称
    "audio": "data:audio/mpeg;base64,SUQzBAAAAAAAIlRTU0UAAAAOAAADTGF2ZjYxLjcuMTAwAAAAAAAAAAAAAAD/40DAAAAAAAAAAAAASW5mbwAAAA8AAAAWAAAJywAfHx8fKioqKio1NTU1Pz8/Pz9KSkpKVVVVVVVfX19fampqamp1dXV1f39/f3+KioqKlZWVlZWfn5+fn6qqqqq1tbW1tb+/v7/KysrKytXV1dXf39/f3+rq6ur19fX19f////", # 参考音频的 base64 编码
    "text": "在一无所知中, 梦里的一天结束了，一个新的轮回便会开始" # 参考音频的文字内容
}

response = requests.post(url, headers=headers, data=json.dumps(data))

# 打印响应状态码和响应内容
print(response.status_code)
print(response.json())  # 如果响应是 JSON 格式
