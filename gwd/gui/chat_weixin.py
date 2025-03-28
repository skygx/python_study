# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   chat_weixin.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/4 下午3:06   hello      1.0         None

'''
import tkinter as tk
import socket
import threading

# 客户端类
class ChatClient:
    def __init__(self, root):
        self.root = root
        self.root.title("简单聊天客户端")

        # 创建消息显示区域
        self.message_listbox = tk.Listbox(root, width=50, height=20)
        self.message_listbox.pack()

        # 创建输入框
        self.input_entry = tk.Entry(root, width=40)
        self.input_entry.pack()

        # 创建发送按钮
        self.send_button = tk.Button(root, text="发送", command=self.send_message)
        self.send_button.pack()

        # 初始化套接字
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 连接到服务器
        self.client_socket.connect(('localhost', 8000))

        # 启动接收消息的线程
        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.receive_thread.daemon = True
        self.receive_thread.start()

    def send_message(self):
        message = self.input_entry.get()
        if message:
            # 发送消息到服务器
            self.client_socket.send(message.encode())
            self.message_listbox.insert(tk.END, f"你: {message}")
            self.input_entry.delete(0, tk.END)

    def receive_messages(self):
        while True:
            try:
                # 接收服务器消息
                data = self.client_socket.recv(1024).decode()
                if not data:
                    break
                self.message_listbox.insert(tk.END, f"对方: {data}")
            except Exception as e:
                print(f"接收消息出错: {e}")
                break

if __name__ == "__main__":
    root = tk.Tk()
    client = ChatClient(root)
    root.mainloop()
