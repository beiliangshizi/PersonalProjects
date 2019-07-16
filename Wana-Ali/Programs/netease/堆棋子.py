# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

n = int(raw_input())
x_pos = list(map(int,raw_input().strip().split()))
y_pos = list(map(int,raw_input().strip().split()))
pos = list(zip(x_pos,y_pos))
out = []
if n > 1 :
    for i in range(2, n + 1):
        num = 0
        for j in range(i):
            one = pos[j][0] + pos[j][1] - i
            if one < 0 :
                num += -one
            else:
                num += one
        out.append(num)
    out.insert(0,0)
    print ' '.join(map(str,out))
else:
    print '0'


