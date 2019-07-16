# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

#动态规划1：求最大公共子序列

def LCS_Lenth(x, y):
    m = len(x) + 1  # 数组x,y从0开始，书籍上，从1开始，故加1
    n = len(y) + 1
    # ----------------------初始化矩阵----------------
    c = [[0 for j in xrange(0, n)] for i in xrange(0, m)]

    b = [[0 for j in xrange(0, n)] for i in xrange(0, m)]
    # 用0、1、2分别表示向上、向斜上方、向左,不能b=c,若是那样的话，则b,c同值同改变
    # -------------------------------------------
    for i in xrange(1, m):  # m=8,i从1到7
        for j in xrange(1, n):  # n=7,j从1到6
            if x[i - 1] == y[j - 1]:  # x,y从标号0开始，故这里比较的话，从i-1，j-1走起
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 1  # 向斜上
            else:
                if c[i - 1][j] >= c[i][j - 1]:
                    c[i][j] = c[i - 1][j]
                    b[i][j] = 0
                else:
                    c[i][j] = c[i][j - 1]
                    b[i][j] = 2
    return b, c


def print_LCS(b, x, i, j):
    if i == 0 and j == 0:
        return
    if b[i][j] == 1:
        print_LCS(b, x, i - 1, j - 1)
        print x[i - 1],  # 这里同理，要输出x[i-1]
    elif b[i][j] == 0:
        print_LCS(b, x, i - 1, j)
    else:
        print_LCS(b, x, i, j - 1)


x = 'ABCBDAB'
y = 'BDCABA'
b, c = LCS_Lenth(x, y)
print '方向变化：', b
print '矩阵值：', c
print '最长公共子序列为：'
print_LCS(b, x, len(x), len(y))



#动态规划2：求矩阵最短路径
# 给定一些NxN的矩阵，对于任意的路线，定义其【和】为其线路上所有节点的数字的和，计算从左上角到右下角的路线和最小值。
# 每条路线只能从某一点到其周围（上下左右）的点，不可斜行。例如：
# 4,6
# 2,8
# 路线和最小值为 4-2-8 14
# 1,2,3
# 4,5,6
# 7,8,9
# 路线和最小值为 1-2-3-6-9 21

def minSum(list1):
    l1=len(list1)
    if l1<2:
        return list1
    list2=list1
    for i in xrange(1,l1):
        list2[0][i]=list1[0][i-1]+list1[0][i]
        list2[i][0]=list1[i-1][0]+list1[i][0]
    for i in xrange(1,l1):
        for j in xrange(1,l1):
            sum1=list2[i][j-1]+list1[i][j]
            sum2=list2[i-1][j]+list1[i][j]
            if sum1<sum2:
                list2[i][j]=sum1
            else:
                list2[i][j]=sum2
    return list2[l1-1][l1-1]

























