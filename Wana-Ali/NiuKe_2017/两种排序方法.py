# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# 考拉有n个字符串字符串，任意两个字符串长度都是不同的。考拉最近学习到有两种字符串的排序方法： 1.根据字符串的字典序排序。
# 例如：
# "car" < "carriage" < "cats" < "doggies < "koala"
# 2.根据字符串的长度排序。例如：
# "car" < "cats" < "koala" < "doggies" < "carriage"
# 考拉想知道自己的这些字符串排列顺序是否满足这两种排序方法，考拉要忙着吃树叶，所以需要你来帮忙验证。
# 输入描述:
# 输入第一行为字符串个数n(n ≤ 100)
# 接下来的n行,每行一个字符串,字符串长度均小于100，均由小写字母组成
# 输出描述:
# 如果这些字符串是根据字典序排列而不是根据长度排列输出"lexicographically",
#
# 如果根据长度排列而不是字典序排列输出"lengths",
#
# 如果两种方式都符合输出"both"，否则输出"none"
# 示例1
# 输入
#
# 3
# a
# aa
# bbb
# 输出
#
# both

n = int(raw_input())
if n == 1:

    p = raw_input()
    print('both')
else:

    a = []
    for i in range(0, n):
        temp = raw_input()
        a.append(temp)
    jud1 = True
    jud2 = True
    for i in range(1, n):
        if (len(a[i - 1]) > len(a[i])):
            jud2 = False
        if a[i - 1] > a[i]:
            jud1 = False
        if jud1 == False and jud2 == False:
            break
    if jud1:
        if jud2:
            print('both')
        else:
            print('lexicographically')
    else:
        if jud2:
            print('lengths')
        else:
            print('none')
