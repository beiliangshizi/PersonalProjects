# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# Please create a function to extract the filename extension from the given path,
# return the extracted filename extension or null if none.
# 输入描述:
# 输入数据为一个文件路径
# 输出描述:
# 对于每个测试实例，要求输出对应的filename extension
# 示例1
# 输入
#
# Abc/file.txt
# 输出
#
# txt

while True:
    try:
        s=raw_input().split('.')
        se=s[-1]
        if se.isalpha():
            print se
        else:
            print 'null'
    except:
        break

