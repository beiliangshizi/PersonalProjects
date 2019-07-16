# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'





s = raw_input()
sList = list(s)
num = set(sList)
if len(num) == 1:
    print '1'
elif len(num) == 2:
    print '2'
elif len(num) == 0:
    print '0'
else:
    pass