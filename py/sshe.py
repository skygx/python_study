#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   sshe.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/2/11 下午 3:20   hello      1.0         None
python sshe.py -i 192.168.226.20 -u linux -p 1 -c hostname
'''
import paramiko
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','--ip', type=str, help='ip address')
parser.add_argument('-u','--username', type=str, help='username')
parser.add_argument('-p','--password', type=str, help='password')
parser.add_argument('-c','--cmd', type=str, help='command')
args = parser.parse_args()

def sshe(ip,username,passwd,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd)
        stdin,stdout,stderr = ssh.exec_command(cmd)
        print(stdout.read())
        print("%s\tOK\n"%(ip))
        ssh.close()
    except:
        print("%s\tError\n"%(ip))

if __name__ == '__main__':
    sshe(args.ip,args.username,args.password,args.cmd)
