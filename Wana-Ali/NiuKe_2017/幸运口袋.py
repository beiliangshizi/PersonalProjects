# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'


# 题目描述
# 一个袋子里面有n个球，每个球上面都有一个号码(拥有相同号码的球是无区别的)。如果一个袋子是幸运的当且仅当所有球的号码的和
# 大于所有球的号码的积。
# 例如：如果袋子里面的球的号码是{1, 1, 2, 3}，这个袋子就是幸运的，因为1 + 1 + 2 + 3 > 1 * 1 * 2 * 3
# 你可以适当从袋子里移除一些球(可以移除0个,但是别移除完)，要使移除后的袋子是幸运的。现在让你编程计算一下你可以获得的
# 多少种不同的幸运的袋子。
# 输入描述:
# 第一行输入一个正整数n(n ≤ 1000)
# 第二行为n个数正整数xi(xi ≤ 1000)
# 输出描述:
# 输出可以产生的幸运的袋子数
# 示例1
# 输入
#
# 3
# 1 1 1
# 输出
#
# 2

def composite(array, Sum, multiply):
    count = 0
    for i in xrange(len(array)):
        if i > 0 and array[i] == array[i - 1]:
            continue
        Sum += array[i]
        multiply *= array[i]
        if Sum > multiply:
            count += 1 + composite(array[i + 1:], Sum, multiply)
        elif array[i] == 1:
            count += composite(array[i + 1:], Sum, multiply)
        else:
            break
        Sum -= array[i]
        multiply /= array[i]
    return count


def isluck(nums):
    Sum = 0
    multiply = 1
    for i in nums:
        Sum += i
        multiply *= i
    if Sum > multiply:
        return True
    else:
        return False


if __name__ == "__main__":
    n = input()
    array = raw_input().split()
    array = [int(i) for i in array]
    array.sort()
    print composite(array, 0, 1)