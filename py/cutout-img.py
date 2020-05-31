#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   cutout-img.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/26  10:57   xguo      1.0         None

'''

import os,paddlehub as hub
from imageio import imwrite
import matplotlib.pyplot as plt

def main():
    humanseg=hub.Module(name='deeplabv3p_xception65_humanseg')
    file='C:\project\python_study\koutu.jpg'
    # path=r'C:\project\python_study\jpg\\'
    # files = [path + i for i in os.listdir(path)]
    # results = humanseg.segmentation(data={'image':files})
    # with open(r'C:\\project\\python_study\\jpg\\after.jpg','w') as jpg:
    #     jpg.write(''.join(results))
    result=humanseg.segmentation(data=file)
    plt.imshow(result,interpolation='bilinear')
    plt.axis("off")
    plt.show()
    # imwrite(r'C:\\project\\python_study\\jpg\\after.jpg',result)


if __name__ == "__main__":
    main()