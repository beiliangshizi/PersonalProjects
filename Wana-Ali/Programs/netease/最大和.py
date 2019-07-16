# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 在一个N*N的数组中寻找所有横，竖，左上到右下，右上到左下，四种方向的直线连续D个数字的和里面最大的值
# 输入描述:
# 每个测试输入包含1个测试用例，第一行包括两个整数 N 和 D :
# 3 <= N <= 100
# 1 <= D <= N
# 接下来有N行，每行N个数字d:
# 0 <= d <= 100
#
#
# 输出描述:
# 输出一个整数，表示找到的和的最大值
#
# 输入例子1:
# 4 2
# 87 98 79 61
# 10 27 95 70
# 20 64 73 29
# 71 65 15 0
#
# 输出例子1:
# 193

# import sys
# [N,D] = list(map(int,raw_input().strip().split()))
# numbers = []
# for i in range(N):
#     oneList = list(map(int,raw_input().strip().split()))
#     numbers.append(oneList)
# cache = [[0]*N]*N
# for i in range(N): #横
#     for k in range(N): #纵
#         icache = []
#         if (i+D-1) < N-1: #x正向
#             sum_x1 = 0
#             for j in range(i,i+D):
#                 sum_x1 += numbers[j][k]
#             icache.append(sum_x1)
#         if (i-D+1) > 0:  #x负向
#             sum_x2 = 0
#             for j in range(i-D+1,i+1):
#                 sum_x2 += numbers[j][k]
#             icache.append(sum_x2)
#         if (k+D-1) < N-1:
#             sum_y1 = 0
#             for j in range(k,k+D):
#                 sum_y1 += numbers[i][j]
#             icache.append(sum_y1)
#         if (k-D+1) >0 :
#             sum_y2 = 0
#             for j in range(k-D+1,k+1):
#                 sum_y2 += numbers[i][j]
#             icache.append(sum_y2)
#         if (i+D-1)<N-1 and (k+D-1) < N-1:
#             sum_xy1 =

N, D = map(int, raw_input().split())
mat = []
for i in range(N):
    mat.append(map(int, raw_input().split()))
maxVal = -float('Inf')
# row
for i in range(N):
    for j in range(N - D + 1):
        if j == 0:
            temp = sum(mat[i][:D])
        else:
            temp = temp - mat[i][j - 1] + mat[i][j + D - 1]
        maxVal = max(maxVal, temp)
# column
for i in range(N):
    for j in range(N - D + 1):
        if j == 0:
            temp = 0
            for k in range(D):
                temp += mat[k][i]
        else:
            temp = temp - mat[j - 1][i] + mat[j + D - 1][i]
        maxVal = max(maxVal, temp)
# diagonal
for i in range(D, N):
    for j in range(i - D + 1):
        if j == 0:
            temp = 0
            for k in range(D):
                temp += mat[N - i + k][k]
        else:
            temp = temp - mat[N - i + j - 1][j - 1] + mat[N - i + j + D - 1][j + D - 1]
        if j == 0:
            temp2 = 0
            for k in range(D):
                temp2 += mat[k][N - i + k]
        else:
            temp2 = temp2 - mat[j - 1][N - i + j - 1] + mat[j + D - 1][N - i + j + D - 1]
        maxVal = max(maxVal, temp)
        maxVal = max(maxVal, temp2)
for j in range(N - D + 1):
    if j == 0:
        temp = 0
        for k in range(D):
            temp += mat[k][k]
    else:
        temp = temp - mat[j - 1][j - 1] + mat[j + D - 1][j + D - 1]
    maxVal = max(maxVal, temp)

# off-diagonal
for i in range(D, N):
    for j in range(0, i - D + 1):
        if j == 0:
            temp = 0
            for k in range(D):
                temp += mat[k][i - 1 - k]
        else:
            temp = temp - mat[j - 1][i - j] + mat[j + D - 1][i - D - j]
        if j == 0:
            temp2 = 0
            for k in range(D):
                temp2 += mat[N - k - 1][N - i + k]
        else:
            temp2 = temp2 - mat[N - j][N - i + j - 1] + mat[N - j - D][N - 1 - i + D + j]
        maxVal = max(maxVal, temp)
        maxVal = max(maxVal, temp2)
for j in range(N - D + 1):
    if j == 0:
        temp = 0
        for k in range(D):
            temp += mat[k][N - 1 - k]
    else:
        temp = temp - mat[j - 1][N - j] + mat[j + D - 1][N - D - j]
    maxVal = max(maxVal, temp)
print maxVal













