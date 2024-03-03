#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   get_json.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/1/2 下午 5:04   hello      1.0         None

'''
from flask import Flask, jsonify,request
import json

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York',
        'type': 'S'
    }
    json_data = json.dumps(data)
    response = app.response_class(
        response=json_data,
        status=200,
        mimetype='application/json'
    )
    return response

@app.route(rule='/api/post', methods=['POST'])
def everything():
    # 获取 JSON 格式的请求体 并解析
    request_body = request.get_json()
    print('Request info: ', request_body)

    # 生成响应信息
    response_info = {'msg': 'receive'}
    print('Response info:', response_info)

    # 将响应信息转换为 JSON 格式
    response_body = jsonify(response_info)

    # 最终对请求进行相应
    return response_body


if __name__ == '__main__':
    # 启动服务 指定主机和端口
    app.run(host='0.0.0.0', port=5000, debug=False)
