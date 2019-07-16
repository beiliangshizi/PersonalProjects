# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# 你就是一个画家！你现在想绘制一幅画，但是你现在没有足够颜色的颜料。为了让问题简单，我们用正整数表示不同颜色的颜料。
# 你知道这幅画需要的n种颜色的颜料，你现在可以去商店购买一些颜料，但是商店不能保证能供应所有颜色的颜料，所以你需要自己
# 混合一些颜料。混合两种不一样的颜色A和颜色B颜料可以产生(A XOR B)这种颜色的颜料(新产生的颜料也可以用作继续混合产生
# 新的颜色,XOR表示异或操作)。本着勤俭节约的精神，你想购买更少的颜料就满足要求，所以兼职程序员的你需要编程来计算出最少
# 需要购买几种颜色的颜料？
# 输入描述:
# 第一行为绘制这幅画需要的颜色种数n (1 ≤ n ≤ 50)
# 第二行为n个数xi(1 ≤ xi ≤ 1,000,000,000)，表示需要的各种颜料.
# 输出描述:
# 输出最少需要在商店购买的颜料颜色种数，注意可能购买的颜色不一定会使用在画中，只是为了产生新的颜色。
# 示例1
# 输入
#
# 3
# 1 7 3
# 输出
#
# 3

import sys


def makeTopZero(ls1, ls2, i, m):
    # x = ls1[i] * (-1) / ls2[i]
    ls3 = [ls1[j] ^ ls2[j] for j in range(m)]
    return ls3


def guassi2(array, n, m):
    p = 0
    for i in range(m):
        j = p
        while j < n:
            if array[j][i]:
                array[j], array[p] = array[p], array[j]
                p += 1
                j += 1
                break
            j += 1
        if j == n:
            continue
        else:
            for k in range(j, n):
                if array[k][i]:
                    array[k] = makeTopZero(array[k], array[p - 1], i, m)
    # print array
    return p


try:
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        n = int(line)
        nums = map(int, sys.stdin.readline().strip().split(" "))

        binNums = map(bin, nums)
        maxLen = 0
        for i in range(len(binNums)):
            binNums[i] = binNums[i][2:]
            i_len = len(binNums[i])
            if i_len > maxLen:
                maxLen = i_len
        pNums = []
        for j in binNums:
            j_len = len(j)
            if j_len < maxLen:
                temp = "0" * (maxLen - j_len) + j
            else:
                temp = j
            pNums.append(map(int, temp))
        # print pNums

        rs = guassi2(pNums, n, maxLen)
        print rs
        # sys.stdout.write(str(rs))

except:
    pass