#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   geo_point.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/17  20:32   xguo      1.0         None

'''

from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType


def main():
    # 链式调用
    c = (
        Geo()
            # 加载图表模型中的中国地图
            .add_schema(maptype="china")
            # 在地图中加入点的属性
            .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
            # 设置坐标属性
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            # 设置全局属性
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(),
            title_opts=opts.TitleOpts(title="Geo-基本示例"),
        )
    )
    # 在 html(浏览器) 中渲染图表
    c.render()
    # 在 Jupyter Notebook 中渲染图表
    c.render_notebook()


if __name__ == "__main__":
    main()