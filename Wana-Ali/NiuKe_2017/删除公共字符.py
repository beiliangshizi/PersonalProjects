# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# 输入两个字符串，从第一字符串中删除第二个字符串中所有的字符。例如，输入”They are students.”和”aeiou”，则删除之后的第一个字符串变成”Thy r stdnts.”
# 输入描述:
# 每个测试输入包含2个字符串
# 输出描述:
# 输出删除后的字符串
# 示例1
# 输入
#
# They are students.
# aeiou
# 输出
#
# Thy r stdnts.


str1 = raw_input()
str2 = raw_input()
str1 = list(str1)
str2 = list(str2)
ret=''
for each in str1:
    if each not in str2:
        ret += each
print ret