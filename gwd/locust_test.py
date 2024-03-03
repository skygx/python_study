#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   locust_test.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/1/12 下午 2:38   hello      1.0         None

'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from locust import HttpUser, TaskSet, task
# 定义用户行为类
class UserBehavior(TaskSet):
    @task  # 任务项
    def test_login(self):
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        url = '/file'
        res = self.client.get(url,headers=header, verify=False)
        #断言方式一
        #assert res.status_code == 200
        #断言方式二
        if res.status_code == 200:
            print('登陆成功！')
        else:
            print('登陆失败！')

    @task  # 任务项
    def test_bksvr(self):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        url = '/bk_svr'
        res = self.client.get(url, headers=header, verify=False)

    @task  # 任务项
    def test_bksvr1(self):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        url = '/bk_svr1'
        res = self.client.get(url, headers=header, verify=False)

    @task  # 任务项
    def test_gateway(self):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        url = '/gateway'
        res = self.client.get(url, headers=header, verify=False)

    @task  # 任务项
    def test_gateway1(self):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        url = '/gateway1'
        res = self.client.get(url, headers=header, verify=False)


class WebSiteUser(HttpUser):
    tasks = [UserBehavior]
    #host = "https://www.cnblogs.com"
    max_wait = 5000
    min_wait = 1000

if __name__ == "__main__":
    import os
    os.system("locust -f locust_test.py --host=http://192.168.226.20:88")#这样写可以直接运行文件，也可以命令调用文件
    # os.system("locust -f locust_test.py --host=http://localhost:8080")#这样写可以直接运行文件，也可以命令调用文件
