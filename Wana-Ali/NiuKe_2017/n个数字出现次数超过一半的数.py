# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# 输入n个整数，输出出现次数大于等于数组长度一半的数。
# 输入描述:
# 每个测试输入包含 n个空格分割的n个整数，n不超过100，其中有一个整数出现次数大于等于n/2。
# 输出描述:
# 输出出现次数大于等于n/2的数。
# 示例1
# 输入
#
# 3 9 3 2 5 6 7 3 2 3 3 3
# 输出
#
# 3

input_str = raw_input()
input_str = input_str.split(' ')
unique_str = set(input_str)
length = len(input_str) / 2

ret = ''
for each in unique_str:
    count = input_str.count(each)
    if count >= length:
        ret += str(each)
print ret