#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   zk_nginx.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/11/6 下午 12:58   hello      1.0         None

'''

from kazoo.client import KazooClient
import time
zk=KazooClient(hosts='192.168.226.20:2181')
zk.start()
config_file='/etc/nginx/nginx.conf20231106'

with open(config_file,'r') as f:
    nginx_config=f.read()
print nginx_config

# nginx_config="""
# user root;
# worker_processes auto;
# error_log /var/log/nginx/error.log;
# pid /run/nginx.pid;
# include /usr/share/nginx/modules/*.conf;
# events {
#     worker_connections 1024;
# }
# http {
#     log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
#                       '$status $body_bytes_sent "$http_referer" '
#                       '"$http_user_agent" "$http_x_forwarded_for"';
#     access_log  /var/log/nginx/access.log  main;
#     sendfile            on;
#     tcp_nopush          on;
#     tcp_nodelay         on;
#     keepalive_timeout   65;
#     types_hash_max_size 4096;
#     include             /etc/nginx/mime.types;
#     default_type        application/octet-stream;
#     upstream bk_svr {
# 	server 192.168.226.20:81 max_fails=3 fail_timeout=30s weight=10;
# 	server 192.168.226.20:82 max_fails=3 fail_timeout=30s weight=10;
#     }
#     server {
#         listen       80;
#         listen       [::]:80;
#         server_name  _;
#         root         /usr/share/nginx/html;
# 	location /hello {
# 	  proxy_pass http://bk_svr/;
#         }
#         location /cgi-bin/ {
# 	  root /usr/share/awstats/wwwroot;
#           gzip off;
#           fastcgi_pass unix:/var/run/fcgiwrap.socket;
#           fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
#           fastcgi_param FCGI_SCRIPT /cgi-bin$fastcgi_script_name;
#           include fastcgi_params;
#         }
#         error_page 404 /404.html;
#         location = /404.html {
#         }
#         error_page 500 502 503 504 /50x.html;
#         location = /50x.html {
#         }
#     }
#     server {
#         listen       443 ssl http2;
#         listen       [::]:443 ssl http2;
#         server_name  _;
#         root         /usr/share/nginx/html;
# 	ssl_certificate /etc/nginx/example.crt;
#         ssl_certificate_key /etc/nginx/example.key;
# 	location / {
# 	  proxy_pass http://bk_svr;
# 	}
#     }
# }
#
# """
# zk.set('/nginx',bytes(nginx_config,encoding='utf-8'))
zk.stop()
