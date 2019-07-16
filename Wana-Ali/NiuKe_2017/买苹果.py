# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'


# 题目描述
# 小易去附近的商店买苹果，奸诈的商贩使用了捆绑交易，只提供6个每袋和8个每袋的包装(包装不可拆分)。
# 可是小易现在只想购买恰好n个苹果，小易想购买尽量少的袋数方便携带。如果不能购买恰好n个苹果，小易将不会购买。
# 输入描述:
# 输入一个整数n，表示小易想购买n(1 ≤ n ≤ 100)个苹果
# 输出描述:
# 输出一个整数表示最少需要购买的袋数，如果不能买恰好n个苹果则输出-1
# 示例1
# 输入
#
# 20
# 输出
#
# 3

if __name__ == '__main__':
    n = input()
    Min = 100
    for i in range(n/8+1):
        num = n - i*8
        if num%6 == 0:
            time = i + num/6
            Min = min(Min, time)
    print -1 if Min == 100 else Min