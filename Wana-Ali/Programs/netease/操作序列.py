# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 小易有一个长度为n的整数序列,a_1,...,a_n。然后考虑在一个空序列b上进行n次以下操作:
# 1、将a_i放入b序列的末尾
# 2、逆置b序列
# 小易需要你计算输出操作n次之后的b序列。
# 输入描述:
# 输入包括两行,第一行包括一个整数n(2 ≤ n ≤ 2*10^5),即序列的长度。
# 第二行包括n个整数a_i(1 ≤ a_i ≤ 10^9),即序列a中的每个整数,以空格分割。
#
#
# 输出描述:
# 在一行中输出操作n次之后的b序列,以空格分割,行末无空格。
#
# 输入例子1:
# 4
# 1 2 3 4
#
# 输出例子1:
# 4 2 1 3

n = int(raw_input(""))
a = map(int, raw_input("").split(" "))
b_left = []
b_right = []

if len(a) % 2 == 0:
    b_left = [a[k] for k in range(len(a) - 1, 0, -2)]
    b_right = [a[k] for k in range(0, len(a), 2)]
else:
    b_left = [a[k] for k in range(len(a) - 1, -1, -2)]
    b_right = [a[k] for k in range(1, len(a), 2)]

print " ".join(map(str, b_left + b_right))
