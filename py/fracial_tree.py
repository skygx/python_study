#/usr/bin/python
#-*- coding:utf-8 -*-
'''
    作者:xguo
    文件:fracial_tree.py
    功能:利用递归绘制分形树
    版本:1.0
    日期:2019/2/20 12:28
'''
import turtle


def draw_branch(branch_length):

    if branch_length > 5 :
        #绘制右侧树枝
        turtle.forward(branch_length)
        print("向前", branch_length)
        turtle.right(20)
        print("右转", 20)
        draw_branch(branch_length - 15)

        #绘制左侧树枝
        turtle.left(40)
        print("左转", 40)
        draw_branch(branch_length - 15)

        turtle.right(20)
        print("右转", 20)
        turtle.backward(branch_length)
        print("向后", branch_length)


def main():
    turtle.penup()
    turtle.left(90)
    turtle.backward(100)
    turtle.pendown()

    draw_branch(60)
    turtle.mainloop()


if __name__ == "__main__":
    main()