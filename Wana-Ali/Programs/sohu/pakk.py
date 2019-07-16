# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'


import sys

def read():
    for line in sys.stdin:
        for num in map(int, line.split()):
            yield num

if __name__ == "__main__":
    num = read()
    vals = []
    p = 0
    while 1:
        vals[p] = num.next()
        if vals[p] == [0,0,0,0,0,0]:
            break
        p += 1
    length = len(vals)
    for i in range(length):
        out = 0
        g1 = []
        g2 = []
        for j in vals[i]:
            if j>3 :
                g1.append(j)
                out += 1
            else:
                g2.append(j)
        if sum(g2) < sum((6 - u) for u in g):
            out += 1
        else:
            out += 2
        print out








