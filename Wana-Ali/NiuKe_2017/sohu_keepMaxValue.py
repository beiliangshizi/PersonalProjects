# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# 给定一个十进制的正整数number，选择从里面去掉一部分数字，希望保留下来的数字组成的正整数最大。
# 输入描述:
# 输入为两行内容，第一行是正整数number，1 ≤ length(number) ≤ 1000。第二行是希望去掉的数字数量cnt
# 1 ≤ cnt < length(number)。
# 输出描述:
# 输出保留下来的结果。
# 示例1
# 输入
# 325
# 1
# 输出
# 35


number = input()
cnt = input()
num = list(str(number))
for i in range(cnt):
    num.remove(min(num))
print eval(''.join(num))

