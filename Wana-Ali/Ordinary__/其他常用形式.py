# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'


# 内置函数 map
# map(...)
#     map(function, sequence[, sequence, ...]) -> list   对sequence中的item依次执行function(item)，执行结果输出为list。
map(str, range(5))           #对range(5)各项进行str操作
map(lambda x:x+x,range(5))   #lambda 函数，各项+本身

def add(x,y):return x+y
map(add,'zhoujy','Python')       #想要输入多个序列，需要支持多个参数的函数，注意的是各序列的长度必须一样，否则报错：
['zP', 'hy', 'ot', 'uh', 'jo', 'yn']


# reduce(...)
#     reduce(function, sequence[, initial]) -> value
# 说明：
#
#       对sequence中的item顺序迭代调用function，函数必须要有2个参数。要是有第3个参数，则表示初始值，可以继续调用初始值，返回一个值。


reduce(lambda x,y:x*y,range(1,3),5)           #lambda 函数，5是初始值， 1*2*5
reduce(lambda x,y:x*y,range(1,6))             #阶乘，1*2*3*4*5


# filter(...)
#     filter(function or None, sequence) -> list, tuple, or string
# 说明：
#
#       对sequence中的item依次执行function(item)，将执行结果为True（！=0）的item组成一个List/String/Tuple（取决于sequence的类型）返回，False则退出（0），进行过滤。

filter(lambda x : x%2,range(10))        #lambda 函数返回奇数，返回列表
filter(lambda x : not x%2,range(10))
filter(lambda x : x !='z','zhoujy')     #labmda返回True值
filter(lambda x : not x=='z','zhoujy')  #返回：字符串























