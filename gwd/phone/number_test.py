# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   gwd
    @File    :   number_test.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2025/1/6 下午2:49   hello      1.0         None

'''
import phonenumbers
from phonenumbers import PhoneNumberFormat

number = "13693367745"
# number = "010-88888888"
parsed_number = phonenumbers.parse(number, "CN")
print(parsed_number)
formatted_number = phonenumbers.format_number(parsed_number, PhoneNumberFormat.INTERNATIONAL)
print(formatted_number)
is_valid = phonenumbers.is_valid_number(parsed_number)
print(is_valid)
# 输出：True 或 False

country_code = phonenumbers.region_code_for_number(parsed_number)
print(country_code)
# 输出：国家代码，如 'US'

country_code = parsed_number.country_code
area_code = parsed_number.national_number
print(f"Country Code: {country_code}, Area Code: {area_code}")
# 输出：国家码和区号

phone_type = phonenumbers.number_type(parsed_number)
print(phone_type)
# 输出：电话号码类型，如 'MOBILE', 'FIXED_LINE'

e164_number = phonenumbers.format_number(parsed_number, PhoneNumberFormat.E164)
print(e164_number)
# 输出：E.164格式的电话号码

# 假设有一个带区号的电话号码
number = "+1 408-555-1234"

# 解析电话号码
phone_number = phonenumbers.parse(number, None)

# 打印解析后的电话号码信息
print("国际格式:", phonenumbers.format_number(phone_number, PhoneNumberFormat.INTERNATIONAL))
print("国家码:", phone_number.country_code)
print("区号:", phonenumbers.format_number(phone_number, PhoneNumberFormat.NATIONAL)[1:4])

# 获取电话号码的地理信息
# geo_info = phonenumbers.geocoder.description_for_number(phone_number, 'zh-CN')
# 打印地理信息
# print("电话号码来自:", geo_info)

# 检查电话号码的携带者（需要携带者数据）
# carrier = phonenumbers.carrier.name_for_number(phone_number, 'zh-CN')
# 打印携带者信息
# print("电话号码的携带者:", carrier)

# 转换电话号码格式为国际格式
international_format = phonenumbers.format_number(phone_number, PhoneNumberFormat.INTERNATIONAL)

# 转换电话号码格式为本地格式
national_format = phonenumbers.format_number(phone_number, PhoneNumberFormat.NATIONAL)

# 打印转换后的电话号码
print("国际格式:", international_format)
print("本地格式:", national_format)

def format_international_number(number):
    phone_number = phonenumbers.parse(number, None)
    country_code = phone_number.country_code
    country = phonenumbers.region_code_for_number(phone_number)
    print(country)
    return phonenumbers.format_number(phone_number, PhoneNumberFormat.INTERNATIONAL)

# 示例
number = "+56 123-456-7890"
international_number = format_international_number(number)
print(f"The international format of {number} is {international_number}")

from phonenumbers import timezone

def get_phone_number_timezone(number):
    phone_number = phonenumbers.parse(number, None)
    return timezone.time_zones_for_number(phone_number)

# 示例
number = "+86 13693367745"
timezone = get_phone_number_timezone(number)
print(f"The number {number} is in the timezone {timezone}")
