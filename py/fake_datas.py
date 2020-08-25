#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   fake_datas.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/8  21:40   xguo      1.0         None

'''

from faker import Faker
from pprint import pprint
import profile

def fake_data(num=10):
    f=Faker("zh_CN")
    datas=[]
    while num:
        data = [f.name(),
                f.address(),
                f.phone_number(),
                f.country(),
                f.province(),
                f.city_suffix(),
                f.district(),
                f.street_name(),
                f.street_suffix(),
                f.random_digit(),
                f.random_element(),
                f.random_int(),
                f.random_letter(),
                f.random_number(),
                f.email(),
                f.url(),
                f.user_name(),
                f.ipv4(),
                f.ssn(),
                f.color_name(),
                f.date(),
                # f.geo_coordinate(),
                f.latitude(),
                f.longitude(),
                f.lexify(),
                f.numerify(),
                f.postcode(),
                ]

        datas.append(data)
        num-=1
    return datas

def main():
    d=fake_data()
    print("地址类".center(100, "-"))
    pprint(d)
    print("公司类".ljust(100,'-'))
    print("个人信息类".rjust(100,'*'))


if __name__ == "__main__":
    main()