# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   rpc_server.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/2/21 下午3:56   hello      1.0         None

'''
import pika

# 建立与 RabbitMQ 服务器的连接
credentials = pika.PlainCredentials('user', 'password')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.226.20', port=5672, virtual_host='/', credentials=credentials))

channel = connection.channel()

# 声明一个队列用于接收客户端的请求
channel.queue_declare(queue='rpc_queue')

# 定义一个处理函数，这里简单地返回传入数字的平方
def fib(n):
    return n * n

# 定义消息处理回调函数
def on_request(ch, method, props, body):
    n = int(body)

    print(f" [.] 计算 {n} 的平方")
    response = fib(n)

    # 发送响应消息到客户端指定的回复队列
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = props.correlation_id),
                     body=str(response))
    # 确认消息已处理
    ch.basic_ack(delivery_tag=method.delivery_tag)

# 配置消费者，从 rpc_queue 队列接收消息
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

print(" [x] 等待 RPC 请求...")
# 开始消费消息
channel.start_consuming()
