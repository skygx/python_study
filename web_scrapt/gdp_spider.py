#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   gdp_spider.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/3/23 下午 8:33   hello      1.0         None

'''

import requests
import parsel
import pandas as pd

class Spider(object):
    def __init__(self):
        self.data_url = "http://gdp.gotohui.com/word"
        self.header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36",
            "cookie": "Hm_lvt_bb16892ab0558b208105b4d832832ee2=1648038712; whatsnssid = 3e472d59f46bd9bc; whatsnslastrefresh=1; Hm_lpvt_bb16892ab0558b208105b4d832832ee2=1648041596"
        }

    def get_page_index(self):
        response = requests.get(url=self.data_url,headers=self.header)

        if response.status_code == 200:
            return response.text
        else:
            return None

    def get_data_url_index(self,html):
        workbook = pd.DataFrame()
        select = parsel.Selector(html)
        data_list = select.xpath('//div[@class="recommend"]/div[@class="list-inline div-country agray"]/a')
        wr = pd.ExcelWriter('gdp.xlsx')
        for data in data_list:
            title = data.xpath("./text()").get()
            workbook.to_excel(wr,sheet_name=title,index=None)
            href = data.xpath("./@href").get()
            url = "https://gdp.gotohui.com"+str(href)
            dt = pd.DataFrame(self.parse_page_index(url))
            print(title,url)
            dt.to_excel(wr,sheet_name=title,index=None)
        wr.save()
        wr.close()
        print("data spider done!!")

    def parse_page_index(self,url):
        response = requests.get(url=url,headers=self.header).text
        select = parsel.Selector(response)
        data_list = select.xpath('//table[@class="ntable table-striped table-hover"]/tr')
        list=[]
        for data in data_list:
            td1 = data.xpath("./td[1]/text()").get()
            td2 = data.xpath("./td[2]/text()").get()
            td3 = data.xpath("./td[3]/text()").get()
            td4 = data.xpath("./td[4]/text()").get()
            d = {
                "时间(年)": td1,
                "GDP(美元)": td2,
                "占世界比例(%)": td3,
                "人均GDP(美元)": td4
            }
            list.append(d)

        return list

    def run(self):
        html = self.get_page_index()
        # print(html)
        self.get_data_url_index(html)

if __name__ == '__main__':
    spider=Spider()
    spider.run()

