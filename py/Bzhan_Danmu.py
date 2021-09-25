#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   Bzhan_Danmu.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/5  21:02   xguo      1.0         None

'''
import requests
import time

def message(msg):
    data = {
        'color': '16777215',
        'fontsize': '25',
        'mode': '1',
        'msg': msg,
        'rnd': '1614950147',
        'roomid': '12488643',
        'bubble': '0',
        'csrf_token': 'd993478be623a642e98fe0fd55a52361',
        'csrf': 'd993478be623a642e98fe0fd55a52361'
    }

    return data

def main():
    url = 'https://api.live.bilibili.com/msg/send'
    cookie = {
        'cookie': "_uuid=829BC585-973F-5350-021D-EC6333559FF330802infoc; buvid3=70C17C0F-7BC9-437F-B78F-82E8D2372BC7138376infoc; blackside_state=1; rpdid=|(J|uk~mkl0J'ulm)YY~)JR; CURRENT_FNVAL=80; DedeUserID=442666164; DedeUserID__ckMd5=fb3384b30d0c296e; SESSDATA=d427c8a7%2C1621998701%2C16cd5*b1; bili_jct=d993478be623a642e98fe0fd55a52361; CURRENT_QUALITY=32; bsource=search_baidu; LIVE_BUVID=AUTO2416149492287375; _dfcaptcha=d4f2537b57a438e8c19efb9e89d9be02; PVID=3; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1614949332; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1614949332"
    }

    list_str = ['111','222','666','你很美']
    for str in list_str:
        new_data = message(str)
        result = requests.post(url,cookies=cookie,data=new_data).text
        print(result)
        time.sleep(1)


if __name__ == "__main__":
    main()