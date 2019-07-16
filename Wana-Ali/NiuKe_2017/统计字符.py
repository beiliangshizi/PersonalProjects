# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# 给定一个英文字符串,请写一段代码找出这个字符串中首先出现三次的那个英文字符。
# 输入描述:
# 输入数据一个字符串，包括字母,数字等。
# 输出描述:
# 输出首先出现三次的那个英文字符
# 示例1
# 输入
#
# Have you ever gone shopping and
# 输出
#
# e

n = raw_input()
m = n.replace(' ','')
#m = m.lower()
s = {}
for i in m:
    if (i>='a' and i<='z') or (i>='A' and i<='Z'):
        if i not in s:
            s[i] = 1
        else:
            s[i]=s[i]+1
        if s[i]>=3:
            print i
            break