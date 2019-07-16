# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

import sys


def cal(tree,a,b,c):
    root = ( tree[0] + tree[-1] + 1 ) / 2
    big_flag = 0
    small_flag = 0
    equal_flag = 0
    for i in [a,b,c] :
        if i - root < 0:
            small_flag += 1
        elif i - root == 0:
            equal_flag +=1
        else:
            big_flag += 1
    if equal_flag:
        return root
    elif big_flag > 0 and small_flag > 0 :
        return root
    elif big_flag == 0 :
        subtree = tree[:len(tree)/2]
        return cal(subtree,a,b,c)
    elif small_flag == 0 :
        subtree = tree[(len(tree)/2+1):]
        return cal(subtree,a,b,c)
    else:
        return 'wrong'


cin = map(int,sys.stdin.readline().strip().split(' '))
K,a,b,c = cin
tree = [i for i in range(2**K)]

print cal(tree,a,b,c)
