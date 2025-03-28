# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   rpc_client.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/2/21 下午3:56   hello      1.0         None

'''
import pika
import uuid

class FibonacciRpcClient:
    def __init__(self):
        # 建立与 RabbitMQ 服务器的连接
        self.credentials = pika.PlainCredentials('user', 'password')
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='192.168.226.20', port=5672, virtual_host='/', credentials=self.credentials))

        #self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()

        # 声明一个独占的临时队列用于接收服务器的响应
        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        # 配置消费者，从临时队列接收服务器的响应
        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

        self.response = None
        self.corr_id = None

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.corr_id = str(uuid.uuid4())
        # 发送请求消息到 rpc_queue 队列，并指定回复队列和关联 ID
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(n))

        # 等待服务器的响应
        while self.response is None:
            self.connection.process_data_events()

        return int(self.response)

# 创建客户端实例
fibonacci_rpc = FibonacciRpcClient()

# 调用远程函数计算 5 的平方
print(" [x] 请求计算 5 的平方")
response = fibonacci_rpc.call(5)
print(" [.] 结果是 %r" % response)
