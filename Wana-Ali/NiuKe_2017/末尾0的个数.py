# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# 输入一个正整数n,求n!(即阶乘)末尾有多少个0？ 比如: n = 10; n! = 3628800,所以答案为2
# 输入描述:
# 输入为一行，n(1 ≤ n ≤ 1000)
# 输出描述:
# 输出一个整数,即题目所求
# 示例1
# 输入
#
# 10
# 输出
#
# 2

n = int(raw_input())
zero_n = 0
for i in range(1,n+1):
    t = i
    nn = 0
    while t%5==0 and t>=5:
        t/=5
        nn+=1
    zero_n+=nn
print zero_n