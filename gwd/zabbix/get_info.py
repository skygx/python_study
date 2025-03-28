# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   get_info.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/11/21 下午1:54   hello      1.0         None

'''

import pyzabbix
import requests
import json
from pprint import pprint

class ZabbixInfo(object):
    def __init__(self, url, user, password):
        self.url = url
        self.user = user
        self.password = password
        self.zapi = pyzabbix.ZabbixAPI(url)
        self.zapi.login(user, password)


    def get_host_info(self, host_name):
        host_info = self.zapi.host.get(filter={'host': host_name})
        return host_info[0]
    def get_host_group_info(self, host_name):
        host_info = self.get_host_info(host_name)
        host_group_info = self.zapi.hostgroup.get(hostids=host_info['hostid'])
        return host_group_info

    def get_host_item_info(self, host_name):
        host_info = self.get_host_info(host_name)
        host_item_info = self.zapi.item.get(hostids=host_info['hostid'])
        return host_item_info

    def get_host_trigger_info(self, host_name):
        host_info = self.get_host_info(host_name)
        host_trigger_info = self.zapi.trigger.get(hostids=host_info['hostid'])
        return host_trigger_info

    def get_host_graph_info(self, host_name):
        host_info = self.get_host_info(host_name)
        host_graph_info = self.zapi.graph.get(hostids=host_info['hostid'])
        return host_graph_info

    def get_host_screen_info(self, host_name):
        host_info = self.get_host_info(host_name)
        host_screen_info = self.zapi.screen.get(hostids=host_info['hostid'])
        return host_screen_info

    def get_host_template_info(self, host_name):
        host_info = self.get_host_info(host_name)
        host_template_info = self.zapi.template.get(hostids=host_info['hostid'])
        return host_template_info

    def get_host_discovery_info(self, host_name):
        host_info = self.get_host_info(host_name)
        host_discovery_info = self.zapi.discoveryrule.get(hostids=host_info['hostid'])
        return host_discovery_info

    def get_host_inventory_info(self, host_name):
        host_info = self.get_host_info(host_name)
        host_inventory_info = self.zapi.host.get(hostids=host_info['hostid'], selectInventory=['inventory'])
        return host_inventory_info
    def get_host_action_info(self, host_name):
        host_info = self.get_host_info(host_name)
        host_action_info = self.zapi.action.get(hostids=host_info['hostid'])
        return host_action_info

    def modify_host_name(self, host_name, new_host_name):
        host_info = self.get_host_info(host_name)
        hostid = host_info['hostid']

        return True
    def get_auth_token(self, user, password):
        payload={
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": user,
                "password": password
            },
            "id": 1,
            "auth": None
        }
        headers = {"Content-Type": "application/json"}
        response = requests.post(self.url, data=json.dumps(payload), headers=headers)
        # auth_token = self.zapi.login(user, password)
        result = response.json()
        if 'result' in result:
            return result['result']
        else:
            raise Exception('auth failed')

    def get_manual_hosts(self,auth_token):
        payload={
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output": ["hostid", "host", "name"],
                "filter": {
                    "flags": "0"
                }
            },
            "auth": auth_token,
            "id": 1
        }
        headers = {"Content-Type": "application/json"}
        response = requests.post(self.url, data=json.dumps(payload), headers=headers)
        result = response.json()
        for host in result['result']:
            print(host['hostid'], host['host'], host['name'])

    def modify_host_name(self, host_name, new_host_name):
        host = self.zapi.host.get(filter={'host': host_name})
        if host:
            hostid = host[0]['hostid']
            self.zapi.host.update({'hostid': hostid, 'host': new_host_name})
            print('host name modified')
        else:
            print('host not found')


def main():
    url = 'http://192.168.226.20:8091/api_jsonrpc.php'
    user = 'Admin'
    password = 'zabbix'
    zabbix_info = ZabbixInfo(url, user, password)
    # host_info = zabbix_info.get_host_info('192.168.226.20')
    # group_info = zabbix_info.get_host_group_info('192.168.226.20')
    # item_info = zabbix_info.get_host_item_info('192.168.226.20')
    # trigger_info = zabbix_info.get_host_trigger_info('192.168.226.20')
    graph_info = zabbix_info.get_host_graph_info('192.168.226.20')
    # screen_info = zabbix_info.get_host_screen_info('192.168.226.20')
    # template_info = zabbix_info.get_host_template_info('192.168.226.20')
    # discovery_info = zabbix_info.get_host_discovery_info('192.168.226.20')
    # inventory_info = zabbix_info.get_host_inventory_info('192.168.226.20')
    # history_info = zabbix_info.get_host_history_info('192.168.226.20')
    # log_info = zabbix_info.get_host_log_info('192.168.226.20')
    # zabbix_info.modify_host_name('192.168.226.20', '192.168.226.20_new')
    # zabbix_info.modify_host_name('192.168.226.20', '192.168.226.20_new')
    zabbix_info.modify_host_name('192.168.226.20_new', '192.168.226.20')
    pprint(graph_info)

    za_token = zabbix_info.get_auth_token(user, password)
    zabbix_info.get_manual_hosts(za_token)



if __name__ == '__main__':
    main()
