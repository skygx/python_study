#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   map_china.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/18  15:56   xguo      1.0         None

'''

from pyecharts import options as opts
from pyecharts.charts import Map

data = [('湖北', 9074), ('浙江', 661), ('广东', 632), ('河南', 493), ('湖南', 463),
        ('安徽', 340), ('江西', 333), ('重庆', 275), ('江苏', 236), ('四川', 231),
        ('山东', 230), ('北京', 191), ('上海', 182), ('福建', 159), ('陕西', 116),
        ('广西', 111), ('云南', 105), ('河北', 104), ('黑龙江', 95), ('辽宁', 69),
        ('海南', 64), ('新疆', 21), ('内蒙古', 21), ('宁夏', 28), ('青海', 11), ('甘肃', 40), ('西藏', 1),
        ('贵州', 38), ('山西', 56), ('吉林', 23), ('台湾', 10), ('天津', 48), ('香港', 14), ('澳门', 8)]


def map_china() -> Map:
    c = (
        Map()
            .add(series_name="确诊病例", data_pair=data, maptype="china", zoom=1, center=[105, 38])
            .set_global_opts(
            title_opts=opts.TitleOpts(title="疫情地图"),
            visualmap_opts=opts.VisualMapOpts(max_=9999, is_piecewise=True,
                                              pieces=[{"max": 9, "min": 0, "label": "0-9", "color": "#FFE4E1"},
                                                      {"max": 99, "min": 10, "label": "10-99", "color": "#FF7F50"},
                                                      {"max": 499, "min": 100, "label": "100-499", "color": "#F08080"},
                                                      {"max": 999, "min": 500, "label": "500-999", "color": "#CD5C5C"},
                                                      {"max": 9999, "min": 1000, "label": ">=1000", "color": "#8B0000"}]
                                              )
        )
    )
    return c


def main():
    d_map = map_china()
    d_map.render()
    d_map.render_notebook()


if __name__ == "__main__":
    main()