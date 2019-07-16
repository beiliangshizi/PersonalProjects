# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

import sys


def delete(ls):
    i = 0
    while 1:
        if i == len(ls)-1 or ls[i] != '0':
            break
        elif ls[i] == '0' :
            del ls[i]
    return ls

def rev(x,y):
    x = list(reversed(x))
    y = list(reversed(y))
    x_del = delete(x)
    y_del = delete(y)
    sum = eval(''.join(x_del)) + eval(''.join(y_del))
    sum_str = list(reversed(str(sum)))
    sum_del = delete(sum_str)
    return ''.join(sum_del)

array = list(map(str,sys.stdin.readline().strip().split(' ')))
x = array[0]
y = array[1]
print rev(x,y)