# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# 给定一个正整数，编写程序计算有多少对质数的和等于输入的这个正整数，并输出结果。输入值小于1000。
# 如，输入为10, 程序应该输出结果为2。（共有两对质数的和为10,分别为(5,5),(3,7)）
# 输入描述:
# 输入包括一个整数n,(3 ≤ n < 1000)
# 输出描述:
# 输出对数
# 示例1
# 输入
#
# 10
# 输出
#
# 2

n = int(raw_input().strip())


def issushu(num):
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def re_num(n):
    count = 0
    for i in range(2, n):
        if issushu(i):
            for j in range(i, n):
                if issushu(j) and i + j == n:
                    count += 1
    return count


print re_num(n)