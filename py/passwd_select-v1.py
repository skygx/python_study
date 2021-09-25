#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   passwd_select-v1.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/9/8  20:33   xguo      1.0         None

'''

'''
web全栈：做网站，管理系统，网络安全维护，大数据平台统计系统
网络爬虫： 网上抓取数据
数据分析： 抓取数据，清洗，筛选，图形化
人工智能： 数据样本训练，模型--应用层
'''
from tkinter import *

class PassSelect:


    def __init__(self):
        self.leng=StringVar().set(6)

    def plus(self):
        self.leng.set(int(self.leng.get())+1)
        print(111)

    def neg(self):

        print(222)

    def showPic(self):
        tk = Tk()
        tk.title('密码选择器')
        # form = width*height+x+y
        cv = Canvas(tk, width=200, height=30)
        cv.pack()
        tk.geometry('+900+300')
        # 网格布局
        f1 = Frame(tk)
        # 规范，网格不超过padx 10 pady 5
        f1.pack(padx=10, pady=5)

        # leng = StringVar()
        # leng.set(6)

        # 设置标签组件  根据行 列 坐标 摆放控件位置
        Label(f1, text='密码长度').grid(row='0', column='0')
        f1r=Frame(f1)
        # 输入框, 只读
        Entry(f1r, width=5, textvariable=self.leng, state='readonly').grid(row='0', column='1')

        Button(f1r, text='+', command=self.plus).grid(row='0', column='3')
        Button(f1r, text='-', command=self.neg).grid(row='0', column='4')

        f1rb = Frame(f1)
        f1rb.grid(row='1', column='1')
        Label(f1, text='密码强度').grid(row='1', column='0')
        # 单选按钮
        Radiobutton(f1rb, text='简单').grid(row='1', column='1')
        Radiobutton(f1rb, text='一般').grid(row='1', column='2')
        Radiobutton(f1rb, text='复杂').grid(row='1', column='3')

        Entry(tk).pack()
        Button(tk, text='点击生成密码').pack()

        f1.mainloop()



def main():
    ps=PassSelect()
    ps.showPic()



if __name__ == "__main__":
    main()