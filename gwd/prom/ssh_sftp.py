#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   ssh_sftp.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/5 下午 12:28   hello      1.0         None

'''
import paramiko

class Connection:
    def __init__(self, ip, port, user, pwd):
        self.ip = ip
        self.port = port
        self.user = user
        self.pwd = pwd
        self.sshClient = paramiko.SSHClient()
        self.sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if pwd != '':
            self.sshClient.connect(ip, port, user, pwd)
        else:
            try:
                self.sshClient.connect(ip, port, user, pwd, look_for_keys=False, timeout=5.0)
            except paramiko.ssh_exception.AuthenticationException:
                self.sshClient.get_transport().auth_none(user)
        self.sftp = paramiko.SFTPClient.from_transport(self.sshClient.get_transport())

    def push(self, local_file, remote_file):
        self.sftp.put(local_file, remote_file)

    def pull(self, remote_file, local_file):
        self.sftp.get(remote_file, local_file)

    def exe(self, cmd):
        try:
            a = self.sshClient.exec_command(cmd, timeout=60000)
            f_in, f_out, f_err = a
            return f_out.read().decode('utf-8')
        except Exception as e:
            print(e)
            return 'Exception no return'

    def exe_invoke(self, cmd, end_str=None):
        """
        交互式执行命令，和exe实现功能相同。执行出错的时候可以尝试
        :param cmd:
        :param end_str: 通过该字段判断命令是否结束
        :param delaytime:
        :return:
        """
        try:
            ssh = self.sshClient.get_transport().open_session()
            ssh.get_pty()
            ssh.invoke_shell()
            ssh.send(cmd + '\n')
            ret = ""
            while True:
                out = ssh.recv(1024)
                # print(out.decode('utf-8'))
                ret = ret + out.decode('utf-8').replace('\r', '')
                print(out.decode('utf-8').replace('\r', ''))
                if end_str in out.decode('utf-8'):
                    break
            return ret
        except Exception as e:
            print(e)
            return 'Exception no return'

    def exists(self, path):
        path_d = '/'.join(path.split('/')[:-1])
        path_b = path.split('/')[-1]
        print('---------')
        print(path_d)
        print(path_b)
        ls = self.exe('ls %s' % path_d).decode().split('\n')
        print(ls)
        if path_b in ls:
            return True
        else:
            return False

    def reconect(self):
        print('reconneting')
        try:
            self.close()
        except:
            pass
        finally:
            self.connect(self.ip, self.port, self.user, self.pwd)

    def __del__(self):
        self.sshClient.close()
        self.sftp.close()

if __name__ == '__main__':
    c=Connection("192.168.226.20",port=22,user="root",pwd="root")
    print(c.exe_invoke("ls /tmp"))
