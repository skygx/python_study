#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   mask_reg.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/26  12:28   xguo      1.0         None

'''

import paddlehub as hub
import os

def main():
    module = hub.Module(name="pyramidbox_lite_mobile_mask")
    # path = r'C:\project\python_study\jpg\\'
    # image_list = [path + i for i in os.listdir(path)]
    file= 'kouzhao.jpg'
    input_dict = {'image': file}
    module.face_detection(data=file)


if __name__ == "__main__":
    main()