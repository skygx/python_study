# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   flask_net_go.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/14 下午5:16   hello      1.0         None

'''
from flask import Flask, jsonify
import requests
import threading
import time

app = Flask(__name__)

# 全局变量用于控制网络读写状态
is_net_going = False

def simulate_network_request():
    """模拟网络读写数据"""
    global is_net_going
    while is_net_going:
        try:
            # 持续向 httpbin.org 发送请求，模拟网络读写
            url = "https://httpbin.org/stream-bytes/102400"  # 每次读取1KB数据
            response = requests.get(url, stream=True)
            for chunk in response.iter_content(chunk_size=1024):
                pass  # 读取数据但不处理
        except Exception as e:
            print(f"Network request failed: {e}")

@app.route('/net_go', methods=['GET'])
def net_go():
    """持续网络读写数据一段时间"""
    global is_net_going
    try:
        # 设置网络读写状态为True
        if not is_net_going:
            is_net_going = True
            # 启动新线程模拟持续网络读写
            threading.Thread(target=simulate_network_request).start()
            return jsonify({"status": "success", "message": "Network data simulation started"}), 200
        else:
            return jsonify({"status": "success", "message": "Network data simulation is already running"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/net_release', methods=['GET'])
def net_release():
    """释放网络读写"""
    global is_net_going
    try:
        # 设置网络读写状态为False，停止模拟
        if is_net_going:
            is_net_going = False
            return jsonify({"status": "success", "message": "Network data simulation stopped"}), 200
        else:
            return jsonify({"status": "success", "message": "Network data simulation is not running"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
