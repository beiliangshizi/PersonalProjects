# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 小明同学学习了不同的进制之后，拿起了一些数字做起了游戏。小明同学知道，在日常生活中我们最常用的是十进制数，而在计算机中，二进制数也很常用。现在对于一个数字x，小明同学定义出了两个函数f(x)和g(x)。 f(x)表示把x这个数用十进制写出后各个数位上的数字之和。如f(123)=1+2+3=6。 g(x)表示把x这个数用二进制写出后各个数位上的数字之和。如123的二进制表示为1111011，那么，g(123)=1+1+1+1+0+1+1=6。 小明同学发现对于一些正整数x满足f(x)=g(x)，他把这种数称为幸运数，现在他想知道，小于等于n的幸运数有多少个？
# 输入描述:
# 每组数据输入一个数n(n<=100000)
#
#
# 输出描述:
# 每组数据输出一行，小于等于n的幸运数个数。
#
# 输入例子1:
# 21
#
# 输出例子1:
# 3

n = input()
dev = [0]
luck = 0
for i in xrange(1,n):
    hex = map(int,list(str(i)))
    flag = 1
    for j in range(len(dev)):
        if dev[len(dev)-j-1] < 1:
            dev[len(dev)-j-1] += 1
            flag = 0
            break
        else:
            dev[len(dev) - j - 1]  = 0
    if flag:
        dev.insert(0,1)
    hex_sum = sum(hex)
    dev_sum = sum(dev)
    if hex_sum == dev_sum:
        luck += 1
print luck + 1