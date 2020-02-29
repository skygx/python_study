#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   Roll_random_v1.0.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/3 11:53   xguo      1.0         实现Roll类，投掷nums个骰子times次，得到出现各种结果的次数和频率

'''
import random

class Roll():

    def __init__(self,nums,times=10):
        '''

        :param nums: 骰子数量
        :param times: 投掷次数
        '''
        self.nums = nums
        self.times = times

        self.roll_result = [0] * (6 * nums)
        self.roll_range = range(nums, 6 * nums + 1)
        self.roll_list = list(self.roll_range)
        self.roll_dict = dict(zip(self.roll_list, self.roll_result))

    def roll_times(self)->int:
        roll = 0
        for i in range(self.nums):
            roll += random.randint(1,6)
        return roll

    def roll(self):
        for i in range(self.times):
            roll = self.roll_times()
            for j in self.roll_range:
                if roll == j:
                    self.roll_dict[j] += 1

    def result(self):
        for key,value in self.roll_dict.items():
            print('点数{}的次数：{},频率：{}'.format(key,value,value / self.times))

def main():
    r = Roll(3,10000)
    r.roll()
    r.result()

if __name__ == "__main__":
    main()