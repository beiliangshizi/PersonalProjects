# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 一个序列有N个数:A[1],A[2],,,A[N],求出最长非降子序列的长度。讲DP基本都会降到的一个问题LIS：longest increasing subseqence

a = [5,3,4,8,6,7]
d = [0]*len(a)
length = 0
for i in range(len(a)):
    d[i] = 1
    for j in range(i):
        if a[j]<=a[i] and d[j]+1 >d[i]:
            d[i] = d[j]+1
    if d[i] > length :
        length = d[i]
print length
print d