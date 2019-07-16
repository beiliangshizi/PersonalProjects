# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# 小易来到了一条石板路前，每块石板上从1挨着编号为：1、2、3.......
# 这条石板路要根据特殊的规则才能前进：对于小易当前所在的编号为K的 石板，小易单次只能往前跳K的一个约数(不含1和K)步，
# 即跳到K+X(X为K的一个非1和本身的约数)的位置。 小易当前处在编号为N的石板，他想跳到编号恰好为M的石板去，小易想知道
# 最少需要跳跃几次可以到达。
# 例如：
# N = 4，M = 24：
# 4->6->8->12->18->24
# 于是小易最少需要跳跃5次，就可以从4号石板跳到24号石板
# 输入描述:
# 输入为一行，有两个整数N，M，以空格隔开。
# (4 ≤ N ≤ 100000)
# (N ≤ M ≤ 100000)
# 输出描述:
# 输出小易最少需要跳跃的步数,如果不能到达输出-1
# 示例1
# 输入
#
# 4 24
# 输出
#
# 5

import itertools


def foo():
    dp = [x for x in itertools.repeat(-1, M * 3 / 2)]
    T = [[] for x in itertools.repeat(None, M)]
    dp[M] = 0
    i = (M - 1) / 2
    while i > 1:
        j = i * 2
        while j < M:
            T[j].append(i)
            j += i
        i -= 1
    i = M - 1
    while i >= N:
        for k in T[i]:
            v = dp[i + k] + 1
            if v == 0:
                continue
            if dp[i] == -1:
                dp[i] = v
            elif v < dp[i]:
                dp[i] = v
        i -= 1
    return dp[N]


while True:
    try:
        (N, M) = (int(x) for x in raw_input().split())
        print foo()
    except EOFError:
        break