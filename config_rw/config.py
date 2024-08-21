# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   config.py.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/6/6 上午9:31   hello      1.0         None

'''

import configparser
import os
import yaml
import tomllib
import json
import abc
# from dotenv import load_dotenv


class Configer(metaclass=abc.ABCMeta):
    def __init__(self, filename: str):
        self.filename = filename

    @abc.abstractmethod
    def load(self):
        raise NotImplementedError(f"subclass must implement this method")

    def file_exists(self):
        if not os.path.exists(self.filename):
            raise FileNotFoundError(f"File {self.filename} not found")


class IniParser(Configer):
    def __init__(self, filename: str):
        super().__init__(filename)

    def load(self):
        super().file_exists()
        config = configparser.ConfigParser()
        config.read(self.filename, encoding="utf-8")
        return config


class YamlParser(Configer):
    def __init__(self, filename: str):
        super().__init__(filename)

    def load(self):
        super().file_exists()
        with open(self.filename, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f.read())
            return config


class TomlParser(Configer):
    def __init__(self, filename: str):
        super().__init__(filename)

    def load(self):
        super().file_exists()
        with open(self.filename, "rb") as f:
            config = tomllib.load(f)
            return config


class JsonParser(Configer):
    def __init__(self, cfgtype: str, filename: str = None):
        super().__init__(cfgtype, filename)

    def load(self):
        super().file_exists()
        with open(self.filename, "r", encoding="utf-8") as f:
            config = json.load(f)
            return config


# class DotenvParser(Configer):
#     def __init__(self, filename: str = None):
#         super().__init__(filename)
#
    # def load(self):
    #     super().file_exists()
    #     load_dotenv(self.filename, override=True)
    #     config = dict(os.environ)
    #     return config

def main():
    # config = TomlParser("config.toml")
    # print(config.load())
    # config = IniParser("app_ip")
    # print(config.load())
    # config = configparser.ConfigParser()
    # with open('app_ip', 'r') as cfgfile:
    #     config.read(cfgfile)
    # ip = config.get('a', 'ip')
    # print(ip)

    with open('ip.yaml', 'r') as file:
        config = yaml.safe_load(file)
    # 访问数组
    array_value = config['b']
    print(array_value)



if __name__ == "__main__":
    main()
