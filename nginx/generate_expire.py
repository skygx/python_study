#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   generate_expire.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/1/29 上午 9:07   hello      1.0         None

'''

from datetime import datetime, timedelta
from base64 import b64encode
import hashlib
# 设置环境变量
resource = b'/resources/index.html'
remote_addr = b'127.0.0.1'
host = b'www.example.com'
mysecret = b'mySecret'
# 生成过期时间戳
now = datetime.utcnow()
expire_dt = now + timedelta(hours=1)
print(expire_dt.strftime('%Y-%m-%d, %H:%M:%S'))
expire_epoch = str.encode(expire_dt.strftime('%Y-%m-%d, %H:%M:%S'))
# 计算字符串的 md5 哈希值
uncoded = expire_epoch + resource + remote_addr + mysecret
md5hashed = hashlib.md5(uncoded).digest()
# 对字符串进行 base64 编码和转换
b64 = b64encode(md5hashed)
unpadded_b64url = b64.replace(b'+', b'-')\
 .replace(b'/', b'_')\
 .replace(b'=', b'')
# 格式化并生成链接
linkformat = "{}{}?md5={}?expires={}"
securelink = linkformat.format(
 host.decode(),
 resource.decode(),
 unpadded_b64url.decode(),
 expire_epoch.decode()
)
print(securelink)
