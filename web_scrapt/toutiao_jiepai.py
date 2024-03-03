#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   toutiao_jiepai.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/4/18 下午 8:28   hello      1.0         获取头条图片 ajax

'''
#requests urllib scrapy pyspider ---- 伪装
#selenium   没有抓不到的数据    慢
#.content   获取二进制数据
#os.path.splitext 获取后缀

# replace   (.*?): (.*?) "$1": "$2"
# auto import package------> alt + enter

import os
from urllib.parse import urlencode

import jsonpath
import requests
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36",
    "Referer": "https://so.toutiao.com/search?keyword=%E8%A1%97%E6%8B%8D&pd=atlas&source=search_subtab_switch&dvpf=pc&aid=4916&page_num=0",
    "Cookie": "n_mh=gzf3l7FBFBHNj74Rhgi-pF6zSGsH_UjCbuL7WvL3LH4; passport_csrf_token=0c181be682b7c2d4b83c1e545e265c1d; sso_uid_tt_ss=b1feee003f9f5c672161fd12c6e88119; toutiao_sso_user_ss=35471d70d8772ddc7f282002b8265c38; ssid_ucp_sso_v1=1.0.0-KDBiMDFhOTJiMDM3NDU5MDY5MWJhYzA1M2RlZmRiOTYwNmJkYWRhZTMKFwjeg-Dlg_SnARD-rpSSBhj2FzgCQO8HGgJsZiIgMzU0NzFkNzBkODc3MmRkYzdmMjgyMDAyYjgyNjVjMzg; uid_tt=b1feee003f9f5c672161fd12c6e88119; uid_tt_ss=b1feee003f9f5c672161fd12c6e88119; sid_tt=35471d70d8772ddc7f282002b8265c38; sessionid=35471d70d8772ddc7f282002b8265c38; sessionid_ss=35471d70d8772ddc7f282002b8265c38; sid_guard=35471d70d8772ddc7f282002b8265c38%7C1648888761%7C5184000%7CWed%2C+01-Jun-2022+08%3A39%3A21+GMT; sid_ucp_v1=1.0.0-KGEzNWJhMmQyYWVjNzNhOTU3MmViZDVjMjczODdhZTUzNmZmYWFkZDEKGQjeg-Dlg_SnARC5l6CSBhj2FyAMOAJA7wcaAmhsIiAzNTQ3MWQ3MGQ4NzcyZGRjN2YyODIwMDJiODI2NWMzOA; ssid_ucp_v1=1.0.0-KGEzNWJhMmQyYWVjNzNhOTU3MmViZDVjMjczODdhZTUzNmZmYWFkZDEKGQjeg-Dlg_SnARC5l6CSBhj2FyAMOAJA7wcaAmhsIiAzNTQ3MWQ3MGQ4NzcyZGRjN2YyODIwMDJiODI2NWMzOA; tt_webid=7052968885016331812; ttwid=1%7CQRye9sIQqc9w_D7nUol1tHx17EHJwvg0qvLjVMveUVs%7C1650284152%7C879ee2b38a267a1073cca97506be10bba813fb5221d98ce07014dd0ff1d62683; odin_tt=f05aac9032a349a74e2888535ff997fbb73bcbb746f9b4f6a9bb4dd06876f6db9d3b8f2f3a16eb2fd3db5ee59d85e26a; _S_DPR=1; _S_IPAD=0; MONITOR_WEB_ID=7052968885016331812; _S_WIN_WH=1920_488"
}

#1. 获取源代码
def get_page_index(keyword, num):
    data = {
        "keyword": keyword,
        "pd": "atlas",
        "source": "search_subtab_switch",
        "dvpf": "pc",
        "aid": "4916",
        "page_num": num,
        "rawJSON": "1",
        "search_id": "2022041820213301015004113727DB5DCB"
    }

    url = "https://so.toutiao.com/search?" + urlencode(data)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return  None

#2. 解析数据
def parse_page_index(html):
    data = json.loads(html)
    json_data = data["rawData"]["data"]
    for item in json_data:
        text = item["text"]
        img = item["img_url"]
        print(img, text)

        # 3. 保存数据
        try:
            with open("./街拍美图/" + text + os.path.splitext(img)[-1], "wb") as f:
                resp = requests.get(img).content
                f.write(resp)
        except OSError as e:
            continue

    # name = jsonpath.jsonpath(data, "$..rawData.data[*].text")
    # url = jsonpath.jsonpath(data, "$..rawData.data[*].img_url")
    # print(name)
    # print(url)

#执行函数
def main(name, num):
    html = get_page_index(name, num)
    # print(html)
    parse_page_index(html)

#函数入口
if __name__ == '__main__':
    name = input("请输入要采集的图片: ")
    for num in range(1, 10):
        main(name, num)
