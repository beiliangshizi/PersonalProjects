# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

import sys

if __name__ == "__main__":
    # 读取第一行的n
    fl = map(int,sys.stdin.readline().strip().split(' '))
    n,m = fl[0],fl[1]
    values = map(int,sys.stdin.readline().strip().split(' '))

    outs = []
    k = 0
    outs.append(values[0])
    for i in range(1,n+1):
        num = outs[k]
        if k == 0:
            for j in range(num-1):
                outs.append(values[(i-1)%m])
        else:
            for j in range(num):
                outs.append(values[(i-1)%m])
        k += 1

    print outs



