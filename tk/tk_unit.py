#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   tk_unit.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/1/10 上午 9:06   hello      1.0         None

'''
import tkinter as tk
def say_hello():
    print("Hello World!")

def show_selection():
    print("Selection is:", var.get())

def show_selection1():
    print("Selection is:", var1.get())

def show_selection2(event):
    selection = event.widget.curselection()
    print("Selection is:", event.widget.get(selection))

def show_selection3():
    print("Selection is:", spinbox.get())

def show_selection4(value):
    print("Selection is:", value)

root = tk.Tk()

var = tk.BooleanVar()
var1 = tk.StringVar()

checkbutton = tk.Checkbutton(root, text="Select me", variable=var, command=show_selection)
checkbutton.pack()

button = tk.Button(root, text="点我", command=say_hello)
button.pack()

radiobutton1 = tk.Radiobutton(root, text="Option 1", variable=var1, value="Option 1", command=show_selection1)
radiobutton2 = tk.Radiobutton(root, text="Option 2", variable=var1, value="Option 2", command=show_selection1)
radiobutton1.pack()
radiobutton2.pack()

listbox = tk.Listbox(root)
listbox.insert("end", "Option 1")
listbox.insert("end", "Option 2")
listbox.bind("<<ListboxSelect>>", show_selection2)
listbox.pack()

spinbox = tk.Spinbox(root, values=(1, 2, 3,4,5), command=show_selection3)
spinbox.pack()

scale = tk.Scale(root, from_=0, to=100, command=show_selection4)
scale.pack()

scrollbar = tk.Scrollbar(root, orient="vertical")
scrollbar.pack(side="right", fill="y")
listbox = tk.Listbox(root, yscrollcommand=scrollbar.set)
for i in range(100):
    listbox.insert("end", "Option " + str(i))
scrollbar.config(command=listbox.yview)
listbox.bind("<MouseWheel>", scrollbar)
listbox.pack()

def draw_line(event):
    canvas.create_line(0, 0, event.x, event.y)

canvas = tk.Canvas(root, width=300, height=300)
canvas.bind("<Button-1>", draw_line)
canvas.pack()

def count_characters(event):
    text = event.widget.get("1.0", "end")
    count = len(text.replace("\n", ""))
    print("Character count:", count)
    print("text: ", text)

text = tk.Text(root)
text.bind("<KeyRelease>", count_characters)
text.pack()

def say_hello():
    print("Hello World!")

menubar = tk.Menu(root)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")

filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Copy")
editmenu.add_command(label="Cut")
editmenu.add_command(label="Paste")
editmenu.add_command(label="显示问候",command=say_hello)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About")

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Edit", menu=editmenu)
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)

def show_input(event):
    print("Input is:", entry.get())

entry = tk.Entry(root)
entry.bind("<Return>", show_input)
entry.pack()

root.mainloop()
