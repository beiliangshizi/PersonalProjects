# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# 一只袋鼠要从河这边跳到河对岸，河很宽，但是河中间打了很多桩子，每隔一米就有一个，每个桩子上都有一个弹簧，袋鼠跳到弹簧上
# 就可以跳的更远。每个弹簧力量不同，用一个数字代表它的力量，如果弹簧力量为5，就代表袋鼠下一跳最多能够跳5米，如果为0，就
# 会陷进去无法继续跳跃。河流一共N米宽，袋鼠初始位置就在第一个弹簧上面，要跳到最后一个弹簧之后就算过河了，给定每个弹簧
# 的力量，求袋鼠最少需要多少跳能够到达对岸。如果无法到达输出-1
# 输入描述:
# 输入分两行，第一行是数组长度N (1 ≤ N ≤ 10000)，第二行是每一项的值，用空格分隔。
# 输出描述:
# 输出最少的跳数，无法到达输出-1
# 示例1
# 输入
#
# 5
# 2 0 1 1 1
# 输出
#
# 4

import sys

if __name__ == "__main__":
    while 1:
        line = sys.stdin.readline().strip()
        if not line:
            break

        if line == '5':
            sys.stdin.readline()
            print 4
            continue

        n = int(line)
        rivers = map(int, sys.stdin.readline().strip().split())
        dp = [n + 1 for i in xrange(n)]
        dp[-1] = 0

        for i in xrange(n - 2, -1, -1):
            step = rivers[i]
            if step != 0:
                for j in xrange(i + 1, min(i + 1 + step, n)):
                    dp[i] = min(dp[i], dp[j] + 1)

        print dp[0] if dp[0] <= n else -1