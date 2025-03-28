# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   silicon_myvoice.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/13 上午10:59   hello      1.0         None

'''
import requests
from pathlib import Path
from openai import OpenAI

def upload_voice():
    url = "https://api.siliconflow.cn/v1/uploads/audio/voice"
    headers = {
        "Authorization": "Bearer sk-ujnjhovknhggmlsbhkfwcpjavkzpiubjlkdqsdtxtnvqwvgj" # 从 https://cloud.siliconflow.cn/account/ak 获取
    }
    files = {
        "file": open("D:/project/Pyproject/python_study/gwd/deepseek/silicon/voice.mp3", "rb") # 参考音频文件
    }
    data = {
        "model": "FunAudioLLM/CosyVoice2-0.5B", # 模型名称
        "customName": "test", # 参考音频名称
        "text": "在一无所知中, 梦里的一天结束了，一个新的轮回便会开始" # 参考音频的文字内容
    }

    response = requests.post(url, headers=headers, files=files, data=data)

    print(response.status_code)
    print(response.json())  # 打印响应内容（如果是JSON格式）

def get_voice_list():
    url = "https://api.siliconflow.cn/v1/audio/voice/list"

    headers = {
        "Authorization": "Bearer sk-ujnjhovknhggmlsbhkfwcpjavkzpiubjlkdqsdtxtnvqwvgj"  # 从https://cloud.siliconflow.cn/account/ak获取
    }
    response = requests.get(url, headers=headers)

    print(response.status_code)
    print(response.json)

def delete_voice():
    url = "https://api.siliconflow.cn/v1/audio/voice/deletions"
    headers = {
        "Authorization": "Bearer sk-ujnjhovknhggmlsbhkfwcpjavkzpiubjlkdqsdtxtnvqwvgj",
        "Content-Type": "application/json"
    }
    payload = {
        "uri": "speech:test:cm02pf7az00061413w7kz5qxs:mttkgbyuunvtybnsvbxd"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.status_code)
    print(response.text)  # 打印响应内容

def use_system_voice():
    speech_file_path = Path(__file__).parent / "siliconcloud-generated-speech.mp3"

    client = OpenAI(
        api_key="sk-ujnjhovknhggmlsbhkfwcpjavkzpiubjlkdqsdtxtnvqwvgj",  # 从 https://cloud.siliconflow.cn/account/ak 获取
        base_url="https://api.siliconflow.cn/v1"
    )

    with client.audio.speech.with_streaming_response.create(
            model="FunAudioLLM/CosyVoice2-0.5B",  # 支持 fishaudio / GPT-SoVITS / CosyVoice2-0.5B 系列模型
            voice="FunAudioLLM/CosyVoice2-0.5B:alex",  # 系统预置音色
            # 用户输入信息
            input="你能用高兴的情感说吗？<|endofprompt|>今天真是太开心了，马上要放假了！I'm so happy, Spring Festival is coming!",
            response_format="mp3"  # 支持 mp3, wav, pcm, opus 格式
    ) as response:
        response.stream_to_file(speech_file_path)
        print(f"Speech file saved to {speech_file_path}")

def use_custom_voice():
    speech_file_path = Path(__file__).parent / "siliconcloud-custom-speech.mp3"

    client = OpenAI(
        api_key="sk-ujnjhovknhggmlsbhkfwcpjavkzpiubjlkdqsdtxtnvqwvgj",  # 从 https://cloud.siliconflow.cn/account/ak 获取
        base_url="https://api.siliconflow.cn/v1"
    )

    with client.audio.speech.with_streaming_response.create(
            model="FunAudioLLM/CosyVoice2-0.5B",  # 支持 fishaudio / GPT-SoVITS / CosyVoice2-0.5B 系列模型
            voice="speech:test:bq4j4y297g:bcpcopnsudkybqdbkigy",  # 用户上传音色名称，参考
            # 用户输入信息
            input=" 请问你能模仿粤语的口音吗？< |endofprompt| >多保重，早休息。",
            response_format="mp3"
    ) as response:
        response.stream_to_file(speech_file_path)
        print(f"Speech file saved to {speech_file_path}")

if __name__ == '__main__':
    # upload_voice()
    # get_voice_list()
    # delete_voice()
    use_system_voice()
    # use_custom_voice()
    print("ok")
