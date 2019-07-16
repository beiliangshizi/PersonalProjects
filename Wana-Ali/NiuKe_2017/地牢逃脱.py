# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# 给定一个 n 行 m 列的地牢，其中 '.' 表示可以通行的位置，'X' 表示不可通行的障碍，牛牛从 (x0 , y0 ) 位置出发，
# 遍历这个地牢，和一般的游戏所不同的是，他每一步只能按照一些指定的步长遍历地牢，要求每一步都不可以超过地牢的边界，
# 也不能到达障碍上。地牢的出口可能在任意某个可以通行的位置上。牛牛想知道最坏情况下，他需要多少步才可以离开这个地牢。
# 输入描述:
# 每个输入包含 1 个测试用例。每个测试用例的第一行包含两个整数 n 和 m（1 <= n, m <= 50），表示地牢的长和宽。
# 接下来的 n 行，每行 m 个字符，描述地牢，地牢将至少包含两个 '.'。接下来的一行，包含两个整数 x0, y0，
# 表示牛牛的出发位置（0 <= x0 < n, 0 <= y0 < m，左上角的坐标为 （0, 0），出发位置一定是 '.'）。
# 之后的一行包含一个整数 k（0 < k <= 50）表示牛牛合法的步长数，接下来的 k 行，每行两个整数 dx, dy 表示每次可选择
# 移动的行和列步长（-50 <= dx, dy <= 50）
# 输出描述:
# 输出一行一个数字表示最坏情况下需要多少次移动可以离开地牢，如果永远无法离开，输出 -1。以下测试用例中，
# 牛牛可以上下左右移动，在所有可通行的位置.上，地牢出口如果被设置在右下角，牛牛想离开需要移动的次数最多，为3次。
# 示例1
# 输入
#
# 3 3
# ...
# ...
# ...
# 0 1
# 4
# 1 0
# 0 1
# -1 0
# 0 -1
# 输出
#
# 3


import sys


def main():
    line_1 = raw_input().split()
    n, m = int(line_1[0]), int(line_1[1])
    l = [raw_input() for i in range(n)]
    line_2 = raw_input().split()
    x0, y0 = int(line_2[0]), int(line_2[1])
    k = input()
    f = [[int(s) for s in raw_input().split()] for i in range(k)]
    step = [[-1] * m for i in range(n)]
    arrive = [[0] * m for i in range(n)]

    if l[x0][y0] != '.':
        return -1
    arrive[x0][y0] = 1
    step[x0][y0] = 0

    current = [[x0, y0]]

    while len(current) > 0:
        nextpoint = []
        for p in current:
            x, y = p[0], p[1]
            for s in f:
                x1, y1 = x + s[0], y + s[1]
                if x1 < 0 or x1 >= n or y1 < 0 or y1 >= m:
                    continue
                if l[x1][y1] != '.' or arrive[x1][y1] == 1:
                    continue
                else:
                    arrive[x1][y1] = 1
                    step[x1][y1] = step[x][y] + 1
                    nextpoint.append([x1, y1])
        current = nextpoint
    res = 0
    for i in range(n):
        for j in range(m):
            s = step[i][j]
            if s == -1 and l[i][j] == '.':
                return -1
            if s > res:
                res = s
    return res


print main()