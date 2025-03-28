# /usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @Project :   python_study
    @File    :   zabbix_api1.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/10/29 下午4:39   hello      1.0         None

"""

import requests
import json

class Zabbix:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.session = requests.Session()
        self.host = "http://192.168.226.20:8091"
        # self.url = self.host + "/zabbix/api_jsonrpc.php"
        self.url = self.host + "/api_jsonrpc.php"
        self.login()

    def login(self):
        params = {
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": self.user,
                "password": self.password
            },
            "id": 1,
            "auth": None
        }

        # print(json.dumps(params))
        r = self.session.post(self.url, json=params, verify=False, timeout=10, headers={"Content-Type": "application/json-rpc"})
        self.auth = r.json()["result"]
        print(self.auth)

    def get_problems(self):
        params = {
            "jsonrpc": "2.0",
            "method": "problem.get",
            "params": {
                "output": [""]
            }
            ,
            "id": 1,
            "auth": self.auth
        }
        r = self.session.post(self.url, json=params)
        print(r.json())
        return r.json()

    def get_group(self):
        params = {
            "jsonrpc": "2.0",
           "method": "hostgroup.get",
            "params": {
                "output": "extend",
                "sortfield": ["name"],
                "real_hosts": True
            },
            "id": 1,
            "auth": self.auth
        }
        r = self.session.post(self.url, json=params)
        print(r.json())
        return r.json()

    def get_host(self):
        params = {
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output": ["host"],
                "selectInventory": [
                    "os"
                ],
                "searchInventory": {
                    "os": "Linux"
                }
            },
            "id": 1,
            "auth": self.auth
        }
        r = self.session.post(self.url, json=params)
        print(r.json())
        return r.json()

    def get_alert(self):
        params = {
            "jsonrpc": "2.0",
           "method": "alert.get",
            "params": {
                "output": "extend",
                "sortfield": ["clock"],
                "sortorder": "DESC",
                "limit": 10,
                "select_acknowledges": "extend",
                "select_items": "extend",
                "select_triggers": "extend"
            },

            "id": 1,
            "auth": self.auth
        }
        r = self.session.post(self.url, json=params)
        print(r.json())
        return r.json()

    def get_trigger(self):
        params = {
            "jsonrpc": "2.0",
            "method": "trigger.get",
            "params": {
                "output": "extend",
                "sortfield": ["lastchange"],
                "sortorder": "DESC",
                "selectHosts": ["name"],
                "selectItems": "extend",
                "limit": 10,

            },
            "id": 1,
            "auth": self.auth
        }
        r = self.session.post(self.url, json=params)
        print(r.json())
        return r.json()

    def get_template(self):
        params = {
            "jsonrpc": "2.0",
            "method": "template.get",
            "params": {
                "output": "extend"
            },
            "id": 1,
            "auth": self.auth
        }
        r = self.session.post(self.url, json=params)
        print(r.json())
        return r.json()
    def get_item(self):
        params = {
            "jsonrpc": "2.0",
            "method": "item.get",
            "params": {
                "output": "extend",
                "sortfield": ["itemid"],
                "sortorder": "DESC",
                "selectHosts": "extend",
                "selectItemDiscovery": "extend",
                "selectTriggers": "extend",
                "selectTags": "extend",
                "limit": 10,
            },
            "id": 1,
            "auth": self.auth
        }
        r = self.session.post(self.url, json=params)
        print(r.json())
        return r.json()

    
def main():
    zabbix = Zabbix("admin", "zabbix")
    zabbix.get_problems()
    zabbix.get_group()
    zabbix.get_host()
    zabbix.get_alert()
    # zabbix.get_trigger()
    # zabbix.get_template()
    # zabbix.get_item()

if __name__ == "__main__":
    main()
