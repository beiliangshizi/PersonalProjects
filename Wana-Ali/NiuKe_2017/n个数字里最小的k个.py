# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# 找出n个数里最小的k个
# 输入描述:
# 每个测试输入包含空格分割的n+1个整数，最后一个整数为k值,n
# 不超过100。
# 输出描述:
# 输出n个整数里最小的k个数。升序输出
# 示例1
# 输入
#
# 3 9 6 8 -10 7 -11 19 30 12 23 5
# 输出
#
# -11 -10 3 6 7

nums = raw_input()
nums = nums.split()

N = len(nums)
k = int(nums[-1])
nums = nums[0:N - 1]

for i in range(N - 1):
    nums[i] = int(nums[i])

Nmin = min(nums)
Nmax = max(nums)

Nh = [0] * (Nmax - Nmin + 1)

for i in nums:
    Nh[i - Nmin] += 1

s = 0
ns = []
for i in range(len(Nh)):
    if Nh[i] != 0:
        s += Nh[i]
        ns = ns + [str(i + Nmin)] * Nh[i]
    if s >= k:
        break
print ' '.join(ns)




# string = raw_input()
# str_list = string.split(' ')
# str_list = list(map(int, str_list))
# k = str_list[-1]
# str_list.pop()
#
# str_list.sort()
# ret = ''
# for i in range(k - 1):
#     ret += str(str_list[i]) + ' '
# ret += str(str_list[k - 1])
# print ret