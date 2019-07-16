# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 将一个区域分为 n×n 的小块，如果某一个方格下面有冰则用 * 表示，无冰则用 0 表示，任给一个这样的区域，求冰田个数？
# - 冰田划分规则：如果两个小块之间能够在不穿越小块的情况下连成直线，则属于**同一冰田

# 输入：
# 6
# 0*0000
# 0**00*
# *00000
# *00*00
# 000**0
# 000*00
#
# 输出：3
import sys

n = int(sys.stdin.readline())
values = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    values[i] = list(sys.stdin.readline().strip())
tag = 1
for i in range(n):
    for j in range(n):
        if values[i][j] == '0' :
            values[i][j]= 0
            continue
        elif (j-1)>=0 and values[i][j-1] > 0 :
            values[i][j] = values[i][j-1]
        elif (i-1)>=0 :
            if values[i-1][j] > 0:
                values[i][j] = values[i-1][j]
            elif (j-1)>=0 and values[i-1][j-1] > 0:
                values[i][j] = values[i-1][j-1]
            elif (j+1)<=(n-1) and values[i-1][j+1] > 0 :
                values[i][j] = values[i-1][j+1]
            else:
                values[i][j] = tag
                tag += 1
        else:
            values[i][j] = tag
            tag += 1
val_set = set()
for i in values:
    val_set.update(i)
print len(val_set)-1
