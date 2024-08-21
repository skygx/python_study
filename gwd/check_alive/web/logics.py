# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   logics.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/6/26 上午8:55   hello      1.0         None

'''

import requests
import copy
from models import db,Url
from config import *
from models import app
from flask_apscheduler import APScheduler
from functools import lru_cache

scheduler = APScheduler()
scheduler.init_app(app)

def check_url_alive(url,search_string):
    try:
        response = requests.get(url, timeout=TIMEOUT)
        if response.status_code in [200,301] :
            # return True
            return search_string in response.text
        else:
            return False
    except requests.exceptions.RequestException:
        return False

# 获取文件中的url列表
def get_url_list(file_path):    # 获取配置文件中的url列表
    dict_url = {}
    url_list = []
    with open(file_path, 'r') as f:
        content = f.readlines()
    for line in content:
        name,ip,port,uri,key = line.split()
        url = 'http://'+ip+':'+port+'/'+uri
        # print(url)
        dict_url["url"] = url
        dict_url["name"] = name
        dict_url["status"] = check_url_alive(url,key)
        print(dict_url)
        url_list.append(copy.deepcopy(dict_url))
    # print(url_list)
    return url_list

def get_url_status():    # 获取数据库中的url的状态
    dict_url = {}
    url_list = []
    urls = Url()
    items = urls.read_all_item()
    for item in items:
        name = item.name
        ip = item.ip
        port = item.port
        uri = item.url
        key = item.key
        url = 'http://'+ip+':'+port+'/'+uri
        dict_url["url"] = url
        dict_url["name"] = name
        dict_url["status"] = check_url_alive(url,key)
        # print(url)
        url_list.append(copy.deepcopy(dict_url))
    return url_list

# @lru_cache(maxsize=128)
def get_url_status_from_env(env_name):
    dict_url = {}
    url_list = []
    urls = Url()
    items = urls.read_item_by_env(env_name)
    for item in items:
        name = item.name
        ip = item.ip
        port = item.port
        uri = item.url
        key = item.key
        status = item.status
        url = 'http://' + ip + ':' + port + '/' + uri
        dict_url["url"] = url
        dict_url["name"] = name
        # dict_url["status"] = check_url_alive(url, key)
        dict_url["status"] = status
        # print(url)
        url_list.append(copy.deepcopy(dict_url))
    return url_list


# @lru_cache(maxsize=128)
def get_all_message():
    dict_url = {}
    url_list = []
    urls = Url()
    items = urls.read_all_item()
    for item in items:
        # print(item.id)
        dict_url["id"] = item.id
        dict_url["name"] = item.name
        dict_url["env"] = item.env
        dict_url["ip"] = item.ip
        dict_url["port"] = item.port
        dict_url["url"] = item.url
        dict_url["key"] = item.key
        dict_url["location"] = item.location
        dict_url["desc"] = item.desc
        url_list.append(copy.deepcopy(dict_url))
    return url_list

def clear_cache():
    get_all_message.cache_clear()

def export_data(ids):
    dict_url = {}
    url_list = []
    urls = Url()
    if ids:
        items = urls.read_item_by_ids(ids)
    else:
        items = urls.read_all_item()
    for item in items:
        dict_url["id"] = item.id
        dict_url["name"] = item.name
        dict_url["env"] = item.env
        dict_url["ip"] = item.ip
        dict_url["port"] = item.port
        dict_url["url"] = item.url
        dict_url["key"] = item.key
        dict_url["location"] = item.location
        dict_url["desc"] = item.desc
        dict_url["status"] = item.status
        url_list.append(copy.deepcopy(dict_url))
    # print(url_list)
    return url_list
def get_item_message_by_id(id):
    dict_url = {}
    url_list = []
    url = Url()
    item = url.read_item_by_id(id)
    dict_url["id"] = item.id
    dict_url["name"] = item.name
    dict_url["env"] = item.env
    dict_url["ip"] = item.ip
    dict_url["port"] = item.port
    dict_url["url"] = item.url
    dict_url["key"] = item.key
    dict_url["location"] = item.location
    dict_url["desc"] = item.desc
   # dict_url["status"] = check_url_alive()
   # url_list.append(copy.deepcopy(dict_url))
    return dict_url

def insert_data_to_db(form):
    name = form.get('name')
    env = form.get('env')
    location = form.get('location')
    ip = form.get('ip')
    port = form.get('port')
    url = str(form.get('url'))
    key = form.get('key')
    desc = form.get('desc')
    print(name, env, location, ip, port, url, key, desc)
    localurl = Url()
    try:
        localurl.create_item(name=name, env=env, location=location, ip=ip, port=port, url=url, key=key, desc=desc)
        # localurl.alter_id()
        return True
    except Exception as e:
        print(e)
        return False

# @lru_cache(maxsize=128)
@scheduler.task('interval', id='update_status', seconds=5, max_instances=5)
def update_status():
    url = Url()
    with scheduler.app.app_context():
        items = url.read_all_item()
        for item in items:
            uri = 'http://' + item.ip + ':' + item.port + '/' + item.url
            status = check_url_alive(uri, item.key)
            item.status = status
            with scheduler.app.app_context():
                try:
                    db.session.commit()
                except Exception as e:
                    db.session.rollback()
                finally:
                    db.session.close()
                    # db.session.remove()

# 未加定时任务的更新状态函数
# def update_old_status():
#     url = Url()
#     if url.is_status_null():
#         items = url.read_all_item()
#         for item in items:
#             uri = 'http://' + item.ip + ':' + item.port + '/' + item.url
#             status = check_url_alive(uri, item.key)
#             item.status = status
#             try:
#                 db.session.commit()
#                 print(f'{item.id} is status {status} update')
#             except Exception as e:
#                 print(e)
#                 db.session.rollback()
#     else:
#         print('status is not null')
#         pass


if __name__ == '__main__':
    # print(get_url_status_from_env('ver'))
    print(update_status())
