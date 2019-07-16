# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# A,B,C三个人是好朋友,每个人手里都有一些糖果,我们不知道他们每个人手上具体有多少个糖果,但是我们知道以下的信息：
# A - B, B - C, A + B, B + C. 这四个数值.每个字母代表每个人所拥有的糖果数.
# 现在需要通过这四个数值计算出每个人手里有多少个糖果,即A,B,C。这里保证最多只有一组整数A,B,C满足所有题设条件。
# 输入描述:
# 输入为一行，一共4个整数，分别为A - B，B - C，A + B，B + C，用空格隔开。
# 范围均在-30到30之间(闭区间)。
# 输出描述:
# 输出为一行，如果存在满足的整数A，B，C则按顺序输出A，B，C，用空格隔开，行末无空格。
# 如果不存在这样的整数A，B，C，则输出No
# 示例1
# 输入
#
# 1 -2 3 4
# 输出
#
# 2 1 3

import sys
while True:
    line = sys.stdin.readline().strip()
    if line == "":
        break
    tmp = [int(var)for var in line.split(" ")]
    a = (tmp[0]+tmp[2])/2
    b = (tmp[1]+tmp[3])/2
    c = (tmp[3]-tmp[1])/2
    if a-b != tmp[0] or b-c!=tmp[1] or a+b!=tmp[2] or b+c!=tmp[3]:
        print("No")
    else:
        print(str(a)+" "+str(b)+" "+str(c))
添加笔记
求