#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   inventory.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/2/11 下午 12:53   hello      1.0         None

'''
import os
import sys
import argparse

try:
    import json
except ImportError:
    import simplejson as json

class Inventory(object):
    def __init__(self):
        self.inventory={}
        self.read_cli_args()
        if self.args.list:
            self.inventory = self.get_hosts()
        elif self.args.host:
            self.inventory = self.empty_inventory()
        else:
            self.inventory = self.empty_inventory()
        print(json.dumps(self.inventory))


    def get_hosts(self):
        # 这里可以从数据库或者其他地方获取主机信息
        hosts = {
            'webservers': {
                'hosts': ['web1', 'web2'],
                'vars': {
                    'ansible_ssh_user': 'root',
                    'ansible_ssh_pass': '123456'
                }
            },
            'dbservers': {
                'hosts': ['db1', 'db2'],
                'vars': {
                    'ansible_ssh_user': 'root',
                    'ansible_ssh_pass': '123456'
                }
            },
            '_meta': {
                'hostvars': {
                    '192.168.28.71': {
                        'host_specific_var': 'foo'
                    },
                    '192.168.28.72': {
                        'host_specific_var': 'bar'
                    }
                }
            }
        }
        return hosts

    def empty_inventory(self):
        return {'_meta': {'hostvars': {}}}

    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action='store_true')
        parser.add_argument('--host', action='store')
        self.args = parser.parse_args()

if __name__ == '__main__':
    # hosts = get_hosts()
    # print(json.dumps(hosts, indent=4))
    Inventory()
