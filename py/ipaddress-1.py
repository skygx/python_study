#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   ipaddress-1.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/30  19:40   xguo      1.0         None

'''

import ipaddress
import getpass

import signal
import difflib
import os
from contextlib import contextmanager
from functools import lru_cache
import requests

from collections import Counter
import itertools

@lru_cache(maxsize=32)
def get_with_cache(url):
    try:
        r = requests.get(url)
        return r.text
    except:
        return "Not Found"


@contextmanager
def tag(name):
    print(f"<{name}>")
    yield
    print(f"</{name}>")


# To Limit CPU time
def time_exceeded(signo, frame):
    print("CPU exceeded...")
    raise SystemExit(1)


def set_max_runtime(seconds):
    # Install the signal handler and set a resource limit
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
    signal.signal(signal.SIGXCPU, time_exceeded)


# To limit memory usage
def set_max_memory(size):
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (size, hard))


def ipaddr():
    net = ipaddress.ip_network('74.125.227.0/30')  # Works for IPv6 too
    # IPv4Network('74.125.227.0/29')

    for addr in net:
        print(addr)
    ip = ipaddress.ip_address("74.125.227.3")

    print(ip in net)
    # True

    ip = ipaddress.ip_address("74.125.227.12")
    print(ip in net)
    # False


def getpw():
    user = getpass.getuser()
    password = getpass.getpass()
    print(user)
    print(password)


def count():
    cheese = ["gouda", "brie", "feta", "cream cheese", "feta", "cheddar",
              "parmesan", "parmesan", "cheddar", "mozzarella", "cheddar", "gouda",
              "parmesan", "camembert", "emmental", "camembert", "parmesan"]

    cheese_count = Counter(cheese)
    print(cheese_count.most_common(3))
    # Prints: [('parmesan', 4), ('cheddar', 3), ('gouda', 2)]


def url_cache():
    for url in ["https://baidu.com/",
                "http://www.sina.com",
                "http://www.163.com"]:
        get_with_cache(url)

    print(get_with_cache.cache_info())


def diff_word():
    print(difflib.get_close_matches('appel', ['ape', 'apple', 'peach', 'puppy'], n=2))


def iterword():
    # for line in itertools.dropwhile(lambda line: line.startswith("//"), string_from_file.split("\n")):
    #     print(line)

    s = itertools.islice(range(50), 10, 20)  # <itertools.islice object at 0x7f70fab88138>
    for val in s:
        print(val)


__all__ = ["ipaddr", 'tag']

def main() -> object:
    ipaddr()
    # getpw()
    with tag("h1"):
        print('This is the title')
    count()
    url_cache()
    diff_word()
    iterword()

if __name__ == "__main__":
    main()
