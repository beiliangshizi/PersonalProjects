# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

#
# 题目描述
# 一个数组有 N 个元素，求连续子数组的最大和。 例如：[-1,2,1]，和最大的连续子数组为[2,1]，其和为 3
# 输入描述:
# 输入为两行。
# 第一行一个整数n(1 <= n <= 100000)，表示一共有n个元素
# 第二行为n个数，即每个元素,每个整数都在32位int范围内。以空格分隔。
# 输出描述:
# 所有连续子数组中和最大的值。
# 示例1
# 输入
#
# 3
# -1 2 1
# 输出
#
# 3


#coding=UTF-8
import sys
num=int(sys.stdin.readline().strip())#人数
list_re=[int(each) for each in sys.stdin.readline().strip().split()]#原数组
#动态规划的思想，设max[i]为以元素i结尾的最大子串和，即目标函数，那么max[i]=max(max[i-1]+a[i],a[i]),
#所以关键在于判断max[i-1]是否大于0，如果大于0，则对于i元素来说，应该加上前者
#初始化
sum_i=0#以第i个元素结尾的目标函数
max_result=list_re[0]#最终值，用于比较以各个元素结尾的值，取大着
for i in range(0,num):
    #计算以第i个元素结尾的目标函数值，即sum_i
    if sum_i>=0:#此时代表sum_i-1
        sum_i=sum_i+list_re[i]
    else:sum_i=list_re[i]
    if sum_i>=max_result:max_result=sum_i#最终值
print max_result