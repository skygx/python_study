# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   es_indices.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/11/20 下午4:11   hello      1.0         None

'''
from elasticsearch import Elasticsearch
from pprint import pprint

# 连接到Elasticsearch服务
class ESoperation:
    def __init__(self, es_host, es_port, es_user, es_pwd):
        self.es_host = es_host
        self.es_port = es_port
        self.es_user = es_user
        self.es_pwd = es_pwd
        self.es = Elasticsearch([f"http://{self.es_user}:{self.es_pwd}@{self.es_host}:{self.es_port}"])
        # self.es = Elasticsearch(["http://elastic:elastic@192.168.226.20:9200"])

    def get_all_indices(self):
        indices = self.es.cat.indices(format='json')
        return indices

    def get_index(self, index):
        index_info = self.es.indices.get(index)
        return index_info

    def create_index(self, index):
        return self.es.indices.create(index)

    def delete_index(self, index):
        return self.es.indices.delete(index)

    def get_node_info(self):
        node_info = self.es.nodes.info()
        return node_info

    def get_cluster_health(self):
        cluster_health = self.es.cluster.health()
        return cluster_health

    def get_cluster_state(self):
        cluster_state = self.es.cluster.state()
        return cluster_state

    def get_node_stats(self):
        nodes_stats = self.es.nodes.stats()
        return nodes_stats
    def get_index_template(self, name):
        template = self.es.indices.get_template(name=name)
        return template

    def get_index_data(self, index, body):
        search_response = self.es.search(index=index, body=body)
        return search_response

    def get_index_info(self, index):
        return self.es.indices.stats(index=index)

    def delete_index_data(self, index, body):
        return self.es.delete_by_query(index=index, body=body, conflicts='proceed')

    def get_index_settings(self, index):
        settings = self.es.indices.get_settings(index=index)
        return settings

    def get_index_mappings(self, index):
        mappings = self.es.indices.get_mapping(index=index)
        return mappings

    def get_index_aliases(self, index):
        aliases = self.es.indices.get_alias(index=index)
        return aliases

    def get_indices_number(self):
        return len(self.get_all_indices())

    def put_index_template(self, name, template):
        return self.es.indices.put_template(name=name, body=template)

    def put_index_settings(self, index, body):
        return self.es.indices.put_settings(index=index, body=body)

    def put_index_aliases(self, index, body):
        return self.es.indices.put_alias(index=index, name=body)

    def put_index_mapping(self, index, body):
        return self.es.indices.put_mapping(index=index, body=body)

    def close_index(self, index):
        return self.es.indices.close(index=index)

def main():
    es = ESoperation(es_host="192.168.226.20", es_port=9200, es_user="elastic", es_pwd="elastic")

    # print("获取所有索引")
    # pprint(es.get_all_indices())

    # print("获取指定索引")
    # index = "logstash*"
    # indice = es.get_index(index=index)
    # pprint(indice)

    # print("创建索引")
    # index = "test_index"
    # es.create_index(index=index)
    #
    # print("删除索引")
    # es.delete_index(index=index)

    # print("获取索引模板")
    # templates = es.get_index_template(name="test_template")

    # print("删除指定索引数据")
    # index = "logstash-logs-2024.11.20"
    # query = {"query": {"match_all": {}}}
    # # pprint(es.get_index_info(index=index))
    # # pprint(es.get_index_data(index=index, body=query))
    #
    # search_response = es.delete_index_data(index=index, body=query)
    # pprint(search_response)

    print("获取索引数量")
    print(es.get_indices_number())

    # print("获取节点信息")
    # node_info = es.get_node_info()
    # pprint(node_info)

    # print("获取节点统计信息")
    # nodes_stats = es.get_node_stats()
    # pprint(nodes_stats)

    print("获取集群健康状态")
    cluster_health = es.get_cluster_health()
    pprint(cluster_health)

    # print("获取集群状态")
    # cluster_state = es.get_cluster_state()
    # pprint(cluster_state)





if __name__ == '__main__':
    main()
