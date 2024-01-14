#/usr/bin/python
#-*- coding:utf-8 -*-
'''
    作者:xguo
    文件:ip_scan.py
    功能:
    版本:1.0
    日期:2023/7/26 19:25
'''

import subprocess
import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter import ttk
def check_unused_ips():
    ip_range = entry.get()
    unused_ips = []
    progress_bar['maximum'] = 254
    progress_bar['value'] = 0
    output.delete(1.0, tk.END)
    
    for i in range(1, 255):
        ip = ip_range + '.' + str(i)
        response = subprocess.call(['ping', '-n', '1', '-w', '1', ip], stdout=subprocess.PIPE)
        if response == 1:
            unused_ips.append(ip)
        progress_bar['value'] += 1
        window.update_idletasks()
    
    if len(unused_ips) > 0:
        for i in range(0, len(unused_ips), 10):
            output.insert(tk.END, "\n".join(unused_ips[i:i+10]) + "\n")
            output.insert(tk.END, "====================\n")
    else:
        output.insert(tk.END, "该网段中没有未使用的IP地址\n")
window = tk.Tk()
window.title("未使用的IP地址检测工具")
window.geometry("400x400")
label = tk.Label(window, text="请输入要检测的网段（例如：192.168.0）:", font=("Arial", 12))
label.pack(pady=10)
entry = tk.Entry(window, width=20, justify='center', font=('Arial', 12))
entry.pack()
button = tk.Button(window, text="检测", command=check_unused_ips, font=("Arial", 12))
button.pack(pady=10)
progress_bar = ttk.Progressbar(window, orient=tk.HORIZONTAL, length=200, mode='determinate')
progress_bar.pack(pady=10)
output = scrolledtext.ScrolledText(window, width=40, height=20, font=("Arial", 12))
output.pack(pady=10)
window.mainloop()