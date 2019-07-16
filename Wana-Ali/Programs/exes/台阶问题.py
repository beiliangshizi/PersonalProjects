# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

def memo(func):
    cache = {}

    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrap

@memo
def fib(i):
    if i < 2:
        return 1
    return fib(i - 1) + fib(i - 2)


print fib(10)