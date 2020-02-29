#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @File    :   Roll_random_v1.0.py    
    @Contact :   guoxin@126.com
    @License :   (C)Copyright 2018-2019, xguo-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/3/3 11:53   xguo      1.0         实现Roll类，投掷nums个骰子times次，得到出现各种结果的次数和频率
2019/3/4 8:39    xguo      2.0         matplotlib,可视化抛掷2个骰子的结果的散点图print_scatter，显示个数字分布频率的直方图print_hist
https://matplotlib.org/gallery.html
'''
import random
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

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

        print(self.roll_dict)

    def print_scratter(self):
        '''
        查看散点图，随机值显示的位置
        :return:
        '''
        # print(self.times)
        roll1_list = []
        roll2_list = []
        for i in range(self.times):
            roll1 = random.randint(1,6)
            roll2 = random.randint(1,6)
            roll1_list.append(roll1)
            roll2_list.append(roll2)

        # print(roll2_list,roll1_list)
        x = range(1,self.times+1)
        plt.scatter(x,roll1_list,c='red',alpha=0.5)
        plt.scatter(x,roll2_list,c='green',alpha=0.5)
        plt.show()

    def print_hist(self):
        '''
        查看直方图，各点数显示频率
        :return:
        '''
        roll_list = []
        for i in range(self.times):
            roll1 = random.randint(1,6)
            roll2 = random.randint(1,6)

            roll_list.append(roll1 + roll2)

        plt.hist(roll_list,bins=range(2,14),density=1, edgecolor='black',linewidth=1)
        plt.title('骰子点数统计')
        plt.xlabel('点数')
        plt.ylabel('频率')
        plt.show()

def main():
    r = Roll(2,10000)
    r.roll()
    r.result()
    # r.print_scratter()
    r.print_hist()

if __name__ == "__main__":
    main()