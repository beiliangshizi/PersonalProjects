# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# 一个只包含'A'、'B'和'C'的字符串，如果存在某一段长度为3的连续子串中恰好'A'、'B'和'C'各有一个，那么这个字符串就是
# 纯净的，否则这个字符串就是暗黑的。例如：
# BAACAACCBAAA 连续子串"CBA"中包含了'A','B','C'各一个，所以是纯净的字符串
# AABBCCAABB 不存在一个长度为3的连续子串包含'A','B','C',所以是暗黑的字符串
# 你的任务就是计算出长度为n的字符串(只包含'A'、'B'和'C')，有多少个是暗黑的字符串。
# 输入描述:
# 输入一个整数n，表示字符串长度(1 ≤ n ≤ 30)
# 输出描述:
# 输出一个整数表示有多少个暗黑字符串
# 示例1
# 输入
#
# 2
# 3
# 输出
#
# 9
# 21

n = int(raw_input())
if n == 1:
    print 3
else:
    # initialization, aa-type:3, ab-type:6
    ans = [3, 6]
    mat = [[1, 1], [2, 1]]
    temp_ans = [0, 0]
    temp = [[0, 0], [0, 0]]
    # number of interation
    n = n - 2
    while n != 0:
        if n & 1 == 1:
            temp_ans[0] = mat[0][0] * ans[0] + mat[0][1] * ans[1]
            temp_ans[1] = mat[1][0] * ans[0] + mat[1][1] * ans[1]
            ans[0] = temp_ans[0]
            ans[1] = temp_ans[1]
        temp[0][0] = mat[0][0] * mat[0][0] + mat[0][1] * mat[1][0]
        temp[0][1] = mat[0][0] * mat[0][1] + mat[0][1] * mat[1][1]
        temp[1][0] = mat[1][0] * mat[0][0] + mat[1][1] * mat[1][0]
        temp[1][1] = mat[1][0] * mat[0][1] + mat[1][1] * mat[1][1]
        mat[0][0] = temp[0][0]
        mat[1][0] = temp[1][0]
        mat[0][1] = temp[0][1]
        mat[1][1] = temp[1][1]
        n = n >> 1
    print ans[0] + ans[1]