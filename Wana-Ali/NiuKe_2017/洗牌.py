# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'


# 题目描述
# 洗牌在生活中十分常见，现在需要写一个程序模拟洗牌的过程。 现在需要洗2n张牌，从上到下依次是第1张，第2张，第3张一直到第2n张。首先，我们把这2n张牌分成两堆，左手拿着第1张到第n张（上半堆），右手拿着第n+1张到第2n张（下半堆）。接着就开始洗牌的过程，先放下右手的最后一张牌，再放下左手的最后一张牌，接着放下右手的倒数第二张牌，再放下左手的倒数第二张牌，直到最后放下左手的第一张牌。接着把牌合并起来就可以了。 例如有6张牌，最开始牌的序列是1,2,3,4,5,6。首先分成两组，左手拿着1,2,3；右手拿着4,5,6。在洗牌过程中按顺序放下了6,3,5,2,4,1。把这六张牌再次合成一组牌之后，我们按照从上往下的顺序看这组牌，就变成了序列1,4,2,5,3,6。 现在给出一个原始牌组，请输出这副牌洗牌k次之后从上往下的序列。
# 输入描述:
# 第一行一个数T(T ≤ 100)，表示数据组数。对于每组数据，第一行两个数n,k(1 ≤ n,k ≤ 100)，接下来一行有2n个数a1,a2,...,a2n(1 ≤ ai ≤ 1000000000)。表示原始牌组从上到下的序列。
# 输出描述:
# 对于每组数据，输出一行，最终的序列。数字之间用空格隔开，不要在行末输出多余的空格。
# 示例1
# 输入
#
# 3
# 3 1
# 1 2 3 4 5 6
# 3 2
# 1 2 3 4 5 6
# 2 2
# 1 1 1 1
# 输出
#
# 1 4 2 5 3 6
# 1 5 4 3 2 6
# 1 1 1 1



import sys
#实现词c++中cin一样的功能
def read():
    for line in sys.stdin:
        for num in map(int, line.split()):
            yield num
# permutation的"乘法"
def perMulit(a, b):
    return [b[i] for i in a]
# 快速幂法计算最终结果,fibonacci数列的一种思路,可以将复杂度降为O(log(n)),思想是运算矩阵
def permutation(n, k, a):
    index = [0] * 2 * n
    for i in range(n):
        index[2*i] = i
        index[2*i+1] = i + n
    while k > 0:
        if k & 1 == 1:
            a = perMulit(index, a)
        index = perMulit(index, index)
        k = k >> 1
    return a
#类似c++中main的那一段
num = read()
T = num.next()
for i in range(T):
    n = num.next()
    k = num.next()
    a = [0] * (2 * n)
    for j in range(2*n):
        a[j] = num.next()
    print ' '.join(map(str, permutation(n, k, a)))

import math

n = int(raw_input())
a = list(map(int, raw_input().split(' ')))
m = int(raw_input())
b = list(map(int, raw_input().split(' ')))


def MinV(n, a, m, b, time):
    sumA = 0
    sumB = 0
    for i in range(n):
        sumA += a[i]
    for j in range(m):
        sumB += b[i]
    cha = sumA - sumB
    if cha < 0:
        cha = -1 * cha
    while cha != 0:
        mini = 0
        minj = 0
        best = 0
        for i in range(n):
            for j in range(m):
                if abs(cha - 2(a[i] - b[j])) < abs(cha - 2 * best):
                    best = a[i] - b[j]
            mini = i
            minj = j
    if best == 0:
        return 100000000
    a[i], b[j] = b[j], a[i]
    if time == 0:
        MinV(n, a, m, b, 1)
    elif time == 1:
        return best


answer = MinV(n, a, m, b, 0)
if answer > 100000000:
    print 0
else:
    print answer





























