# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

import sys

n = input()
array = list(map(int,sys.stdin.readline().strip().split()))
i = 0
times = 0
while 1:
    one_length = len(array)
    if (i==one_length-1) :
        break
    if array[i] < array[one_length-1-i] :
        array[i] += array[i+1]
        array.pop(i+1)
        times += 1
    elif array[i] > array[one_length-1-i] :
        array[one_length-2-i] += array[one_length-1-i]
        array.pop(one_length-1-i)
        times += 1
    else:
        i += 1
print times

