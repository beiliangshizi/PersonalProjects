# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# 输入两个整数 n 和 m，从数列1，2，3.......n 中随意取几个数,使其和等于 m ,要求将其中所有的可能组合列出来
# 输入描述:
# 每个测试输入包含2个整数,n和m
# 输出描述:
# 按每个组合的字典序排列输出,每行输出一种组合
# 示例1
# 输入
#
# 5 5
# 输出
#
# 1 4
# 2 3
# 5

string = raw_input()
n, m = string.split(' ')
n = int(n)
m = int(m)
s = 0
a = []


def definesum(s, cur, a):
    if (s == m):
        for k in range(len(a) - 1):
            print a[k],
        print a[len(a) - 1]

    for i in range(cur, n + 1):
        if (s + i > m):
            return
        if (s + i <= m):
            a.append(i)
            definesum(s + i, i + 1, a)
            a.remove(i)


definesum(0, 1, a)