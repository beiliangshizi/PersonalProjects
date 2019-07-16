# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# 小易有一个圆心在坐标原点的圆，小易知道圆的半径的平方。小易认为在圆上的点而且横纵坐标都是整数的点是优雅的，
# 小易现在想寻找一个算法计算出优雅的点的个数，请你来帮帮他。
# 例如：半径的平方如果为25
# 优雅的点就有：(+/-3, +/-4), (+/-4, +/-3), (0, +/-5) (+/-5, 0)，一共12个点。
# 输入描述:
# 输入为一个整数，即为圆半径的平方,范围在32位int范围内。
# 输出描述:
# 输出为一个整数，即为优雅的点的个数
# 示例1
# 输入
#
# 25
# 输出
#
# 12

import math

r_square = int(raw_input())
i = 0
count = 0
while i ** 2 <= r_square / 2.0:
    j_square = r_square - i ** 2
    j = int(math.sqrt(j_square))
    if j ** 2 == j_square:
        if i == 0 or i == j:
            count += 4
        else:
            count += 8
    i += 1
print count