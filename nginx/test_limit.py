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
    def test_root(self):
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        url = '/'
        res = self.client.get(url,headers=header, verify=False)

    @task  # 任务项
    def test_conn1(self):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        url = '/conn_1/'
        res = self.client.get(url, headers=header, verify=False)

    @task  # 任务项
    def test_conn5(self):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        url = '/conn_5/'
        res = self.client.get(url, headers=header, verify=False)

    @task  # 任务项
    def test_conn10(self):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        url = '/conn_10/'
        res = self.client.get(url, headers=header, verify=False)

    @task  # 任务项
    def test_rate10B(self):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        url = '/rate_10B/'
        res = self.client.get(url, headers=header, verify=False)

    @task  # 任务项
    def test_rate50B(self):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        url = '/rate_50B/'
        res = self.client.get(url, headers=header, verify=False)
    @task  # 任务项
    def test_rate4K(self):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        url = '/rate_4KB/'
        res = self.client.get(url, headers=header, verify=False)
    @task  # 任务项
    def test_rate(self):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        url = '/rate/'
        res = self.client.get(url, headers=header, verify=False)

    @task  # 任务项
    def test_req10(self):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        url = '/req_1_0/'
        res = self.client.get(url, headers=header, verify=False)

    @task  # 任务项
    def test_req15(self):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        url = '/req_1_5/'
        res = self.client.get(url, headers=header, verify=False)

    @task  # 任务项
    def test_req15nodelay(self):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        url = '/req_1_5_nodelay/'
        res = self.client.get(url, headers=header, verify=False)

    @task  # 任务项
    def test_download(self):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        url = '/download/'
        res = self.client.get(url, headers=header, verify=False)

class WebSiteUser(HttpUser):
    tasks = [UserBehavior]
    #host = "https://www.cnblogs.com"
    max_wait = 5000
    min_wait = 1000

if __name__ == "__main__":
    import os
    os.system("locust -f test_limit.py --host=http://192.168.226.20:89")#这样写可以直接运行文件，也可以命令调用文件

