#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   ansible_generate_inventory-v1.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/11/9  8:53   xguo      1.0         指定list.xlsx文件输出hosts文件

'''
import pandas as pd

file = '../data/list.xlsx'
result = '../dist/hosts'

# excel 表头对应host中变量名
head_dict = {"hostname":"","host":"ansible_ssh_host","user":"ansible_ssh_user",
             "pass":"ansible_ssh_pass","port":"ansible_ssh_port","sudo_pass":"ansible_sudo_pass","connect":"ansible_connection",
             "shell":"ansible_shell_type","python":"ansible_python_interpreter"}

class GenerateList:
    def __init__(self,file,result):
        self.file = file
        self.result = result
        self.header = list()
        self.df = pd.DataFrame

    def read_excel(self):
        df = pd.read_excel(self.file,converters = {'hostname': str, 'ip': str,'user':str,'pass':str,'port':int,'name':str})

        header = df.columns.values
        test_data = []
        for i in df.index.values:  # 获取行号的索引，并对其进行遍历：
            # 根据i来获取每一行指定的数据 并利用to_dict转成字典
            row_data = df.loc[i, :].to_dict()
            test_data.append(row_data)

        for h in header:
            if h not in head_dict.keys():
                head_dict.update({f"{h}":h})

        self.header = header
        self.df = df


    def concat_str(self):
        header = self.header
        df = self.df
        d_nan = df.notna()
        data = []

        for i in df.index.values:
            assert (d_nan.loc[i,header[0]] or d_nan.loc[i,header[1]]), "Both hostname and ip can't be None at the same time!"
            if d_nan.loc[i,'hostname'] == True:
                constr = str(df.loc[i,'hostname']) + " "
            else:
                constr = ""
            for h in header[1:]:
                value = df.loc[i,h]
                key = head_dict[h]

                if d_nan.loc[i,h] == False:
                    continue

                if value:
                    constr = constr + str(key) + "=" + str(value) + " "
            constr = constr + "\n"
            print(constr)
            data.append(constr)
        with open(self.result,'w') as f:
            f.writelines(data)

def main():
    g = GenerateList(file,result)
    g.read_excel()
    g.concat_str()

if __name__ == "__main__":
    main()