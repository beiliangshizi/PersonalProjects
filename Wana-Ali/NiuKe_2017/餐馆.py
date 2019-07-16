# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# 某餐馆有n张桌子，每张桌子有一个参数：a 可容纳的最大人数； 有m批客人，每批客人有两个参数:b人数，c预计消费金额。
# 在不允许拼桌的情况下，请实现一个算法选择其中一部分客人，使得总预计消费金额最大
# 输入描述:
# 输入包括m+2行。
# 第一行两个整数n(1 <= n <= 50000),m(1 <= m <= 50000)
# 第二行为n个参数a,即每个桌子可容纳的最大人数,以空格分隔,范围均在32位int范围内。
# 接下来m行，每行两个参数b,c。分别表示第i批客人的人数和预计消费金额,以空格分隔,范围均在32位int范围内。
# 输出描述:
# 输出一个整数,表示最大的总预计消费金额
# 示例1
# 输入
#
# 3 5
# 2 4 2
# 1 3
# 3 5
# 3 7
# 5 9
# 1 10
# 输出
#
# 20


def search(nums, target):
    if target <= nums[0]:
        return 0
    if target > nums[-1]:
        return -1

    l = 0
    r = len(nums) - 1
    while (l + 1) != r:
        mid = (l + r) / 2
        if target <= nums[mid]:
            r = mid
        else:
            l = mid
    return r


while True:
    try:
        n, m = map(int, raw_input().split())
        a = map(int, raw_input().split())

        guest = []
        for i in range(m):
            guest.append(map(int, raw_input().split()))

        guest.sort(key=lambda x: x[1], reverse=True)
        a.sort()

        value = 0

        count = 0
        j = 0
        i = 0
        while i < m:
            index = search(a, guest[i][0])
            if index >= 0:
                j = j + 1
                value += guest[i][1]
                del a[index]
                if j == n:
                    break
            i = i + 1

        print value

    except:
        break
