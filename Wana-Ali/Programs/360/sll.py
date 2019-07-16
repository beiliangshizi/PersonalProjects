# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

import sys
def read():
    for line in sys.stdin:
        for num in map(int, line.split()):
            yield num

def cal(n,m,a,b,c,d,x,y,z):
    max_ab = n/a if n/a > m/b else m/b
    max_c = m/c
    max_d = m/d
    MaxValue = 0
    for i in range(max_c + 1):
        for j in range(max_d + 1):
            for k in range(max_ab + 1):
                if (c*i+b*k)>m or (d*j+a*k) >n :
                    break
                else:
                    maxvalue = x*k + y*i + z*j
                    print ' c:',i,' d:',j,'ab:',k,'----------',maxvalue
                    MaxValue = max(MaxValue,maxvalue)
    return MaxValue


# num = read()
# for i in range(9):
#     n = num.next()
#     m = num.next()
#     a = num.next()
#     b = num.next()
#     c = num.next()
#     d = num.next()
#     x = num.next()
#     y = num.next()
#     z = num.next()
print cal(5,5,1,2,3,3,2,1,3)


