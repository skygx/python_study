# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   map_beijing.py
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/18  15:58   xguo      1.0         None

'''

from pyecharts import options as opts
from pyecharts.charts import Map

data = [('东城区', 19), ('西城区', 56), ('朝阳区', 76), ('海淀区', 70), ('丰台区', 156),
        ('石景山区', 15), ('门头沟区', 5), ('房山区', 20), ('通州区', 19), ('顺义区', 10),
        ('昌平区', 29), ('大兴区', 62), ('怀柔区', 7), ('密云区', 7), ('延庆区', 1),
        ]


def map_beijing() -> Map:
    c = (Map(init_opts=opts.InitOpts(width='900px',
                                     height='800px')) .add(series_name="北京确诊病例",
                                                           data_pair=data,
                                                           maptype="北京") .set_global_opts(title_opts=opts.TitleOpts(title="疫情地图"),
                                                                                          visualmap_opts=opts.VisualMapOpts(max_=200,
                                                                                                                            is_piecewise=True,
                                                                                                                            pieces=[{"max": 9,
                                                                                                                                     "min": 0,
                                                                                                                                     "label": "0-9",
                                                                                                                                     "color": "#FFE4E1"},
                                                                                                                                    {"max": 30,
                                                                                                                                     "min": 10,
                                                                                                                                     "label": "10-30",
                                                                                                                                     "color": "#FF7F50"},
                                                                                                                                    {"max": 50,
                                                                                                                                     "min": 30,
                                                                                                                                     "label": "30-50",
                                                                                                                                     "color": "#F08080"},
                                                                                                                                    {"max": 100,
                                                                                                                                     "min": 50,
                                                                                                                                     "label": "50-100",
                                                                                                                                     "color": "#CD5C5C"},
                                                                                                                                    {"max": 200,
                                                                                                                                     "min": 100,
                                                                                                                                     "label": ">=100",
                                                                                                                                     "color": "#8B0000"}])))
    return c


def main():
    d_map = map_beijing()
    d_map.render('beijing.html')
    d_map.render_notebook()


if __name__ == "__main__":
    main()
