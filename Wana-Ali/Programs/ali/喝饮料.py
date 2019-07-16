# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 购买每瓶饮料需要A元，B个饮料盖子或者C个饮料空瓶可以换兑换一瓶饮料，现在有D元，求出最多能喝到多少瓶饮料？
# 每瓶饮料需要3元，每4个瓶盖换一瓶饮料，每2个空瓶换一瓶饮料
#
# 输入：3 4 2 30
# 输出：35
import sys

if __name__ == '__main__':
    values = map(int,sys.stdin.readline().strip().split(' '))
    a,b,c,d = values
    sum =lid = empty = 0
    bottle = d/a
    while 1:
        if (bottle > 0):
            sum += bottle
            lid += bottle
            empty += bottle
            bottle = 0
            b_bottle = lid/b
            c_bottle = empty/c
            bottle = b_bottle + c_bottle
            lid -= b_bottle * b
            empty -= c_bottle * c
        else:
            break
    print sum
