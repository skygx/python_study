# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   remote_monitor.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/9/4 下午2:20   hello      1.0         None

'''
#!/usr/bin/python3
import paramiko

# 指定本地的RSA私钥文件
# key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')

# 建立连接
trans = paramiko.Transport(('192.168.226.20', 22))
# trans.connect(username='root', pkey=key)
trans.connect(username='root', password='root')

# 创建ssh对象，将_transport指定为上面的trans
ssh = paramiko.SSHClient()
ssh._transport = trans

# 创建sftp对象，指定连接的通道
# sftp = paramiko.SFTPClient.from_transport(trans)

# 上传psut.py文件
# sftp.put(localpath='/root/psut.py', remotepath='/root/p.py')

# 添加可执行权限，运行脚本
# ssh.exec_command('chmod +x /root/p.py')
stdin, stdout, stderr = ssh.exec_command('/root/py_test/psutil_test.py')
print(stdout.read().decode())

#关闭连接
ssh.close()
