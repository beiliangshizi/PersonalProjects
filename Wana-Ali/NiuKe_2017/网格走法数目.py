# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# 有一个X*Y的网格，小团要在此网格上从左上角到右下角，只能走格点且只能向右或向下走。请设计一个算法，计算小团有多少种走法。
# 给定两个正整数int x,int y，请返回小团的走法数目。
# 输入描述:
# 输入包括一行，逗号隔开的两个正整数x和y，取值范围[1,10]。
# 输出描述:
# 输出包括一行，为走法的数目。
# 示例1
# 输入
#
# 3 2
# 输出
#
# 10

def stepNum(X, Y):
    dp = [[0] * (Y + 1) for i in range(X + 1)]
    for i in range(X + 1):
        dp[i][0] = 1
    for j in range(1, Y + 1):
        dp[0][j] = 1
    for i in range(1, X + 1):
        for j in range(1, Y + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]


if __name__ == '__main__':
    XY = raw_input().split()
    X = int(XY[0])
    Y = int(XY[1])
    print stepNum(X, Y)



# import math
#
# x, y = map(int, raw_input().split(' '))
#
# print math.factorial(x + y) / math.factorial(x) / math.factorial(y)