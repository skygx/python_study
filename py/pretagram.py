#/usr/bin/python
#-*- coding:utf-8 -*-
'''
    作者:xguo
    文件:pretagram.py
    功能:
    版本:1.0
    日期:2019/2/19 22:04
'''

import turtle


def draw_pretagram(size):
    # tl = turtle.Turtle()

    for i in range(0,5):
        turtle.forward(size)
        turtle.right(144)



def main():

    turtle.penup()
    turtle.backward(100)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor("red")

    turtle.begin_fill()
    for i in range(50, 100, 20):
        draw_pretagram(i)
    turtle.end_fill()
    turtle.mainloop()
    # turtle.exitonclick()


if __name__ == "__main__":
    main()
