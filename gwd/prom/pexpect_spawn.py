#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   pexpect_spawn.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/3/25 上午 10:05   hello      1.0         None

'''

import sys
import pexpect

child = pexpect.spawn('ssh root@192.168.226.20')
fout = open('mylog.txt','w')
child.logfile = fout

child.expect("password:")
child.sendline("root")
child.expect('#')
child.sendline('ls /root')
child.expect('#')
