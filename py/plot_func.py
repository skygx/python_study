#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   plot_func.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/26  16:08   xguo      1.0         None

'''

import numpy as np
from matplotlib import pyplot as plt

def main():

    x = np.arange(1, 11)  # x轴数据
    y = x * x + 5  # 函数关系
    plt.title("y=x*x+5")  # 图像标题
    plt.xlabel("x")  # x轴标签
    plt.ylabel("y")  # y轴标签
    plt.plot(x, y)  # 生成图像
    plt.show()  # 显示图像


if __name__ == "__main__":
    main()