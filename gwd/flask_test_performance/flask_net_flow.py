# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   flask_net_flow.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/14 下午5:08   hello      1.0         None

'''
from flask import Flask, jsonify
import requests

app = Flask(__name__)

# 模拟网络读写数据的函数
def simulate_network_request(size_in_mb=100):
    """模拟网络请求，增加网络读写数据"""
    url = "https://httpbin.org/stream-bytes/{}".format(size_in_mb * 1024 * 1024)
    response = requests.get(url, stream=True)
    for chunk in response.iter_content(chunk_size=1024):
        pass  # 这里只是读取数据，不进行实际处理
    return response.status_code

@app.route('/net_up', methods=['GET'])
def net_up():
    """增加网络读写数据"""
    try:
        # 模拟下载10MB数据
        simulate_network_request(size_in_mb=10)
        return jsonify({"status": "success", "message": "Network data usage increased"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/net_down', methods=['GET'])
def net_down():
    """减少网络读写数据（逻辑上停止模拟请求）"""
    try:
        # 减少网络读写数据的逻辑可以是停止模拟请求
        return jsonify({"status": "success", "message": "Network data usage decreased"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
