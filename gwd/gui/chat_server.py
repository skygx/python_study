# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   chat_server.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/4 下午3:34   hello      1.0         None

'''
import socket
import threading

# 存储所有客户端连接
clients = []

def handle_client(client_socket, client_address):
    try:
        while True:
            # 接收客户端消息
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            # 广播消息给所有客户端
            broadcast(message, client_socket)
    except Exception as e:
        print(f"处理客户端 {client_address} 时出错: {e}")
    finally:
        # 客户端断开连接，移除该客户端
        clients.remove(client_socket)
        client_socket.close()

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                # 发送消息给其他客户端
                client.send(message.encode('utf-8'))
            except Exception as e:
                print(f"广播消息时出错: {e}")
                clients.remove(client)
                client.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 8888))
    server.listen(5)
    print("服务器已启动，等待客户端连接...")

    while True:
        # 接受新的客户端连接
        client_socket, client_address = server.accept()
        print(f"客户端 {client_address} 已连接")
        clients.append(client_socket)
        # 为每个客户端启动一个线程处理消息
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    start_server()
