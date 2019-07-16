# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

#
# 题目描述
# 请设计一个算法能够完成两个用字符串存储的整数进行相加操作，对非法的输入则返回error
# 输入描述:
# 输入为一行，包含两个字符串，字符串的长度在[1,100]。
# 输出描述:
# 输出为一行。合法情况输出相加结果，非法情况输出error
# 示例1
# 输入
#
# 123 123
# abd 123
# 输出
#
# 246
# Error


h = raw_input().split()
a = h[0]
b = h[1]
if a.isdigit() and b.isdigit():
    a = int(a)
    b = int(b)
    print a+b
else:
    print 'error'