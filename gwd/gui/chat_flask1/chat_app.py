# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   chat_app.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/4 下午3:50   hello      1.0         None

'''
from flask import Flask, request, jsonify, render_template
import threading
import time

app = Flask(__name__)

# 存储消息的列表
messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    message = data.get('message')
    if message:
        messages.append(message)
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error', 'message': '消息不能为空'})

@app.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run(debug=True)
