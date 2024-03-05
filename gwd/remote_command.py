#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   remote_command.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/5 上午 9:18   hello      1.0         None

'''

import paramiko

hostname="192.168.226.20"
username="root"
password="root"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname, port=22, username=username, password=password)
excute_cmds_list=['df -h','df -i','free -h','ps aux --sort=-%cpu|head -n 10','ps aux --sort=-%mem|head -n 10']
command = '\n'.join(excute_cmds_list)
stdin, stdout, stderr=ssh.exec_command(command)

# stdin, stdout, stderr = ssh.exec_command('ls -l /tmp')

print(stdout.read().decode('utf-8'))
ssh.close()
