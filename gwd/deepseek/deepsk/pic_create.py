# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   pic_create.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/3/10 下午4:43   hello      1.0         None

'''
import pollinations as ai

model_obj = ai.Model()


image = model_obj.generate(
    prompt=f'A beautiful landscape {ai.realistic}',
    model=ai.flux,
    width=1024,
    height=1024,
    seed=42
)

image.save('image-output.jpg')

print(image.url)
