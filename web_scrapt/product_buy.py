#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   product_buy.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/2/8 下午 8:13   hello      1.0         None

'''

from selenium.webdriver import Firefox, Chrome
import time
from PIL import Image
import zxing

web = Chrome()
web.get('https://www.taobao.com/')
time.sleep(1)
web.find_element_by_link_text('亲，请登录').click()
time.sleep(1)
web.find_element_by_id('fm-login-id').send_keys('skygx2011')
web.find_element_by_id('fm-login-password').send_keys('Gx!2135501')
time.sleep(1)
web.find_element_by_class_name('fm-button fm-submit password-login').click()

# web.find_element_by_xpath('//*[@id="login"]/div[1]/i').click()
# time.sleep(1)
# qrimg_file = '../png/taobao.png'
#
# web.execute_script('function download_image(){var canvas = document.getElementByTagName("canvas");canvas.toBlob(function(blob) {saveAs(blob, "output.png");}, "image/png");};')
#
# web.save_screenshot(qrimg_file)
#
# img = Image.open(qrimg_file)
# img.save(qrimg_file)
# zx = zxing.BarCodeReader()
# QR_code_info = zx.decode(qrimg_file)
# print(QR_code_info)

# web.get('https://cart.taobao.com/cart.htm')
# time.sleep(1)
