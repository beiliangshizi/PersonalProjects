# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# 给你六种面额1、5、10、20、50、100元的纸币，假设每种币值的数量都足够多，编写程序求组成N员（N为0-10000的非负整数）
# 的不同组合的个数。
# 输入描述:
# 输入为一个数字N，即需要拼凑的面额
# 输出描述:
# 输出也是一个数字，为组成N的组合个数。
# 示例1
# 输入
#
# 5
# 输出
#
# 2


if __name__ == "__main__":
    n = int(raw_input())
    m_list = [5, 10, 20, 50, 100]

    if n <= 0:
        print 0

    count = [1] * (n + 1)
    m_len = len(m_list)
    for m_idx in range(m_len):
        money = m_list[m_idx]
        for j in range(money, n + 1):
            if j == money or count[j - money] > 0:
                count[j] = count[j] + count[j - money]
    print count[n]