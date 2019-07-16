# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# 现在有一棵合法的二叉树，树的节点都是用数字表示，现在给定这棵树上所有的父子关系，求这棵树的高度
# 输入描述:
# 输入的第一行表示节点的个数n（1 ≤ n ≤ 1000，节点的编号为0到n-1）组成，
# 下面是n-1行，每行有两个整数，第一个数表示父节点的编号，第二个数表示子节点的编号
# 输出描述:
# 输出树的高度，为一个整数
# 示例1
# 输入
#
# 5
# 0 1
# 0 2
# 1 3
# 1 4
# 输出
#
# 3

myDic = {'0':[1,0]}
high = 1;
nLen = int(raw_input())
for x in range(nLen - 1):
    [key,val] = raw_input().split(' ')
    if myDic.has_key(key) and myDic[key][1] < 2:
        myDic[key][1] = myDic[key][1] + 1
        myDic[val] = [myDic[key][0] + 1, 0]
        if myDic[val][0] > high:
            high = myDic[val][0]
            pass
print high

