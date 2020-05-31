#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   geoip-city.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/30  9:51   xguo      1.0         None

'''

import pygeoip

gi = pygeoip.GeoIP(r"I:\test\GeoLiteCity.dat")

def regGeoStr(ip):
    try:
        rec = gi.record_by_name(ip)
        city = rec['city']
        country = rec['country_code3']
        if city != "":
            geoLoc = city + ',' + country + "   location: {" + str(rec['longitude']) + ", " + str(rec['latitude'])+"}"
        else:
            geoLoc = country
        return geoLoc
    except Exception as e:
        print(e)
        return "Unregistered"

if __name__ == '__main__':
    print(regGeoStr("162.243.128.36"))

