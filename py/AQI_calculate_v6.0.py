#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   AQI_calculate_v1.0.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/5 10:24   xguo      1.0         AQI计算
2019/3/5 10:24   xguo      2.0         读取json文件
2019/3/7 15:00   xguo      3.0         输出到csv格式文件
2019/3/7 15:30   xguo      4.0         添加判断文件是csv还是json
2019/3/8 9:00    xguo      5.0         实现爬虫抓取pm25.in实时数据
2019/3/9 11:10   xguo      6.0         通过bs4获取网页指定信息，保存成csv格式文件
'''

from bs4 import BeautifulSoup
import requests
import csv

def get_city_url(url):
    session = requests.Session()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}
    r = session.get(url, headers=headers,timeout=500)
    city_list = []
    soup = BeautifulSoup(r.text,'lxml')
    div_city = soup.find_all('div',{'class':'bottom'})[1]
    city_info_list = div_city.find_all('a')

    for city in city_info_list:
        city_name = city.text
        city_link = city['href'][1:]
        city_list.append((city_name,city_link))
    return city_list

def get_city_info(url):
    # print(url)
    session = requests.Session()

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}
    r = session.get(url,headers=headers,timeout=500)
    # r.headers(header)
    api_list = []
    soup = BeautifulSoup(r.text,'lxml')
    div_data = soup.find_all('div',{'class':'span1'})

    for data in div_data[:8]:
        aqi_value = data.find('div',{'class':'value'}).text.strip()
        caption = data.find('div',{'class':'caption'}).text.strip()
        api_list.append(aqi_value)

    return api_list

def main():
    url = 'http://pm25.in/'
    city_list = get_city_url(url)
    # print(city_list)
    f = open('city_aqi.csv','w',encoding='utf-8')
    writer = csv.writer(f)
    header = ['City','AQI','PM2.5/1h','PM10/1h','CO/1h','NO2/1h','O3/1h','O3/8h','SO2/1h']
    writer.writerow(header)
    for i,city in enumerate(city_list):
        city_name = city[0]
        aqi = get_city_info(url + city[1])
        print('已处理{}条，总共{}条'.format(i + 1, len(city_list)))
        # if (i+1)%10 == 0:
        #     print('已处理{}条，总共{}条'.format(i+1,len(city_list)))
        row = [city_name] + aqi
        writer.writerow(row)
        f.flush()
    f.close()

if __name__ == "__main__":
    main()