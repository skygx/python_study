# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   app.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/4 下午3:58   hello      1.0         None

'''
from flask import Flask, request, jsonify, render_template, session
from flask_socketio import SocketIO, send, emit
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
socketio = SocketIO(app)

# 存储在线用户信息，键为用户 ID，值为用户名
online_users = {}
# 存储聊天消息，每条消息是一个包含用户名和内容的字典
chat_messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    if username:
        # 简单模拟生成用户 ID
        user_id = len(online_users) + 1
        online_users[user_id] = username
        session['user_id'] = user_id
        return jsonify({'status': 'success', 'user_id': user_id, 'username': username})
    return jsonify({'status': 'error', 'message': '用户名不能为空'})

@socketio.on('connect')
def handle_connect():
    user_id = session.get('user_id')
    if user_id in online_users:
        username = online_users[user_id]
        # 广播新用户加入消息
        socketio.emit('user_joined', {'username': username})

@socketio.on('send_message')
def handle_send_message(data):
    user_id = session.get('user_id')
    if user_id in online_users:
        username = online_users[user_id]
        message = data.get('message')
        if message:
            chat_messages.append({'username': username, 'message': message})
            # 广播消息给所有连接的客户端
            socketio.emit('new_message', {'username': username, 'message': message})

if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
