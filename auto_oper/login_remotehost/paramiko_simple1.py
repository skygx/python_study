#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   paramiko_simple1.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/3/25 上午 10:18   hello      1.0         None

'''

import paramiko

hostname = "192.168.226.20"
username = "root"
password = "root"
paramiko.util.log_to_file('./syslogin.log')
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.connect(hostname=hostname,username=username,password=password)
stdin,stdout,stderr = ssh.exec_command('free -m')
print(stdout.read())
ssh.close()
