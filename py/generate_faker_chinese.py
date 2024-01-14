#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   generate_faker_chinese.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/11/21 下午 5:21   hello      1.0         None

'''

from faker import Faker
from faker.providers import internet

faker_data = Faker(locale='zh_CN')

def generate_data(num,sep):
    datas=[]
    for i in range(num):
        # 模拟姓名
        female=faker_data.name_female()
        male=faker_data.name_male()
        # 模拟身份证号码 18-50岁
        ssn=faker_data.ssn(min_age=18, max_age=50)
        # 模拟手机号码
        phone=faker_data.phone_number()
        # 模拟银行卡号
        card=faker_data.credit_card_number()
        # 模拟IP地址
        ip=faker_data.ipv4_private()
        # 模拟公司名称
        company=faker_data.company()
        # 模拟城市位置
        city=faker_data.city()
        # 模拟具体街道
        address=faker_data.address()
        # 模拟个人配置信息
        profile=faker_data.profile()
        # 模拟邮政编码
        post=faker_data.postcode()
        # 模拟随机uri地址
        uri=faker_data.uri()
        data=[female,male,ssn,phone,card,ip,company,city,address,profile,post,uri]
        dtr=[str(i) for i in data]
        d=f"{sep}".join(dtr)
        datas.append(d)
    print(datas)
    return datas

def main():
    datas=generate_data(100,"|")
    with open('D:/project/Pyproject/python_study/txt/faker.txt', 'w', encoding='utf-8') as f:
        for i in range(len(datas)):
            print(datas[i])
            f.writelines(str(datas[i]))
            f.writelines(str("\n"))

if __name__ == '__main__':
    main()
