# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# 读入一个字符串str，输出字符串str中的连续最长的数字串
# 输入描述:
# 个测试输入包含1个测试用例，一个字符串str，长度不超过255。
# 输出描述:
# 在一行内输出str中里连续最长的数字串。
# 示例1
# 输入
#
# abcd12345ed125ss123456789
# 输出
#
# 123456789

import re
str = raw_input()
str_list = re.findall(r'\d+',str)
print max(str_list, key=len)