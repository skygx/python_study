#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   generate_faker_log.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/11/24 下午 3:50   hello      1.0         None
'$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';
'''
from faker import Faker
from faker.providers import internet
from faker import Factory

print(dir(Faker))

faker_data = Faker(locale='zh_CN')

def generate_log(num):
    ip=faker_data.ipv4()
    user=faker_data.user_name()
    time=faker_data.date_time()
    request=faker_data.http_method()
    # status=faker_data.status()
    uri_path=faker_data.uri_path()
    user_agent=faker_data.user_agent()
    data=f"{ip} {user} [{time}] {request}  {uri_path} {user_agent}"
    return data

def main():
    d=generate_log(2)
    print(d)

if __name__ == '__main__':
    main()
