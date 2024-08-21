#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   trigger_test1.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/4/3 下午 2:43   hello      1.0         None

'''

from functools import partial


class EventTrigger:
    def __init__(self):
        self.events = {}

    def register_event(self, event_name):
        self.events[event_name] = []

    def unregister_event(self, event_name):
        if event_name in self.events:
            del self.events[event_name]

    def add_event_listener(self, event_name, callback):
        if event_name in self.events:
            self.events[event_name].append(callback)

    def remove_event_listener(self, event_name, callback):
        if event_name in self.events and callback in self.events[event_name]:
            self.events[event_name].remove(callback)

    def trigger_event(self, event_name, *args, **kwargs):
        if event_name in self.events:
            for callback in self.events[event_name]:
                callback(*args, **kwargs)


def my_callback(param1, param2):
    print(param1, param2)


trigger = EventTrigger()
trigger.register_event('my_event')
trigger.add_event_listener('my_event', partial(my_callback, 'hello'))
trigger.trigger_event('my_event', 'world')
