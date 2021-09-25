# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   ansible_result.py
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/8/17  13:34   xguo      1.0         实现数据读取
2020/8/17  14:14   xguo      2.0         1.实现decide_line
                                               shift_line
                                               save_data
                                               deal_data
                                               print_output
                                               print_excel
                                         2.调试输出

'''

import re
import pprint
import pandas as pd


class Ansible_Deal:
    output = {}
    symbol = ['|', '>>', '=>']

    def __init__(self, file):
        self.file = file

    '''
    处理行是否为ansible执行状态信息行
    '''

    def decide_line(self, line):
        flag = ''
        if '|' in line and '>>' in line or '=>' in line:
            flag = True
        else:
            flag = False
        return flag

    ''':data:导入数据
    转换每个ansible命令输出为一行
    '''

    def shift_line(self, data):
        lines = []
        numbers = []
        result = []
        for i in range(0, len(data)):
            data[i].strip('')
            if self.decide_line(data[i]):
                # print(f'{i+1} true')
                d = data[i].strip().replace('\n', '')
                line = d
                numbers.append(i)
            else:
                # print(f'{i+1} false')
                d = data[i].strip().replace('\n', '')
                line += d
                # continue
            lines.append(line)
        for i in numbers[1:]:
            result.append(lines[i - 1])

        result.append(lines[-1])
        return result

    ''':host:主机名
       :line:转为一行的行号
       :status:执行状态  success,failed,unreachable
       :code:执行状态码  rc=0  rc=127等
       :msg: 执行结果
    '''

    def save_data(self, host, line, status, code, msg):
        self.output[f"{host}-{line}"] = {'hostname': host,
                                         'status': status, 'code': code, 'msg': msg}
        # self.output[line]={'hostname':host,'status':status,'code':code,'msg':msg}

    '''
    读取源ansible结果文件，核心处理函数
    '''

    def deal_data_multiline(self):
        with open(self.file, 'r') as f:
            data = f.readlines()

        result = self.shift_line(data)

        for i in range(0, len(result)):
            result[i] = result[i].replace("=>", '|').replace(">>", '|')
            # result[i]=re.sub('=>','|',result[i])
            msg = result[i].split('|')
            if len(msg) == 3:
                host, sts, message = msg
                self.save_data(host, i, sts, '', message)
            elif len(msg) == 4:
                host, sts, code_id, message = msg
                self.save_data(host, i, sts, code_id, message)
            else:
                print(f'{i} wrong line')
            # print(result[i])
            # print(host,sts,message)

    '''
    stdout显示输出
    '''

    def print_output(self):
        pprint.pprint(self.output)

    ''':path: excel输出路径和文件名
    ansible处理结果输出到excel
    '''

    def print_excel(self, path):

        pf = pd.DataFrame(self.output).T
        # print(pf)
        order = ['hostname', 'status', 'code', 'msg']
        pf = pf[order]

        columns_map = {
            'hostname': '主机名',
            'status': '状态',
            'code': '状态码',
            'msg': '结果消息'
        }

        pf.rename(columns=columns_map, inplace=True)
        file_path = pd.ExcelWriter(path)
        pf.fillna(' ', inplace=True)
        pf.to_excel(file_path, encoding='utf-8', index=False)
        file_path.save()
        print('excel output down!')


def main():
    deal = Ansible_Deal('../txt/test.txt')
    deal.deal_data_multiline()
    # deal.print_output()
    deal.print_excel('../result.xlsx')


if __name__ == "__main__":
    main()
