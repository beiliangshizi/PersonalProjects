# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# 对于一个整数X，定义操作rev(X)为将X按数位翻转过来，并且去除掉前导0。例如:
# 如果 X = 123，则rev(X) = 321;
# 如果 X = 100，则rev(X) = 1.
# 现在给出整数x和y,要求rev(rev(x) + rev(y))为多少？
# 输入描述:
# 输入为一行，x、y(1 ≤ x、y ≤ 1000)，以空格隔开。
# 输出描述:
# 输出rev(rev(x) + rev(y))的值
# 示例1
# 输入
#
# 123 100
# 输出
#
# 223

import sys


def rev(x):
    tmp_x = str(x)

    result = [tmp_x[-i - 1] for i in range(len(tmp_x))]
    result = int(''.join(result))
    return result


while True:
    line = sys.stdin.readline().strip()
    if line == "":
        break
    tmp = line.split(" ")
    res = rev(tmp[0]) + rev(tmp[1])
    print(rev(res))