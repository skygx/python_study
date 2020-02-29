#/usr/bin/python
#-*- coding:utf-8 -*-
'''
    作者:xguo
    文件:tkinter-test.py
    功能:利用递归绘制分形树
    版本:1.0
    日期:2019/12/213:50
'''
from tkinter import *
from tkinter.scrolledtext import ScrolledText

top = Tk()
top.title("Simple Editor")
contents=ScrolledText()
filename=Entry()

def load():
    with open(filename.get()) as file:
        contents.delete('1.0',END)
        contents.insert(INSERT,file.read())

def save():
    with open(filename.get(),'w') as file:
        file.write(contents.get('1.0',END))



def main():
    contents.pack(side=BOTTOM,expand=True,fill=BOTH)
    filename.pack(side=LEFT,expand=True,fill=X)
    Button(text='Open',command=load).pack(side=LEFT)
    Button(text='Save',command=save).pack(side=LEFT)

    mainloop()


if __name__ == "__main__":
    main()