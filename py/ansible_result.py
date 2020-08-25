#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   ansible_result.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/8/17  13:34   xguo      1.0         实现数据读取

'''
import re

class Ansible_Deal:
    def __init__(self,file):
        self.file=file

    def deal_data(self):
        hosts=[]
        status=[]
        return_code=[]
        result=[]
        symbol=['|', '>>', '=>']

        with open(self.file,'r') as f :
            data=f.readlines()
        for i in range(0,len(data)):
            for s in symbol:
                if s in data[i]:
                    # line.append(i+1)
                    temp=i
                    print()
                else:
                    data[temp]=data[temp]+data[i]
            print(data)

        # print(line)
            # print(data[i],end='')

def main():
    deal=Ansible_Deal('../txt/test.txt')
    deal.deal_data()


if __name__ == "__main__":
    main()