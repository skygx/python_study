# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   es_utils.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/9/5 上午9:35   hello      1.0         None

'''

from elasticsearch import Elasticsearch
import json

class EsClient:
    def __init__(self, host='192.168.226.20', port=9200, user=None, password=None):
        self.es = Elasticsearch(hosts=[{'host': host, 'port': port}], http_auth=(user, password), timeout=30, verify_certs=False)

    def create_index(self, index, body):
        if not self.es.indices.exists(index=index):
            self.es.indices.create(index=index, body=body, ignore=400)
    def search(self, index, body):
        return self.es.search(index=index, body=body)

    def index(self, index, body):
        return self.es.index(index=index, body=body)

    def delete(self, index, id):
        return self.es.delete(index=index, id=id)

    def update(self, index, id, body):
        return self.es.update(index=index, id=id, body=body)
    def get(self, index, id):
        return self.es.get(index=index, id=id)
    def exists(self, index, id):
        return self.es.exists(index=index, id=id)

    def count(self, index):
        return self.es.count(index=index)

    def bulk(self, actions):
        return self.es.bulk(actions)

    def delete_index(self, index):
        return self.es.indices.delete(index=index)

    # def get_all_index(self):
    #     return self.es.indices.get_alias("*")

    def get_index_mapping(self, index):
        return self.es.indices.get_mapping(index=index)

    def get_index_settings(self, index):
        return self.es.indices.get_settings(index=index)

    def get_index_stats(self, index):
        return self.es.indices.stats(index=index)

    def get_cluster_health(self):
        return self.es.cluster.health()

    def get_cluster_state(self):
        return self.es.cluster.state()

    def get_cluster_nodes(self):
        return self.es.nodes.info()

    def get_cluster_stats(self):
        return self.es.cluster.stats()

    def get_cluster_pending_tasks(self):
        return self.es.cluster.pending_tasks()

    def get_cluster_settings(self):
        return self.es.cluster.get_settings()

    def get_cluster_allocation_explain(self, index, body):
        return self.es.cluster.allocation_explain(index=index, body=body)

    def define_index_template(self, name, body):
        return self.es.indices.put_template(name=name, body=body)

    def get_index_template(self, name):
        return self.es.indices.get_template(name=name)

    def define_index_mapping(self, index, body):
        return self.es.indices.put_mapping(index=index, body=body)

def main():
    es = EsClient(host='192.168.226.20', port=9200, user='elastic', password='elastic')
    query = {"query": {"match_all": {}}}
    result = es.search(index='sys_info', body=query)
    # print(result)
    for hit in result["hits"]["hits"]:
        print(
            "%(hostname)s  %(ip)s  %(cup_per)s  %(mem_per)s  %(disk_per)s  %(net_recv)s  %(net_sent)s  %(current_time)s" %
            hit["_source"])
    # print(es.count(index='sys_info'))

    # print(es.get_all_index())
    # print(es.get_index_mapping(index='sys_info'))
    # print(es.get_index_settings(index='sys_info'))
    # print(es.get_index_stats(index='sys_info'))

    new_mapping = { "settings": {
      "number_of_shards": 1,
      "number_of_replicas": 0
  },
        "mappings": {
    "properties": {
    "net_recv": {
    "type": "float"
    },
    "hostname": {
    "type": "text",
    "fields": {
    "keyword": {
    "ignore_above": 256,
    "type": "keyword"
    }
    }
    },
    "cpu_per": {
    "type": "float"
    },
    "net_sent": {
    "type": "float"
    },
    "ip": {
    "type": "text",
    "fields": {
    "keyword": {
    "ignore_above": 256,
    "type": "keyword"
    }
    }
    },
    "disk_per": {
    "type": "float"
    },
    "current_time": {
    "type": "date",
    },
    "mem_per": {
    "type": "float"
    }
    }
    }
    }

    # es.define_index_mapping(index='sys_info1', body=new_mapping)
    es.delete_index(index='sys_info')
    es.create_index(index='sys_info', body=new_mapping)
    print(es.get_index_mapping(index='sys_info'))

if __name__ == '__main__':
    main()
