#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   sign_diy.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/10/2 下午 1:18   hello      1.0         None

'''


import re
import requests
from PIL import Image
name=input("请输入需要商务签名的姓名："+"\n")
data={
        'id':name,      #需要设计的姓名
        'id1':905,      #一笔商务签设计
        'id2':'#FFFFFF',#背景：白色
        'id4':'#000000',#阴影：黑色
        'id6':'#000000' #颜色：黑色
        }
startUrl = 'http://www.yishuzi.com/b/re13.php'
UA = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1'}
html = requests.post(startUrl,headers = UA, data=data).text
img_path=r'<img src="(.*?)">'
imgurls =re.findall(img_path,html)
img_url=imgurls[0]
print(img_url)
img_data = requests.get(url = img_url,headers = UA).content
with open("../jpg/{}.gif".format(name),'wb') as f:
     f.write(img_data)
     print("已保存为：【"+"{}.gif".format(name)+"】文件")
img = Image.open("../jpg/{}.gif".format(name))
img.show()
