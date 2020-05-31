#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   iris_seaborn.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/29  20:34   xguo      1.0         None

'''
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn import tree


def main():
    sns.set(style="ticks", color_codes=True)
    iris_datas = load_iris()
    # iris = pd.DataFrame(iris_datas.data, columns=['SpealLength', 'Spealwidth', 'PetalLength', 'PetalLength'])
    iris = pd.DataFrame(iris_datas.data)
    df02 = iris.iloc[:, [0, 2, 3]]
    print(iris)
    sns.pairplot(df02)
    plt.show()


if __name__ == "__main__":
    main()