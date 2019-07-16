# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# 尽管是一个CS专业的学生，小B的数学基础很好并对数值计算有着特别的兴趣，喜欢用计算机程序来解决数学问题，现在，
# 她正在玩一个数值变换的游戏。她发现计算机中经常用不同的进制表示一个数，如十进制数123表达为16进制时只包含两位数
# 7、11（B），用八进制表示为三位数1、7、3，按不同进制表达时，各个位数的和也不同，如上述例子中十六进制和八进制中
# 各位数的和分别是18和11,。 小B感兴趣的是，一个数A如果按2到A-1进制表达时，各个位数之和的均值是多少？她希望你能
# 帮她解决这个问题？ 所有的计算均基于十进制进行，结果也用十进制表示为不可约简的分数形式。
# 输入描述:
# 输入中有多组测试数据，每组测试数据为一个整数A(1 ≤ A ≤ 5000).
# 输出描述:
# 对每组测试数据，在单独的行中以X/Y的形式输出结果。
# 示例1
# 输入
#
# 5
# 3
# 输出
#
# 7/3
# 2/1

def getJZ(num, b):
    sum = 0
    while (num > 0):
        i = num % b
        num = num / b
        sum += i
    return sum


def getSum(a1):
    su = 0
    for x in range(2, a1):
        su += getJZ(a1, x)
    return su


def gcd(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        temp = a % b
        a = b
        b = temp

    return a


def getResult(a):
    c = getSum(a)
    g = gcd(c, a - 2)
    # print g
    n1 = c / g
    n2 = (a - 2) / g
    return str(n1) + '/' + str(n2)


while 1:
    try:
        X = int(raw_input())
    except:
        break
    print getResult(X)