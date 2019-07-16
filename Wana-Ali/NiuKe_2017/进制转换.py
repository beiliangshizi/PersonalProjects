# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# 给定一个十进制数M，以及需要转换的进制数N。将十进制数M转化为N进制数
# 输入描述:
# 输入为一行，M(32位整数)、N(2 ≤ N ≤ 16)，以空格隔开。
# 输出描述:
# 为每个测试实例输出转换后的数，每个输出占一行。如果N大于9，则对应的数字规则参考16进制（比如，10用A表示，等等）
# 示例1
# 输入
#
# 7 2
# 输出
#
# 111

def trans(M,N):
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    if M>0:
        temp = M
        res = ''
        while temp>0:
            a = temp%N
            temp = temp/N
            res = nums[a]+res
        return res
    temp = -M
    res = ''
    while temp > 0:
        a = temp % N
        temp = temp / N
        res = nums[a] + res
    return '-'+res
if __name__ == '__main__':
    M, N = [int(x) for x in raw_input().strip().split(' ')]
    print trans(M,N)